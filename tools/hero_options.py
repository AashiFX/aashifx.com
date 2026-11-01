"""Four alternative master-hero illustrations for AashiFX (900x780). Run: python3 tools/hero_options.py"""
import os, random, math
ns = {}; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "illustrations.py")).read(), ns)
globals().update({k: v for k, v in ns.items() if not k.startswith("__")})
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hero_options")
NAMES = [("brand","BrandX"),("office","OfficeX"),("tech","TechX"),("trade","TradeX"),("drive","DriveX"),("power","PowerX")]
def starfield(n, seed, ymax=420):
    r = random.Random(seed)
    return ''.join(f'<circle cx="{r.randint(8,892)}" cy="{r.randint(8,ymax)}" r="{r.choice([.8,1,1.3,1.8])}" fill="#fff" opacity="{r.choice([.3,.5,.8])}"/>' for _ in range(n))
def svg(defs, body): return f'<svg viewBox="0 0 900 780" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice"><defs>{defs}</defs>{body}</svg>'
def label(x, y, t, size=24, fill="#f2f4fa", pill=False):
    s = ''
    if pill: s += rect(x - len(t)*7.2 - 12, y - size, len(t)*14.4 + 24, size + 14, "#060a1c", 13, .72)
    return s + f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Georgia,serif" font-size="{size}" fill="{fill}">{t}</text>'
def badge_icon(k):
    return {
     "brand": g(0,0,.42,0,logo_mark()), "office": g(0,2,.3,0,doc(180,230,G,4)),
     "tech": g(0,0,.5,0,rect(-60,-60,120,120,"#0a1430",16,1,G,6)+rect(-36,-36,72,72,"none",8,1,B,4)+path("M-60 -24h-28M-60 24h-28M60 -24h28M60 24h28M-24 -60v-28M24 -60v-28M-24 60v28M24 60v28","none",G,6)),
     "trade": g(0,8,.62,0,cube(60,Y,G)), "drive": g(0,8,.27,0,car(G)), "power": g(0,10,.3,0,excavator(G))}[k]
def medallion(x, y, k, r=40, sc=.62):
    return circ(x,y,r+8,PAL[k][2],.18)+circ(x,y,r,"#0d1737",1,G,4)+g(x,y,sc,0,badge_icon(k))

# ---------- 1. City at sunset: six districts of one city ----------
def opt1():
    r = random.Random(3)
    defs = '<linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0f1740"/><stop offset=".38" stop-color="#2d2a78"/><stop offset=".6" stop-color="#b5567a"/><stop offset=".78" stop-color="#f2a65a"/><stop offset="1" stop-color="#f8dc94"/></linearGradient><linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1230"/><stop offset="1" stop-color="#05070f"/></linearGradient><linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6e7b0"/><stop offset="1" stop-color="#b8922e"/></linearGradient>'
    B_ = 640
    far = ''.join(rect(x, B_-r.randint(150,300), r.randint(26,52), 400, "#2a2260", 2, .55) for x in range(-10, 900, 46))
    def wins(cx, w, h, cols, rows, col, o=.9):
        s = ''
        for i in range(cols):
            for j in range(rows):
                if (i*7+j*3) % 5: s += rect(cx-w/2+10+i*((w-20)/cols), B_-h+14+j*((h-28)/rows), (w-20)/cols-6, (h-28)/rows-8, col, 2, o)
        return s
    # BrandX studio tower + billboard
    c0 = 85; b0 = rect(c0-50, B_-250, 100, 250, "url(#gold)", 4) + wins(c0,100,250,3,9,"#fff4cf",.55) + rect(c0-72, B_-330, 144, 84, "#f7f9fc", 8) + circ(c0-30, B_-288, 24, G) + circ(c0-6, B_-288, 24, B, .85) + circ(c0-18, B_-270, 24, T, .85) + rect(c0+22, B_-300, 38, 8, D, 4, .6) + rect(c0+22, B_-282, 30, 6, D, 4, .4) + path(f"M{c0-40} {B_-246}V{B_-262}M{c0+40} {B_-246}V{B_-262}", "none", S, 4)
    c1 = 235; b1 = rect(c1-50, B_-300, 100, 300, "#eef2fb", 4) + wins(c1,100,300,3,11,"#3a5ba8",.8) + g(c1, B_-330, .24, 0, doc(180,230,G,4)) + rect(c1-50, B_-306, 100, 10, "#cfd7ea")
    c2 = 385; b2 = rect(c2-45, B_-340, 90, 340, "#16306a", 6) + wins(c2,90,340,3,12,"#7cf0ff",.85) + path(f"M{c2} {B_-340}V{B_-410}", "none", S, 4) + circ(c2, B_-414, 6, "#ff6b5a") + ''.join(path(f"M{c2-rr} {B_-372}A{rr} {rr} 0 0 1 {c2+rr} {B_-372}", "none", B, 4, .8) for rr in (18, 32, 46))
    c3 = 535; cols = [G,B,T,O,P,"#ff6b5a"]
    b3 = ''.join(rect(c3-62+(i%3)*42, B_-40-(i//3)*40, 40, 36, cols[(i*2+1)%6], 3) + path(f"M{c3-58+(i%3)*42} {B_-34-(i//3)*40}h30", "none", D, 2, .35) for i in range(6)) + path(f"M{c3-70} {B_-92}V{B_-190}H{c3+60}V{B_-92}", "none", S, 6) + path(f"M{c3} {B_-190}V{B_-130}", "none", G, 4) + rect(c3-14, B_-130, 28, 14, G, 3)
    c4 = 685; b4 = rect(c4-70, B_-120, 140, 18, "#1d2850", 4) + rect(c4-40, B_-102, 14, 102, "#1d2850") + rect(c4+26, B_-102, 14, 102, "#1d2850") + g(c4, B_-142, .27, 0, car(G)) + path(f"M{c4-70} {B_-120}H{c4+70}", "none", "#fff", 2, .5) + g(c4+52, B_-178, .13, 0, bus(B)) 
    c5 = 825; b5 = g(c5-4, B_, .85, 0, crane(330, W)) + rect(c5-52, B_-130, 78, 130, "#1d2850", 3, .9) + ''.join(path(f"M{c5-52} {B_-130+i*26}H{c5+26}", "none", O, 3, .8) for i in range(5))
    ground = rect(0, B_, 900, 140, "url(#gd)") + rect(0, B_, 900, 4, G, 0, .8) + ''.join(rect(40+i*90, B_+46, 50, 5, "#fff", 2, .5) for i in range(10))
    sun = circ(450, 520, 250, "#ffd986", .18) + circ(450, 520, 150, "#ffe7a8", .9)
    labels = ''.join(label(c, 700, nm, 23, "#f2f4fa") for c, (_, nm) in zip((c0,c1,c2,c3,c4,c5), NAMES))
    return svg(defs, rect(0,0,900,780,"url(#sk)") + starfield(70, 5, 260) + sun + far + b3 + b0 + b1 + b2 + b4 + b5 + ground + labels)

# ---------- 2. The Road: Design. Document. Deliver. ----------
def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(u**3*p0[i] + 3*u*u*t*p1[i] + 3*u*t*t*p2[i] + t**3*p3[i] for i in (0, 1))
def opt2():
    defs = '<linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a1030"/><stop offset=".55" stop-color="#26397e"/><stop offset=".8" stop-color="#e3a15a"/><stop offset="1" stop-color="#fbe3a0"/></linearGradient><radialGradient id="sn"><stop offset="0" stop-color="#fff3c4"/><stop offset=".4" stop-color="#ffd986" stop-opacity=".8"/><stop offset="1" stop-color="#ffd986" stop-opacity="0"/></radialGradient>'
    P = [((-30,760),(220,640),(260,720),(420,610)), ((420,610),(560,520),(640,560),(930,470))]
    def pt(t):
        seg = 0 if t < .5 else 1; tt = t*2 if t < .5 else (t-.5)*2
        return bez(*P[seg], tt)
    d = f"M{P[0][0][0]} {P[0][0][1]}C{P[0][1][0]} {P[0][1][1]} {P[0][2][0]} {P[0][2][1]} {P[0][3][0]} {P[0][3][1]}C{P[1][1][0]} {P[1][1][1]} {P[1][2][0]} {P[1][2][1]} {P[1][3][0]} {P[1][3][1]}"
    hills = path("M0 520C150 440 260 520 380 470S640 430 900 500V780H0Z", "#1c2c64", o=.9) + path("M0 590C120 520 280 600 420 540S700 520 900 560V780H0Z", "#121e4a") + path("M0 660C160 610 320 690 520 630S780 620 900 650V780H0Z", "#0b1332")
    road = path(d, "none", G, 150, .22) + path(d, "none", "#070b1c", 134) + path(d, "none", "#fff", 5).replace('/>', ' stroke-dasharray="20 24"/>')
    stations = ''; keys = [k for k,_ in NAMES]; ts = [.1, .25, .41, .58, .76, .93]
    for idx, (k, nm) in enumerate(NAMES):
        x, y = pt(ts[idx]); s_ = 1.15 - idx*.1
        up = y - 150*s_
        stations += path(f"M{x} {y-14}V{up+40*s_}", "none", G, 3, .8) + g(x, up, s_, 0, medallion(0,0,k,46,.7)) + circ(x, y-14, 8, G)
        stations += label(x, y + 46, nm, 20*s_ + 4, "#f2f4fa", True)
    sun = circ(700, 470, 230, "url(#sn)") 
    flags = ''
    return svg(defs, rect(0,0,900,780,"url(#sk)") + starfield(80, 9, 330) + sun + hills + road + stations + sparkle(120,120,1.6) + sparkle(780,160,1.2))

# ---------- 3. Floating island ----------
def isobox(cx, by, w, h, top, left, right):
    hw, hd = w*.866, w*.5
    t = [(cx, by-h-hd), (cx+hw, by-h), (cx, by-h+hd), (cx-hw, by-h)]
    return (poly([(cx-hw, by-h), (cx, by-h+hd), (cx, by+hd), (cx-hw, by)], left) + poly([(cx+hw, by-h), (cx, by-h+hd), (cx, by+hd), (cx+hw, by)], right) + poly(t, top))
def opt3():
    defs = '<linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0f1a4d"/><stop offset=".6" stop-color="#3a3a8c"/><stop offset="1" stop-color="#d98a7a"/></linearGradient><radialGradient id="gl"><stop offset="0" stop-color="#ffd986" stop-opacity=".7"/><stop offset="1" stop-color="#ffd986" stop-opacity="0"/></radialGradient><linearGradient id="beam" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ffd986" stop-opacity=".6"/><stop offset="1" stop-color="#ffd986" stop-opacity="0"/></linearGradient>'
    cx_, cy_ = 450, 440
    top = [(cx_, 215), (cx_+380, 440), (cx_, 665), (cx_-380, 440)]
    slab = poly(top, "#1c2f66") + poly([(cx_-380,440),(cx_,665),(cx_,705),(cx_-380,480)], "#101c45") + poly([(cx_+380,440),(cx_,665),(cx_,705),(cx_+380,480)], "#0b1433")
    rock = poly([(cx_-380,480),(cx_,705),(cx_+380,480),(cx_+250,560),(cx_+120,640),(cx_+20,770),(cx_-70,650),(cx_-200,600),(cx_-300,540)], "#2d2457") + poly([(cx_-380,480),(cx_,705),(cx_-70,650),(cx_-200,600),(cx_-300,540)], "#3a2f6a", .8)
    rim = path(f"M{cx_-380} 440L{cx_} 215L{cx_+380} 440L{cx_} 665Z", "none", G, 4, .9)
    pos = [("brand",320,320,88,120,("#fbe7a8",G,"#9a7a1c")),("office",580,320,88,150,("#ffffff","#dfe6f5","#b9c4de")),("power",205,445,88,70,("#ffb98a",O,"#b85a2a")),
           ("tech",695,445,88,190,("#9fe6ff","#3d86d8","#245aa0")),("trade",325,565,88,64,("#9fe8cf",T,"#1c9a76")),("drive",575,565,88,56,("#c7cfdf","#5a6b94","#3a4a74"))]
    order = sorted(pos, key=lambda p: p[2])
    paths = ''.join(path(f"M{cx_} {440}L{x} {y}", "none", G, 3, .7).replace('/>',' stroke-dasharray="2 10"/>') for _,x,y,_,_,_ in pos)
    center = isobox(cx_, 480, 56, 130, "#f6e7b0", G, "#9a7a1c") + circ(cx_, 322, 40, "url(#gl)") + circ(cx_, 330, 26, "#f2d27a", 1, "#fff", 3) + ''
    center += f'<g transform="translate({cx_} 330)"><rect x="-17" y="-4" width="34" height="8" rx="4" fill="{D}" transform="rotate(45)"/><rect x="-17" y="-4" width="34" height="8" rx="4" fill="{W}" transform="rotate(-45)"/></g>'
    beam = poly([(cx_-36, 290), (cx_+36, 290), (cx_+150, 0), (cx_-150, 0)], "url(#beam)", .8)
    bld = ''
    for k, x, y, w, h, (tp, lf, rt) in order:
        by = y + 40
        bld += isobox(x, by, w*.8, h, tp, lf, rt)
        if k == "brand": bld += g(x, by - h - 36, .5, 0, logo_mark())
        if k == "office": bld += g(x, by - h - 44, .22, 0, doc(180,230,G,4))
        if k == "tech": bld += path(f"M{x} {by-h-20}V{by-h-70}", "none", S, 4) + circ(x, by-h-74, 6, "#ff6b5a")
        if k == "trade": bld += g(x-30, by-h-18, .42, 0, cube(60,Y,G)) + g(x+26, by-h-8, .42, 0, cube(60,"#9fd0ff",B,"#2a6fc0"))
        if k == "drive": bld += g(x, by-h-24, .2, 0, car(G))
        if k == "power": bld += g(x, by-h+10, .26, 0, crane(330, "#fff"))
    labels = ''.join(label(x, y+104, nm, 22, "#f2f4fa", True) for (k, nm), (_, x, y, *_) in zip(NAMES, [(p[0],p[1],p[2]) for p in [next(q for q in pos if q[0]==kk) for kk,_ in NAMES]]))
    clouds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#fff" opacity=".1"/>' for x,y,rx,ry in [(110,200,110,26),(790,170,130,28),(150,640,120,24),(780,620,140,26),(450,740,200,22)])
    return svg(defs, rect(0,0,900,780,"url(#sk)") + circ(450,400,380,"url(#gl)") + starfield(80, 4, 300) + clouds + beam + rock + slab + rim + paths + center + bld + labels + sparkle(120,120,1.5) + sparkle(800,110,1.2))

# ---------- 4. Six pillars, one establishment ----------
def opt4():
    defs = '<linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1233"/><stop offset=".6" stop-color="#2a2a70"/><stop offset="1" stop-color="#6a4a8a"/></linearGradient><linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6e7b0"/><stop offset="1" stop-color="#b8922e"/></linearGradient><linearGradient id="col" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#aab4cc"/><stop offset=".45" stop-color="#f6f8fd"/><stop offset="1" stop-color="#8e9ab8"/></linearGradient><radialGradient id="halo"><stop offset="0" stop-color="#ffd986" stop-opacity=".75"/><stop offset="1" stop-color="#ffd986" stop-opacity="0"/></radialGradient><linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101a3c"/><stop offset="1" stop-color="#05070f"/></linearGradient><radialGradient id="coref" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#f6e7b0"/><stop offset="1" stop-color="#b8922e"/></radialGradient>'
    xs = [140 + i*124 for i in range(6)]
    ped = poly([(70,270),(450,70),(830,270)], "url(#gold)") + poly([(130,252),(450,98),(770,252)], "#101e4a") + circ(450, 198, 64, "url(#halo)") + circ(450,200,40,"url(#coref)",1,Y,3) + f'<g transform="translate(450 200)"><rect x="-27" y="-6" width="54" height="12" rx="6" fill="{D}" transform="rotate(45)"/><rect x="-27" y="-6" width="54" height="12" rx="6" fill="{W}" transform="rotate(-45)"/><circle r="5" fill="{G}"/></g>'
    ped += ''.join(path(f"M{x} 252L{x+ (450-x)*0:.0f} 252", "none") for x in ()) 
    ent = rect(50, 270, 800, 40, "url(#gold)", 3) + rect(50, 310, 800, 16, "#8a6a22") 
    cols = ''
    for x, (k, nm) in zip(xs, NAMES):
        cols += rect(x-26, 326, 52, 262, "url(#col)") + ''.join(path(f"M{x+dx} 330V584", "none", "#7d89a8", 2, .55) for dx in (-14,-5,5,14)) + rect(x-38, 326, 76, 18, "#e9edf7", 3) + rect(x-38, 584, 76, 18, "#e9edf7", 3) + medallion(x, 440, k, 40, .6)
    steps = rect(30, 602, 840, 24, "#27386f") + rect(10, 626, 880, 28, "#1b2a58") + rect(-10, 654, 920, 32, "#121c40")
    names = ''.join(label(x, 646, nm, 20, "#e8c766") for x, (_, nm) in zip(xs, NAMES))
    floor = rect(0, 686, 900, 94, "url(#gr)") + ''.join(rect(x-22, 700, 44, 80, "#fff", 0, .05) for x in xs)
    rays = ''.join(poly([(450,200),(450+dx-30,780),(450+dx+30,780)], "#ffd986", .05) for dx in (-420,-250,-90,90,250,420))
    return svg(defs, rect(0,0,900,780,"url(#sk)") + circ(450,200,330,"url(#halo)") + rays + starfield(90, 6, 300) + ped + ent + cols + steps + names + floor + sparkle(90,120,1.4) + sparkle(820,130,1.1))

OPTS = [("1-city-sunset","City at sunset","Six districts of one city: studio, office, tech, port, highway and construction under one sunset skyline.",opt1),
        ("2-the-road","The road","Design. Document. Deliver. A journey road with six stations and a sunrise at the end.",opt2),
        ("3-floating-island","Floating island","One island world: a golden AashiFX beacon at the centre, six buildings around it.",opt3),
        ("4-six-pillars","Six pillars","Literally six pillars holding one establishment, with the AashiFX emblem on top.",opt4)]
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f, t, d, fn in OPTS:
        open(os.path.join(OUT, f + ".svg"), "w").write(fn())
    print([ (f, os.path.getsize(os.path.join(OUT, f + ".svg"))) for f,*_ in OPTS])
