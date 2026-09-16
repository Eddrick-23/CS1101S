"""Generate MkDocs pages directly from the solution source files."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from mkdocs.structure.files import File, Files


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIRECTORY = REPOSITORY_ROOT / "solutions"
QUESTION_PATTERN = re.compile(r"^Q(?P<number>\d+)$", re.IGNORECASE)


@dataclass(frozen=True)
class Question:
    number: int
    source: Path

    @property
    def page_name(self) -> str:
        return f"q{self.number}.md"


@dataclass(frozen=True)
class Practice:
    name: str
    slug: str
    questions: tuple[Question, ...]


def _title(value: str) -> str:
    """Turn a solution directory name into a readable page title."""
    return value.replace("_", " ").replace("-", " ")


def _slug(value: str) -> str:
    """Turn a solution directory name into a stable URL segment."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _discover_practices() -> tuple[Practice, ...]:
    if not SOLUTIONS_DIRECTORY.exists():
        return ()

    practices: list[Practice] = []
    for directory in sorted(path for path in SOLUTIONS_DIRECTORY.iterdir() if path.is_dir()):
        questions: list[Question] = []
        for source in directory.glob("*.py"):
            match = QUESTION_PATTERN.match(source.stem)
            if match:
                questions.append(Question(int(match.group("number")), source))

        if questions:
            practices.append(
                Practice(
                    name=directory.name,
                    slug=_slug(directory.name),
                    questions=tuple(sorted(questions, key=lambda question: question.number)),
                )
            )

    return tuple(practices)


def _code_fence(source_code: str) -> str:
    """Choose a fence longer than any backtick run in the source code."""
    longest_run = max((len(run) for run in re.findall(r"`+", source_code)), default=0)
    return "`" * max(3, longest_run + 1)


def _practice_page(practice: Practice) -> str:
    links = "\n".join(
        f"- [Question {question.number}]({question.page_name})"
        for question in practice.questions
    )
    return f"# {_title(practice.name)}\n\nSelect a question to view its solution.\n\n{links}\n"


def _question_page(practice: Practice, question: Question) -> str:
    source_code = question.source.read_text(encoding="utf-8").rstrip()
    fence = _code_fence(source_code)
    source_path = question.source.relative_to(REPOSITORY_ROOT).as_posix()
    return (
        f"# Question {question.number}\n\n"
        f"Source: `{source_path}`\n\n"
        f"{fence}python\n{source_code}\n{fence}\n"
    )


def on_config(config):
    """Build navigation from the practice directories and question files."""
    navigation: list[object] = [{"Home": "index.md"}]
    for practice in _discover_practices():
        pages: list[dict[str, str]] = [{"Overview": f"{practice.slug}/index.md"}]
        pages.extend(
            {f"Question {question.number}": f"{practice.slug}/{question.page_name}"}
            for question in practice.questions
        )
        navigation.append({_title(practice.name): pages})

    config.nav = navigation
    return config


def on_files(files: Files, config) -> Files:
    """Expose every question as an in-memory Markdown page."""
    for practice in _discover_practices():
        files.append(
            File.generated(
                config,
                f"{practice.slug}/index.md",
                content=_practice_page(practice),
            )
        )
        for question in practice.questions:
            files.append(
                File.generated(
                    config,
                    f"{practice.slug}/{question.page_name}",
                    content=_question_page(practice, question),
                )
            )
    return files


def on_page_markdown(markdown: str, page, **kwargs) -> str:
    """Add the discovered practice links to the homepage."""
    if page.file.src_uri != "index.md":
        return markdown

    practices = _discover_practices()
    if not practices:
        return f"{markdown}\n\n_No practices are available yet._\n"

    links = "\n".join(
        f"- [{_title(practice.name)}]({practice.slug}/index.md)"
        for practice in practices
    )
    return f"{markdown}\n\n## Practices\n\n{links}\n"
