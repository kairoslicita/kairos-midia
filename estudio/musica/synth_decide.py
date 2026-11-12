# Trilhas da série "Você decide o lance" (#1 d1 19,0 s; #2 d2 20,6 s). Reaproveita build() de synth_reels2.py.
exec(open('musica/synth_reels2.py').read().split("# R2: drop")[0])
build('musica/trilhas/reel_d1.wav',19.0,[3.6,8.4,14.0],14.0,116,ticks=[i*1.0 for i in range(1,14)],stamps=[0.2],coins=[15.6],alerts=[9.1,9.9,10.7])
build('musica/trilhas/reel_d2.wav',20.6,[3.4,7.8,12.8,16.8],8.3,124,ticks=[i*1.0 for i in range(0,8)],stamps=[0.2],coins=[8.3,17.6],alerts=[4.2,5.1])
print('ok')
