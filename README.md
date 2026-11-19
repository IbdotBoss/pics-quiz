# PICS test practice

Live at https://ibdotboss.github.io/pics-quiz/

A study app for the MOD002647 Professional Issues, Computing and Society in-class test. The test has 40 questions in 50 minutes. Questions 1 to 20 have one answer and carry 2 marks each. Questions 21 to 40 have several correct answers and carry 3 marks each.

GitHub Pages serves `docs/index.html`. It is one self-contained file that works offline, and `index.html` is the same file for opening locally. Marks are kept in the browser's localStorage.

## What it does

The papers are listed in the order to work through them. Each question paper has a Study button and a Test button. Study shows every question on one page with the right answers already marked. Test asks you the same questions.

| Paper | What you get |
|---|---|
| Revision notes | A cheat sheet and one sheet of notes per week. |
| 2024-25 past paper | The real 40 questions in order, keyed against the slides. The module provided this paper as support material. The test is timed at 50 minutes. |
| Core set | 84 questions, one for each list, body, Act and number on the cheat sheet. The ids are in `bank/core.txt`. |
| Practice by week | You pick the weeks and sources, then study or test. Each test answer is marked at once, with the explanation and the slide it came from. |
| Corrections | Every question you have got wrong, until you get it right. |
| Mock test | 40 questions in test format, 50 minutes, marked at the end. Weeks are weighted like the 2024-25 paper, so Data Protection, the Computer Misuse Act and Freedom of Information carry most of it. As on that paper, 8 of the 20 choose-all questions have every option correct. Questions you have seen least come first. |

## How answers are decided

The lecture slides decide every answer. Where a slide is unclear or disagrees with current law, the question carries a note. A choose-all question scores only when every box is right.

Subagents drafted the lecture and seminar questions one week at a time. Every answer key was then read against the slide text. Questions about module admin, such as the report word count, were removed, and stems were reworded to ask for the fact directly. Questions from the set readings were drafted the same way, and their keys were not re-checked one by one.

## Design

`design.md` holds the visual system. The quiz looks like the exam paper. You answer with a pen X in a square box, and the paper comes back marked, with a green tick for each right answer and red for each wrong or missed one.

## Building

```bash
python build.py
```

The build reads `bank/*.json` and `notes/*.md`, and runs the notes through pandoc. It checks every question for valid answer indices, the right shape for its type, and duplicate ids or options. It writes nothing if any question fails. Otherwise it writes `docs/index.html` and a local copy at `index.html`, both from `template.html`.

`bank/pastpaper.json` holds the past paper and its key. `fonts/fetch.py` downloads the two embedded typefaces, Archivo and Reenie Beanie, both under the SIL Open Font License.
