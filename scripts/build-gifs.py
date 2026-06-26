#!/usr/bin/env python3
"""Build all animated GIFs for the README.

One generator, several scenes. Each scene renders SVG frames -> PNG via
rsvg-convert and assembles an animated GIF with Pillow. No ffmpeg/gifski.

Run: python3 scripts/build-gifs.py
Outputs into assets/: demo.gif, structured.gif, relations.gif, layout.gif,
linking.gif
"""
import os
import subprocess
import tempfile
from PIL import Image

BG, CARD, FG, DIM, GRAY, BORDER = "#0d1117", "#161b22", "#c9d1d9", "#8b949e", "#6e7681", "#30363d"
TYPE = {
    "PERSON": "#d2a8ff", "ORG": "#79c0ff", "GPE": "#7ee787",
    "DATE": "#ffa657", "MONEY": "#f2cc60", "KEY": "#79c0ff",
    "STR": "#7ee787", "NUM": "#ffa657",
}
ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
MONO = 'font-family:"SF Mono","JetBrains Mono",Menlo,Consolas,monospace;'
SANS = "font-family:-apple-system,Segoe UI,Roboto,sans-serif;"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_open(w, h):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<style>.m{{{MONO}}}.s{{{SANS}}}</style>',
        f'<rect width="{w}" height="{h}" fill="{BG}"/>',
    ]


def head(p, w, title, sub):
    p.append(f'<text x="36" y="40" class="s" font-size="19" font-weight="700" fill="{FG}">{esc(title)}</text>')
    p.append(f'<text x="38" y="62" class="m" font-size="12" fill="{DIM}">{esc(sub)}</text>')


def render(svg, path, w, h):
    sp = path + ".svg"
    open(sp, "w").write(svg)
    subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), sp, "-o", path], check=True)
    os.remove(sp)


def build(name, w, h, frames):
    """frames: list of (svg_body_parts, duration_ms)."""
    tmp = tempfile.mkdtemp()
    imgs, durs = [], []
    for i, (parts, ms) in enumerate(frames):
        path = os.path.join(tmp, f"{name}{i:02d}.png")
        render("\n".join(svg_open(w, h) + parts + ["</svg>"]), path, w, h)
        imgs.append(Image.open(path).convert("RGB"))
        durs.append(ms)
    out = os.path.join(ASSETS, name + ".gif")
    os.makedirs(ASSETS, exist_ok=True)
    imgs[0].save(out, save_all=True, append_images=imgs[1:], duration=durs,
                 loop=0, optimize=True, disposal=2)
    print(f"wrote {out} ({len(imgs)} frames, {os.path.getsize(out)//1024} KB)")


# ---------------------------------------------------------------- hero (NER)
def hero():
    w, h = 860, 430
    L1 = [("Tim Cook", "PERSON"), (" announced that ", None), ("Apple", "ORG"), (" will open a new", None)]
    L2 = [("store in ", None), ("Paris", "GPE"), (" on ", None), ("March 3, 2026", "DATE"),
          (", investing ", None), ("$2 billion", "MONEY"), (".", None)]
    ents = [("Tim Cook", "PERSON"), ("Apple", "ORG"), ("Paris", "GPE"),
            ("March 3, 2026", "DATE"), ("$2 billion", "MONEY")]

    def spans(chunks, active):
        o = []
        for t, ty in chunks:
            if ty and ty in active:
                o.append(f'<tspan fill="{TYPE[ty]}" font-weight="700">{esc(t)}</tspan>')
            elif ty:
                o.append(f'<tspan fill="{GRAY}">{esc(t)}</tspan>')
            else:
                o.append(f'<tspan fill="{FG}">{esc(t)}</tspan>')
        return "".join(o)

    def frame(active):
        p = []
        head(p, w, "Entity Extraction", "text in -> structured entities out")
        p += [
            f'<rect x="36" y="84" width="{w-72}" height="92" rx="10" fill="{CARD}" stroke="{BORDER}"/>',
            f'<text x="52" y="108" class="m" font-size="12" fill="{DIM}">INPUT</text>',
            f'<text x="52" y="136" class="s" font-size="18" xml:space="preserve">{spans(L1, active)}</text>',
            f'<text x="52" y="162" class="s" font-size="18" xml:space="preserve">{spans(L2, active)}</text>',
            f'<text x="36" y="208" class="m" font-size="12" fill="{DIM}">EXTRACTED ENTITIES</text>',
        ]
        y = 224
        for t, ty in ents:
            if ty not in active:
                continue
            p.append(f'<rect x="36" y="{y}" width="92" height="26" rx="6" fill="{TYPE[ty]}"/>')
            p.append(f'<text x="82" y="{y+18}" text-anchor="middle" class="m" font-size="12" font-weight="700" fill="#0d1117">{ty}</text>')
            p.append(f'<text x="140" y="{y+18}" class="s" font-size="16" fill="{FG}">{esc(t)}</text>')
            y += 34
        return p

    frames = [(frame(set()), 900)]
    active = []
    for _, ty in ents:
        active.append(ty)
        frames.append((frame(set(active)), 800))
    frames.append((frame(set(active)), 2600))
    build("demo", w, h, frames)


# -------------------------------------------------- structured extraction (JSON)
def structured():
    w, h = 860, 360
    text = "Invoice A-204 from Globex Corp, dated 2026-05-01, total $4,500, net 30."
    rows = [
        ('"invoice_id"', '"A-204"', "STR"),
        ('"vendor"', '"Globex Corp"', "STR"),
        ('"date"', '"2026-05-01"', "STR"),
        ('"total"', "4500", "NUM"),
        ('"currency"', '"USD"', "STR"),
        ('"net_days"', "30", "NUM"),
    ]

    def frame(n):
        p = []
        head(p, w, "Structured Extraction", "prompt + schema -> typed JSON")
        p += [
            f'<rect x="36" y="84" width="360" height="120" rx="10" fill="{CARD}" stroke="{BORDER}"/>',
            f'<text x="52" y="108" class="m" font-size="12" fill="{DIM}">INPUT</text>',
            f'<text x="52" y="134" class="s" font-size="15" fill="{FG}">Invoice A-204 from Globex</text>',
            f'<text x="52" y="156" class="s" font-size="15" fill="{FG}">Corp, dated 2026-05-01,</text>',
            f'<text x="52" y="178" class="s" font-size="15" fill="{FG}">total $4,500, net 30.</text>',
            f'<rect x="420" y="84" width="{w-456}" height="248" rx="10" fill="{CARD}" stroke="{BORDER}"/>',
            f'<text x="436" y="108" class="m" font-size="12" fill="{DIM}">OUTPUT</text>',
            f'<text x="436" y="134" class="m" font-size="14" fill="{FG}">{{</text>',
        ]
        y = 158
        for i, (k, v, ty) in enumerate(rows):
            if i >= n:
                break
            comma = "," if i < len(rows) - 1 else ""
            p.append(f'<text x="452" y="{y}" class="m" font-size="14">'
                     f'<tspan fill="{TYPE["KEY"]}">{esc(k)}</tspan>'
                     f'<tspan fill="{DIM}">: </tspan>'
                     f'<tspan fill="{TYPE[ty]}">{esc(v)}</tspan>'
                     f'<tspan fill="{DIM}">{comma}</tspan></text>')
            y += 26
        if n >= len(rows):
            p.append(f'<text x="436" y="{y}" class="m" font-size="14" fill="{FG}">}}</text>')
        return p

    frames = [(frame(0), 700)]
    for i in range(1, len(rows) + 1):
        frames.append((frame(i), 600))
    frames.append((frame(len(rows)), 2600))
    build("structured", w, h, frames)


# --------------------------------------------------------- relation extraction
def relations():
    w, h = 860, 340
    triples = [
        ("Tim Cook", "PERSON", "is CEO of", "Apple", "ORG"),
        ("Apple", "ORG", "headquartered in", "Cupertino", "GPE"),
        ("Apple", "ORG", "founded in", "1976", "DATE"),
    ]

    def chip(p, x, y, label, ty, wch):
        ww = wch
        p.append(f'<rect x="{x}" y="{y}" width="{ww}" height="30" rx="8" fill="{TYPE[ty]}"/>')
        p.append(f'<text x="{x+ww/2}" y="{y+20}" text-anchor="middle" class="s" font-size="14" font-weight="700" fill="#0d1117">{esc(label)}</text>')
        return ww

    def frame(n):
        p = []
        head(p, w, "Relation Extraction", "entities -> subject - relation -> object")
        p.append(f'<text x="36" y="98" class="s" font-size="15" fill="{DIM}" xml:space="preserve">Tim Cook is CEO of Apple, which is headquartered in Cupertino and was founded in 1976.</text>')
        y = 130
        for i, (s, sty, rel, o, oty) in enumerate(triples):
            if i >= n:
                break
            sw = max(96, len(s) * 9 + 24)
            ow = max(96, len(o) * 9 + 24)
            x = 36
            chip(p, x, y, s, sty, sw)
            ax = x + sw
            p.append(f'<line x1="{ax+6}" y1="{y+15}" x2="{ax+150}" y2="{y+15}" stroke="{GRAY}" stroke-width="2" marker-end="url(#arw)"/>')
            p.append(f'<text x="{ax+78}" y="{y+10}" text-anchor="middle" class="m" font-size="11" fill="{DIM}">{esc(rel)}</text>')
            chip(p, ax + 160, y, o, oty, ow)
            y += 52
        # arrowhead def
        p.insert(0, f'<defs><marker id="arw" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{GRAY}"/></marker></defs>')
        return p

    frames = [(frame(0), 700)]
    for i in range(1, len(triples) + 1):
        frames.append((frame(i), 800))
    frames.append((frame(len(triples)), 2400))
    build("relations", w, h, frames)


# ----------------------------------------------------------- document layout
def layout():
    w, h = 860, 380
    # regions on a mock page: (x,y,w,h,label,color)
    regions = [
        (60, 96, 320, 34, "Title", "#79c0ff"),
        (60, 140, 320, 70, "Paragraph", "#7ee787"),
        (60, 220, 320, 64, "Table", "#ffa657"),
        (60, 294, 150, 56, "Figure", "#d2a8ff"),
    ]

    def frame(n):
        p = []
        head(p, w, "Document & Layout Extraction", "PDF / scan -> typed regions")
        # page
        p.append(f'<rect x="40" y="84" width="360" height="280" rx="6" fill="#ffffff" opacity="0.06" stroke="{BORDER}"/>')
        for i, (x, y, rw, rh, lab, col) in enumerate(regions):
            if i >= n:
                continue
            p.append(f'<rect x="{x}" y="{y}" width="{rw}" height="{rh}" rx="4" fill="none" stroke="{col}" stroke-width="2"/>')
            p.append(f'<rect x="{x}" y="{y-16}" width="{len(lab)*8+16}" height="16" rx="3" fill="{col}"/>')
            p.append(f'<text x="{x+8}" y="{y-4}" class="m" font-size="11" font-weight="700" fill="#0d1117">{esc(lab)}</text>')
        # legend
        p.append(f'<text x="440" y="108" class="m" font-size="12" fill="{DIM}">DETECTED</text>')
        ly = 132
        for i, (_, _, _, _, lab, col) in enumerate(regions):
            if i >= n:
                continue
            p.append(f'<rect x="440" y="{ly}" width="14" height="14" fill="{col}"/>')
            p.append(f'<text x="462" y="{ly+12}" class="s" font-size="14" fill="{FG}">{esc(lab)}</text>')
            ly += 26
        return p

    frames = [(frame(0), 700)]
    for i in range(1, len(regions) + 1):
        frames.append((frame(i), 750))
    frames.append((frame(len(regions)), 2400))
    build("layout", w, h, frames)


# --------------------------------------------------------------- entity linking
def linking():
    w, h = 860, 320

    def frame(stage):
        p = []
        head(p, w, "Entity Linking", "mention -> canonical knowledge-base entry")
        p.append(f'<text x="36" y="104" class="s" font-size="16" fill="{FG}" xml:space="preserve">...a new <tspan fill="#79c0ff" font-weight="700">Apple</tspan> store opened downtown.</text>')
        # mention chip
        p.append(f'<rect x="36" y="128" width="120" height="30" rx="8" fill="#79c0ff"/>')
        p.append(f'<text x="96" y="148" text-anchor="middle" class="s" font-size="14" font-weight="700" fill="#0d1117">"Apple"</text>')
        if stage >= 1:
            p.append(f'<line x1="160" y1="143" x2="250" y2="143" stroke="{GRAY}" stroke-width="2"/>')
            p.append(f'<text x="205" y="136" text-anchor="middle" class="m" font-size="10" fill="{DIM}">resolve</text>')
            # candidates
            p.append(f'<rect x="262" y="120" width="560" height="48" rx="8" fill="{CARD}" stroke="#7ee787"/>')
            p.append(f'<text x="278" y="140" class="s" font-size="15" font-weight="700" fill="{FG}">Apple Inc.</text>')
            p.append(f'<text x="278" y="159" class="m" font-size="12" fill="{DIM}">Q312 - technology company - chosen</text>')
            p.append(f'<text x="690" y="150" class="m" font-size="20" fill="#7ee787">OK</text>')
        if stage >= 2:
            p.append(f'<rect x="262" y="180" width="560" height="40" rx="8" fill="{CARD}" stroke="{BORDER}" opacity="0.7"/>')
            p.append(f'<text x="278" y="205" class="s" font-size="14" fill="{GRAY}">apple (fruit)   -   Q89   -   rejected</text>')
            p.append(f'<rect x="262" y="232" width="560" height="40" rx="8" fill="{CARD}" stroke="{BORDER}" opacity="0.7"/>')
            p.append(f'<text x="278" y="257" class="s" font-size="14" fill="{GRAY}">Apple Records   -   Q213710   -   rejected</text>')
        return p

    frames = [(frame(0), 800), (frame(1), 1100), (frame(2), 2600)]
    build("linking", w, h, frames)


# --------------------------------------------------------- which tool? (flow)
def decision():
    w, h = 900, 560
    steps_def = [
        ("Input is PDFs or scanned docs?", "Docling / Marker / Unstructured", "ORG"),
        ("Want a managed API, no hosting?", "Comprehend / Google / Azure", "PERSON"),
        ("Arbitrary fields from messy text?", "LLM + Instructor / Outlines", "GPE"),
        ("Custom entity types, no training?", "GLiNER (zero-shot)", "DATE"),
        ("Have labeled data, fixed schema?", "spaCy / SpanMarker (train)", "MONEY"),
    ]
    qx, qw, qh = 40, 380, 52
    cx, cw = 480, 380
    y0, gap = 100, 80

    def frame(n):
        p = []
        head(p, w, "Which tool should I pick?", "answer top-down; first YES wins")
        for i, (q, rec, ty) in enumerate(steps_def):
            if i >= n:
                continue
            y = y0 + i * gap
            # question box
            p.append(f'<rect x="{qx}" y="{y}" width="{qw}" height="{qh}" rx="10" fill="{CARD}" stroke="{BORDER}"/>')
            p.append(f'<text x="{qx+18}" y="{y+32}" class="s" font-size="15" fill="{FG}">{esc(q)}</text>')
            # YES arrow -> recommendation chip
            ay = y + qh // 2
            p.append(f'<line x1="{qx+qw}" y1="{ay}" x2="{cx}" y2="{ay}" stroke="{GRAY}" stroke-width="2" marker-end="url(#arw2)"/>')
            p.append(f'<text x="{qx+qw+18}" y="{ay-6}" class="m" font-size="10" fill="{TYPE[ty]}">YES</text>')
            p.append(f'<rect x="{cx}" y="{y+6}" width="{cw}" height="40" rx="8" fill="{TYPE[ty]}"/>')
            p.append(f'<text x="{cx+cw/2}" y="{y+32}" text-anchor="middle" class="s" font-size="15" font-weight="700" fill="#0d1117">{esc(rec)}</text>')
            # NO connector down to next question
            if i < len(steps_def) - 1:
                p.append(f'<line x1="{qx+30}" y1="{y+qh}" x2="{qx+30}" y2="{y+gap}" stroke="{BORDER}" stroke-width="2"/>')
                p.append(f'<text x="{qx+40}" y="{y+qh+18}" class="m" font-size="9" fill="{DIM}">no</text>')
        # default fallback
        if n > len(steps_def):
            yd = y0 + len(steps_def) * gap
            p.append(f'<text x="{qx+18}" y="{yd+6}" class="m" font-size="12" fill="{DIM}">else (just NER):</text>')
            p.append(f'<rect x="{cx}" y="{yd-14}" width="{cw}" height="40" rx="8" fill="none" stroke="#56d4dd" stroke-width="2"/>')
            p.append(f'<text x="{cx+cw/2}" y="{yd+12}" text-anchor="middle" class="s" font-size="15" font-weight="700" fill="#56d4dd">Start with a Hugging Face NER model</text>')
        p.insert(0, f'<defs><marker id="arw2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{GRAY}"/></marker></defs>')
        return p

    frames = [(frame(0), 700)]
    for i in range(1, len(steps_def) + 1):
        frames.append((frame(i), 800))
    frames.append((frame(len(steps_def) + 1), 900))
    frames.append((frame(len(steps_def) + 1), 3000))
    build("decision", w, h, frames)


if __name__ == "__main__":
    hero()
    structured()
    relations()
    layout()
    linking()
    decision()
