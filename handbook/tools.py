"""A dashboard tool as a 3-page chapter: opener, how it works, and a mission card.

Each tool gets its own colour (it overrides the part's theme on its pages).
"""
from lib import *


def tool_theme(key, name, c1, c2):
    THEMES[key] = (name, c1, c2, f"color-mix(in srgb, {c1} 9%, white)", f"color-mix(in srgb, {c1} 70%, #1E2340)")
    theme(key)


def opener(no, name, tagline, art, stats_, who, why, inside, find, section):
    """Page A: the tool's opener."""
    st = "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in stats_)
    ins = "".join(f'<div class="ins">{chip(ic, size="9mm", isz="4.8mm")}<div><b>{t}</b><span>{x}</span></div></div>' for ic, t, x in inside)
    wh = "".join(f'<div class="why"><span>{i + 1}</span><p>{w}</p></div>' for i, w in enumerate(why))
    add(f'''<div class="th"><div class="th-dots"></div><div class="th-no">TOOL {no:02d}</div>
<div class="th-txt"><div class="kicker" style="color:#FFE08A">Your dashboard</div><h1>{name}</h1><p>{tagline}</p>
<div class="th-st">{st}</div></div>{img(art, "th-art")}</div>'''
        + two(box(h3("Why it matters", "target") + wh), box(h3("Who it's for", "users") + who + findit(*find), "soft"), ratio="1.15fr 0.85fr", gap="4mm")
        + h3("What's inside", "layout-grid")
        + f'<div class="inside">{ins}</div>',
        section=section)


def howto(name, shots, steps_, notes, section):
    """Page B: how it works, with screenshots and numbered steps."""
    top = laptop("shots/" + shots[0][0] + ".jpg", shots[0][1])
    rest = ""
    if len(shots) > 1:
        rest = grid([browser("shots/" + s + ".jpg", c) for s, c in shots[1:]], len(shots) - 1, "mt", gap="4mm")
    add(head(f"{name} · How it works", "How to use it,", "step by step.")
        + two(top, vsteps(steps_), ratio="1.12fr 0.88fr", gap="5mm") + rest
        + grid(notes, len(notes), "push", gap="4mm"),
        section=section)


def mission(name, missions, worksheet, reward, section):
    """Page C: the practical mission card + worksheet."""
    ms = []
    for i, (t, time, tasks) in enumerate(missions, 1):
        tk = "".join(f'<div class="check"><i></i><span>{x}</span></div>' for x in tasks)
        ms.append(f'<div class="ms"><div class="msh"><span>MISSION {i}</span><em>{icon("clock", "3.4mm", "#fff")} {time}</em></div><b>{t}</b>{tk}</div>')
    add(head(f"{name} · Do it now", "Your missions.", "Tick them off.", "Do these on your dashboard, then fill in the worksheet. Small, real actions beat reading about careers.")
        + grid(ms, len(ms), gap="3.4mm")
        + h3("Your worksheet", "pen-line") + worksheet
        + f'<div class="done push">{icon("party-popper", "8mm", "var(--c1)")}<div><b>Mission complete!</b><span>{reward}</span></div>'
          f'<div class="sig"><span>Done on</span><i></i></div><div class="sig"><span>Checked by parent / teacher</span><i></i></div></div>',
        section=section)


def wtable(cols, rows=5, widths=None, prefill=None):
    """A blank fill-in table."""
    body = []
    for r in range(rows):
        if prefill and r < len(prefill):
            body.append(prefill[r] + [""] * (len(cols) - len(prefill[r])))
        else:
            body.append(["&nbsp;"] * len(cols))
    return table(cols, body, "fill", widths)
