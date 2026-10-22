# Trilhas originais da semana 27-30/10 + efeitos do Reel "Desligou o computador?"
import numpy as np, pathlib, sys
src=open(pathlib.Path(__file__).with_name('synth2.py')).read().split('def reel_B')[0]
exec(src)  # helpers: Mix, kick, snare, hat, epiano, pad, bass, pluck, bell, vinyl, sine, saw, lp, note, rng, sr
rng=np.random.default_rng(11)

def reel_D():  # 100 BPM, Dm Bb F C, drop em 14.6
    T=21.5; M=Mix(T); b=60/100; off=14.6
    while off>0: off-=4*b
    prog=[(62,[62,65,69]),(58,[58,62,65]),(53,[57,60,65]),(60,[60,64,67])]
    t=off; k=0
    while t<T:
        root,ch=prog[(k//4)%4]; sec=0 if t<3.2 else 1 if t<7 else 2 if t<11 else 3 if t<14.6 else 4 if t<17.4 else 5
        if sec<=4: M.put(t+b/2,hat(.09),.3)
        if sec==0 and k%4==0: M.put(t,pad(ch,4*b,.02,.10),0,1)
        if sec in (1,2,4):
            if k%2==0: M.put(t,kick(.85))
            if k%4==2: M.put(t,snare(.22))
        if sec in (2,4):
            for j in range(4): M.put(t+j*b/4,pluck(ch[(k+j)%3]+12,.16,.08,.28),.5*(1 if j%2 else -1))
        if k%4==0 and sec in (1,2,4): M.put(t,bass(root-24,4*b*.95,.26,.04))
        if sec==4 and k%4==0: M.put(t,pad([m+12 for m in ch],4*b,.07,.12),0,1)
        if sec==3: M.put(t,kick(.5)); M.put(t+b/2,snare(.06+.16*(t-11)/3.6))
        if sec==5 and k%4==0: M.put(t,pad(ch,4*b+.5,.025,.11),0,1); M.put(t,bell(ch[-1]+12,.05),.2)
        t+=b; k+=1
    n=int(3.6*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); M.put(11,(z-lp(z,.35))*(x/3.6)**2*.18)
    M.put(14.6,kick(1.3)); n=int(1.4*sr); x=np.arange(n)/sr; M.put(14.6,lp(rng.standard_normal(n),.08)*np.exp(-x*3)*.3)
    return M

def sfx(M):
    def tone(f0,f1,d,g=.3,w='sine'):
        n=int(d*sr); x=np.arange(n)/sr; f=f0+(f1-f0)*x/d; ph=2*np.pi*np.cumsum(f)/sr
        s=np.sin(ph) if w=='sine' else 2*((ph/2/np.pi)%1)-1
        return s*np.minimum(1,x/.004)*np.exp(-x*3/d)*g
    def whoosh(d=.45,g=.22):
        n=int(d*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); e=np.sin(np.pi*x/d)**2
        return (.4*lp(z,.05)+.6*lp(z,.2)*(x/d))*e*g*1.6
    def click(g=.35):
        n=int(.03*sr); x=np.arange(n)/sr; return rng.standard_normal(n)*np.exp(-x*300)*g+np.sin(2*np.pi*1800*x)*np.exp(-x*200)*g
    def ding(m,g=.18): return bell(m,g)
    M.put(.45,tone(420,60,.55,.35)); M.put(.45,click(.4))           # computador desliga
    M.put(1.1,whoosh(.35,.2)); M.put(1.15,kick(.7))                   # "O robô, não."
    for t in (3.2,7.0,11.0,17.4): M.put(t-.15,whoosh())
    for i,t in enumerate((3.7,4.5,5.3)): M.put(t,ding(81+i*2,.16),.3*(i-1))  # notificações
    for i,t in enumerate((8.2,8.9,9.6)): M.put(t,tone(880,1320,.18,.14),.4*(i-1)); M.put(t+.09,ding(88,.08))  # ganhando
    for k,t in enumerate((11.2,11.5,12.0,12.3,12.8,13.1,13.6,13.9)):  # lances
        M.put(t,tone(300 if k%2==0 else 900,280 if k%2==0 else 1100,.09,.18),.3 if k%2 else -.3)
    M.put(15.0,click(.5)); M.put(15.05,tone(600,1200,.12,.16)); M.put(15.6,ding(84,.14)); M.put(15.75,ding(88,.12))
    M.put(17.9,tone(500,900,.1,.14)); M.put(18.0,click(.25))

def carrossel(T,bpm,prog,style,seed):
    global rng; rng=np.random.default_rng(seed); M=Mix(T); b=60/bpm; t=0; k=0
    while t<T:
        root,ch=prog[(k//4)%4]
        if style=='lofi':
            if k%4==0: M.put(t,epiano(ch,4*b*1.02,.12),0,1); M.put(t,bass(root-12,4*b*.9,.17,.025))
            if k%4==0 or k%8==6: M.put(t,kick(.55))
            if k%4==2: M.put(t,snare(.16,True))
            M.put(t+b/2,hat(.05),.3)
            if k%8==5: M.put(t+b/2,bell(ch[-1]+12,.05),-.3)
        else:
            if k%4==0: M.put(t,pad(ch,4*b+.4,.025,.10),0,1); M.put(t,bass(root-12,4*b*.9,.15,.03))
            if k%2==0: M.put(t,kick(.4))
            M.put(t+b/2,hat(.06),.25)
            if k%2==1: M.put(t,pluck(ch[k%3]+12,.2,.07,.2),.4)
        t+=b; k+=1
    if style=='lofi': M.put(0,vinyl(T,.012),0,1)
    return M

if __name__=='__main__':
    out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.')
    M=reel_D(); sfx(M); M.out(str(out/'reel_D_desligou.wav'),2.0)
    carrossel(48.0,80,[(53,[53,57,60,64]),(50,[50,53,57,60]),(55,[55,58,62,65]),(48,[52,55,58,60])],'lofi',21).out(str(out/'carrossel_C_lofi_preco.wav'),.01,.3,.2)
    carrossel(42.0,104,[(57,[57,60,64]),(60,[60,64,67]),(55,[55,59,62]),(53,[53,57,60])],'tech',33).out(str(out/'carrossel_D_tech_modos.wav'),.01,.3,.2)
    print('ok')
