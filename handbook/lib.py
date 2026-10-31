"""Page-building helpers for the OneGrasp Career Fitment Handbook.

Every helper returns an HTML string. A page is one A4 sheet; build.py
collects them in order, numbers them and prints the PDF with Chromium.
"""
import html as _html

E = _html.escape

PAGES = []          # (kind, html) in book order
TOC = []            # ("part", no, title, page_index) / ("sub", None, title, page_index)


def add(body, kind="std", section="", dark=False, bg=None):
    PAGES.append({"kind": kind, "body": body, "section": section, "dark": dark, "bg": bg})


def placeholder(label):
    """Marks where a page copied from an existing Canva design is merged in."""
    PAGES.append({"kind": "canva", "body": "", "section": label, "dark": False, "bg": None})


# ---------- small building blocks ----------

def img(src, cls="", alt="", style=""):
    return f'<img src="assets/{src}" class="{cls}" alt="{E(alt)}" style="{style}">'


def shot(src, caption="", cls="", style="", url="careerfitment.onegrasp.com"):
    """A screenshot in a browser frame."""
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return (f'<figure class="shot {cls}" style="{style}"><div class="chrome"><i></i><i></i><i></i>'
            f'<span>{E(url)}</span></div><img src="assets/{src}" alt=""></figure>{cap}')


def head(eyebrow, t1, t2="", lead=""):
    t2h = f'<span class="red">{t2}</span>' if t2 else ""
    br = "<br>" if t2 else ""
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="eyebrow">{eyebrow}</div><h1 class="title">{t1}{br}{t2h}</h1>{ld}'


def cards(items, cols=2, cls=""):
    """items: (title, text) or (num/icon, title, text)."""
    out = []
    for it in items:
        if len(it) == 3:
            n, t, x = it
            out.append(f'<div class="card"><div class="cnum">{n}</div><h4>{t}</h4><p>{x}</p></div>')
        else:
            t, x = it
            out.append(f'<div class="card"><h4>{t}</h4><p>{x}</p></div>')
    return f'<div class="grid g{cols} {cls}">{"".join(out)}</div>'


def stats(items, cls=""):
    return '<div class="stats ' + cls + '">' + "".join(
        f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in items) + "</div>"


def bullets(items, cls=""):
    return f'<ul class="ticks {cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def steps(items, cls=""):
    out = []
    for i, it in enumerate(items, 1):
        t, x = it
        out.append(f'<div class="step"><div class="sn">{i}</div><div><h4>{t}</h4><p>{x}</p></div></div>')
    return f'<div class="steps {cls}">{"".join(out)}</div>'


def note(label, text, cls=""):
    return f'<div class="note {cls}"><b>{label}</b> {text}</div>'


def band(label, text, cls=""):
    return f'<div class="band {cls}"><div class="bl">{label}</div><div class="bt">{text}</div></div>'


def findit(*crumbs):
    return '<div class="findit"><b>Find it</b> ' + ' <span>›</span> '.join(crumbs) + '</div>'


def table(header, rows, cls="", widths=None):
    cg = ""
    if widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    th = "".join(f"<th>{h}</th>" for h in header)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="tbl {cls}">{cg}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def two(a, b, cls="", ratio="1fr 1fr"):
    return f'<div class="two {cls}" style="grid-template-columns:{ratio}"><div>{a}</div><div>{b}</div></div>'


def box(inner, cls=""):
    return f'<div class="box {cls}">{inner}</div>'


def h3(t):
    return f'<h3 class="h3">{t}</h3>'


def p(t, cls=""):
    return f'<p class="{cls}">{t}</p>'


def kv(items, cls=""):
    return '<dl class="kv ' + cls + '">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in items) + "</dl>"


def divider(part, title, sub, items, image=None):
    """A dark section-opening page."""
    lis = "".join(f"<li>{i}</li>" for i in items)
    im = img(image, "div-art") if image else ""
    TOC.append(("part", part, title, len(PAGES)))
    add(f'''<div class="div-wrap"><div class="div-part">PART {part:02d}</div>
<h1 class="div-title">{title}</h1><p class="div-sub">{sub}</p>
<div class="div-list"><div class="eyebrow light">In this part</div><ol>{lis}</ol></div>{im}</div>''',
        kind="divider", section=title, dark=True)


def mark(title):
    """Adds a contents entry pointing at the next page added."""
    TOC.append(("sub", None, title, len(PAGES)))
