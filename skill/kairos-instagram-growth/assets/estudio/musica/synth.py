import numpy as np, wave
sr=44100; T=21.5; N=int(sr*T); L=np.zeros(N); R=np.zeros(N)
BPM=120; beat=60/BPM; off=0.6; bar=4*beat
rng=np.random.default_rng(7)
def place(t,sig,pan=0.0,g=1.0):
    i=int(t*sr)
    if i>=N: return
    n=min(len(sig),N-i)
    if i<0: return
    L[i:i+n]+=sig[:n]*g*(1-pan)/1; R[i:i+n]+=sig[:n]*g*(1+pan)/1
def env(n,a=.005,d=.2,s=0.,r=.05,dur=None):
    x=np.arange(n)/sr; e=np.ones(n)
    e=np.minimum(1,x/max(a,1e-4))*np.exp(-x/d) if s==0 else np.minimum(1,x/a)*(s+(1-s)*np.exp(-x/d))
    if dur: e*=np.clip((dur-x)/r,0,1)
    return e
def lp(x,c):
    y=np.zeros_like(x); a=c; prev=0.
    for i in range(len(x)): prev+=a*(x[i]-prev); y[i]=prev
    return y
def saw(f,n,det=0):
    x=np.arange(n)/sr; s=0
    for d in ([-det,0,det] if det else [0]): s=s+2*((x*f*(1+d))%1)-1
    return s/(3 if det else 1)
def note(m): return 440*2**((m-69)/12)
def kick():
    n=int(.35*sr); x=np.arange(n)/sr; f=50+90*np.exp(-x*30); ph=2*np.pi*np.cumsum(f)/sr
    return np.sin(ph)*np.exp(-x*9)*0.9
def clap():
    n=int(.25*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); z=z-lp(z,.15)
    return z*np.exp(-x*18)*0.35
def hat(o=False):
    n=int((.18 if o else .05)*sr); x=np.arange(n)/sr; z=rng.standard_normal(n); z=z-lp(z,.5)
    return z*np.exp(-x*(18 if o else 70))*0.18
def bass(m,d):
    n=int(d*sr); s=saw(note(m),n)+0.5*np.sin(2*np.pi*note(m-12)*np.arange(n)/sr)
    return lp(s,.06)*env(n,.005,.35,.6,.04,d)*0.32
def pad(ms,d,c=.03,g=.12):
    n=int(d*sr); s=sum(saw(note(m),n,.004) for m in ms)/len(ms)
    x=np.arange(n)/sr; e=np.minimum(1,x/.4)*np.clip((d-x)/.4,0,1)
    return lp(s,c)*e*g
def pluck(m,d=.22,g=.14):
    n=int(d*sr); x=np.arange(n)/sr; s=saw(note(m),n); s=lp(s,.25)
    return s*np.exp(-x*14)*g
def stab(ms,g=.16):
    n=int(.35*sr); x=np.arange(n)/sr; s=sum(saw(note(m),n,.006) for m in ms)/len(ms)
    return lp(s,.2)*np.exp(-x*7)*g
# progression Am F C G  (roots midi)
prog=[(57,[57,60,64]),(53,[53,57,60]),(48,[52,55,60]),(55,[55,59,62])]
nb=int((T-off)/beat)+1
for b in range(-2,nb):
    t=off+b*beat
    if t<0: continue
    bi=(b//4)%4; root,ch=prog[bi]
    sec = 0 if t<3.2 else 1 if t<7.0 else 2 if t<11.0 else 3 if t<14.6 else 4 if t<17.4 else 5
    # hats ticking from start
    if sec in (0,1,2,3,4): place(t+beat/2,hat(),.3); 
    if sec in (2,4): place(t,hat(),-.3,.7)
    if sec==0: place(t,np.sin(2*np.pi*note(root-12)*np.arange(int(.4*sr))/sr)*np.exp(-np.arange(int(.4*sr))/sr*6)*.25)
    if sec in (1,2,4) or (sec==3): place(t,kick())
    if sec in (2,4) and b%2==1: place(t,clap(),0,1)
    if b%4==0 and sec>=1 and sec!=5:
        place(t,bass(root-12,bar*0.98),0,1)
    if sec in (2,4):
        arp=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+12]
        for k in range(4): place(t+k*beat/4,pluck(arp[k]),.4*(1 if k%2 else -1))
    if sec==4 and b%2==0: place(t,stab([m+12 for m in ch]),0,1)
    if sec==5 and b%4==0: pass
# pads per bar
b=0
t=off
while t<T:
    bi=int(round((t-off)/bar))%4; root,ch=prog[bi]
    c=.02 if t<11 else .02+.08*min(1,(t-11)/3.6) if t<14.6 else .06
    place(t,pad(ch,bar+.4,c,.10 if t<14.6 else .13),0,1)
    t+=bar
# build 11-14.6: snare roll + riser
for k in range(int(3.6/ (beat/4))):
    tt=11+k*beat/4; place(tt,clap()*(0.3+0.7*k/28),0,.6)
n=int(3.6*sr); z=rng.standard_normal(n); x=np.arange(n)/sr
place(11,(z-lp(z,.3))*(x/3.6)**2*0.25)
# drop impact
n=int(1.5*sr); x=np.arange(n)/sr; z=rng.standard_normal(n)
place(14.6,lp(z,.08)*np.exp(-x*3)*0.5+np.sin(2*np.pi*45*x)*np.exp(-x*4)*0.6)
# intro clock tick feel handled by hats; outro fade
fade=np.ones(N); fs=int(19.5*sr); fade[fs:]=np.linspace(1,0,N-fs)
L*=fade; R*=fade
# simple stereo delay on mix
d=int(.375*sr); L[d:]+=0.18*R[:-d]; R[d:]+=0.18*L[:-d]
m=max(np.abs(L).max(),np.abs(R).max()); L/=m/0.89; R/=m/0.89
st=np.stack([L,R],1); 
w=wave.open('musica_reel_kairos.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
print('ok')
