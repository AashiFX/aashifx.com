"""Modern, abstract hero directions for AashiFX (900x780): glass, contour, ribbons, blueprint."""
import os, math, random
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "hero_modern")
G="#d9b44a"; Y="#f1d98a"; B="#3ea6ff"; T="#2fd0a0"; P="#9b7bff"; O="#ff8a4a"; W="#f7f9fc"; C="#7cf0ff"
NAMES = [("BrandX","Branding & Creative Design"),("OfficeX","SmartDocs & Documentation"),("TechX","IT & Digital Solutions"),("TradeX","Trading, Procurement & Supply"),("DriveX","Transportation & Mobility"),("PowerX","Equipment & Industrial Support")]
COLS = [B, G, C, T, O, P]
SANS = 'font-family="Inter,\'Segoe UI\',system-ui,Arial,sans-serif"'; SERIF = 'font-family="Georgia,\'Times New Roman\',serif"'
GLYPH = {
 0: '<circle cx="-10" cy="-6" r="16"/><circle cx="10" cy="-6" r="16"/><circle cx="0" cy="10" r="16"/>',
 1: '<path d="M-18 -26h24l12 12v40h-36z M6 -26v12h12 M-10 0h20 M-10 10h20 M-10 20h12"/>',
 2: '<path d="M-16 -16h32v32h-32z M-6 -6h12v12h-12z M-8 -26v10 M8 -26v10 M-8 16v10 M8 16v10 M-26 -8h10 M-26 8h10 M16 -8h10 M16 8h10"/>',
 3: '<path d="M0 -26L24 -13V13L0 26L-24 13V-13Z M0 0L24 -13 M0 0L-24 -13 M0 0V26"/>',
 4: '<path d="M-28 10L-22 -4Q-18 -14 -8 -14H10Q20 -14 24 -4L30 10 M-30 10h60v8h-60z"/><circle cx="-16" cy="22" r="5"/><circle cx="16" cy="22" r="5"/>',
 5: '<path d="M6 -28L-14 4H0L-6 28L16 -6H2Z"/>'}
def glyph(i, x, y, s=1, col=W, sw=2.6): return f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{GLYPH[i]}</g>'
GRAIN = '<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0"/></filter>'
def wrap(defs, body, grain=.07): return f'<svg viewBox="0 0 900 780" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice"><defs>{defs}{GRAIN}<filter id="b60" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter><filter id="b24" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="24"/></filter><filter id="b6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter></defs>{body}<rect width="900" height="780" filter="url(#grain)" opacity="{grain}"/></svg>'

# ---------- A. Aurora Glass ----------
def optA():
    defs = '<linearGradient id="gs" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".65"/><stop offset=".5" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity=".3"/></linearGradient><linearGradient id="gf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset="1" stop-color="#fff" stop-opacity=".03"/></linearGradient>'
    blobs = (f'<g filter="url(#b60)"><circle cx="690" cy="170" r="230" fill="{G}" opacity=".6"/><circle cx="170" cy="230" r="250" fill="{B}" opacity=".55"/><circle cx="290" cy="660" r="240" fill="{T}" opacity=".45"/><circle cx="740" cy="640" r="230" fill="{P}" opacity=".5"/></g>')
    grid = ''.join(f'<path d="M{x} 0V780" stroke="#fff" stroke-opacity=".035"/>' for x in range(0,900,60)) + ''.join(f'<path d="M0 {y}H900" stroke="#fff" stroke-opacity=".035"/>' for y in range(0,780,60))
    cards = ''
    pos = [(52,86),(488,66),(52,296),(488,276),(52,506),(488,486)]
    for i,((nm,sub),(x,y)) in enumerate(zip(NAMES,pos)):
        col = COLS[i]
        cards += (f'<g><rect x="{x}" y="{y}" width="360" height="176" rx="30" fill="#0a1030" opacity=".35"/><rect x="{x}" y="{y}" width="360" height="176" rx="30" fill="url(#gf)" stroke="url(#gs)" stroke-width="1.6"/>'
                  f'<circle cx="{x+78}" cy="{y+88}" r="52" fill="{col}" opacity=".16"/><circle cx="{x+78}" cy="{y+88}" r="52" fill="none" stroke="{col}" stroke-opacity=".7" stroke-width="1.4"/>'
                  + glyph(i, x+78, y+88, 1.05, W) +
                  f'<text x="{x+150}" y="{y+84}" {SERIF} font-size="34" fill="#fff">{nm}</text><text x="{x+150}" y="{y+114}" {SANS} font-size="14.5" fill="#fff" opacity=".7">{sub}</text>'
                  f'<path d="M{x+150} {y+136}H{x+300}" stroke="{col}" stroke-width="3" stroke-linecap="round"/></g>')
    return wrap(defs, '<rect width="900" height="780" fill="#050818"/>' + blobs + grid + cards, .09)

# ---------- B. Gold Contour ----------
def optB():
    defs = f'<radialGradient id="bgc" cx=".5" cy=".5" r=".7"><stop offset="0" stop-color="#14224f"/><stop offset=".7" stop-color="#070c22"/><stop offset="1" stop-color="#03050e"/></radialGradient><radialGradient id="orb"><stop offset="0" stop-color="#fff6d2"/><stop offset=".35" stop-color="{G}"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient><linearGradient id="st1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{Y}"/><stop offset="1" stop-color="{G}"/></linearGradient><linearGradient id="st2" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{B}"/><stop offset="1" stop-color="{C}"/></linearGradient>'
    cx, cy = 450, 392; rings = ''
    N = 38
    for i in range(N):
        Rr = 36 + i*10.6; ph = i*.16
        pts = []
        for a in range(0, 360, 4):
            t = math.radians(a)
            rr = Rr*(1 + .05*math.sin(3*t+ph) + .03*math.sin(5*t+2*ph) + .012*math.sin(8*t+ph*1.7))
            pts.append((cx + rr*math.cos(t)*1.05, cy + rr*math.sin(t)*.9))
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x,y in pts) + "Z"
        grad = "url(#st1)" if i % 2 == 0 else "url(#st2)"
        op = max(.08, .9 - i*.021); w = 2.4 if i % 6 == 0 else 1.1
        rings += f'<path d="{d}" fill="none" stroke="{grad}" stroke-width="{w}" stroke-opacity="{op:.2f}"/>'
    nodes = ''
    for i,(nm,sub) in enumerate(NAMES):
        a = math.radians(-90 + i*60); R_ = 262
        x, y = cx + R_*math.cos(a)*1.05, cy + R_*math.sin(a)*.9
        lx, ly = cx + (R_+62)*math.cos(a)*1.05, cy + (R_+62)*math.sin(a)*.9
        anchor = "middle" if abs(math.cos(a)) < .2 else ("start" if math.cos(a) > 0 else "end")
        dy = -14 if math.sin(a) < -.5 else (30 if math.sin(a) > .5 else 4)
        nodes += (f'<path d="M{cx} {cy}L{x:.1f} {y:.1f}" stroke="{G}" stroke-opacity=".28" stroke-dasharray="2 8"/><circle cx="{x:.1f}" cy="{y:.1f}" r="16" fill="#060b20" stroke="{G}" stroke-width="2"/>'
                  + glyph(i, x, y, .3, Y, 3.2) +
                  f'<text x="{lx:.1f}" y="{ly+dy:.1f}" text-anchor="{anchor}" {SERIF} font-size="25" fill="#f2f4fa">{nm}</text>')
    core = f'<circle cx="{cx}" cy="{cy}" r="120" fill="url(#orb)" opacity=".85" filter="url(#b24)"/><circle cx="{cx}" cy="{cy}" r="34" fill="url(#orb)"/><g stroke="#05070f" stroke-width="7" stroke-linecap="round" transform="translate({cx} {cy})"><path d="M-14 -14L14 14M14 -14L-14 14"/></g>'
    ticks = ''.join(f'<path d="M{x} 758v12" stroke="#fff" stroke-opacity=".22"/>' for x in range(30,900,30))
    return wrap(defs, '<rect width="900" height="780" fill="url(#bgc)"/>' + rings + nodes + core + ticks, .08)

# ---------- C. Silk Ribbons ----------
def optC():
    defs = f'<radialGradient id="bgc" cx=".55" cy=".5" r=".8"><stop offset="0" stop-color="#101d4a"/><stop offset="1" stop-color="#03050e"/></radialGradient><radialGradient id="core"><stop offset="0" stop-color="#fff"/><stop offset=".25" stop-color="{Y}"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient><linearGradient id="beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{Y}" stop-opacity=".95"/><stop offset="1" stop-color="{Y}" stop-opacity="0"/></linearGradient>'
    ys = [110, 230, 350, 470, 590, 700]; cx, cy = 480, 390; rib = ''; labels = ''
    for k, y0 in enumerate(ys):
        col = COLS[k]; sgn = (k - 2.5)
        for j in range(18):
            off = (j - 9) * 2.9; sp = (j - 9) * .5
            d = f"M-30 {y0+off:.1f}C230 {y0 - sgn*70 + off*1.2:.1f} 330 {cy + sgn*34 + off*.6:.1f} {cx} {cy + sp*.25:.1f}"
            rib += f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.3" stroke-opacity="{.22 + .5*(1-abs(j-9)/9):.2f}"/>'
        labels += f'<circle cx="26" cy="{y0}" r="5" fill="{col}"/><text x="42" y="{y0+7}" {SANS} font-size="20" font-weight="600" fill="#f2f4fa" letter-spacing="1.2">{NAMES[k][0].upper()}</text>'
    out = ''
    for j in range(22):
        off = (j - 11) * 1.4; a = 1 - abs(j - 11)/11
        out += f'<path d="M{cx} {cy+off*.15:.1f}C{cx+140} {cy+off*1.4:.1f} {cx+280} {cy-off*3.2:.1f} 940 {cy+off*5.5:.1f}" fill="none" stroke="url(#beam)" stroke-width="1.3" stroke-opacity="{.15+.6*a:.2f}"/>'
    core = f'<circle cx="{cx}" cy="{cy}" r="190" fill="url(#core)" opacity=".55" filter="url(#b24)"/><circle cx="{cx}" cy="{cy}" r="44" fill="url(#core)"/><circle cx="{cx}" cy="{cy}" r="74" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="1.2"/><circle cx="{cx}" cy="{cy}" r="110" fill="none" stroke="{Y}" stroke-opacity=".3" stroke-dasharray="3 9"/>'
    stars = ''.join(f'<circle cx="{random.Random(i).randint(10,890)}" cy="{random.Random(i*3).randint(10,770)}" r="{random.Random(i*5).choice([.7,1,1.4])}" fill="#fff" opacity=".35"/>' for i in range(90))
    tag = f'<text x="450" y="752" text-anchor="middle" {SERIF} font-style="italic" font-size="26" fill="{Y}">Design. Document. Deliver.</text>'
    return wrap(defs, '<rect width="900" height="780" fill="url(#bgc)"/>' + stars + rib + out + core + labels + tag, .08)

# ---------- D. Blueprint City ----------
def wire(cx, by, w, h, col, detail=0):
    hw, hd = w*.866, w*.5
    top = [(cx, by-h-hd), (cx+hw, by-h), (cx, by-h+hd), (cx-hw, by-h)]; bot = [(cx, by-hd), (cx+hw, by), (cx, by+hd), (cx-hw, by)]
    s = f'<path d="M{" L".join(f"{x:.1f} {y:.1f}" for x,y in top)}Z" fill="{col}" fill-opacity=".14" stroke="{col}" stroke-width="2"/>'
    s += f'<path d="M{top[3][0]:.1f} {top[3][1]:.1f}V{bot[3][1]:.1f}L{bot[2][0]:.1f} {bot[2][1]:.1f}V{top[2][1]:.1f}M{top[1][0]:.1f} {top[1][1]:.1f}V{bot[1][1]:.1f}L{bot[2][0]:.1f} {bot[2][1]:.1f}" fill="{col}" fill-opacity=".07" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>'
    for t_ in range(1, detail+1):
        yy = h*t_/(detail+1)
        s += f'<path d="M{cx-hw:.1f} {by-yy:.1f}L{cx:.1f} {by-yy+hd:.1f}L{cx+hw:.1f} {by-yy:.1f}" fill="none" stroke="{col}" stroke-opacity=".45" stroke-width="1"/>'
    return s
def optD():
    defs = '<linearGradient id="bgc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a1c4a"/><stop offset="1" stop-color="#030818"/></linearGradient><pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.1" fill="#9fb8ff" opacity=".35"/></pattern>'
    cx, cy = 450, 490; lat = ''
    for i in range(-9, 10):
        lat += f'<path d="M{cx+i*52-460*.866*1:.0f} {cy-460*.5*1:.0f}L{cx+i*52+460*.866:.0f} {cy+460*.5:.0f}" stroke="{B}" stroke-opacity=".16"/>'
        lat += f'<path d="M{cx+i*52+460*.866:.0f} {cy-460*.5:.0f}L{cx+i*52-460*.866:.0f} {cy+460*.5:.0f}" stroke="{B}" stroke-opacity=".16"/>'
    pos = [(310,380,96,150,B,5),(590,380,96,230,G,8),(700,500,96,300,C,10),(320,640,100,76,T,3),(205,500,90,100,O,3),(580,640,100,64,P,2)]
    order = sorted(range(6), key=lambda i: pos[i][1])
    shapes = ''; lab = ''
    for i in order:
        x, y, w, h, col, dt = pos[i]; shapes += wire(x, y+30, w*.8, h, col, dt)
    for i,(x,y,w,h,col,dt) in enumerate(pos):
        lx = 70 if x < 450 else 830; anc = "start" if x < 450 else "end"; ly = y - h - 70 + 10
        top_y = y + 30 - h - w*.4*.5
        lab += f'<path d="M{x} {top_y-4:.0f}L{x} {ly+16:.0f}" stroke="{col}" stroke-opacity=".7" stroke-dasharray="3 5"/><circle cx="{x}" cy="{top_y-4:.0f}" r="4" fill="{col}"/>'
        lab += f'<text x="{x}" y="{ly:.0f}" text-anchor="middle" {SANS} font-size="12.5" letter-spacing="2" fill="{col}">0{i+1}</text><text x="{x}" y="{ly-16:.0f}" text-anchor="middle" {SERIF} font-size="24" fill="#f2f4fa">{NAMES[i][0]}</text>'
    links = ''.join(f'<path d="M450 490L{x} {y+30}" stroke="{G}" stroke-opacity=".5" stroke-dasharray="2 9" stroke-width="1.6"/>' for x,y,*_ in pos)
    core = f'<circle cx="450" cy="490" r="64" fill="{G}" opacity=".25" filter="url(#b24)"/><path d="M450 460L482 478V502L450 520L418 502V478Z" fill="none" stroke="{Y}" stroke-width="2.4"/><path d="M438 480L462 500M462 480L438 500" stroke="{Y}" stroke-width="3" stroke-linecap="round"/>'
    title = f'<text x="40" y="52" {SANS} font-size="12" letter-spacing="3" fill="#9fb8ff" opacity=".8">AASHIFX · SIX PILLARS · ONE ESTABLISHMENT</text><path d="M40 66H320" stroke="#9fb8ff" stroke-opacity=".4"/><text x="860" y="750" text-anchor="end" {SANS} font-size="11" letter-spacing="2.5" fill="#9fb8ff" opacity=".7">INDIA · GCC</text>'
    return wrap(defs, '<rect width="900" height="780" fill="url(#bgc)"/><rect width="900" height="780" fill="url(#dots)"/>' + lat + links + shapes + core + lab + title, .06)

OPTS = [("A-aurora-glass","Aurora Glass","Deep gradient glow with frosted glass cards, fine line icons and grain. Editorial, UI-art feel."),
        ("B-gold-contour","Gold Contour","Topographic contour lines in gold and blue radiating from a glowing core. Luxury, abstract."),
        ("C-silk-ribbons","Silk Ribbons","Six threads of light, one per pillar, flowing into one core and out as one beam."),
        ("D-blueprint-city","Blueprint City","Fine-line isometric architecture drawing of six pillars on a dotted blueprint, with index markers.")]
FN = {"A-aurora-glass": optA, "B-gold-contour": optB, "C-silk-ribbons": optC, "D-blueprint-city": optD}
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f, *_ in OPTS: open(os.path.join(OUT, f + ".svg"), "w").write(FN[f]())
    print([(f, os.path.getsize(os.path.join(OUT, f + ".svg"))) for f, *_ in OPTS])
