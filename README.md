# PICS test practice

A study app for the MOD002647 Professional Issues, Computing and Society in-class test. The test has 40 questions in 50 minutes. Questions 1 to 20 have one answer and carry 2 marks each. Questions 21 to 40 have several correct answers and carry 3 marks each.

The public site is `docs/index.html`, served by GitHub Pages. `index.html` is the full local build, which also holds the 2024-25 past paper. That paper and its key are gitignored and never published. Each build is one self-contained file that works offline. Marks are kept in the browser's localStorage.

## What it does

| Paper | What you get |
|---|---|
| Mock test | 40 questions in test format, 50 minutes, marked at the end. Weeks are weighted like the 2024-25 paper, so Data Protection, the Computer Misuse Act and Freedom of Information carry most of it. Questions you have seen least come first. |
| 2024-25 past paper | The real 40 questions in order, keyed against the slides. Local build only. |
| Practice by week | You pick the weeks and sources. Each answer is marked at once, with the explanation and the slide it came from. |
| Corrections | Every question you have got wrong, until you get it right. |
| Revision notes | A cheat sheet and one sheet of notes per week. |

## How answers are decided

The test is marked against the lecture slides, so the slides decide every answer. Where a slide is unclear or disagrees with current law, the question carries a note. A choose-all question scores only when every box is right, because the real marking scheme is not published.

Subagents drafted the lecture and seminar questions one week at a time. Every answer key was then read against the slide text. Questions from the set readings were drafted the same way, and their keys were not re-checked one by one.

## Design

`design.md` holds the visual system. The quiz looks like the exam paper. You answer with a pen X in a square box, and the paper comes back marked in red.

## Building

```bash
python build.py
```

The build reads `bank/*.json` and `notes/*.md`, and runs the notes through pandoc. It checks every question for valid answer indices, the right shape for its type, and duplicate ids or options. It writes nothing if any question fails. Otherwise it writes `index.html` with everything and `docs/index.html` without the past paper, both from `template.html`.

`bank/pastpaper.py` holds the past paper and its key. Run it to regenerate `pastpaper.json`. `fonts/fetch.py` downloads the two embedded typefaces, Archivo and Reenie Beanie, both under the SIL Open Font License.
