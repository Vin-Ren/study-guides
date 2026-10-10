"""Compile the original lesson notes and question bank into a static guide."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

import mistune


ROOT = Path(__file__).resolve().parent
SOURCES = [
    ("decks-01-03.md", ["L01", "L02", "L03"]),
    ("decks-04-07.md", ["L04", "L05", "L06", "L07"]),
    ("decks-08-10.md", ["L08", "L09", "L10"]),
]
MARKDOWN = mistune.create_markdown(plugins=["table", "strikethrough", "url"])


def split_decks(source: str) -> list[tuple[str, str]]:
    sections = re.split(r"(?m)^##\s+", source)
    decks = []
    for section in sections[1:]:
        title, _, body = section.partition("\n")
        decks.append((title.strip(), body.strip()))
    return decks


def split_phases(body: str) -> tuple[str, str, str]:
    marker = re.search(r"(?im)^###\s+Solved slide exercises and mini-cases\s*$", body)
    trap = re.search(r"(?im)^###\s+Quiz traps\s*$", body)
    if not marker and not trap:
        return body, "", ""
    if marker and trap and marker.start() < trap.start():
        return body[: marker.start()], body[marker.end() : trap.start()], body[trap.end() :]
    if marker:
        return body[: marker.start()], body[marker.end() :], ""
    return body[: trap.start()], "", body[trap.end() :]


def render_deck(ident: str, title: str, body: str, phase: str) -> str:
    if not body.strip():
        return ""
    heading = html.escape(title)
    rendered = MARKDOWN(body)
    return f'<article class="deck" id="{phase}-{ident.lower()}"><div class="deck-heading"><span>{ident}</span><h3>{heading}</h3></div>{rendered}</article>'


def render_questions(questions: list[dict]) -> tuple[str, str]:
    cards = []
    key = []
    labels = "ABCD"
    for number, question in enumerate(questions, 1):
        stem = html.escape(question["stem"])
        topic = html.escape(question["topic"])
        ref = html.escape(question["ref"])
        choices = []
        for choice_index, choice in enumerate(question["options"]):
            value = labels[choice_index]
            choices.append(
                f'<label class="choice"><input type="radio" name="q{number}" value="{choice_index}"><span class="choice-letter">{value}</span><span>{html.escape(choice)}</span></label>'
            )
        answer = labels[question["answer"]]
        explanation = html.escape(question["explanation"])
        cards.append(
            f'<section class="question" id="question-{number}" data-answer="{question["answer"]}" data-topic="{topic}">'
            f'<div class="question-meta"><span>Question {number:02}</span><span>{topic}</span><span>{ref}</span></div>'
            f'<h3>{stem}</h3><div class="choices">{"".join(choices)}</div>'
            f'<button type="button" class="check-answer">Check answer</button>'
            f'<div class="feedback" aria-live="polite" hidden><strong>Answer: {answer}</strong><p>{explanation}</p></div></section>'
        )
        key.append(f'<li><a href="#question-{number}">Q{number}</a> — <strong>{answer}</strong>. {explanation} <small>{ref}</small></li>')
    return "\n".join(cards), "\n".join(key)


def main() -> None:
    concepts = []
    exercises = []
    traps = []
    toc = []
    for filename, identifiers in SOURCES:
        source = (ROOT / "content" / filename).read_text(encoding="utf-8")
        decks = split_decks(source)
        if len(decks) != len(identifiers):
            raise ValueError(f"{filename}: expected {len(identifiers)} H2 deck sections, found {len(decks)}")
        for ident, (title, body) in zip(identifiers, decks, strict=True):
            concept_body, exercise_body, trap_body = split_phases(body)
            concepts.append(render_deck(ident, title, concept_body, "concept"))
            exercises.append(render_deck(ident, title, exercise_body, "exercise"))
            traps.append(render_deck(ident, title, trap_body, "trap"))
            toc.append(f'<a href="#concept-{ident.lower()}"><span>{ident}</span>{html.escape(title)}</a>')
    questions = json.loads((ROOT / "questions.json").read_text(encoding="utf-8"))
    question_html, answer_html = render_questions(questions)
    template = (ROOT / "template.html").read_text(encoding="utf-8")
    replacements = {
        "@@STYLE@@": (ROOT / "assets" / "style.css").read_text(encoding="utf-8"),
        "@@SCRIPT@@": (ROOT / "assets" / "app.js").read_text(encoding="utf-8"),
        "@@TOC@@": "\n".join(toc),
        "@@CONCEPTS@@": "\n".join(concepts),
        "@@EXERCISES@@": "\n".join(exercises),
        "@@TRAPS@@": "\n".join(traps),
        "@@QUESTIONS@@": question_html,
        "@@ANSWER_KEY@@": answer_html,
        "@@QUESTION_COUNT@@": str(len(questions)),
    }
    for needle, value in replacements.items():
        template = template.replace(needle, value)
    (ROOT / "index.html").write_text(template, encoding="utf-8")
    print(f"Built {len(toc)} lectures and {len(questions)} questions")


if __name__ == "__main__":
    main()
