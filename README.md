# CS1101S solutions

This repository publishes solution code as a Material for MkDocs website. The
Python files under `solutions/` are the source of truth: a MkDocs hook discovers
them and creates the site navigation and question pages automatically.

**Website:** [CS1101S Sample PA Solutions](https://eddrick-23.github.io/CS1101S/)

## Repository structure

```text
.
├── solutions/
│   └── PA1_Practice_B/       # One directory per practice
│       ├── Q6.py             # One Python file per question
│       ├── Q7.py
│       └── ...
├── docs/
│   ├── docs/
│   │   └── index.md          # Homepage introduction
│   ├── hooks.py              # Discovers and renders solution files
│   └── mkdocs.yml            # Site, theme, and Markdown configuration
├── pyproject.toml            # Python dependencies
└── uv.lock                   # Locked dependency versions
```

## How page generation works

During each MkDocs build, `docs/hooks.py` scans the immediate subdirectories of
`solutions/`.

- Each subdirectory becomes a practice section and landing page.
- Each Python file named `Q<number>.py` becomes a separate question page.
- Questions are ordered numerically, so `Q10.py` appears after `Q9.py`.
- The homepage and navigation receive links to every discovered practice.
- The Python source is displayed with syntax highlighting directly from the
  original file; generated Markdown pages are not stored in the repository.

For example, `solutions/PA1_Practice_B/Q6.py` is published at
`/pa1-practice-b/q6/`.

## Adding solutions

To add another question to an existing practice, add a file following the
question naming convention:

```text
solutions/PA1_Practice_B/Q11.py
```

To add another practice, create a new directory and place its question files
inside it:

```text
solutions/PA2_Practice_A/
├── Q1.py
└── Q2.py
```

No navigation or documentation configuration changes are required. The new
practice and questions will be discovered the next time the site is served or
built. Python files that do not match `Q<number>.py` are ignored by the hook.

## Local development

Install the locked dependencies and start the development server:

```sh
uv sync
uv run mkdocs serve -f docs/mkdocs.yml
```

Open <http://127.0.0.1:8000>. MkDocs watches the project and rebuilds the site
when files change.

Run a strict production build before publishing changes:

```sh
uv run mkdocs build --strict --clean -f docs/mkdocs.yml
```

The generated site is written to `docs/site/` and is excluded from Git.
