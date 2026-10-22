import numpy as np, wave, sys
sr=44100
rng=np.random.default_rng(3)
def lp(x,c):
    from scipy.signal import lfilter
    return lfilter([c],[1,-(1-c)],x)
def saw(f,n,det=0):
    x=np.arange(n)/sr; s=0; ds=[-det,0,det] if det else [0]
    for d in ds: s=s+2*((x*f*(1+d))%1)-1
    return s/len(ds)
def tri(f,n): x=np.arange(n)/sr; return 2*np.abs(2*((x*f)%1)-1)-1
def sine(f,n): return np.sin(2*np.pi*f*np.arange(n)/sr)
def note(m): return 440*2**((m-69)/12)
class Mix:
    def __init__(s,T): s.N=int(sr*T); s.L=np.zeros(s.N); s.R=np.zeros(s.N); s.T=T
    def put(s,t,sig,pan=0,g=1):
        i=int(t*sr)
        if i<0 or i>=s.N: return
        n=min(len(sig),s.N-i); s.L[i:i+n]+=sig[:n]*g*(1-pan); s.R[i:i+n]+=sig[:n]*g*(1+pan)
    def out(s,name,fade=1.5,delay=.375,wet=.18):
        d=int(delay*sr); L=s.L.copy(); R=s.R.copy(); L[d:]+=wet*s.R[:-d]; R[d:]+=wet*s.L[:-d]
        f=np.ones(s.N); k=int(fade*sr); f[-k:]=np.linspace(1,0,k); f[:int(.02*sr)]=np.linspace(0,1,int(.02*sr))
        L*=f; R*=f; m=max(abs(L).max(),abs(R).max()); L/=m/.89; R/=m/.89
        w=wave.open(name,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.stack([L,R],1)*32767).astype(np.int16).tobytes()); w.close()
def kick(p=1):
    n=int(.35*sr); x=np.arange(n)/sr; f=48+95*np.exp(-x*30); return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-x*9)*.9*p
def snare(g=.3,lofi=False):
    n=int(.25*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); z=z-lp(z,.15)
    if lofi: z=lp(z,.3)
    return (z*np.exp(-x*16)+.4*sine(190,n)*np.exp(-x*25))*g
def hat(g=.16,o=False):
    n=int((.16 if o else .05)*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); z=z-lp(z,.5); return z*np.exp(-x*(16 if o else 70))*g
def epiano(ms,d,g=.12):
    n=int(d*sr); x=np.arange(n)/sr; s=sum(sine(note(m),n)+.3*sine(note(m)*2,n)*np.exp(-x*3) for m in ms)/len(ms)
    return s*np.exp(-x*1.2)*np.minimum(1,x/.01)*g
def pad(ms,d,c=.03,g=.1):
    n=int(d*sr); s=sum(saw(note(m),n,.004) for m in ms)/len(ms); x=np.arange(n)/sr
    return lp(s,c)*np.minimum(1,x/.5)*np.clip((d-x)/.5,0,1)*g
def bass(m,d,g=.3,c=.05):
    n=int(d*sr); x=np.arange(n)/sr; s=saw(note(m),n)+.6*sine(note(m-12),n); return lp(s,c)*np.minimum(1,x/.005)*(.6+.4*np.exp(-x*3))*np.clip((d-x)/.05,0,1)*g
def pluck(m,d=.25,g=.13,c=.25):
    n=int(d*sr); x=np.arange(n)/sr; return lp(saw(note(m),n),c)*np.exp(-x*12)*g
def bell(m,g=.1):
    n=int(1.2*sr); x=np.arange(n)/sr; return (sine(note(m),n)+.5*sine(note(m)*2.76,n)*np.exp(-x*4))*np.exp(-x*2.5)*g
def vinyl(T,g=.02):
    n=int(T*sr); z=lp(rng.standard_normal(n),.2)*g; cr=(rng.random(n)>.9996)*rng.standard_normal(n)*.3; return z+cr

def reel_B():  # lo-fi hip hop tenso, 90 BPM, drop em 14.6
    T=21.5; M=Mix(T); bpm=90; b=60/bpm; off=14.6-8*b*2  # align: drop at bar boundary
    while off>0: off-=4*b
    prog=[(57,[57,60,64,67]),(53,[53,57,60,64]),(50,[50,53,57,60]),(52,[52,56,59,62])]
    M.put(0,vinyl(T),0,1)
    t=off; k=0
    while t<T:
        root,ch=prog[(k//4)%4]; sec=0 if t<3.2 else 1 if t<11 else 2 if t<14.6 else 3 if t<18.5 else 4
        if k%4==0: M.put(t,epiano(ch,4*b*1.02,.13 if sec<3 else .16),0,1)
        if sec>=1 and sec!=4:
            if k%4 in (0,) or (k%8==6): M.put(t,kick(.8))
            if k%4==2: M.put(t,snare(.28,True))
            M.put(t+b/2,hat(.08),.3); M.put(t,hat(.06),-.3)
        if sec in (1,3) and k%4==0: M.put(t,bass(root-12,4*b*.95,.26,.03))
        if sec==3 and k%2==0: M.put(t,bell(ch[-1]+12,.07),.3)
        if sec==2: M.put(t,snare(.12*(1+(t-11)/3.6),True)); M.put(t+b/2,snare(.10*(1+(t-11)/3.6),True))
        t+=b; k+=1
    n=int(3.6*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); M.put(11,(z-lp(z,.3))*(x/3.6)**2*.18)
    n=int(1.2*sr); x=np.arange(n)/sr; M.put(14.6,sine(45,n)*np.exp(-x*4)*.6+lp(rng.standard_normal(n),.06)*np.exp(-x*4)*.4)
    M.out('reel_B_lofi_tenso.wav',2.0)

def reel_C():  # corporativo animado, maior, 124 BPM
    T=21.5; M=Mix(T); bpm=124; b=60/bpm; off=14.6
    while off>0: off-=4*b
    prog=[(60,[60,64,67]),(55,[55,59,62]),(57,[57,60,64]),(53,[53,57,60])]
    t=off; k=0
    while t<T:
        root,ch=prog[(k//4)%4]; sec=0 if t<3.2 else 1 if t<11 else 2 if t<14.6 else 3 if t<18.8 else 4
        if sec in (0,1,2,3): M.put(t+b/2,hat(.12),.3)
        if sec in (1,3): M.put(t,kick())
        if sec in (1,3) and k%2==1: M.put(t,snare(.24))
        if sec==0 and k%2==0: M.put(t,pluck(ch[0]+12,.2,.10),-.2)
        if sec in (1,3): 
            for j in range(2): M.put(t+j*b/2,pluck(ch[(k*2+j)%3]+12,.22,.12,.3),.4*(1 if j else -1))
        if k%4==0 and sec>=1 and sec!=4: M.put(t,bass(root-12,4*b*.95,.28,.06))
        if sec==3 and k%4==0: M.put(t,pad([m+12 for m in ch],4*b,.08,.12),0,1)
        if sec==2: M.put(t,snare(.08+.18*(t-11)/3.6)); M.put(t+b/2,snare(.06+.16*(t-11)/3.6))
        if sec==4 and k%4==0: M.put(t,pad(ch,4*b+.5,.03,.12))
        t+=b; k+=1
    n=int(3.6*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); M.put(11,(z-lp(z,.4))*(x/3.6)**2*.2)
    M.put(14.6,kick(1.2)); n=int(1.5*sr); x=np.arange(n)/sr; M.put(14.6,lp(rng.standard_normal(n),.1)*np.exp(-x*3)*.35)
    M.out('reel_C_corporativo_animado.wav',2.0)

def carrossel(name,style):  # 48 s contínuo, fatiado por slide depois
    T=48.0; M=Mix(T)
    if style=='lofi':
        bpm=84; b=60/bpm; prog=[(57,[57,60,64,67]),(53,[53,57,60,64]),(48,[52,55,59,60]),(55,[55,59,62,65])]
        M.put(0,vinyl(T,.015),0,1); t=0; k=0
        while t<T:
            root,ch=prog[(k//4)%4]
            if k%4==0: M.put(t,epiano(ch,4*b*1.02,.12),0,1); M.put(t,bass(root-12,4*b*.9,.18,.025))
            if k%4==0 or k%8==5: M.put(t,kick(.6))
            if k%4==2: M.put(t,snare(.18,True))
            M.put(t+b/2,hat(.05),.3)
            if k%8==3: M.put(t+b/2,bell(ch[-1]+12,.05),-.3)
            t+=b; k+=1
    else:  # minimal tech
        bpm=110; b=60/bpm; prog=[(57,[57,64,69]),(53,[53,60,65]),(55,[55,62,67]),(52,[52,59,64])]
        t=0; k=0
        while t<T:
            root,ch=prog[(k//4)%4]
            if k%4==0: M.put(t,pad(ch,4*b+.4,.025,.11),0,1)
            if k%2==0: M.put(t,kick(.45))
            M.put(t+b/2,hat(.07),.25)
            for j in range(2): M.put(t+j*b/2,pluck(ch[(k+j)%3]+12,.18,.07,.2),.5*(1 if j else -1))
            if k%4==0: M.put(t,bass(root-24+12,4*b*.9,.16,.03))
            t+=b; k+=1
    M.out(name,2.5,.3,.2)
reel_B(); reel_C(); carrossel('carrossel_A_lofi.wav','lofi'); carrossel('carrossel_B_minimal_tech.wav','tech')
print('ok')
