"""AashiFX modern illustration system: aurora glow + gold contours + frosted glass + fine line icons + grain."""
import math, random
G="#c9d3e6"; Y="#eef3fb"; B="#3ea6ff"; T="#2fd0a0"; P="#6f8cff"; O="#ff8a4a"; W="#f7f9fc"; C="#7cf0ff"
SANS = 'font-family="Inter,\'Segoe UI\',system-ui,Arial,sans-serif"'; SERIF = 'font-family="Georgia,\'Times New Roman\',serif"'
def _c(x,y,r): return f'<circle cx="{x}" cy="{y}" r="{r}"/>'
GL = {  # fine line glyphs, drawn around (0,0) within about +-28
 "brand3": _c(-10,-6,16)+_c(10,-6,16)+_c(0,10,16),
 "doc": '<path d="M-18 -26h24l12 12v40h-36z M6 -26v12h12 M-10 0h20 M-10 10h20 M-10 20h12"/>',
 "chip": '<path d="M-16 -16h32v32h-32z M-6 -6h12v12h-12z M-8 -26v10 M8 -26v10 M-8 16v10 M8 16v10 M-26 -8h10 M-26 8h10 M16 -8h10 M16 8h10"/>',
 "cube": '<path d="M0 -26L24 -13V13L0 26L-24 13V-13Z M0 0L24 -13 M0 0L-24 -13 M0 0V26"/>',
 "car": '<path d="M-28 10L-22 -4Q-18 -14 -8 -14H10Q20 -14 24 -4L30 10 M-30 10h60v8h-60z"/>'+_c(-16,22,5)+_c(16,22,5),
 "bolt": '<path d="M6 -28L-14 4H0L-6 28L16 -6H2Z"/>',
 "building": '<path d="M-14 26V-26h28V26 M-20 26h40 M-8 -18h4 M4 -18h4 M-8 -8h4 M4 -8h4 M-8 2h4 M4 2h4 M-4 26v-10h8v10"/>',
 "pen": '<path d="M-22 22l4-12 22-22 8 8-22 22z M2 -8l8 8"/>',
 "megaphone": '<path d="M-24 -6h8l22 -16v44l-22 -16h-8z M-16 16l4 12h8l-4 -12 M16 -6c4 3 4 9 0 12"/>',
 "phone": '<path d="M-12 -28h24a4 4 0 0 1 4 4v48a4 4 0 0 1-4 4h-24a4 4 0 0 1-4-4v-48a4 4 0 0 1 4-4z M-4 20h8"/>',
 "chart": '<path d="M-24 26V-22 M-24 26h48 M-14 20V4 M-2 20V-10 M10 20V-2 M22 20V-18"/>',
 "gear": '<path d="M0 -28v8 M0 28v-8 M-28 0h8 M28 0h-8 M-20 -20l6 6 M20 20l-6 -6 M-20 20l6 -6 M20 -20l-6 6"/>'+_c(0,0,12)+_c(0,0,20),
 "server": '<path d="M-24 -26h48v16h-48z M-24 -6h48v16h-48z M-24 14h48v14h-48z M-16 -18h2 M-16 2h2 M-16 21h2"/>',
 "shield": '<path d="M0 -28L24 -20V2C24 16 12 24 0 28C-12 24 -24 16 -24 2V-20Z M-8 2l6 6 12-14"/>',
 "cloud": '<path d="M-18 18h30a10 10 0 0 0 2-20 14 14 0 0 0-27-4 11 11 0 0 0-5 24z"/>',
 "database": '<ellipse cx="0" cy="-16" rx="20" ry="8"/><path d="M-20 -16v32a20 8 0 0 0 40 0v-32 M-20 0a20 8 0 0 0 40 0"/>',
 "network": _c(0,-20,6)+_c(-20,18,6)+_c(20,18,6)+_c(0,2,8)+'<path d="M0 -14V-6 M-6 8L-16 14 M6 8L16 14"/>',
 "wrench": '<path d="M20 -22a11 11 0 0 0-14 14L-20 18a4 4 0 0 0 6 6L8 2a11 11 0 0 0 14-14l-8 8-7-7z"/>',
 "magnifier": _c(-5,-5,18)+'<path d="M8 8l18 18"/>',
 "cart": '<path d="M-28 -22h8l6 32h30l6 -22h-40 M-8 20h.1 M18 20h.1"/>'+_c(-8,21,3)+_c(18,21,3),
 "helmet": '<path d="M-22 8a22 22 0 0 1 44 0z M-28 8h56v6h-56z M-3 -16v12"/>',
 "flask": '<path d="M-8 -28h16 M-6 -28v18L-22 20a4 4 0 0 0 4 6h36a4 4 0 0 0 4-6L6 -10v-18 M-14 8h28"/>',
 "microscope": '<path d="M-8 -28l12 6-8 20-12-6z M6 -4a14 14 0 0 1 6 24 M-18 26h36 M-2 -14l4 2"/>',
 "truck": '<path d="M-28 -14h30v26h-30z M2 -4h16l10 10v6h-26z"/>'+_c(-14,16,5)+_c(18,16,5),
 "bus": '<path d="M-26 -22h52v34h-52z M-26 -6h52 M-19 -14h8 M-4 -14h8 M11 -14h8 M-16 12v6 M16 12v6"/>'+_c(-14,20,4)+_c(14,20,4),
 "pin": '<path d="M0 28C-14 12-22 2-22 -8a22 22 0 0 1 44 0C22 2 14 12 0 28z"/>'+_c(0,-8,7),
 "key": _c(-14,0,11)+'<path d="M-3 0h28 M16 0v9 M23 0v6"/>',
 "crane": '<path d="M-6 28V-18 M6 28V-18 M-6 -6l12 -12 M-6 8l12 -14 M-26 -18h44 M6 -18l-20 -10 M-20 -18v14 M-20 -4l-3 6h6z M-12 28h24"/>',
 "excavator": '<path d="M-28 24h40v-8h-40z M-24 16V6h20v10 M-24 6V-6h12v12 M-4 8L12 -16l14 6 M26 -10l-6 14l12 4z"/>'+_c(-20,20,2),
 "generator": '<path d="M-26 -12h52v28h-52z M-18 16v6 M18 16v6 M-14 -4h14 M-14 4h14 M6 -6l-6 8h8l-4 8l10 -12h-8z"/>',
 "people": _c(-10,-10,7)+'<path d="M-24 20a14 14 0 0 1 28 0"/>'+_c(14,-6,6)+'<path d="M6 20a12 12 0 0 1 22 0"/>',
 "folder": '<path d="M-26 -18h16l4 6h32v30h-52z"/>',
 "stamp": '<path d="M-10 -28h20v14h-20z M-16 -14h32v14h-32z M-24 4h48v8h-48z M-24 22h48"/>',
 "checklist": '<path d="M-24 -18l4 4 8 -8 M-24 0l4 4 8 -8 M-24 18l4 4 8 -8 M-2 -16h24 M-2 2h24 M-2 20h24"/>',
 "laptop": '<path d="M-20 -18h40v28h-40z M-28 20h56"/>',
 "globe": _c(0,0,22)+'<path d="M-22 0h44 M0 -22a30 30 0 0 1 0 44 M0 -22a30 30 0 0 0 0 44"/>',
 "wifi": '<path d="M-24 -4a34 34 0 0 1 48 0 M-16 6a22 22 0 0 1 32 0 M-8 16a10 10 0 0 1 16 0"/>'+_c(0,24,2),
 "lock": '<path d="M-16 -2h32v26h-32z M-10 -2v-10a10 10 0 0 1 20 0v10 M0 8v6"/>',
 "bulb": '<path d="M-8 14h16 M-6 22h12 M-16 -4a16 16 0 1 1 32 0c0 8-6 10-7 18h-18c-1-8-7-10-7-18z"/>',
 "compass": _c(0,0,24)+'<path d="M-9 9L-5 -5 9 -9 5 5z"/>',
 "calendar": '<path d="M-24 -18h48v42h-48z M-24 -4h48 M-12 -26v12 M12 -26v12 M-12 8h.1 M0 8h.1 M12 8h.1"/>',
 "brochure": '<path d="M-28 -16l18 4v32l-18 -4z M-10 -12l20 -4v32l-20 4z M10 -16l18 4v32l-18 -4z"/>',
 "poster": '<path d="M-18 -28h36v56h-36z M-10 -16h20 M-10 -6h20 M-10 4h12 M-10 16h6"/>',
 "steering": _c(0,0,24)+_c(0,0,5)+'<path d="M-24 0h14 M24 0h-14 M0 5v19"/>',
 "route": '<path d="M-22 22C-22 2 0 12 0 -8S22 -8 22 -24"/>'+_c(-22,22,4)+_c(22,-24,4),
 "flowchart": '<path d="M-8 -28h16v10h-16z M-26 8h16v12h-16z M10 8h16v12h-16z M0 -18v8 M-18 8v-10h36v10"/>',
 "layers": '<path d="M0 -24L26 -11 0 2-26 -11z M-26 1L0 14 26 1 M-26 13L0 26 26 13"/>',
 "palette": '<path d="M0 -26a26 26 0 1 0 0 52c5 0 6-4 4-7s0-7 6-7h8a8 8 0 0 0 8-8c0-18-12-30-26-30z"/>'+_c(-10,-8,2)+_c(2,-14,2)+_c(12,-6,2)+_c(-14,6,2),
 "image": '<path d="M-26 -20h52v40h-52z M-26 12l16 -14 10 10 8 -8 18 18"/>'+_c(-12,-8,4),
 "calculator": '<path d="M-16 -26h32v52h-32z M-10 -20h20v10h-20z M-8 2h.1 M0 2h.1 M8 2h.1 M-8 12h.1 M0 12h.1 M8 12h.1 M-8 20h.1 M0 20h.1 M8 20h.1"/>',
 "clipboard": '<path d="M-16 -20h32v46h-32z M-8 -26h16v8h-16z M-8 -4h16 M-8 6h16 M-8 16h10"/>',
 "languages": '<path d="M-26 -14h26 M-13 -22v8 M-22 -14c2 12 10 18 18 22 M-4 -14c-2 12 -10 18 -18 22 M4 26l9 -26 9 26 M7 16h12"/>',
 "cabinet": '<path d="M-20 -26h40v52h-40z M-20 0h40 M-6 -13h12 M-6 13h12"/>',
 "tag": '<path d="M-26 -2l22 -22h20v20l-22 22z"/>'+_c(8,-12,2),
 "target": _c(0,0,24)+_c(0,0,14)+_c(0,0,4),
 "chat": '<path d="M-24 -20h48v30h-20l-12 12v-12h-16z M-12 -8h24 M-12 2h14"/>',
 "download": '<path d="M0 -24v32 M-12 -4l12 12 12-12 M-24 24h48"/>',
 "terminal": '<path d="M-26 -20h52v40h-52z M-16 -8l8 6-8 6 M-2 8h14"/>',
 "sync": '<path d="M22 -8a24 24 0 0 0-42 -4 M-22 8a24 24 0 0 0 42 4 M22 -24v16h-16 M-22 24v-16h16"/>',
 "pulse": '<path d="M-28 0h12l6 -16 10 32 6 -16h14"/>',
}
# which glyphs each page shows: slug -> (main, secondary1, secondary2)
SG = {
 "logo-identity":("brand3","pen","palette"),"corporate-branding":("building","tag","doc"),"graphic-design":("palette","pen","image"),
 "flyers-posters-banners":("poster","megaphone","image"),"social-media":("phone","chat","image"),"brochures-catalogues-profiles":("brochure","doc","image"),
 "marketing-advertising":("megaphone","chart","target"),"creative-strategy":("bulb","compass","flowchart"),
 "quotations-invoices":("calculator","doc","tag"),"business-proposals":("doc","people","chart"),"company-profiles":("building","doc","globe"),
 "reports-statements":("clipboard","chart","doc"),"sops-templates":("flowchart","checklist","doc"),"agreements-letters":("stamp","doc","pen"),
 "bilingual-docs":("languages","doc","globe"),"office-admin-systems":("cabinet","folder","layers"),
 "computer-laptop-support":("laptop","wrench","gear"),"os-installation":("download","laptop","chip"),"software-deployment":("terminal","download","layers"),
 "networking-infrastructure":("network","wifi","server"),"windows-server-admin":("server","lock","people"),"backup-recovery":("database","shield","sync"),
 "troubleshooting-maintenance":("wrench","gear","magnifier"),"integration-automation":("sync","gear","cloud"),
 "general-trading":("globe","cube","cart"),"industrial-commercial-supplies":("building","gear","cube"),"product-sourcing":("magnifier","cube","tag"),
 "procurement-support":("cart","checklist","doc"),"vendor-coordination":("people","chat","cube"),"safety-materials":("helmet","shield","cube"),
 "medical-scientific":("microscope","pulse","flask"),"laboratory-equipment":("flask","microscope","gear"),"multi-category-supply":("layers","cube","cart"),
 "car-rental":("car","key","calendar"),"corporate-vehicle-rental":("car","building","doc"),"transportation-solutions":("bus","route","pin"),
 "fleet-management":("truck","car","chart"),"vehicle-operations":("steering","key","wrench"),"mobility-solutions":("route","bus","pin"),"logistics-coordination":("truck","pin","route"),
 "equipment-rental":("excavator","key","calendar"),"heavy-machinery-support":("crane","wrench","gear"),"generator-rental-supply":("generator","bolt","key"),
 "industrial-equipment":("gear","building","wrench"),"scientific-equipment":("microscope","flask","chip"),"site-operational-support":("helmet","people","flowchart"),
 "equipment-sourcing":("magnifier","excavator","tag"),"manpower-operational-assistance":("people","helmet","checklist"),
 # pillars + pages
 "pillar-brand":("brand3","pen","palette"),"pillar-office":("doc","stamp","languages"),"pillar-tech":("chip","server","wifi"),
 "pillar-trade":("cube","cart","globe"),"pillar-drive":("car","route","key"),"pillar-power":("crane","generator","helmet"),
 "page-contact":("chat","phone","people"),"page-about":("compass","people","bulb"),"page-portfolio":("image","layers","pen"),"page-services":("layers","chip","car"),
 "profile-car":("brochure","car","doc"),"profile-heavy":("brochure","crane","doc"),
}
PALS = {"brand":(B,P,T),"office":(G,B,T),"tech":(B,C,P),"trade":(T,B,G),"drive":(B,T,P),"power":(O,B,G),"site":(G,B,T)}
ACC = {"brand":B,"office":G,"tech":C,"trade":T,"drive":P,"power":O,"site":G}
GRAIN = '<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4"/><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0"/></filter>'
FILT = '<filter id="b60" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter><filter id="b24" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="24"/></filter>'
DEFS = ('<linearGradient id="gs" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset=".5" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity=".3"/></linearGradient>'
        '<linearGradient id="gf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".17"/><stop offset="1" stop-color="#fff" stop-opacity=".03"/></linearGradient>'
        f'<linearGradient id="st1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{Y}"/><stop offset="1" stop-color="{G}"/></linearGradient>'
        f'<linearGradient id="st2" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{B}"/><stop offset="1" stop-color="{C}"/></linearGradient>'
        f'<radialGradient id="orb"><stop offset="0" stop-color="#fff6d2"/><stop offset=".35" stop-color="{G}"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient>')
def glyph(name, x, y, s=1, col=W, sw=2.4): return f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{GL[name]}</g>'
def contours(cx, cy, n, r0, step, seed, op0=.6, kx=1.05, ky=.9, amp=1.0):
    out = ''
    for i in range(n):
        Rr = r0 + i*step; ph = i*.16 + seed
        pts = []
        for a in range(0, 360, 9):
            t = math.radians(a)
            rr = Rr*(1 + amp*(.05*math.sin(3*t+ph) + .03*math.sin(5*t+2*ph) + .012*math.sin(8*t+ph*1.7)))
            pts.append((round(cx + rr*math.cos(t)*kx), round(cy + rr*math.sin(t)*ky)))
        d = "M" + " L".join(f"{x} {y}" for x, y in pts) + "Z"
        out += f'<path d="{d}" fill="none" stroke="url(#{"st1" if i%2==0 else "st2"})" stroke-width="{2.2 if i%6==0 else 1.0}" stroke-opacity="{max(.06, op0 - i*op0/n*.95):.2f}"/>'
    return out
def svg_wrap(w, h, body, grain=.08, extra_defs=''):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice"><defs>{DEFS}{GRAIN}{FILT}{extra_defs}</defs>{body}<rect width="{w}" height="{h}" filter="url(#grain)" opacity="{grain}"/></svg>'
def glass(x, y, w, h, rx=30, tint=None):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="#0a1030" opacity=".4"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#gf)" stroke="url(#gs)" stroke-width="1.6"/>')

def art(key, pillar, seed=1):
    """800x600 service / page illustration"""
    main, s1, s2 = SG[key]; r = random.Random(seed*131 + len(key)); pal = PALS[pillar]; acc = ACC[pillar]
    blobs = ''.join(f'<circle cx="{r.randint(60,740)}" cy="{r.randint(60,540)}" r="{r.randint(170,250)}" fill="{pal[i]}" opacity="{.42+.1*i:.2f}"/>' for i in range(3))
    blobs = f'<g filter="url(#b60)">{blobs}<circle cx="{r.choice([140,660])}" cy="{r.randint(100,500)}" r="150" fill="{G}" opacity=".35"/></g>'
    ccx = r.choice([190, 610]); ccy = r.randint(250, 370)
    cont = contours(ccx, ccy, 13, 30, 28, seed*.9, .95)
    chip = lambda x, y, g_, col: glass(x-62, y-62, 124, 124, 32) + f'<circle cx="{x}" cy="{y}" r="40" fill="{col}" opacity=".16"/><circle cx="{x}" cy="{y}" r="40" fill="none" stroke="{col}" stroke-opacity=".8" stroke-width="1.4"/>' + glyph(g_, x, y, 1.15, W, 2.1)
    def card_at(cx, cy=300, sc=3.1, size=300): 
        return glass(cx-size/2, cy-size/2, size, size, 46) + f'<circle cx="{cx}" cy="{cy}" r="{size*.347:.0f}" fill="{acc}" opacity=".13"/><circle cx="{cx}" cy="{cy}" r="{size*.347:.0f}" fill="none" stroke="{acc}" stroke-opacity=".75" stroke-width="1.6"/><circle cx="{cx}" cy="{cy}" r="{size*.393:.0f}" fill="none" stroke="#fff" stroke-opacity=".12" stroke-dasharray="3 9"/>' + glyph(main, cx, cy, sc, W, 1.5)
    lay = seed % 4
    link = lambda x1, y1, x2, y2: f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#fff" stroke-opacity=".3" stroke-dasharray="2 8"/>'
    if lay == 0:
        cx = 400; shapes = link(cx, 300, cx+172, 160) + link(cx, 300, cx-184, 450) + card_at(cx) + chip(cx+172, 160, s1, pal[1]) + chip(cx-184, 450, s2, pal[2])
    elif lay == 1:
        cx = 270; shapes = link(cx, 300, 590, 170) + link(cx, 300, 590, 430) + card_at(cx) + chip(590, 170, s1, pal[1]) + chip(590, 430, s2, pal[2]) + chip(690, 300, s2, pal[0]).replace(chip(690, 300, s2, pal[0]), '')
    elif lay == 2:
        cx = 530; shapes = link(cx, 300, 210, 170) + link(cx, 300, 210, 430) + card_at(cx) + chip(210, 170, s1, pal[1]) + chip(210, 430, s2, pal[2])
    else:
        cx = 400; shapes = (f'<circle cx="{cx}" cy="300" r="190" fill="none" stroke="#fff" stroke-opacity=".14"/><circle cx="{cx}" cy="300" r="140" fill="{acc}" opacity=".12"/><circle cx="{cx}" cy="300" r="140" fill="none" stroke="{acc}" stroke-opacity=".8" stroke-width="1.6"/>' + glyph(main, cx, 300, 4.3, W, 1.4)
                  + chip(cx+int(190*math.cos(math.radians(-40))), 300+int(190*math.sin(math.radians(-40))), s1, pal[1]) + chip(cx+int(190*math.cos(math.radians(140))), 300+int(190*math.sin(math.radians(140))), s2, pal[2]))
    spark = ''.join(f'<path d="M{x} {y-7}V{y+7}M{x-7} {y}H{x+7}" stroke="#fff" stroke-opacity=".5" stroke-width="1.3" stroke-linecap="round"/>' for x, y in [(r.randint(40,760), r.randint(40,560)) for _ in range(6)])
    dots = ''.join(f'<circle cx="{r.randint(10,790)}" cy="{r.randint(10,590)}" r="{r.choice([.8,1,1.4])}" fill="#fff" opacity="{r.choice([.25,.45,.7])}"/>' for _ in range(40))
    return svg_wrap(800, 600, '<rect width="800" height="600" fill="#050818"/>' + blobs + cont + dots + spark + shapes)

NAMES = [("BrandX","Branding & Creative Design"),("OfficeX","SmartDocs & Documentation"),("TechX","IT & Digital Solutions"),("TradeX","Trading, Procurement & Supply"),("DriveX","Transportation & Mobility"),("PowerX","Equipment & Industrial Support")]
KEYS = ["brand","office","tech","trade","drive","power"]
COLS = [B, G, C, T, P, O]
HEX_POS = [(325,56),(618,184),(618,440),(325,620),(32,440),(32,184)]
def hero_mix(links=None):
    """900x780 master hero: aurora + gold contours + core + six glass pillar cards (optionally linked)"""
    links = links or {}
    blobs = f'<g filter="url(#b60)"><circle cx="700" cy="150" r="230" fill="{G}" opacity=".5"/><circle cx="150" cy="210" r="250" fill="{B}" opacity=".5"/><circle cx="250" cy="660" r="240" fill="{T}" opacity=".4"/><circle cx="760" cy="650" r="230" fill="{P}" opacity=".45"/></g>'
    cont = contours(450, 390, 34, 40, 11, 0.3, .8, 1.15, .95, .9)
    cx, cy = 450, 390
    lines = ''.join(f'<path d="M{cx} {cy}L{x+125} {y+52}" stroke="{G}" stroke-opacity=".35" stroke-dasharray="2 9"/>' for x, y in HEX_POS)
    core = f'<circle cx="{cx}" cy="{cy}" r="140" fill="url(#orb)" opacity=".8" filter="url(#b24)"/><circle cx="{cx}" cy="{cy}" r="46" fill="url(#orb)"/><circle cx="{cx}" cy="{cy}" r="64" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="1.2"/><g stroke="#05070f" stroke-width="8" stroke-linecap="round" transform="translate({cx} {cy})"><path d="M-15 -15L15 15M15 -15L-15 15"/></g>'
    cards = ''
    for i, ((nm, sub), (x, y)) in enumerate(zip(NAMES, HEX_POS)):
        col = COLS[i]; k = KEYS[i]; gl = SG["pillar-" + k][0]
        body = (glass(x, y, 250, 104, 28) + f'<circle cx="{x+54}" cy="{y+52}" r="34" fill="{col}" opacity=".18"/><circle cx="{x+54}" cy="{y+52}" r="34" fill="none" stroke="{col}" stroke-opacity=".85" stroke-width="1.5"/>'
                + glyph(gl, x+54, y+52, .85, W, 2.4) + f'<text x="{x+104}" y="{y+60}" {SERIF} font-size="30" fill="#fff">{nm}</text><path d="M{x+104} {y+74}H{x+196}" stroke="{col}" stroke-width="2.6" stroke-linecap="round"/>')
        cards += f'<a href="{links[k]}" aria-label="{nm}"><g class="pl">{body}</g></a>' if k in links else f'<g>{body}</g>'
    dots = ''.join(f'<circle cx="{random.Random(i).randint(10,890)}" cy="{random.Random(i*3).randint(10,770)}" r="{random.Random(i*5).choice([.8,1.1,1.5])}" fill="#fff" opacity=".4"/>' for i in range(70))
    return svg_wrap(900, 780, '<rect width="900" height="780" fill="#050818"/>' + blobs + cont + dots + lines + core + cards, .08).replace('preserveAspectRatio="xMidYMid slice"', 'role="img" aria-label="AashiFX: six pillars around one core" preserveAspectRatio="xMidYMid slice"')

if __name__ == "__main__":
    import os, sys
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_sheet"); os.makedirs(out, exist_ok=True)
    for i, k in enumerate(SG):
        pil = "brand" if i < 8 else "office" if i < 16 else "tech" if i < 24 else "trade" if i < 33 else "drive" if i < 40 else "power" if i < 48 else "site"
        open(os.path.join(out, f"{i:02d}-{k}.svg"), "w").write(art(k, pil, i+1))
    open(os.path.join(out, "hero.svg"), "w").write(hero_mix())
    print(len(SG))
