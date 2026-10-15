# Tvorets

### From an idea to a result, with the whole workflow coordinated.

**English** · [Русский](README.md) · [Quick start](QUICKSTART.en.md)

Describe what you want to achieve. **Tvorets gives your AI agent a way to organize the work:** establish the goal, choose an approach, combine skills and tools, manage dependencies, build the result, and verify it.

A website, a game, a CRM, a bot, a presentation, and a marketing project each need a different workflow. Tvorets assembles that workflow around the task and keeps responsibility for the result through delivery.

**Created by Anton Kazakov · [@kazakovant](https://t.me/kazakovant)**

“Tvorets” (Творец) means “creator” in Russian. The core reference documents are currently in Russian. This README and the English quick start explain how to use the kit, including a prompt for an agent that can read those references and work in your preferred language.

## Start with a real problem

> “I run a renovation company. Clients request extra work through voice messages. I want to extract the request, compare it with the original estimate, and prepare a change for approval.”

Tvorets directs the agent to understand the process, identify the required data, build a clear user journey, select suitable tools, and verify the result. The agent handles ordinary technical decisions. The owner resolves material questions about the goal and authority to act.

You can start with a detailed brief, a sketch, a reference, or an existing project. When the product goal is unclear, the first step is to establish it.

## What makes the approach useful

### One goal coordinates the tools

Design, implementation, motion, editing, and testing each receive a concrete contribution. Tvorets keeps responsibility for integrating their outputs into the intended result. Specialist skills contribute their expertise within the project workflow.

### Dependencies determine the order

Each substantial step has inputs, an output, and a check before another step relies on it. Independent work can proceed in parallel. When an input changes, the affected dependencies are revisited.

For a web product, that might look like this:

```text
Business goal → user journey → data and behavior
              → interface → purposeful motion → browser verification
```

A game or a presentation may need a different order. The workflow follows the task.

### Different skills can work together

Frontend Design can guide composition, UI/UX Pro Max can inform interaction, Impeccable can help review an interface, Emil Kowalski's skills can guide motion, Humanizer can edit prose, and Playwright can support browser verification. Tvorets selects their contributions according to the goal and the tools actually available.

An unfamiliar task can call for research and a new workflow. Existing brand decisions, output requirements, and the owner's goal remain in place as tools change. The available routes are open to new tasks and combinations.

### Repairs and handoffs are part of the work

Tvorets directs the agent to reproduce a problem, investigate its cause, make a scoped repair, and check the affected behavior. Project state records accepted decisions, the current version, verification results, and the next action so work can continue after a pause.

## What you can build

| Task | What to verify |
|---|---|
| Websites and applications | The main user journey, original input, states, and mobile layout |
| Games | A playable loop, controls, feedback, and restart behavior |
| CRMs and internal tools | Data operations, relationships, persistence, and required permissions |
| Bots and automation | The path from a real event to the intended response or action |
| Marketing projects | An evidence-grounded offer, usable materials, and a working inquiry path |
| Presentations and documents | The requested format, content, legibility, and an openable file |
| Spreadsheets and dashboards | Calculations, sources, and a useful conclusion |

## Get started

1. [Download the kit](https://github.com/Tatonoma911/tvorets/archive/refs/heads/main.zip).
2. Open your project in an AI-agent environment with file access and the tools the task requires.
3. Give the agent this prompt:

```text
Read TVORETS.md and work as Tvorets. Read the Russian references as needed,
but communicate with me and produce the deliverables in English.

I want to build [what] for [whom], so they can [action and useful outcome].
Success means [what I can open, do, or independently verify].

Organize the work, combine suitable skills and tools, make ordinary technical
decisions, and verify the result. If material information is missing,
inspect the available sources first, then ask a precise question.
Show the result and state what has not been verified.
```

In Codex, you can install `skill/tvorets` as a user skill and invoke `$tvorets`. See the [English quick start](QUICKSTART.en.md) for installation and prompts for existing projects.

## Inside the kit

| Document | Purpose |
|---|---|
| [TVORETS.md](TVORETS.md) | Core operating protocol |
| [SKILL-ORCHESTRATION.md](SKILL-ORCHESTRATION.md) | Skill coordination, combinations, and execution order |
| [CAPABILITY-ROUTER.md](CAPABILITY-ROUTER.md) | Task-specific workflows and acceptance checks |
| [KNOWLEDGE-LIBRARY.md](KNOWLEDGE-LIBRARY.md) | Finding implementation guides, APIs, MCP servers, and components |
| [AUTONOMOUS-REPAIR.md](AUTONOMOUS-REPAIR.md) | Investigation and repair |
| [PRODUCT-REVIEW.md](PRODUCT-REVIEW.md), [TEST-MATRIX.md](TEST-MATRIX.md) | Product usefulness and verification |
| [CONTINUITY-AND-HANDOFF.md](CONTINUITY-AND-HANDOFF.md) | Resuming work and handing it over |
| [EVIDENCE.md](EVIDENCE.md), [project-state template](PROJECT-STATE.template.md) | Recording state and evidence |

The knowledge guide points to Build Your Own X, Public APIs, Awesome MCP Servers, Awesome Cursor Rules, and Origin UI / coss ui. Full third-party collections and the specialist skills mentioned above are separate dependencies; this kit does not bundle or automatically install them.

## Verification status

Version **1.7** received an independent source review of eight identified instruction conflicts, dependency sequencing, and tool combinations. Links and synchronized copies were checked. The evidence-integrity utility includes **13 repeatable unit tests**:

```sh
python tests/test_evidence.py
```

The [1.7 report](TEST-RESULTS-1.7.md) records the scope. These checks cover instructions and the utility. Each product needs its own verification. Comparative performance benchmarks and complete execution tests of every skill combination have not been performed.

## Access and terms

The kit is publicly available at no charge. You need a running AI agent; its environment determines which actions are available. Models, hosting, paid services, and account access are supplied separately. Tvorets operates while the agent is running and within the permissions it has been given.

**Version 1.7 · October 16, 2026.** [Changelog](CHANGELOG.md). The author has not yet specified a separate license. Public availability does not grant an MIT, Apache, or other standard license.

Questions, feedback, and examples of use: **[Anton Kazakov — @kazakovant](https://t.me/kazakovant)**. For a bug report, include the goal, environment, action taken, and expected result. Remove secrets and personal data from examples.
