# Contributing to the Teaching Resources

Thank you for considering a contribution. This repository is a teaching portfolio, so the
resources pages must stay trustworthy: every link is something an instructor can put in front
of students without checking a licence first.

## What can be proposed

A new resource for any page in [`resources/`](resources/README.md) is welcome if it satisfies
**all** of the following:

1. **Free to access** — no paywall, login wall, or trial-only access required to reach the
   useful content. Commercial tools are acceptable only if a permanent free tier exists.
2. **Current** — maintained or last reviewed recently; no abandoned pages or dead projects.
3. **Verifiable** — hosted by an identifiable organisation, project, or author. Pages of
   unclear origin, or sites that redistribute other people's material without permission, are
   rejected. Official standard texts (ASTM, BS EN, IS, BDS EN, BNBC) are never linked to
   pirated copies; link the issuing body instead.
4. **Described in your own words** — write one to two original sentences. Do not copy or
   closely paraphrase the resource's own tagline, abstract, or another list's wording.

## How to propose

**Issue (simplest):** open an issue titled `Resource suggestion: <name>` containing the title,
URL, target course, license or terms, last-updated date if visible, and your one-to-two
sentence description in your own words.

**Pull request:** edit the relevant page in `resources/` directly. Keep the existing entry
format exactly:

```markdown
- [Resource name](https://example.org) — one to two sentences in your own words stating
  who it suits and one concrete way it is used in class.
```

Place the entry under the most fitting heading, or propose a new heading in the pull-request
description. The weekly link-check workflow will run automatically on your pull request.

## Content corrections and data rules

Corrections to course documents, standard values, or code are just as welcome as new
resources: open an issue describing the correction and the reason. Two standing rules:

- **All data must be synthetic** or properly licensed. Never commit student records,
  employer documents, or any personal data; example datasets are generated, not collected.
- **Standards are cited, never copied.** Corrections should state the standard number
  and the public source of the corrected value, not paste copyrighted text.

## Fork adaptability

Badges and Colab links are pre-configured for the `SyedRafiAhmedGIS` account. To adapt a
fork under a different username, run the following once from the repository root, then
review the result with `git diff` before committing:

```bash
grep -rl "SyedRafiAhmedGIS" . | xargs sed -i 's/SyedRafiAhmedGIS/<your-username>/g'
```

The command rewrites every occurrence in the working tree (README badges, notebook Colab
links, citation files); `git diff` is the safety net, and nothing in git history changes.

## Canonical coverage measurement

The coverage figure quoted in the README and CHANGELOG is exactly the one CI measures:

```bash
pytest code/ --cov=concrete_analysis --cov=gis_demo.gis_intro_demo --cov-report=term
```

As of v1.2.0 this yields 67 tests, 224 statements, 9 missed, **96 % line coverage**.
Do not quote a coverage figure measured with a wider scope (for example `--cov=code`):
that counts the test files themselves as production code and inflates the result.

## Review process

Each suggestion is checked against the four rules above, the link is opened and its title and
content confirmed, and the entry is edited for consistent tone before merging. Contributors
are credited in the commit history.

## License

By contributing, you agree that your description text is original and is licensed under the
same [MIT License](LICENSE) as the repository. Third-party resources you link remain under
their own licenses and ownership.
