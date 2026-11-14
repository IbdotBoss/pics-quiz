# PICS Test Practice

Study app for the MOD002647 Professional Issues: Computing and Society in-class test
(40 questions, 50 minutes: 20 single-answer at 2 marks, 20 choose-all at 3 marks).

The public site is `docs/index.html` (GitHub Pages). `index.html` is the full local build, which also holds the
2024-25 past paper; that paper and its key are gitignored and never published. Each is one
self-contained file and works offline. Progress is kept in the
browser's localStorage.

## Modes

- **Mock test**: 40 questions in test format, 50 minutes, marked at the end. Weighted like the
  2024-25 paper (data protection, Computer Misuse Act and FOI carry most of it), at most a few
  from the set readings, least-seen questions first.
- **2024-25 past paper** (local build only): the real 40 questions in order, keyed against the slides.
- **Practice by week**: pick weeks and sources; the explanation and slide reference show after
  each answer.
- **My wrong answers**: drill what you missed.
- **Revision notes**: a cheat sheet plus notes per week.

## How answers are decided

The lecture slides are the authority, because the test is marked against them. Where a slide is
ambiguous or disagrees with current law, the question carries a note saying so. Choose-all
questions are marked all-or-nothing; the real scheme is not published.

Lecture and seminar questions were drafted per week and every answer key was then checked
against the slide text. Questions from the set readings were drafted the same way but their keys
were not individually re-checked.

## Building

```bash
python build.py
```

Reads `bank/*.json` and `notes/*.md` (notes go through pandoc), validates every question
(answer indices, single/multi shape, duplicate ids and options) and writes `index.html` (local, everything) and
`docs/index.html` (public, no past paper) from `template.html`. It writes nothing if any question fails.

`bank/pastpaper.py` holds the past paper and its key; run it to regenerate `pastpaper.json`.
