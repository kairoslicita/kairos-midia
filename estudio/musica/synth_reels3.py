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

# R7 (33 s): drop após o gancho (3.2); tiques nas linhas que entram; robô cobre a partir de 14.6+2.6
cov7=[14.6+2.6+.25+.3+i*1.0 for i in range(4)]
build('musica/trilhas/reel_r7.wav',33.0,[3.2,9.0,14.6,21.8,27.0],3.2,118,
      ticks=[.6,.8,1.0,1.2]+[3.6,3.95,4.3]+[9.35,9.6,9.85,10.1]+cov7+[22.15,22.45,22.75],stamps=[1.45],coins=[5.9,12.0,28.0],alerts=[11.8])
# R8 (18.4 s): carimbo no ENCERRADO (6.4) e nos cortes secos (7.0, 8.05); drop no robô (9.4)
cov8=[9.4+.3+.3+i*.85 for i in range(3)]
build('musica/trilhas/reel_r8.wav',18.4,[2.4,9.4,14.6],9.4,128,
      ticks=[2.4+1.2+i*.33 for i in range(8)]+cov8,stamps=[.5,6.4,7.0,8.05],coins=[15.0],alerts=[2.4+i*.8 for i in range(5)]+[9.4+.3+3*.85+.3])
# R9 (29.6 s): carimbos nos erros; alertas nas notificações; drop na virada (16.6)
build('musica/trilhas/reel_r9.wav',29.6,[3.0,7.6,12.0,16.6,24.4],16.6,120,
      ticks=[7.6+.4,7.6+.7,7.6+1.0],stamps=[.35,.85,1.35,3.0+1.9,7.6+1.7],coins=[16.6+.7+.35+i*1.45 for i in range(4)]+[24.9],alerts=[12.0+.45+i*.75 for i in range(4)])
print('ok')
