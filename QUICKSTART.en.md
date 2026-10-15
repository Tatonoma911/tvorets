# Tvorets quick start

[English overview](README.en.md) · [Русский](QUICKSTART.md)

Tvorets coordinates an AI agent's work from a product goal to a verified deliverable. It is a set of instructions and supporting files. Your agent supplies the model and execution tools.

## Use the kit directly

1. Download and extract the repository.
2. Open your project in an AI-agent environment.
3. Make the Tvorets files available to the agent and use the prompt below. If the kit lives outside the project, include its actual path.

```text
Read TVORETS.md and act as Tvorets, the orchestrator for this task.
Read the Russian reference files as needed and work in English.

Build [deliverable] for [user] to solve [specific problem].
The main action is [action]. Success is [observable acceptance criterion].
The output format is [format/platform].

Choose the workflow and combine the tools and skills that help achieve it.
Make ordinary technical decisions independently. Inspect existing material
before asking questions. If the goal or a material owner decision is missing,
ask before dependent implementation. Verify the result and show me how to use it.
```

State any deadline, existing brand, required integrations, and authorized external actions if they matter. Keep credentials out of the prompt.

## Install as a Codex skill

Copy the repository's `skill/tvorets` folder into your user skill directory, usually `~/.codex/skills/tvorets`. If that directory contains your own changes, preserve them before updating. Refresh skill discovery using the mechanism supported by your Codex environment, then invoke `$tvorets` with a concrete task.

The folder includes its references. This copy operation does not install third-party specialist skills, MCP servers, accounts, or API keys. If your agent cannot install skills, use `TVORETS.md` directly.

## Repair an existing project

```text
Read TVORETS.md and AUTONOMOUS-REPAIR.md. Work as Tvorets in English.
Investigate this project and reproduce [problem]. Preserve my data and working
features. Find the cause, repair it, and repeat the original scenario.
Check affected behavior and report the evidence and remaining limitations.
```

## Improve an interface

```text
Work as Tvorets in English. The user's main task is [task].
Open the current interface, inspect the complete journey, and make the next
action clear. Preserve [accepted brand/constraints]. Choose appropriate design
and motion skills, implement improvements, and verify desktop and mobile
behavior with original input.
```

## What to expect

Tvorets establishes the goal, orders work by dependencies, combines suitable specialist contributions, integrates their outputs, and checks the result. Routine technical decisions stay with the agent. Material missing goals or owner decisions are clarified. A requested approval stage remains part of the workflow.

Delivery should include the usable artifact, required source files, usage instructions, verification evidence, and anything that remains unverified. The exact checks depend on the task and available tools.

## Optional evidence utility

For the bundled evidence-integrity utility, use Python 3.9 or newer:

```sh
python tests/test_evidence.py
python scripts/check_evidence.py --help
```

The utility checks recorded files and hashes. It does not execute the tests described in a record or approve a release. See [EVIDENCE.md](EVIDENCE.md) and the [current verification report](TEST-RESULTS-1.7.md).
