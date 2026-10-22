import numpy as np, sys
sys.path.insert(0,'.')
exec(open('musica/synth2.py').read().split("def reel_B")[0])  # reutiliza instrumentos
def tick(g=.25):
    n=int(.04*sr); x=np.arange(n)/sr; return sine(1800,n)*np.exp(-x*120)*g
def whoosh(d=.35,g=.22):
    n=int(d*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); z=(lp(z,.06)*(1-x/d)+lp(z,.4)*(x/d))*np.sin(np.pi*x/d)**1.5; return z*g*3
def coin(g=.2):
    n=int(.5*sr); x=np.arange(n)/sr; return (sine(1318,n)+sine(1975,n)*.8)*np.exp(-x*7)*g
def stamp(g=.7):
    n=int(.4*sr); x=np.arange(n)/sr; return (sine(70,n)*np.exp(-x*10)+lp(rng.standard_normal(n),.2)*np.exp(-x*30)*.5)*g
def alert(g=.2):
    n=int(.25*sr); x=np.arange(n)/sr; return sine(520,n)*np.exp(-x*10)*g
def build(name,T,cuts,drop,bpm,ticks=(),stamps=(),coins=(),alerts=()):
    M=Mix(T); b=60/bpm; off=drop
    while off>0: off-=4*b
    prog=[(57,[57,60,64]),(53,[53,57,60]),(55,[55,59,62]),(52,[52,56,59])]
    t=off; k=0
    while t<T:
        root,ch=prog[(k//4)%4]; sec=0 if t<drop-3.5 else 1 if t<drop else 2
        if t>=0:
            M.put(t+b/2,hat(.10),.3)
            if sec>=1 or k%2==0: M.put(t,kick(.9 if sec==2 else .7))
            if k%2==1 and sec>=1: M.put(t,snare(.24))
            if sec>=1:
                for j in range(2): M.put(t+j*b/2,pluck(ch[(k*2+j)%3]+12,.22,.11,.3),.4*(1 if j else -1))
            if k%4==0: M.put(t,bass(root-12,4*b*.95,.28 if sec==2 else .2,.05))
            if sec==2 and k%4==0: M.put(t,pad([m+12 for m in ch],4*b,.08,.11),0,1)
        t+=b; k+=1
    # riser antes do drop
    n=int(2.0*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); M.put(drop-2.0,(z-lp(z,.4))*(x/2.0)**2*.2)
    M.put(drop,kick(1.2)); n=int(1.2*sr); x=np.arange(n)/sr; M.put(drop,lp(rng.standard_normal(n),.1)*np.exp(-x*3)*.3)
    for c in cuts: M.put(max(0,c-.06),whoosh(.28,.16),0)
    for c in ticks: M.put(c,tick(),.2)
    for c in stamps: M.put(c,stamp(),0)
    for c in coins: M.put(c,coin(),0)
    for c in alerts: M.put(c,alert(),-.2)
    M.out(name,1.5)
# R2: drop no reveal do preço (5.4+1.2); ticks: chips e digitação
build('musica/trilhas/reel_r2.wav',18.5,[2.4,5.4,8.4,12.0,15.0],6.6,124,
      ticks=[2.4+i*.62 for i in range(4)]+[8.4+i*.1 for i in range(11)],stamps=[1.0+.1],coins=[6.6,16.0],alerts=[])
# R3: drop quando o robô cobre (4.6); ticks a cada cobertura
cov=[4.6+.35+i*1.05+.38 for i in range(5)]
build('musica/trilhas/reel_r3.wav',18.5,[2.4,4.6,10.4,13.4],4.6,124,
      ticks=cov,alerts=[.25,.55,.85,1.15]+[2.4+i*.5 for i in range(4)],coins=[10.9,14.0])
cov4=[4.6+(.35+i*1.05+.38)*1 for i in range(5)]
build('musica/trilhas/reel_r4.wav',15.5,[2.3,4.6,9.6,11.8],4.6,124,ticks=cov4,alerts=[2.3,2.8,3.3],stamps=[.5,3.8],coins=[10.1,12.4])
print('ok')
