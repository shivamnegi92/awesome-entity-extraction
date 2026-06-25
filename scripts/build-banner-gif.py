#!/usr/bin/env python3
"""Build assets/demo.gif: an entity-extraction hero animation.

A sentence lights up entity by entity while a structured output panel fills in.
Renders SVG frames -> PNG via rsvg-convert -> animated GIF via Pillow.
No ffmpeg/gifski needed.
"""
import os
import subprocess
import tempfile
from PIL import Image

W, H = 860, 430
BG = "#0d1117"
CARD = "#161b22"
FG = "#c9d1d9"
DIM = "#8b949e"
GRAY = "#6e7681"

# entity type -> color
COLORS = {
    "PERSON": "#d2a8ff",
    "ORG": "#79c0ff",
    "GPE": "#7ee787",
    "DATE": "#ffa657",
    "MONEY": "#f2cc60",
}

# sentence as ordered chunks; ("text", None) = plain, ("text", "TYPE") = entity.
LINE1 = [("Tim Cook", "PERSON"), (" announced that ", None), ("Apple", "ORG"), (" will open a new", None)]
LINE2 = [("store in ", None), ("Paris", "GPE"), (" on ", None), ("March 3, 2026", "DATE"),
         (", investing ", None), ("$2 billion", "MONEY"), (".", None)]

# entities in reveal order: (text, type)
ENTITIES = [("Tim Cook", "PERSON"), ("Apple", "ORG"), ("Paris", "GPE"),
            ("March 3, 2026", "DATE"), ("$2 billion", "MONEY")]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def line_tspans(chunks, active):
    out = []
    for text, typ in chunks:
        if typ and typ in active:
            color = COLORS[typ]
            weight = ' font-weight="700"'
        elif typ:
            color = GRAY
            weight = ""
        else:
            color = FG
            weight = ""
        out.append(f'<tspan fill="{color}"{weight}>{esc(text)}</tspan>')
    return "".join(out)


def frame_svg(active):
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '<style>.m{font-family:"SF Mono","JetBrains Mono",Menlo,Consolas,monospace;}'
        '.s{font-family:-apple-system,Segoe UI,Roboto,sans-serif;}</style>',
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
        f'<text x="36" y="44" class="s" font-size="20" font-weight="700" fill="{FG}">Entity Extraction</text>',
        f'<text x="38" y="68" class="m" font-size="13" fill="{DIM}">text in -&gt; structured entities out</text>',
        # input card
        f'<rect x="36" y="88" width="{W-72}" height="92" rx="10" fill="{CARD}" stroke="#30363d"/>',
        f'<text x="52" y="112" class="m" font-size="12" fill="{DIM}">INPUT</text>',
        f'<text x="52" y="140" class="s" font-size="18" xml:space="preserve">{line_tspans(LINE1, active)}</text>',
        f'<text x="52" y="166" class="s" font-size="18" xml:space="preserve">{line_tspans(LINE2, active)}</text>',
        f'<text x="36" y="212" class="m" font-size="12" fill="{DIM}">EXTRACTED ENTITIES</text>',
    ]
    y = 228
    for text, typ in ENTITIES:
        if typ not in active:
            continue
        color = COLORS[typ]
        # type chip
        p.append(f'<rect x="36" y="{y}" width="92" height="26" rx="6" fill="{color}"/>')
        p.append(f'<text x="82" y="{y+18}" text-anchor="middle" class="m" font-size="12" font-weight="700" fill="#0d1117">{typ}</text>')
        # entity value
        p.append(f'<text x="140" y="{y+18}" class="s" font-size="16" fill="{FG}">{esc(text)}</text>')
        y += 34
    p.append("</svg>")
    return "\n".join(p)


def render(svg, path):
    sp = path + ".svg"
    open(sp, "w").write(svg)
    subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), sp, "-o", path], check=True)
    os.remove(sp)


def main():
    # cumulative reveal: 0 entities, then 1..5, with holds
    steps = []
    active = []
    steps.append((list(active), 900))           # just the sentence (gray entities)
    for text, typ in ENTITIES:
        active.append(typ)
        steps.append((list(active), 800))
    steps.append((list(active), 2600))          # hold full result

    tmp = tempfile.mkdtemp()
    imgs, durs = [], []
    for i, (active, ms) in enumerate(steps):
        path = os.path.join(tmp, f"f{i:02d}.png")
        render(frame_svg(set(active)), path)
        imgs.append(Image.open(path).convert("RGB"))
        durs.append(ms)
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "demo.gif"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    imgs[0].save(out, save_all=True, append_images=imgs[1:], duration=durs,
                 loop=0, optimize=True, disposal=2)
    print("wrote", out, f"({len(imgs)} frames, {os.path.getsize(out)//1024} KB)")


if __name__ == "__main__":
    main()
