"""Check declared local evidence integrity. Does not run tests or approve releases."""
import argparse
import hashlib
import json
from pathlib import Path, PureWindowsPath


def inspect_manifest(manifest, root):
    root = Path(root).resolve(strict=True)
    errors = []

    def files(records, label):
        if not isinstance(records, list) or not records:
            errors.append(label + ': nonempty file list required')
            return
        seen = set()
        for record in records:
            try:
                name = record['path']
                expected = record['sha256']
                if not isinstance(name, str) or not name or Path(name).is_absolute() or PureWindowsPath(name).drive:
                    raise ValueError('relative file path required')
                path = (root / name).resolve(strict=True)
                if not path.is_relative_to(root) or not path.is_file():
                    raise ValueError('file must remain inside project root')
                if path in seen:
                    raise ValueError('duplicate file')
                seen.add(path)
                if not isinstance(expected, str) or len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
                    raise ValueError('lowercase SHA-256 required')
                data = path.read_bytes()
                if not data:
                    raise ValueError('empty evidence/source file')
                if hashlib.sha256(data).hexdigest() != expected:
                    raise ValueError('hash mismatch: stale or changed file')
            except (KeyError, TypeError, ValueError, OSError) as exc:
                errors.append(label + ': ' + str(exc))

    if not isinstance(manifest, dict) or type(manifest.get('schema_version')) is not int or manifest.get('schema_version') != 1:
        return ['schema_version 1 required']
    files(manifest.get('sources'), 'sources')
    checks = manifest.get('checks')
    if not isinstance(checks, list) or not checks:
        return errors + ['nonempty checks required']
    seen = set()
    required_count = 0
    for check in checks:
        if not isinstance(check, dict):
            errors.append('invalid check object')
            continue
        identifier = check.get('id')
        if not isinstance(identifier, str) or not identifier.strip() or identifier in seen:
            errors.append('unique nonempty check id required')
            continue
        seen.add(identifier)
        required = check.get('required')
        status = check.get('status')
        if type(required) is not bool:
            errors.append(identifier + ': explicit boolean required field needed')
        if required is True:
            required_count += 1
            if status != 'PASS':
                errors.append(identifier + ': required check is not PASS')
        if status not in ('PASS', 'FAIL', 'BLOCKED', 'NOT_RUN'):
            errors.append(identifier + ': invalid status')
        if check.get('kind') not in ('runtime', 'visual', 'static', 'manual', 'integration'):
            errors.append(identifier + ': valid check kind required')
        if not isinstance(check.get('criterion'), str) or not check['criterion'].strip():
            errors.append(identifier + ': criterion required')
        if status == 'PASS':
            files(check.get('evidence'), identifier)
        elif not isinstance(check.get('reason'), str) or not check['reason'].strip():
            errors.append(identifier + ': non-PASS reason required')
    if required_count == 0:
        errors.append('at least one required check needed')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--root', required=True, type=Path)
    args = parser.parse_args()
    try:
        document = json.loads(args.manifest.read_text(encoding='utf-8-sig'))
        errors = inspect_manifest(document, args.root)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({'status': 'EVIDENCE_INVALID' if errors else 'EVIDENCE_CONSISTENT',
                      'errors': errors, 'release_approval': False}, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
