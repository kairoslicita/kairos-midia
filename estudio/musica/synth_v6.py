# Trilhas do lote V6 (dispensa: o tempo acaba). Atenção: filmr3.py tira o "b" final do modo; para o modo xb, copiar reel_xb.wav para reel_x.wav antes do render. xa 17,8 s; xb 19,2 s. Reaproveita build() de synth_reels2.py.
exec(open('musica/synth_reels2.py').read().split("# R2: drop")[0])
build('musica/trilhas/reel_xa.wav',17.8,[3.2,6.2,10.8,14.0],7.9,126,ticks=[i*.5 for i in range(0,13)]+[4.1+i*.42 for i in range(5)],stamps=[0.15,11.3],coins=[7.9,11.0],alerts=[6.8])
build('musica/trilhas/reel_xb.wav',19.2,[3.6,7.6,11.4,15.6],11.4,120,ticks=[7.6+i*.5 for i in range(4)]+[12.1+i*.9 for i in range(3)],stamps=[0.2,9.6],coins=[16.4],alerts=[1.2,5.3])
print('ok')
