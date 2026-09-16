# CS1101S solutions

The MkDocs site reads Python solutions from `solutions/` and creates one page per
practice and question.

To preview the site locally:

```sh
uv run mkdocs serve -f docs/mkdocs.yml
```

Then open <http://127.0.0.1:8000>.

New practice directories and question files named `Q<number>.py` are discovered
automatically the next time the site is built or served.
