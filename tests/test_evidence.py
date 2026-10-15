import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_evidence.py'
spec = importlib.util.spec_from_file_location('checker', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'project'
        self.root.mkdir()
        self.src = self.root / 'app.py'
        self.src.write_text('print(42)', encoding='utf-8')
        self.log = self.root / 'result.txt'
        self.log.write_text('Observed 42', encoding='utf-8')
        entry = lambda p: {'path': p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
        self.manifest = {'schema_version': 1, 'sources': [entry(self.src)], 'checks': [{
            'id': 'answer', 'required': True, 'status': 'PASS', 'kind': 'runtime',
            'criterion': 'prints 42', 'evidence': [entry(self.log)]}]}

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_record_is_not_release_approval(self):
        self.assertEqual([], checker.inspect_manifest(self.manifest, self.root))

    def test_changed_source_invalidates_old_pass(self):
        self.src.write_text('print(41)', encoding='utf-8')
        self.assertTrue(checker.inspect_manifest(self.manifest, self.root))

    def test_changed_log_invalidates_record(self):
        self.log.write_text('failed', encoding='utf-8')
        self.assertTrue(checker.inspect_manifest(self.manifest, self.root))

    def test_missing_evidence(self):
        self.log.unlink()
        self.assertTrue(checker.inspect_manifest(self.manifest, self.root))

    def test_empty_evidence(self):
        self.log.write_bytes(b'')
        self.manifest['checks'][0]['evidence'][0]['sha256'] = hashlib.sha256(b'').hexdigest()
        self.assertTrue(checker.inspect_manifest(self.manifest, self.root))

    def test_no_checks_cannot_pass(self):
        self.manifest['checks'] = []
        self.assertTrue(checker.inspect_manifest(self.manifest, self.root))

    def test_required_unrun_or_blocked_cannot_pass(self):
        for status in ['FAIL', 'BLOCKED', 'NOT_RUN', 'SKIP']:
            with self.subTest(status=status):
                self.manifest['checks'][0].update(status=status, reason='not observed')
                self.assertTrue(checker.inspect_manifest(self.manifest, self.root))

    def test_optional_gap_is_explicit(self):
        self.manifest['checks'].append({'id':'physical-phone','required':False,
          'status':'NOT_RUN','kind':'manual','criterion':'works on phone','reason':'device unavailable'})
        self.assertEqual([],checker.inspect_manifest(self.manifest,self.root))

    def test_escape_and_absolute_paths_rejected(self):
        outside = self.root.parent / 'secret.txt'
        outside.write_text('not for manifest',encoding='utf-8')
        for path in ['../secret.txt', str(outside), 'C:\\private\\secret.txt']:
            with self.subTest(path=path):
                self.manifest['checks'][0]['evidence'][0]['path'] = path
                self.assertTrue(checker.inspect_manifest(self.manifest,self.root))

    def test_string_false_not_boolean(self):
        self.manifest['checks'][0]['required'] = 'false'
        self.assertTrue(checker.inspect_manifest(self.manifest,self.root))

    def test_duplicate_check_rejected(self):
        self.manifest['checks'].append(copy.deepcopy(self.manifest['checks'][0]))
        self.assertTrue(checker.inspect_manifest(self.manifest,self.root))

    def test_untrusted_command_is_never_run(self):
        sentinel=self.root/'should-not-exist'
        self.manifest['command']=['python','-c',f'open({str(sentinel)!r},"w").write("bad")']
        checker.inspect_manifest(self.manifest,self.root)
        self.assertFalse(sentinel.exists())

    def test_bad_schema(self):
        for malformed in [[],None,{}, {'schema_version':2}, {**self.manifest,'schema_version':True}, {**self.manifest,'schema_version':1.0}]:
            self.assertTrue(checker.inspect_manifest(malformed,self.root))


if __name__ == '__main__':
    unittest.main(verbosity=2)
