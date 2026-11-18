"""Build index.html from bank/*.json and notes/*.md.

Checks every question's shape and fails loudly rather than shipping a broken one.
Usage: python build.py
"""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
errors, questions, seen_ids = [], [], set()


def kind(src):
    s = src.lower()
    if "seminar" in s:
        return "seminar"
    if "lecture" in s:
        return "lecture"
    return "reading"


for path in sorted(glob.glob(os.path.join(HERE, "bank", "*.json"))):
    name = os.path.basename(path)
    for q in json.load(open(path, encoding="utf8")):
        qid = q.get("id", "?")
        def bad(msg):
            errors.append(f"{name} {qid}: {msg}")
        for k in ("id", "week", "topic", "type", "q", "options", "answer", "explain", "source"):
            if k not in q or q[k] in ("", None, []):
                bad(f"missing {k}")
        if errors and errors[-1].startswith(f"{name} {qid}: missing"):
            continue
        if qid in seen_ids:
            bad("duplicate id")
        seen_ids.add(qid)
        n, a = len(q["options"]), q["answer"]
        if q["type"] not in ("single", "multi"):
            bad("bad type")
        if any((not isinstance(i, int)) or i < 0 or i >= n for i in a) or len(set(a)) != len(a):
            bad("answer index out of range or repeated")
        if q["type"] == "single" and len(a) != 1:
            bad("single needs exactly one answer")
        if q["type"] == "multi" and (len(a) < 2 or n < 3):
            bad("multi needs two or more answers and three or more options")
        if n < 2 or n > 7:
            bad(f"{n} options")
        norm = [" ".join(o.lower().split()) for o in q["options"]]
        if len(set(norm)) != n and not qid.startswith("pp-"):  # the printed paper repeats an option in Q14
            bad("duplicate options")
        q["flag"] = q.get("flag", "") or ""
        q["kind"] = kind(q["source"])
        questions.append(q)

core = set()
for line in open(os.path.join(HERE, "bank", "core.txt"), encoding="utf8"):
    if not line.startswith("#"):
        core.update(line.split())
unknown = core - {q["id"] for q in questions}
if unknown:
    errors.append("core.txt names ids that are not in the bank: " + " ".join(sorted(unknown)))
for q in questions:
    q["core"] = q["id"] in core

if errors:
    print("\n".join(errors))
    sys.exit(f"{len(errors)} problem(s); nothing written")

notes = []
for path in sorted(glob.glob(os.path.join(HERE, "notes", "*.md"))):
    m = re.search(r"(\d+)", os.path.basename(path))
    html = subprocess.run(["pandoc", "-f", "gfm", "-t", "html", path], capture_output=True, check=True).stdout.decode("utf8")
    notes.append({"week": int(m.group(1)) if m else 0, "html": html})
notes.sort(key=lambda n: n["week"])

tpl = open(os.path.join(HERE, "template.html"), encoding="utf8").read()
import base64
for key, name in (("/*FONT_ARCHIVO*/", "Archivo.woff2"), ("/*FONT_REENIE*/", "ReenieBeanie.woff2")):
    assert key in tpl
    tpl = tpl.replace(key, base64.b64encode(open(os.path.join(HERE, "fonts", name), "rb").read()).decode())
assert "/*DATA*/" in tpl


def write(path, qs, ns):
    data = json.dumps({"questions": qs, "notes": ns}, ensure_ascii=False).replace("</", "<\\/")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf8").write(tpl.replace("/*DATA*/", data))


# docs/index.html is what GitHub Pages serves. index.html is the same file for opening locally.
write(os.path.join(HERE, "docs", "index.html"), questions, notes)
write(os.path.join(HERE, "index.html"), questions, notes)

from collections import Counter
c = Counter((q["week"], q["type"]) for q in questions)
for w in sorted({q["week"] for q in questions}):
    print(f"week {w:>2}: {c[(w,'single')]:>3} single  {c[(w,'multi')]:>3} multi")
print(len(core), "in the core set")
print(len(questions), "questions,", sum(1 for q in questions if q["flag"]), "flagged,", len(notes), "note files")
