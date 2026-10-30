exec(open('musica/synth_reels3.py').read().split('# R7 (33 s)')[0])
# R10 · voo: tensão até a falha do Wi-Fi; virada em 11.6 ("O robô, não.")
build('musica/trilhas/reel_r10.wav',20.0,[2.8,5.0,8.9,11.6,14.8,16.0],11.6,124,
      ticks=[5.4+i*.25 for i in range(8)]+[7.6],stamps=[8.95,11.6],coins=[12.5,14.9,16.6],alerts=[9.2,9.7,10.2,10.7])
print('ok')
# R10 opção A (tomada contínua): virada em 8.6 ("O robô, não.")
build('musica/trilhas/reel_a.wav',20.0,[2.8,6.0,8.6,11.4,12.57,16.57],8.6,124,
      ticks=[2.9+i*.3 for i in range(7)],stamps=[6.0,8.6],coins=[9.6,14.3,17.1],alerts=[6.3,6.8,7.3,7.8])
build('musica/trilhas/reel_h.wav',3.6,[2.05],2.05,124,alerts=[.35,1.05],coins=[1.1],stamps=[2.05])
build('musica/trilhas/reel_h.wav',4.5,[3.0],3.0,124,alerts=[.9],coins=[.95],stamps=[3.0])
