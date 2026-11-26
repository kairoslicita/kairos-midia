# Trilhas do lote V7 (dispensa: C "Esperando a prorrogação?" 18,0 s; D "17:57" 17,4 s). Reaproveita build() de synth_reels2.py.
exec(open('musica/synth_reels2.py').read().split("# R2: drop")[0])
build('musica/trilhas/reel_xc.wav',18.0,[3.3,7.3,11.0,14.5],8.9,122,ticks=[4.2,5.2,6.2]+[7.3+i*.8 for i in range(3)],stamps=[0.15,8.9],coins=[12.3],alerts=[4.2])
build('musica/trilhas/reel_xd.wav',17.4,[3.3,6.6,9.9,13.8],10.2,124,ticks=[3.4+i*.09*3 for i in range(5)]+[10.2+i*.75 for i in range(3)],stamps=[0.15],coins=[7.5,10.5,11.3,12.0],alerts=[1.0])
print('ok')
