"""Page-building helpers for the OneGrasp Career Fitment Handbook (v2).

Every helper returns an HTML string. A page is one A4 sheet; build.py
collects them in order, numbers them and prints the PDF with Chromium.
Each part of the book has its own colour theme (THEMES); `part()` switches it.
"""
import html as _html
import math
import os

E = _html.escape
HERE = os.path.dirname(os.path.abspath(__file__))

PAGES = []          # dicts in book order
TOC = []            # ("part", no, title, idx, theme) / ("sub", None, title, idx, theme)

THEMES = {
    #  key       name                       c1         c2         soft       deep
    "brand":   ("OneGrasp",                "#E5383B", "#1E2340", "#FFF1F0", "#1E2340"),
    "meet":    ("Meet OneGrasp",           "#E5383B", "#FF8A3D", "#FFF3EE", "#9F1D20"),
    "test":    ("The Assessment",          "#0EA5E9", "#2563EB", "#EAF6FE", "#0B4A8B"),
    "dims":    ("The 8 Dimensions",        "#8B5CF6", "#EC4899", "#F5F0FF", "#4C1D95"),
    "report":  ("Your Report",             "#10B981", "#0EA5A4", "#ECFBF4", "#065F46"),
    "dash":    ("Your Dashboard",          "#F97316", "#F5B700", "#FFF5EB", "#9A3412"),
    "startup": ("Startups & Funding",      "#D946EF", "#F43F5E", "#FDF0FD", "#86198F"),
    "research": ("Research & Conferences", "#6366F1", "#06B6D4", "#EEF0FF", "#312E81"),
    "family":  ("Parents & Schools",       "#0284C7", "#22C55E", "#EAF5FC", "#075985"),
}
CUR = {"theme": "brand"}

# the eight dimensions' own colours (match the brochure's dimension wheel)
DIMC = ["#3B5BDB", "#E03131", "#7048E8", "#D6336C", "#1C7ED6", "#F08C00", "#2F9E44", "#0C8599"]


def theme(key):
    if key not in THEMES:
        THEMES[key] = THEMES["brand"]
    CUR["theme"] = key


def add(body, section="", kind="std", bg=None):
    PAGES.append({"kind": kind, "body": body, "section": section, "theme": CUR["theme"], "bg": bg})


def mark(title):
    TOC.append(("sub", None, title, len(PAGES), CUR["theme"]))


# ---------------------------------------------------------------- icons
_ICON_CACHE = {}
ICONS = False  # editorial design: no decorative icons
ALIAS = {"help-circle": "circle-help", "alert-triangle": "triangle-alert", "bar-chart": "chart-column", "pie-chart": "chart-pie", "home": "house"}


def icon(name, size="5mm", color="currentColor", stroke=2, cls="ic"):
    if not ICONS:
        return ""
    if name not in _ICON_CACHE:
        p = os.path.join(HERE, "vendor", "lucide", ALIAS.get(name, name) + ".svg")
        if not os.path.exists(p):
            print("missing icon:", name)
            p = os.path.join(HERE, "vendor", "lucide", "circle.svg")
        s = open(p).read()
        s = s[s.index("<svg"):]
        _ICON_CACHE[name] = s
    s = _ICON_CACHE[name]
    s = s.replace('width="24"', f'width="{size}"').replace('height="24"', f'height="{size}"')
    s = s.replace('stroke="currentColor"', f'stroke="{color}"').replace('stroke-width="2"', f'stroke-width="{stroke}"')
    s = s.replace("<svg", f'<svg class="{cls}"', 1)
    return s


def chip(name, color=None, bg=None, size="10mm", isz="5.2mm"):
    """An icon in a soft round chip."""
    return ""


# ---------------------------------------------------------------- basic blocks

def img(src, cls="", alt="", style=""):
    return f'<img src="assets/{src}" class="{cls}" alt="{E(alt)}" style="{style}">'


def laptop(src, caption="", style="", pins=None, cls=""):
    """A screenshot in a laptop frame. pins: [(n, x%, y%)] numbered markers."""
    pin = ""
    for n, x, y in (pins or []):
        pin += f'<span class="pin" style="left:{x}%;top:{y}%">{n}</span>'
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return (f'<figure class="laptop {cls}" style="{style}"><div class="lscreen"><div class="lcam"></div>'
            f'<div class="limg"><img src="assets/{src}" alt="">{pin}</div></div><div class="lbase"></div>{cap}</figure>')


def browser(src, caption="", style="", cls="", url="careerfitment.onegrasp.com"):
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return (f'<figure class="browser {cls}" style="{style}"><div class="bbar"><i></i><i></i><i></i><span>{E(url)}</span></div>'
            f'<img src="assets/{src}" alt="">{cap}</figure>')


def paper(src, caption="", style="", tilt=0):
    """A report page shown as a sheet of paper."""
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="paper" style="transform:rotate({tilt}deg);{style}"><img src="assets/{src}" alt="">{cap}</figure>'


def photo(src, caption="", style="", cls="", tape=True):
    t = '<i class="tape"></i>' if tape else ""
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="photo {cls}" style="{style}">{t}<img src="assets/{src}" alt="">{cap}</figure>'


def head(kicker, t1, t2="", lead="", center=False):
    t2h = f'<span class="c1">{t2}</span>' if t2 else ""
    br = "<br>" if t2 else ""
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    cc = " center" if center else ""
    return f'<header class="hd{cc}"><div class="kicker">{kicker}</div><h1 class="title">{t1}{br}{t2h}</h1>{ld}</header>'


def p(t, cls=""):
    return f'<p class="{cls}">{t}</p>'


def h3(t, ic=None):
    i = icon(ic, "4.6mm", "var(--c1)") + " " if ic else ""
    return f'<h3 class="h3">{i}{t}</h3>'


def two(a, b, cls="", ratio="1fr 1fr", gap="5mm"):
    return f'<div class="two {cls}" style="grid-template-columns:{ratio};gap:{gap}"><div>{a}</div><div>{b}</div></div>'


def grid(items, cols=3, cls="", gap="3.2mm"):
    return f'<div class="grid {cls}" style="grid-template-columns:repeat({cols},1fr);gap:{gap}">' + "".join(items) + "</div>"


def box(inner, cls="", style=""):
    return f'<div class="box {cls}" style="{style}">{inner}</div>'


def card(title, text, ic=None, color=None, num=None, cls=""):
    c = color or "var(--c1)"
    top = ""
    if ic:
        top = chip(ic, c, f"color-mix(in srgb, {c} 13%, white)")
    elif num is not None:
        top = f'<span class="cnum" style="background:{c}">{num}</span>'
    return f'<div class="card {cls}" style="--cc:{c}">{top}<h4>{title}</h4><p>{text}</p></div>'


def cards(items, cols=3, cls=""):
    """items: (icon, title, text[, color])"""
    out = []
    for i, it in enumerate(items):
        ic, t, x = it[0], it[1], it[2]
        c = it[3] if len(it) > 3 else None
        out.append(card(t, x, ic, c))
    return grid(out, cols, cls)


def bullets(items, cls="", ic="check", color=None):
    c = color or "var(--c1)"
    return f'<ul class="ticks {cls}">' + "".join(f'<li><span>{i}</span></li>' for i in items) + "</ul>"


def numbered(items, cls=""):
    return f'<ol class="nlist {cls}">' + "".join(f"<li><span>{i + 1:02d}</span><div>{t}</div></li>" for i, t in enumerate(items)) + "</ol>"


def stats(items, cls=""):
    """items: (value, label[, icon])"""
    out = []
    for it in items:
        ic = icon(it[2], "5mm", "var(--c1)") if len(it) > 2 else ""
        out.append(f'<div class="stat">{ic}<b>{it[0]}</b><span>{it[1]}</span></div>')
    return f'<div class="stats {cls}">' + "".join(out) + "</div>"


def steps(items, cls="", cols=None):
    """Numbered step cards on a connector line. items: (title, text[, icon])"""
    n = len(items)
    cols = cols or n
    out = []
    for i, it in enumerate(items, 1):
        ic = f"<b>{i:02d}</b>"
        out.append(f'<div class="st"><div class="stn">{ic}</div><div class="stk">STEP {i}</div><h4>{it[0]}</h4><p>{it[1]}</p></div>')
    return f'<div class="steps {cls}" style="grid-template-columns:repeat({cols},1fr)">' + "".join(out) + "</div>"


def vsteps(items, cls=""):
    """Vertical numbered timeline. items: (title, text)"""
    out = []
    for i, (t, x) in enumerate(items, 1):
        out.append(f'<div class="vs"><div class="vsn">{i}</div><div><h4>{t}</h4><p>{x}</p></div></div>')
    return f'<div class="vsteps {cls}">' + "".join(out) + "</div>"


CALLOUT = {
    "simple": ("", "In simple words", "var(--c1)", ""),
    "example": ("", "Example", "var(--c1)", ""),
    "try": ("", "Try this", "var(--c1)", ""),
    "parent": ("", "For parents", "var(--c1)", ""),
    "warn": ("", "Caution", "#B42318", ""),
    "good": ("", "Good to know", "var(--c1)", ""),
    "ananya": ("", "Ananya's story", "var(--c1)", ""),
    "teacher": ("", "For teachers", "var(--c1)", ""),
    "task": ("", "Your task", "var(--c1)", ""),
}


def callout(kind, text, title=None, cls=""):
    ic, label, c, bg = CALLOUT[kind]
    return (f'<div class="callout {cls}" style="--k:{c}"><div class="cot"><b>{title or label}</b></div>'
            f'<div class="cob">{text}</div></div>')


def findit(*crumbs):
    return (f'<div class="findit"><b>Find it</b>'
            + '<span class="sep">›</span>'.join(f"<span class='cr'>{c}</span>" for c in crumbs) + "</div>")


def table(header, rows, cls="", widths=None):
    cg = ""
    if widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    th = "".join(f"<th>{h}</th>" for h in header)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="tbl {cls}">{cg}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def quote(text, who="", cls=""):
    w = f'<div class="qwho">{who}</div>' if who else ""
    return f'<blockquote class="quote {cls}"><span class="qm">“</span>{text}{w}</blockquote>'


def band(text, title="", ic="sparkles", cls=""):
    t = f"<b>{title}</b> " if title else ""
    return f'<div class="band {cls}"><div>{t}{text}</div></div>'


def tag(t, c="var(--c1)"):
    return f'<span class="tag" style="--t:{c}">{t}</span>'


def pills(items):
    return '<div class="pills">' + "".join(f'<span class="pill">{i}</span>' for i in items) + "</div>"


def check_list(items, cols=1):
    return grid([f'<div class="check"><i></i><span>{t}</span></div>' for t in items], cols, gap="1.6mm 5mm")


def lines(n):
    return "".join('<div class="wline"></div>' for _ in range(n))


# ---------------------------------------------------------------- charts (SVG)

def _pt(cx, cy, r, a):
    return cx + r * math.cos(a), cy + r * math.sin(a)


def wheel(labels, colors, sub=None, center=("The", "Whole You"), size=150):
    """A segmented donut wheel with a label in each segment (the 8 dimensions)."""
    n = len(labels)
    cx = cy = 100
    R, r = 96, 44
    segs = []
    for i in range(n):
        a0 = -math.pi / 2 + i * 2 * math.pi / n + 0.012
        a1 = -math.pi / 2 + (i + 1) * 2 * math.pi / n - 0.012
        x0, y0 = _pt(cx, cy, R, a0); x1, y1 = _pt(cx, cy, R, a1)
        x2, y2 = _pt(cx, cy, r, a1); x3, y3 = _pt(cx, cy, r, a0)
        segs.append(f'<path d="M{x0:.2f},{y0:.2f} A{R},{R} 0 0,1 {x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f} A{r},{r} 0 0,0 {x3:.2f},{y3:.2f} Z" fill="{colors[i]}"/>')
        am = (a0 + a1) / 2
        tx, ty = _pt(cx, cy, (R + r) / 2, am)
        num = f"{i + 1:02d}"
        lab = labels[i].split("\n")
        t = f'<text x="{tx:.1f}" y="{ty - 3 - 3.6 * (len(lab) - 1):.1f}" class="wn">{num}</text>'
        for k, l in enumerate(lab):
            t += f'<text x="{tx:.1f}" y="{ty + 6 + k * 7.2:.1f}" class="wl">{l}</text>'
        segs.append(t)
    c = f'<circle cx="100" cy="100" r="{r - 3}" fill="#fff"/><text x="100" y="97" class="wc1">{center[0]}</text><text x="100" y="111" class="wc2">{center[1]}</text>'
    return f'<svg viewBox="0 0 200 200" class="wheel" style="width:{size}mm">{"".join(segs)}{c}</svg>'


def radar(labels, values, color="#8B5CF6", size=80, maxv=100, compare=None):
    n = len(labels)
    cx = cy = 100
    R = 66
    out = []
    for ring in (0.25, 0.5, 0.75, 1):
        pts = " ".join(f"{_pt(cx, cy, R * ring, -math.pi / 2 + i * 2 * math.pi / n)[0]:.1f},{_pt(cx, cy, R * ring, -math.pi / 2 + i * 2 * math.pi / n)[1]:.1f}" for i in range(n))
        out.append(f'<polygon points="{pts}" fill="none" stroke="#E4E0EC" stroke-width="0.8"/>')
    for i in range(n):
        x, y = _pt(cx, cy, R, -math.pi / 2 + i * 2 * math.pi / n)
        out.append(f'<line x1="100" y1="100" x2="{x:.1f}" y2="{y:.1f}" stroke="#E4E0EC" stroke-width="0.8"/>')
        lx, ly = _pt(cx, cy, R + 16, -math.pi / 2 + i * 2 * math.pi / n)
        out.append(f'<text x="{lx:.1f}" y="{ly + 2:.1f}" class="rl">{labels[i]}</text>')
    if compare:
        pts = " ".join(f"{_pt(cx, cy, R * v / maxv, -math.pi / 2 + i * 2 * math.pi / n)[0]:.1f},{_pt(cx, cy, R * v / maxv, -math.pi / 2 + i * 2 * math.pi / n)[1]:.1f}" for i, v in enumerate(compare))
        out.append(f'<polygon points="{pts}" fill="none" stroke="#9CA3AF" stroke-dasharray="3 2" stroke-width="1.2"/>')
    pts = " ".join(f"{_pt(cx, cy, R * v / maxv, -math.pi / 2 + i * 2 * math.pi / n)[0]:.1f},{_pt(cx, cy, R * v / maxv, -math.pi / 2 + i * 2 * math.pi / n)[1]:.1f}" for i, v in enumerate(values))
    out.append(f'<polygon points="{pts}" fill="{color}" fill-opacity="0.22" stroke="{color}" stroke-width="2"/>')
    for i, v in enumerate(values):
        x, y = _pt(cx, cy, R * v / maxv, -math.pi / 2 + i * 2 * math.pi / n)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{color}"/>')
    return f'<svg viewBox="0 0 200 200" class="radar" style="width:{size}mm">{"".join(out)}</svg>'


def donut(parts, size=46, hole=0.58, center=None):
    """parts: (label, value, color)"""
    tot = sum(v for _, v, _ in parts)
    a = -math.pi / 2
    out = []
    R = 48
    r = R * hole
    for lab, v, c in parts:
        a1 = a + 2 * math.pi * v / tot
        large = 1 if a1 - a > math.pi else 0
        x0, y0 = _pt(50, 50, R, a); x1, y1 = _pt(50, 50, R, a1)
        x2, y2 = _pt(50, 50, r, a1); x3, y3 = _pt(50, 50, r, a)
        out.append(f'<path d="M{x0:.2f},{y0:.2f} A{R},{R} 0 {large},1 {x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f} A{r},{r} 0 {large},0 {x3:.2f},{y3:.2f} Z" fill="{c}"/>')
        a = a1
    ct = ""
    if center:
        ct = f'<text x="50" y="50" class="dc1">{center[0]}</text><text x="50" y="60" class="dc2">{center[1]}</text>'
    return f'<svg viewBox="0 0 100 100" class="donut" style="width:{size}mm">{"".join(out)}{ct}</svg>'


def legend(parts):
    return '<div class="legend">' + "".join(f'<div><i style="background:{c}"></i><span>{l}</span><b>{v}</b></div>' for l, v, c in parts) + "</div>"


def hbars(rows, color=None, maxv=100, unit="", cls=""):
    """rows: (label, value[, color])"""
    out = []
    for r in rows:
        c = r[2] if len(r) > 2 else (color or "var(--c1)")
        w = max(2, 100 * r[1] / maxv)
        out.append(f'<div class="hb"><span class="hbl">{r[0]}</span><div class="hbt"><i style="width:{w:.0f}%;background:{c}"></i></div><b>{r[1]}{unit}</b></div>')
    return f'<div class="hbars {cls}">' + "".join(out) + "</div>"


def hexagon(labels, values, color="#E03131", size=62):
    """RIASEC hexagon."""
    cx = cy = 100
    R = 62
    out = []
    for ring in (0.33, 0.66, 1):
        pts = " ".join(f"{_pt(cx, cy, R * ring, -math.pi / 2 + i * math.pi / 3)[0]:.1f},{_pt(cx, cy, R * ring, -math.pi / 2 + i * math.pi / 3)[1]:.1f}" for i in range(6))
        out.append(f'<polygon points="{pts}" fill="none" stroke="#EADFDF" stroke-width="1"/>')
    pts = " ".join(f"{_pt(cx, cy, R * v / 100, -math.pi / 2 + i * math.pi / 3)[0]:.1f},{_pt(cx, cy, R * v / 100, -math.pi / 2 + i * math.pi / 3)[1]:.1f}" for i, v in enumerate(values))
    out.append(f'<polygon points="{pts}" fill="{color}" fill-opacity=".2" stroke="{color}" stroke-width="2"/>')
    for i, l in enumerate(labels):
        x, y = _pt(cx, cy, R + 20, -math.pi / 2 + i * math.pi / 3)
        bx, by = _pt(cx, cy, R, -math.pi / 2 + i * math.pi / 3)
        out.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="9" fill="{color}"/><text x="{bx:.1f}" y="{by + 3.4:.1f}" class="hxl">{l[0]}</text>')
        out.append(f'<text x="{x:.1f}" y="{y + 3:.1f}" class="hxn">{l}</text>')
    return f'<svg viewBox="0 0 200 200" class="hex" style="width:{size}mm">{"".join(out)}</svg>'


def ring(value, label, color="var(--c1)", size=24):
    r = 40
    c = 2 * math.pi * r
    return (f'<div class="ring" style="width:{size}mm"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="{r}" stroke="#EEE9E2" stroke-width="11" fill="none"/>'
            f'<circle cx="50" cy="50" r="{r}" stroke="{color}" stroke-width="11" fill="none" stroke-linecap="round" stroke-dasharray="{c * value / 100:.1f} {c:.1f}" transform="rotate(-90 50 50)"/>'
            f'<text x="50" y="57" class="rv">{value}</text></svg><span>{label}</span></div>')


def gauge(value, label, color="#DC2626", size=40):
    a = math.pi * (1 - value / 100)
    x, y = 50 + 40 * math.cos(a), 52 - 40 * math.sin(a)
    return (f'<div class="gauge" style="width:{size}mm"><svg viewBox="0 0 100 60"><path d="M10,52 A40,40 0 0,1 90,52" stroke="#EEE" stroke-width="10" fill="none" stroke-linecap="round"/>'
            f'<path d="M10,52 A40,40 0 0,1 {x:.1f},{y:.1f}" stroke="{color}" stroke-width="10" fill="none" stroke-linecap="round"/>'
            f'<text x="50" y="50" class="gv">{value}%</text></svg><span>{label}</span></div>')


# ---------------------------------------------------------------- divider (chapter opener)

def divider(part, key, title, sub, items, art, art2=None):
    theme(key)
    TOC.append(("part", part, title, len(PAGES), key))
    lis = "".join(f'<li><span>{i + 1:02d}</span>{t}</li>' for i, t in enumerate(items))
    a2 = img(art2, "dv-art2") if art2 else ""
    add(f'''<div class="dv">
<div class="dv-dots"></div><div class="dv-blob b1"></div><div class="dv-blob b2"></div>
<div class="dv-logo">{img("art/logo.png")}<span>Career Fitment Handbook</span></div>
<div class="dv-num">{part:02d}</div>
<div class="dv-txt"><div class="dv-part">PART {part:02d}</div><h1 class="dv-title">{title}</h1><p class="dv-sub">{sub}</p></div>
<div class="dv-list"><div class="dv-lh">In this part</div><ol>{lis}</ol></div>
{img(art, "dv-art")}{a2}
<div class="dv-foot"><span>{title}</span><span>careerfitment.onegrasp.com</span></div></div>''', section=title, kind="divider")


# ---------------------------------------------------------------- design system v3
ACC = {"red": ("#C72D35", "#B0262E"), "blue": ("#2196C8", "#1672A0"), "purple": ("#7754B8", "#6243A3"), "green": ("#279B70", "#1F7D5A"),
       "orange": ("#F09A24", "#B76A06"), "gold": ("#E5B73B", "#8C6A0C"), "navy": ("#17243A", "#17243A")}
CHAPTER = {"brand": "red", "meet": "red", "test": "blue", "dims": "purple", "report": "blue", "dash": "orange", "skills": "green",
           "startup": "gold", "research": "blue", "family": "red", "action": "orange"}
CH_ICON = {"meet": "building-2", "test": "clipboard-check", "dims": "brain", "report": "file-chart-column", "dash": "layout-dashboard",
           "skills": "sprout", "startup": "rocket", "research": "microscope", "family": "heart-handshake", "action": "flag"}


def accent(name):
    c, d = ACC[name]
    return (c, c, f"color-mix(in srgb, {c} 9%, white)", d)


def set_theme(key, name, acc):
    THEMES[key] = (name,) + accent(acc)


for _k in list(THEMES):
    THEMES[_k] = (THEMES[_k][0],) + accent(CHAPTER.get(_k, "red"))
THEMES.setdefault("skills", ("Skills for Life & Work",) + accent("green"))
THEMES.setdefault("action", ("Your Action Plan",) + accent("orange"))
DIMC[:] = ["#7754B8", "#C72D35", "#2196C8", "#279B70", "#F09A24", "#B5891A", "#17243A", "#5E7189"]
ICONS = True


def chip(name, color=None, bg=None, size="10mm", isz="5.2mm"):
    c = color or "var(--c1)"
    b = bg or f"color-mix(in srgb, {c} 13%, white)"
    return f'<span class="it chip" style="width:{size};height:{size};background:{b}">{icon(name, isz, c, 1.75)}</span>'


def tile(name, size="8mm", isz="4.6mm", solid=False, color="var(--c1)"):
    if solid:
        return f'<span class="it" style="width:{size};height:{size};background:{color}">{icon(name, isz, "#fff", 1.75)}</span>'
    return chip(name, color, None, size, isz)


def h3(t, ic=None):
    return f'<h3 class="h3">{tile(ic, "7mm", "4mm") if ic else ""}<span>{t}</span></h3>'


CALLOUT.update({
    "simple": ("lightbulb", "In simple words", "#E5B73B", "#8C6A0C"), "example": ("users", "Example", "#279B70", "#1F7D5A"),
    "try": ("footprints", "Try this", "#F09A24", "#B76A06"), "parent": ("heart-handshake", "For parents", "#2196C8", "#1672A0"),
    "warn": ("triangle-alert", "Caution", "#C72D35", "#B0262E"), "good": ("info", "Good to know", "#2196C8", "#1672A0"),
    "ananya": ("user-round", "Ananya's story", "#7754B8", "#6243A3"), "teacher": ("school", "For teachers", "#2196C8", "#1672A0"),
    "task": ("square-check-big", "Your task", "#F09A24", "#B76A06")})


def callout(kind, text, title=None, cls=""):
    ic, label, c, d = CALLOUT[kind]
    return (f'<div class="callout {cls}" style="--k:{c};--kt:{d}"><div class="cot">{tile(ic, "6mm", "3.6mm", color=c)}<b>{title or label}</b></div>'
            f'<div class="cob">{text}</div></div>')


def stats(items, cls=""):
    out = []
    for it in items:
        ic = tile(it[2], "7mm", "4mm") if len(it) > 2 else ""
        out.append(f'<div class="stat">{ic}<b>{it[0]}</b><span>{it[1]}</span></div>')
    return f'<div class="stats {cls}">' + "".join(out) + "</div>"


def mindmap(center, sub, nodes, height=110, cw=36, nw=48):
    """Radial mind map. nodes: (icon, title, text[, colour]). Laid out on an ellipse around the centre."""
    n = len(nodes)
    cols = ["#7754B8", "#2196C8", "#279B70", "#F09A24", "#C72D35", "#B5891A", "#17243A", "#5E7189"]
    lines, html = [], []
    for i, nd in enumerate(nodes):
        a = -math.pi / 2 + (i + (0.5 if n % 2 == 0 else 0)) * 2 * math.pi / n
        x, y = 50 + 37 * math.cos(a), 50 + 41 * math.sin(a)
        c = nd[3] if len(nd) > 3 else cols[i % len(cols)]
        lines.append(f'<line x1="50" y1="50" x2="{x:.1f}" y2="{y:.1f}" stroke="{c}" stroke-width=".35" stroke-dasharray="1.2 .8"/>'
                     f'<circle cx="{x:.1f}" cy="{y:.1f}" r=".9" fill="{c}"/>')
        txt = f"<p>{nd[2]}</p>" if nd[2] else ""
        html.append(f'<div class="nd" style="left:{x:.1f}%;top:{y:.1f}%;--nc:{c};--w:{nw}mm">{tile(nd[0], "7mm", "4mm", color=c)}<b>{nd[1]}</b>{txt}</div>')
    return (f'<div class="mm" style="height:{height}mm"><svg class="lines" viewBox="0 0 100 100" preserveAspectRatio="none">{"".join(lines)}</svg>'
            f'<div class="ctr" style="left:50%;top:50%;width:{cw}mm;height:{cw}mm"><b>{center}</b><span>{sub}</span></div>{"".join(html)}</div>')


def roadmap(stops, ry="50%", per_row=4):
    """Road with numbered stations, labels alternating above/below; wraps every per_row stops. stops: (title, text[, colour])"""
    cols = ["#2196C8", "#7754B8", "#F09A24", "#279B70", "#C72D35", "#B5891A", "#17243A"]
    rows = []
    for r0 in range(0, len(stops), per_row):
        out = []
        for i in range(r0, min(r0 + per_row, len(stops))):
            s_ = stops[i]
            c = s_[2] if len(s_) > 2 else cols[i % len(cols)]
            d = "up" if (i - r0) % 2 == 0 else "dn"
            out.append(f'<div class="stn {d}" style="--sc:{c}"><div class="sp"></div><div class="dot">{i + 1:02d}</div><div class="lb"><b>{s_[0]}</b><span>{s_[1]}</span></div><div class="sp"></div></div>')
        rows.append(f'<div class="rm" style="grid-template-columns:repeat({per_row},1fr);--ry:{ry}">' + "".join(out) + "</div>")
    return "".join(rows)


def itiles(items, cols=2, gap="3mm 5mm"):
    """Icon + title + text tiles. items: (icon, title, text)"""
    return grid([f'<div class="itile">{tile(i, "9mm", "5mm")}<div><b>{t}</b><span>{x}</span></div></div>' for i, t, x in items], cols, gap=gap)


def compare(a_title, a_items, b_title, b_items):
    li = lambda xs: "".join(f'<p class="small" style="color:var(--body);margin-bottom:1.2mm">{x}</p>' for x in xs)
    return (f'<div class="cmp"><div class="a"><h5>{icon("x", "3.4mm", "#C72D35", 2.4)}{a_title}</h5>{li(a_items)}</div>'
            f'<div class="b"><h5>{icon("check", "3.4mm", "#279B70", 2.4)}{b_title}</h5>{li(b_items)}</div></div>')


OPENER_PHOTO = {"meet": "gallery/g02.jpg", "test": "gallery/g08.jpg", "dims": "gallery/g14.jpg", "report": "gallery/g10.jpg", "dash": "gallery/g16.jpg",
                "skills": "gallery/g11.jpg", "startup": "gallery/g04.jpg", "research": "gallery/g05.jpg", "family": "gallery/g12.jpg", "action": "gallery/g15.jpg"}


def divider(part, key, title, sub, items, art=None, art2=None):
    theme(key)
    TOC.append(("part", part, title, len(PAGES), key))
    stops = "".join(f'<div class="stop"><span>{i + 1:02d}</span><div><b>{t}</b><em>{{{{REF:{t}}}}}</em></div></div>' for i, t in enumerate(items))
    add(f'''<div class="op"><div class="panel"><div class="pin">
<div class="num">{part:02d}</div><div class="part">Part {part:02d}</div>
<div class="icon">{icon(CH_ICON.get(key, "compass"), "9mm", "#fff", 1.6)}</div>
<h1>{title}</h1><p class="sub">{sub}</p></div>
<div class="logo">{img("art/logo.png")}</div></div>
<img class="photo3" src="assets/{OPENER_PHOTO.get(key, "gallery/g02.jpg")}" alt="">
<div class="route"><div class="rh3">{icon("route", "4mm", "currentColor", 2)} In this part</div>{stops}</div></div>''', section=title, kind="divider")


# ---------------------------------------------------------------- quotes (v4)
OPQ = {"meet": ("Education is the most powerful weapon which you can use to change the world.", "Nelson Mandela"),
       "test": ("The unexamined life is not worth living.", "Socrates, in Plato's Apology"),
       "dims": ("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs, Stanford, 2005"),
       "report": ("Dream is not that which you see while sleeping, it is something that does not let you sleep.", "A. P. J. Abdul Kalam"),
       "dash": ("The best way to predict the future is to invent it.", "Alan Kay"),
       "skills": ("Excellence is a continuous process and not an accident.", "A. P. J. Abdul Kalam"),
       "startup": ("I don't believe in taking right decisions. I take decisions and then make them right.", "Ratan Tata"),
       "research": ("Nothing in life is to be feared, it is only to be understood.", "Marie Curie"),
       "family": ("Children must be taught how to think, not what to think.", "Margaret Mead"),
       "action": ("Arise, awake, and stop not till the goal is reached.", "Swami Vivekananda")}


def qband(text, who, color=None):
    c = f' style="--qc:{color}"' if color else ""
    return f'<blockquote class="qb"{c}><p>{text}</p><cite>{who}</cite></blockquote>'


def quote_page(text, who, photo, color="#C72D35"):
    bar = "".join(f'<i style="background:{c}"></i>' for c in ("#C72D35", "#F09A24", "#E5B73B", "#279B70", "#2196C8", "#7754B8"))
    add(f'''<div class="qpage" style="--c1:{color}"><img src="assets/{photo}" alt=""><div class="bar">{bar}</div>
<div class="qtx"><p>{text}</p><cite>{who}</cite></div>
<div class="ft"><span>Career Fitment Handbook 2026–27</span><span>OneGrasp Education Pvt. Ltd.</span></div></div>''', kind="full")


_div_old = divider


def divider(part, key, title, sub, items, art=None, art2=None):
    _div_old(part, key, title, sub, items, art, art2)
    q = OPQ.get(key)
    if q:
        PAGES[-1]["body"] = PAGES[-1]["body"][:-len("</div>")] + f'<blockquote class="oq">“{q[0]}”<cite>{q[1]}</cite></blockquote></div>'
