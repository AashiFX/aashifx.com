import random, math
G="#d9b44a"; B="#3ea6ff"; T="#2fd0a0"; W="#f7f9fc"; D="#0b1226"; O="#ff8a4a"; P="#9b7bff"; K="#121a33"; S="#c7cfdf"; Y="#f1d98a"
PAL = {  # per pillar: bg1, bg2, glow
 "brand":("#1b2a63","#05070f","#3ea6ff"),"office":("#2b2410","#05070f","#d9b44a"),"tech":("#0d2a52","#05070f","#3ea6ff"),
 "trade":("#10343a","#05070f","#2fd0a0"),"drive":("#1a2a5c","#05070f","#d9b44a"),"power":("#2a1f48","#05070f","#ff8a4a"),
 "site":("#1b2a63","#05070f","#d9b44a")}
def g(x=0,y=0,s=1,r=0,c=""): return f'<g transform="translate({x} {y}) rotate({r}) scale({s})">{c}</g>'
def rect(x,y,w,h,f,rx=0,o=1,st=None,sw=0): 
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" opacity="{o}"' + (f' stroke="{st}" stroke-width="{sw}"' if st else '') + '/>'
def circ(x,y,r,f="none",o=1,st=None,sw=0): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" opacity="{o}"' + (f' stroke="{st}" stroke-width="{sw}"' if st else '') + '/>'
def path(d,f="none",st=None,sw=0,o=1,cap="round"): return f'<path d="{d}" fill="{f}" opacity="{o}"' + (f' stroke="{st}" stroke-width="{sw}" stroke-linecap="{cap}" stroke-linejoin="round"' if st else '') + '/>'
def poly(pts,f,o=1): return f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{f}" opacity="{o}"/>'
def doc(w=180,h=230,head=G,rows=4,col=W):
    s=rect(-w/2,-h/2,w,h,col,12)+rect(-w/2,-h/2,w,h*.2,head,12)+rect(-w/2,-h/2+h*.12,w,h*.08,head)
    for r in range(rows): s+=rect(-w/2+18,-h/2+h*.3+r*h*.12,(w-36)*(1-.18*(r%3)),8,D,4,.45)
    return s
def phone(w=120,h=230,screen=B):
    return rect(-w/2,-h/2,w,h,K,18,1,S,3)+rect(-w/2+8,-h/2+22,w-16,h-44,screen,8,.9)+rect(-14,-h/2+8,28,6,S,3)
def laptop(w=320,screen=B):
    h=w*.62
    return rect(-w/2,-h,w,h,K,10,1,S,3)+rect(-w/2+12,-h+12,w-24,h-24,screen,5,.85)+poly([(-w/2-20,6),(w/2+20,6),(w/2+4,22),(-w/2-4,22)],S)
def browser(w=300,h=210,bar=G):
    return rect(-w/2,-h/2,w,h,W,12)+rect(-w/2,-h/2,w,34,bar,12)+rect(-w/2,-h/2+22,w,12,bar)+circ(-w/2+20,-h/2+17,5,W)+circ(-w/2+38,-h/2+17,5,W)+circ(-w/2+56,-h/2+17,5,W)
def bars(w=200,h=130,n=5,cols=(G,B,T)):
    s=''
    for i in range(n):
        bh=h*(.3+.7*((i*37)%10)/10); s+=rect(-w/2+i*(w/n)+4,h/2-bh,w/n-10,bh,cols[i%len(cols)],5)
    return s+path(f"M{-w/2} {h/2}H{w/2}",st=S,sw=3)
def gear(r=60,col=G,hole=D):
    return circ(0,0,r,"none",1,col,r*.3).replace('/>',f' stroke-dasharray="{r*.42} {r*.42}"/>')+circ(0,0,r*.84,col)+circ(0,0,r*.32,hole)
def cube(s=60,top=Y,left=G,right="#9a7a1c"):
    return poly([(0,-s),(s*.87,-s*.5),(0,0),(-s*.87,-s*.5)],top)+poly([(-s*.87,-s*.5),(0,0),(0,s),(-s*.87,s*.5)],left)+poly([(s*.87,-s*.5),(0,0),(0,s),(s*.87,s*.5)],right)
def car(col=G,w=1):
    return (path("M-160 28L-138 -8Q-100 -50 -40 -50H60Q110 -50 140 -8L166 28Q172 52 150 52H-150Q-172 52 -160 28Z",col)+poly([(-118,-6),(-84,-38),(-6,-38),(-6,-6)],D,.75)+poly([(6,-6),(6,-38),(60,-38),(100,-6)],D,.75)
      +circ(-95,52,31,D,1,S,4)+circ(95,52,31,D,1,S,4)+circ(-95,52,12,S)+circ(95,52,12,S)+rect(-166,18,18,12,Y,3)+rect(148,18,18,12,"#ff6b5a",3))
def truck(col=W,cab=G):
    return rect(-170,-70,210,110,col,10)+path("M50 -40H110L150 0V40H50Z",cab)+poly([(60,-30),(60,0),(135,0),(104,-30)],D,.7)+circ(-110,44,26,D,1,S,4)+circ(-30,44,26,D,1,S,4)+circ(110,44,26,D,1,S,4)+rect(-150,-50,110,12,G,4,.8)
def bus(col=G):
    s=rect(-190,-70,380,120,col,26)
    for i in range(6): s+=rect(-170+i*58,-52,44,40,D,6,.7)
    return s+circ(-120,52,28,D,1,S,4)+circ(120,52,28,D,1,S,4)
def crane(h=360,col=W):
    s=rect(-8,-h,16,h,col,0,.0)
    s+=path(f"M-18 0V{-h}M18 0V{-h}",st=col,sw=5)
    for y in range(0,int(h)-40,60): s+=path(f"M-18 {-y}L18 {-y-60}M18 {-y}L-18 {-y-60}",st=col,sw=3)
    s+=path(f"M-170 {-h}H260",st=col,sw=6)+path(f"M0 {-h-50}L-18 {-h}M0 {-h-50}L18 {-h}M0 {-h-50}L-160 {-h}M0 {-h-50}L240 {-h}",st=col,sw=3)
    s+=rect(-190,-h-12,50,26,G)+path(f"M180 {-h}V{-h+110}",st=G,sw=3)+poly([(180,-h+110),(165,-h+135),(195,-h+135)],G)
    return s
def excavator(col=G):
    return (rect(-150,30,300,44,D,22,1,S,4)+circ(-120,52,14,S)+circ(120,52,14,S)+circ(0,52,14,S)+rect(-110,-20,170,60,col,10)+path("M-110 -20H-30V-80H-80Z",col)+poly([(-92,-26),(-48,-26),(-48,-68),(-80,-68)],D,.7)
      +path("M40 -10L130 -90L200 -40",st=col,sw=20)+path("M200 -40L230 20L180 40L170 -10Z",O)+circ(40,-10,12,D)+circ(130,-90,12,D))
def generator(col=O):
    return rect(-130,-70,260,150,col,16)+rect(-110,-50,150,60,D,8,.8)+''.join(rect(-100+i*28,-42,14,44,S,4,.9) for i in range(5))+circ(80,-20,22,W)+path("M82 -36L70 -18H80L76 -4L90 -24H80Z",G,o=1)+rect(-150,80,300,14,D,4)+circ(-100,106,18,D,1,S,3)+circ(100,106,18,D,1,S,3)
def flask(col=T):
    return path("M-30 -100H30V-40L90 80Q100 110 70 110H-70Q-100 110 -90 80L-30 -40Z","none",S,6)+path("M-60 40H60L90 80Q100 110 70 110H-70Q-100 110 -90 80Z",col,o=.9)+circ(-10,60,8,W,.8)+circ(20,80,6,W,.8)+rect(-40,-110,80,14,S,5)
def beaker(col=B):
    return path("M-60 -80V90Q-60 110 -40 110H40Q60 110 60 90V-80","none",S,6)+rect(-54,0,108,100,col,10,.85)+rect(-70,-90,140,12,S,5)+''.join(path(f"M-60 {y}H-40","none",S,3) for y in (-40,-10,20))
def helmet(col=G):
    return path("M-110 40Q-110 -80 0 -90Q110 -80 110 40Z",col)+rect(-130,36,260,22,col,8)+rect(-14,-90,28,70,"#9a7a1c",6)+path("M-80 -10Q-70 -50 -30 -60","none",W,6,.5)
def vest(col=O):
    return path("M-70 -90L-30 -100Q0 -70 30 -100L70 -90L90 -30V100H-90V-30Z",col)+rect(-90,10,180,22,Y,0,.95)+rect(-90,50,180,22,Y,0,.95)+path("M0 -70V100","none",D,4,.5)
def shield(col=B):
    return path("M0 -110L100 -70V10Q100 80 0 120Q-100 80 -100 10V-70Z",col)+path("M-40 5L-10 35L45 -25","none",W,14)
def cloud(col=W):
    return path("M-90 40Q-130 40 -130 0Q-130 -40 -90 -42Q-80 -90 -30 -90Q20 -90 30 -50Q80 -60 100 -20Q130 -10 125 20Q120 40 90 40Z",col)
def server():
    s=''
    for i in range(3): s+=rect(-110,-110+i*76,220,64,K,10,1,S,3)+circ(-84,-78+i*76,7,[T,B,G][i])+rect(-60,-84+i*76,140,12,S,5,.4)
    return s
def nodes(pts,links,col=B):
    s=''.join(path(f"M{pts[a][0]} {pts[a][1]}L{pts[b][0]} {pts[b][1]}","none",col,3,.8) for a,b in links)
    return s+''.join(circ(x,y,r,K,1,G,4) for x,y,r in [(p[0],p[1],p[2] if len(p)>2 else 16) for p in pts])
def magnifier(col=G):
    return circ(0,0,60,"rgba(255,255,255,.12)",1,col,12)+path("M44 44L100 100","none",col,18)
def megaphone(col=G):
    return path("M-90 -30L70 -90V90L-90 30Z",col)+rect(-130,-34,50,68,O,12)+path("M90 -40Q130 0 90 40","none",W,8)+path("M110 -70Q170 0 110 70","none",W,6,.6)
def bulb(col=Y):
    return circ(0,-20,70,col)+rect(-28,44,56,18,S,5)+rect(-22,66,44,14,S,5)+path("M-18 -10L0 20L18 -10","none",D,5,.6)
def compass(col=G):
    return circ(0,0,100,K,1,col,8)+poly([(0,-80),(18,0),(0,80),(-18,0)],"#ff6b5a")+poly([(0,-80),(18,0),(-18,0)],W)+circ(0,0,8,col)
def pin(col="#ff6b5a"):
    return path("M0 80C-60 10 -70 -20 -70 -40A70 70 0 0 1 70 -40C70 -20 60 10 0 80Z",col)+circ(0,-40,24,W)
def person(col=B,s=1):
    return g(0,0,s,0,circ(0,-30,26,W)+path("M-46 60Q-46 0 0 0Q46 0 46 60Z",col))
def folder(col=G):
    return path("M-110 -60H-30L-10 -36H110Q120 -36 120 -26V70Q120 80 110 80H-100Q-110 80 -110 70Z",col)+rect(-110,-26,230,106,Y,12,.9)
def cart(col=G):
    return path("M-120 -80H-90L-60 40H80L100 -40H-80","none",col,12)+circ(-40,70,14,col)+circ(60,70,14,col)+rect(-50,-30,40,36,B,6)+rect(0,-30,40,36,T,6)
def stamp(col=G):
    return rect(-60,-100,120,70,col,14)+rect(-24,-30,48,60,col)+rect(-90,30,180,26,col,8)+path("M-70 78H70","none",W,6)
def lock(col=G):
    return rect(-60,-10,120,100,col,14)+path("M-36 -10V-44A36 36 0 0 1 36 -44V-10","none",col,14)+circ(0,36,12,D)
def check(col=T,r=30):
    return circ(0,0,r,col)+path(f"M{-r*.4} 0L{-r*.1} {r*.35}L{r*.45} {-r*.3}","none",W,r*.2)
def wheel(col=G):
    return circ(0,0,90,"none",1,col,16)+circ(0,0,22,col)+path("M0 -22V-90M-20 12L-80 44M20 12L80 44","none",col,14)
def key(col=G):
    return circ(-50,0,36,"none",1,col,14)+path("M-14 0H100M70 0V28M96 0V22","none",col,14)
def building(col=B):
    s=rect(-70,-120,140,200,K,6,1,S,3)
    for r in range(5):
        for c in range(3): s+=rect(-52+c*42,-100+r*34,26,20,[col,Y,W][(r+c)%3],3,.85)
    return s
def brandboard():
    return rect(-170,-110,340,220,W,14)+circ(-100,-30,44,G)+circ(-60,-30,44,B,.8)+circ(-80,10,44,T,.8)+rect(0,-80,140,18,D,6,.6)+rect(0,-50,100,12,D,6,.35)+''.join(rect(i*34,-10,28,28,[G,B,T,O,D][i],6) for i in range(0,5))+rect(0,40,140,40,"#eef1f8",8)
def logo_mark():
    return circ(0,0,100,"none",1,G,6)+poly([(0,-70),(60,40),(-60,40)],B,.9)+poly([(0,-30),(34,34),(-34,34)],T,.95)+circ(0,16,10,W)
def poster(col=G):
    return rect(-90,-130,180,260,W,10)+rect(-90,-130,180,110,col,10)+circ(0,-75,34,D,.7)+rect(-60,10,120,14,D,6,.7)+rect(-60,34,90,10,D,6,.4)+rect(-60,100,70,16,col,8)
def flyer():
    return g(0,0,1,-8,doc(150,210,B,3,W))+g(30,10,1,8,doc(150,210,G,3,"#fff"))
def banner_roll(col=B):
    return rect(-80,-140,160,260,col,10)+rect(-80,-140,160,16,D,6,.6)+circ(0,-40,38,W,.9)+rect(-50,20,100,12,W,6,.9)+rect(-40,44,80,10,W,6,.6)+rect(-60,120,120,10,S,5)+rect(-50,128,100,8,S,4)
def brochure(col=G):
    return poly([(-190,-110),(-60,-100),(-60,110),(-190,100)],W)+poly([(-60,-100),(70,-110),(70,100),(-60,110)],"#e8edf7")+poly([(70,-110),(190,-100),(190,110),(70,100)],W)+rect(-170,-80,90,60,col,6)+rect(-40,-80,90,12,D,6,.6)+rect(-40,-56,70,10,D,6,.35)+circ(130,-30,34,B)+rect(88,30,86,10,D,5,.5)
def social():
    s=''
    for i,c in enumerate([B,G,T,O,P,W]): s+=rect(-150+(i%3)*104,-100+(i//3)*104,96,96,c,14,.95)
    return s+circ(-102,-52,20,W,.9)+path("M-8 -70L16 -30L-8 -34Z",D,o=.6)
def heart(): return path("M0 40C-70 -10 -40 -60 0 -30C40 -60 70 -10 0 40Z","#ff6b5a")
def chat(col=T):
    return path("M-120 -80H80Q100 -80 100 -60V20Q100 40 80 40H-30L-80 80V40H-120Q-140 40 -140 20V-60Q-140 -80 -120 -80Z",col)+rect(-100,-50,150,10,W,5,.9)+rect(-100,-26,110,10,W,5,.7)
def invoice():
    return doc(190,250,G,3,W)+rect(-70,30,140,50,D,6,.18)+rect(10,48,60,14,G,4)+circ(55,-85,0,W)
def chartline(col=T): return path("M-100 40L-40 -10L10 20L90 -60","none",col,10)+circ(90,-60,10,col)
def report(): return rect(-110,-130,220,260,W,12)+rect(-110,-130,220,36,B,12)+rect(-110,-110,220,16,B)+g(0,20,.9,0,bars(160,120,5,(G,B,T)))
def checklist():
    s=rect(-110,-130,220,260,W,12)+rect(-110,-130,220,36,T,12)+rect(-110,-110,220,16,T)
    for i in range(4): s+=rect(-84,-70+i*50,22,22,"none",1,D,4).replace('rx="0"','rx="5"')+(path(f"M-80 {-60+i*50}L-74 {-52+i*50}L-64 {-68+i*50}","none",T,5) if i<3 else '')+rect(-48,-66+i*50,110,10,D,5,.45)
    return s
def contract():
    return doc(190,250,D,4,W).replace(f'fill="{D}"',f'fill="#1f2a4d"')+path("M-60 90Q-40 60 -20 90T20 84","none",B,5)+g(60,70,1,0,circ(0,0,26,"none",1,"#ff6b5a",5)+circ(0,0,16,"none",1,"#ff6b5a",3))
def bilingual():
    return g(-70,0,1,-5,doc(150,210,B,4,W))+g(70,0,1,5,doc(150,210,G,4,W))+rect(-100,-60,60,10,D,5,.55)+rect(40,-60,60,10,D,5,.55)+rect(30,-34,70,10,D,5,.4)
def cabinet():
    s=''
    for i in range(3): s+=rect(-80,-110+i*80,160,70,K,8,1,S,3)+rect(-24,-86+i*80,48,10,S,5)+circ(0,-58+i*80,0,S)
    return s+folder(G).replace('<path','<path')[:0]
def desk_stack(): return cube(46,Y,G)+g(70,60,1,0,cube(46,"#9fd0ff",B,"#2a6fc0"))
def screen(w=300,col=B): return rect(-w/2,-w*.3,w,w*.6,K,12,1,S,4)+rect(-w/2+14,-w*.3+14,w-28,w*.6-28,col,6,.85)+rect(-30,w*.3,60,20,S)+rect(-70,w*.3+16,140,10,S,4)
def usb(): return rect(-30,-90,60,110,S,8)+rect(-18,-130,36,50,W,4)+rect(-8,-120,8,16,D)+rect(4,-120,8,16,D)+rect(-24,20,48,60,B,8)
def wifi(col=G): return ''.join(path(f"M{-r} {-r*.2}A{r} {r} 0 0 1 {r} {-r*.2}","none",col,10) for r in (40,80,120))+circ(0,30,12,col)
def router(): return rect(-110,10,220,50,K,10,1,S,3)+circ(-80,35,6,T)+circ(-60,35,6,G)+path("M-70 10L-90 -70M70 10L90 -70","none",S,8)+wifi(B).replace('<path','<path')
def database(col=B): return ''.join(f'<ellipse cx="0" cy="{y}" rx="80" ry="24" fill="{col}" opacity=".95"/>' for y in (60,10,-40)) +rect(-80,-40,160,100,col)+''.join(f'<ellipse cx="0" cy="{y}" rx="80" ry="24" fill="{col}" stroke="{W}" stroke-width="3" opacity=".95"/>' for y in (60,10,-40))
def arrow(col=G,l=120): return path(f"M0 0H{l}M{l-24} -22L{l} 0L{l-24} 22","none",col,12)
def truck_route(): return path("M-250 100Q-150 20 -60 80T120 30T250 -60","none",G,5).replace('/>',' stroke-dasharray="4 14"/>')+pin().replace('<path','<path')
def worker(col=O,s=1): return g(0,0,s,0,helmet(G).replace('M-110 40Q-110 -80 0 -90Q110 -80 110 40Z','M-60 -22Q-60 -90 0 -96Q60 -90 60 -22Z') .replace('rect x="-130" y="36" width="260" height="22"','rect x="-78" y="-26" width="156" height="14"')[:0]+circ(0,-50,28,"#f2c8a0")+path("M-34 -66Q0 -110 34 -66Z",G)+rect(-40,-70,80,10,G,4)+path("M-52 60Q-52 -14 0 -14Q52 -14 52 60Z",col)+rect(-52,22,104,12,Y))
def hut(): return poly([(-110,-10),(0,-80),(110,-10)],"#9a7a1c")+rect(-96,-10,192,90,S,6)+rect(-20,16,40,64,K,4)+rect(-80,6,40,30,B,4,.8)+rect(40,6,40,30,B,4,.8)
def microscope(col=S): return path("M-20 -100L40 -60L10 10L-50 -30Z",col)+rect(30,-20,18,120,col,4)+path("M-70 100H90","none",col,14)+path("M60 30Q110 30 110 -20","none",col,10)+rect(-70,60,90,12,col,4)
def stetho(col=B): return path("M-60 -90V0Q-60 50 0 50Q60 50 60 0V-90","none",col,10)+circ(0,70,26,G)+circ(-60,-96,12,col)+circ(60,-96,12,col)+path("M0 50V44","none",col,10)
def pipes(): return path("M-120 60V-20H0V-80H120","none",S,26)+path("M-120 60V-20H0V-80H120","none",B,8,.7)+circ(-120,60,24,K,1,S,6)+circ(120,-80,24,K,1,S,6)+circ(0,-20,16,G)
def factory(): return poly([(-130,100),(-130,-10),(-70,-50),(-70,-10),(-10,-50),(-10,-10),(50,-50),(50,100)],K)+rect(60,-90,40,190,S,4)+''.join(rect(-110+i*38,20,24,22,[Y,B,Y,B][i],3) for i in range(3))+circ(80,-110,18,W,.5)+circ(100,-136,24,W,.3)
def shelves():
    s=rect(-150,-120,300,240,K,8,1,S,3)
    for y in (-40,40): s+=rect(-150,y,300,10,S)
    for i,c in enumerate([G,B,T]): s+=rect(-130+i*50,-110,44,66,c,5)+rect(-130+i*50,-30,44,66,[B,T,G][i],5)+rect(-130+i*50,50,44,60,[T,G,B][i],5)
    return s+''.join(rect(40+i*40,-100+(i%2)*10,32,54,[O,W,P][i],5) for i in range(3))
def globe(col=B): return circ(0,0,100,col,.85)+path("M-100 0H100M0 -100C50 -50 50 50 0 100M0 -100C-50 -50 -50 50 0 100","none",W,4,.7)+path("M-90 -40Q0 -10 90 -40M-90 40Q0 10 90 40","none",W,4,.5)
def handshake(): return person(B,.9).replace('<g','<g',1)
def two_people(): return g(-70,0,1,0,person(B,1))+g(70,0,1,0,person(O,1))+path("M-30 30H30","none",G,8)
def steering(): return wheel(G)
def dashboard(): return rect(-170,-110,340,220,K,14,1,S,3)+g(-80,-10,.8,0,bars(120,100,4))+path("M10 -60H150","none",W,8,.5)+g(80,30,1,0,circ(0,0,50,"none",1,G,10)+path("M0 0L30 -30","none",W,6))
def bus_stop(): return bus(B)
def road_pins(): return path("M-250 100C-100 -20 100 160 250 20","none",G,6).replace('/>',' stroke-dasharray="3 16"/>')+g(-170,70,.6,0,pin())+g(40,60,.6,0,pin("#2fd0a0"))+g(200,-10,.6,0,pin("#3ea6ff"))
def city(): return ''.join(rect(-180+i*52,60-h,44,h,[K,"#1d2850","#16203f"][i%3],4,1,S,2) for i,h in enumerate([120,200,150,250,180,140,220])) 
def keyfob(): return key(G)
def card(): return rect(-110,-70,220,140,G,14)+rect(-110,-30,220,28,D,0,.8)+rect(-90,20,80,12,D,5,.5)
def sparkle(x,y,s=1,c=Y): return g(x,y,s,0,path("M0 -18L4 -4L18 0L4 4L0 18L-4 4L-18 0L-4 -4Z",c))

# ---------- scenes ----------
def swatches(x,y,cols=(G,B,T,O,W)): return ''.join(rect(x+i*44,y,36,36,c,9) for i,c in enumerate(cols))
def wrench(col=S): return path("M-90 90L40 -40","none",col,22)+circ(60,-60,40,"none",1,col,18)+rect(40,-100,40,30,"#0b1226",0,0)
def appgrid(): return ''.join(rect(-84+(i%3)*60,-84+(i//3)*60,50,50,[G,B,T,O,P,W,B,G,T][i],12,.95) for i in range(9))
S_={}
def sc(name):
    def deco(f): S_[name]=f; return f
    return deco
sc("logo-identity")(lambda: g(400,280,1.9,0,logo_mark())+swatches(250,470)+sparkle(160,160,1.4)+sparkle(650,150))
sc("corporate-branding")(lambda: g(400,280,1.35,0,brandboard())+g(640,440,.9,-8,card())+g(170,450,.8,8,doc(120,160,G,2))+sparkle(650,140))
sc("graphic-design")(lambda: g(400,300,1.05,0,rect(-230,-160,460,320,W,16)+circ(-110,-20,76,G)+poly([(-10,80),(90,-90),(190,80)],B)+circ(130,-70,34,T)+rect(-200,100,220,14,D,7,.35))+g(600,430,1.4,35,path("M0 -60L16 0L0 30L-16 0Z",Y)+rect(-6,30,12,70,S,5))+sparkle(170,130))
sc("flyers-posters-banners")(lambda: g(230,310,1.15,-7,poster())+g(410,320,1.05,5,poster(B))+g(590,320,.95,0,banner_roll(T))+sparkle(400,110,1.3))
sc("social-media")(lambda: g(250,310,1.15,-7,phone(160,320,P))+g(520,290,1.1,0,social())+g(660,140,1,0,heart())+g(150,130,.7,0,heart()))
sc("brochures-catalogues-profiles")(lambda: g(400,300,1.45,0,brochure())+sparkle(130,150,1.2))
sc("marketing-advertising")(lambda: g(250,330,1.6,-8,megaphone())+g(560,250,1,0,rect(-130,-90,260,140,W,10)+rect(-110,-70,140,18,D,6,.7)+rect(-110,-40,100,12,D,6,.4)+g(80,0,.9,0,chartline(G))+rect(-110,0,70,30,G,8))+path("M-10 60V200M10 60V200","none",S,8,1).replace('M-10','M520').replace('M10','M600')+sparkle(650,120))
sc("creative-strategy")(lambda: g(250,300,1.5,0,bulb())+g(560,300,1.3,0,compass())+path("M330 270Q400 200 470 270","none",G,5).replace('/>',' stroke-dasharray="3 14"/>')+sparkle(400,130,1.3))
sc("quotations-invoices")(lambda: g(380,300,1.5,0,invoice())+g(600,420,1.3,0,circ(0,0,50,G)+path("M-4 -26V26M-18 -12H12Q22 -12 22 -2T12 8H-18","none",D,6))+g(180,170,1,0,check()))
sc("business-proposals")(lambda: g(320,310,1.3,-7,doc(200,260,B,5))+g(490,320,1.3,6,doc(200,260,G,5))+g(600,170,1.4,0,check())+sparkle(160,150))
sc("company-profiles")(lambda: g(290,310,1.25,-4,doc(200,260,G,3))+g(540,300,1.7,0,building())+sparkle(430,120,1.2))
sc("reports-statements")(lambda: g(400,300,1.55,0,report())+g(640,200,1.2,0,circ(0,0,46,"none",1,T,12)+path("M0 -46A46 46 0 0 1 40 22","none",G,12))+g(160,420,1,0,chartline(B)))
sc("sops-templates")(lambda: g(380,300,1.5,0,checklist())+g(610,400,1.3,0,gear(48,G))+g(560,230,.7,0,gear(32,B)))
sc("agreements-letters")(lambda: g(380,300,1.5,0,contract())+g(610,430,1.1,0,stamp(O))+g(180,150,1,-30,path("M0 -60L10 0L0 30L-10 0Z",Y)+rect(-4,30,8,60,S,4)))
sc("bilingual-docs")(lambda: g(400,300,1.45,0,bilingual())+f'<text x="250" y="150" font-family="Georgia,serif" font-size="46" fill="{B}">EN</text><text x="500" y="150" font-family="Tahoma,Arial" font-size="52" fill="{G}">ع</text>')
sc("office-admin-systems")(lambda: g(300,320,1.3,0,folder(G))+g(480,300,1.3,0,folder(B).replace(Y,"#9fd0ff"))+g(660,330,1.1,0,folder(T).replace(Y,"#9fe8cf"))+g(400,150,1,0,check())+path("M200 460H620","none",S,4,.5))
sc("computer-laptop-support")(lambda: g(380,350,1.35,0,laptop(340))+g(620,200,1.6,0,gear(40,G))+g(600,430,1,35,wrench())+sparkle(170,160))
sc("os-installation")(lambda: g(380,290,1.2,0,screen(400,B)+rect(-120,10,240,16,D,8,.5)+rect(-120,10,160,16,T,8)+circ(0,-50,28,W,.9))+g(640,440,1,0,usb()))
sc("software-deployment")(lambda: g(250,300,1.7,0,appgrid())+g(430,300,1,0,arrow(G,120))+g(630,230,.55,0,laptop(260))+g(630,430,.55,0,laptop(260)))
sc("networking-infrastructure")(lambda: nodes([(250,170,22),(550,170,22),(150,300,18),(650,300,18),(400,300,28)],[(0,4),(1,4),(2,4),(3,4),(0,1)])+g(400,450,1,0,router()))
sc("windows-server-admin")(lambda: g(330,300,1.5,0,server())+g(600,260,1.2,0,lock(G))+g(600,420,.9,0,person(B)))
sc("backup-recovery")(lambda: g(240,310,1.4,0,database(B))+g(400,310,1,0,arrow(G,100))+g(590,300,1.3,0,shield(T)))
sc("troubleshooting-maintenance")(lambda: g(380,350,1.3,0,laptop(320))+g(600,260,1.4,0,wrench())+g(180,200,1.2,0,gear(36,B))+sparkle(640,130))
sc("integration-automation")(lambda: nodes([(180,200,30),(620,200,30),(180,420,30),(620,420,30)],[(0,1),(0,2),(1,3),(2,3)],G)+g(400,310,1.3,0,gear(70,B)))
sc("general-trading")(lambda: g(400,280,1.7,0,globe(B))+g(200,470,.8,0,cube(60))+g(400,500,.8,0,cube(60,"#9fe8cf",T,"#1c9a76"))+g(600,470,.8,0,cube(60,"#9fd0ff",B,"#2a6fc0")))
sc("industrial-commercial-supplies")(lambda: g(260,320,1.6,0,factory())+g(580,330,1.4,0,pipes())+sparkle(660,130))
sc("product-sourcing")(lambda: g(300,340,1.5,0,cube(80))+g(500,330,.9,0,cube(70,"#9fd0ff",B,"#2a6fc0"))+g(560,240,1.6,0,magnifier(G)))
sc("procurement-support")(lambda: g(300,330,1.5,0,cart(G))+g(560,270,1.3,0,doc(180,230,T,3,W))+g(640,170,1,0,check()))
sc("vendor-coordination")(lambda: g(400,300,1.6,0,two_people())+g(400,140,1.1,0,cube(44))+g(400,470,1,0,path("M-150 0H150","none",S,4,.5)))
sc("safety-materials")(lambda: g(260,330,1.5,0,helmet(G))+g(540,310,1.4,0,vest(O))+g(660,150,.9,0,shield(T)))
sc("medical-scientific")(lambda: g(270,320,1.5,0,stetho(B))+g(540,320,1.4,0,microscope(S))+g(660,140,.8,0,pin(T)))
sc("laboratory-equipment")(lambda: g(260,330,1.5,0,flask(T))+g(470,340,1.3,0,beaker(B))+g(640,350,1,0,flask(O))+sparkle(400,110,1.2))
sc("multi-category-supply")(lambda: g(400,300,1.6,0,shelves())+sparkle(130,130,1.2)+sparkle(680,470))
sc("car-rental")(lambda: path("M60 470H740","none",S,4,.4)+g(400,340,1.6,0,car(G))+g(160,150,1.2,0,key(G))+sparkle(650,130,1.2))
sc("corporate-vehicle-rental")(lambda: g(300,380,1.25,0,car(B))+g(580,250,1.5,0,building(B))+g(650,440,.8,0,rect(-50,-30,100,70,"#7a5a2a",8)+rect(-20,-46,40,18,"#7a5a2a",6)))
sc("transportation-solutions")(lambda: path("M40 470H760","none",S,4,.4)+g(400,340,1.5,0,bus(G))+g(150,170,.9,0,person(B))+g(650,170,.9,0,person(O)))
sc("fleet-management")(lambda: g(250,430,.62,0,car(G))+g(420,430,.62,0,car(B))+g(590,430,.62,0,car(T))+g(400,230,1.05,0,dashboard()))
sc("vehicle-operations")(lambda: g(300,300,1.7,0,steering())+g(580,380,1.3,0,key(G))+g(600,190,.9,0,check()))
sc("mobility-solutions")(lambda: road_pins()+g(250,340,.7,0,car(G))+g(520,200,.6,0,bus(B)))
sc("logistics-coordination")(lambda: path("M40 480H760","none",S,4,.4)+g(360,350,1.25,0,truck())+g(640,170,1.1,0,pin("#ff6b5a"))+path("M470 330Q560 260 630 220","none",G,5).replace('/>',' stroke-dasharray="3 14"/>'))
sc("equipment-rental")(lambda: g(380,340,1.45,0,excavator())+g(650,170,1.3,0,key(G))+path("M40 480H760","none",O,5,.6))
sc("heavy-machinery-support")(lambda: g(300,520,1.0,0,crane(380,W))+g(580,420,.85,0,excavator()))
sc("generator-rental-supply")(lambda: g(400,330,1.6,0,generator())+g(180,170,1.6,0,path("M13 -50L-20 0H0L-10 50L28 -8H6Z",G)))
sc("industrial-equipment")(lambda: g(240,310,1.5,0,gear(80,G))+g(420,230,1.1,0,gear(56,B))+g(520,400,1.3,0,gear(66,O))+g(620,230,.7,0,gear(40,T)))
sc("scientific-equipment")(lambda: g(300,320,1.6,0,microscope(S))+g(560,340,1.3,0,flask(B))+sparkle(650,130,1.2))
sc("site-operational-support")(lambda: g(300,360,1.5,0,hut())+g(560,360,1.6,0,worker(O))+path("M60 470H740","none",O,5,.6)+g(660,430,.7,0,poly([(0,-50),(26,40),(-26,40)],O)))
sc("equipment-sourcing")(lambda: g(300,350,1.1,0,excavator())+g(600,230,1.7,0,magnifier(G)))
sc("manpower-operational-assistance")(lambda: g(220,360,1.5,0,worker(O))+g(400,330,1.7,0,worker(B))+g(580,360,1.5,0,worker(T)))
# extras
sc("page-contact")(lambda: g(300,300,1.5,0,chat(T))+g(570,310,1.6,0,phone(150,300,T))+g(580,170,1,0,heart())+sparkle(160,150,1.2))
sc("page-about")(lambda: g(300,310,1.8,0,compass(G))+g(560,300,1.6,0,person(B,1.4))+sparkle(650,140,1.3)+sparkle(160,460))
sc("page-portfolio")(lambda: g(240,300,1.1,-6,rect(-100,-130,200,260,W,10)+circ(0,-30,50,G)+rect(-70,50,140,14,D,6,.5))+g(420,310,1.1,0,rect(-100,-130,200,260,W,10)+poly([(-80,40),(0,-90),(80,40)],B)+rect(-70,60,140,14,D,6,.5))+g(590,300,1.1,6,rect(-100,-130,200,260,W,10)+circ(0,-30,50,T)+rect(-70,50,140,14,D,6,.5)))
sc("page-services")(lambda: ''.join(g(170+(i%3)*230,210+(i//3)*210,.9,0,rect(-90,-70,180,140,K,16,1,c,4)+ic_) for i,(c,ic_) in enumerate([(B,g(0,0,.6,0,logo_mark())),(G,g(0,0,.5,0,doc(100,130,G,3))),(B,g(0,0,.6,0,gear(40,B))),(T,g(0,0,.6,0,cube(50,"#9fe8cf",T,"#1c9a76"))),(G,g(0,10,.5,0,car(G))),(O,g(0,10,.4,0,excavator()))])))
sc("profile-car")(lambda: g(300,300,1.4,-4,doc(200,260,G,3))+g(540,370,.95,0,car(B))+path("M400 470H700","none",S,4,.4))
sc("profile-heavy")(lambda: g(290,300,1.4,-4,doc(200,260,O,3))+g(540,350,.8,0,excavator())+path("M400 470H720","none",O,5,.5))

def render(scene, pillar, seed=1):
    c1,c2,gl = PAL[pillar]
    r=random.Random(seed*7+len(scene))
    decor=''.join(f'<circle cx="{r.randint(20,780)}" cy="{r.randint(20,300)}" r="{r.choice([.8,1,1.4])}" fill="#fff" opacity="{r.choice([.25,.45,.65])}"/>' for _ in range(34))
    rx=r.choice([160,640]); decor+=circ(rx,r.randint(150,450),r.randint(130,210),"none",.18,gl,2)+circ(rx,300,r.randint(60,100),"none",.1,"#fff",2)
    body=S_[scene]()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient><radialGradient id="l" cx="{r.choice([.3,.5,.7])}" cy="{r.choice([.3,.45])}" r=".62"><stop offset="0" stop-color="{gl}" stop-opacity=".5"/><stop offset="1" stop-color="{gl}" stop-opacity="0"/></radialGradient></defs><rect width="800" height="600" fill="url(#b)"/><rect width="800" height="600" fill="url(#l)"/>{decor}{body}</svg>'''
