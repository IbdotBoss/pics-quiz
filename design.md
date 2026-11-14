# Design: PICS test practice

## Brief

- **Subject.** A closed-book in-class test for MOD002647 at ARU. Forty questions in fifty minutes, answered by putting an X in a box on a printed paper.
- **Audience.** Stage, revising in the days before the test, on a phone and a laptop, many short sessions.
- **The one job.** Get him answering questions fast and show him exactly what he got wrong and which slide settles it.
- **Material.** 507 written questions, the 2024-25 paper, revision notes, the printed paper's own layout and cover wording.
- **Absent.** No logo, no photos, no illustrations. None are invented.
- **Footer.** The home and results pages end with "End of paper", a credit linking to ibrahimuthman.me, and a GitHub mark linking to the repo.
- This is a product surface used daily, so `product-surfaces.md` applies. It should be quiet and quick, and still look like it belongs to this test.

## Concept

The quiz is the exam paper. You answer in pen and it comes back marked.

Signature: a blue pen X in a square box while answering. Once marked, a green tick sits beside each right answer, and a red cross or ring marks each wrong or missed one. Stage asked for green on correct answers on 2026-11-14, because red on a right answer read as wrong.

## References

- **The 2024-25 printed paper**, measured from the docx. Body text 15pt, headings 20 to 22pt, 1 inch margins, answer boxes 0.25in square with a 1pt line and no rounding, marks printed in brackets after each question, a cover page with "Guidelines for candidates". Taken: the square 24px box, zero radius, black rules, bracketed marks, the cover page as the home screen. Left out: Word's default face and the centred cover layout.
- No live quiz products were surveyed. The paper is the reference because rehearsing its look is part of the job.

## Tokens

```css
:root {
  --paper: #fff;      /* the sheet */
  --desk: #e4e4e0;    /* behind the sheet at 800px and wider */
  --ink: #141414;     /* text, rules, boxes, primary button */
  --ink-2: #4a4a4a;   /* secondary text, 8.9:1 on paper */
  --hair: #c9c9c4;    /* table and section dividers only */
  --pen: #1b2f8a;     /* the candidate's X, and focus rings */
  --red: #c4161c;     /* wrong and missed marks, 5.9:1 on paper */
  --green: #1a7a3c;   /* the tick and the word Correct, 5.4:1 on paper */
  --t-xs: .84rem; --t-s: .94rem; --t-m: 1.0625rem; --t-l: 1.375rem; --t-xl: 1.875rem;
}
```

Spacing sits on a 4px base. Radius is 0 everywhere.

## Type

- **Archivo**, variable in width and weight, SIL OFL. One family doing two jobs. Headings and question numbers use it condensed to 75% width at weight 700, like a form heading. Body text uses normal width at 400, stems at 600.
- **Reenie Beanie**, SIL OFL, for one thing only, the circled mark on the results page.
- Five text sizes plus the one large mark. No letter-spacing changes.
- Both faces are embedded in the page as base64 woff2, latin subset, so the file still works offline and makes no font request.

## Assets

Type and rules only, plus five hand-drawn SVG paths: three X variants, a tick, a cross and a ring. Nothing is missing from Stage.

## Motion

None. Marks appear at once.

## Refused

- **Warm cream ground, system font, rounded cards.** This was the first build and is the most common generated look.
- **Dark green ground, serif, gold accent.** Direction B. Stage called it generic AI slop on 2026-11-14.
- **Highlighter and mono type.** Direction C. Long option text in a mono face is tiring, and it leans on three colours for meaning.
- **A progress bar and stat tiles.** The question number and the answered count say the same thing in words.
- **Dark mode.** The concept is a white sheet, so the page commits to one theme.

## Overrides

- `web-quality` asks each shipped colour scheme to pass. One scheme ships, and it passes.
- `ui-skills` assumes Tailwind and a component library. This is one static file with native inputs, so neither is used. The native `confirm` dialog guards handing in a paper with blanks.
- The handwritten mark is decoration. It is hidden from screen readers and the same mark is stated in text beside it.

## Stack

One static HTML file built by `build.py`, with questions, notes and fonts inlined. There are no routes and no server data, and it has to open by double-click offline.
