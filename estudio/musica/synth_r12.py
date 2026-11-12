# Trilha do R12 (Robô de lances é permitido?, 20,5 s). Reaproveita build() de synth_reels2.py sem re-gerar as outras trilhas.
src=open('musica/synth_reels2.py').read().split("# R2: drop")[0]
exec(src)
build('musica/trilhas/reel_r12.wav',20.5,[3.6,8.0,13.0,17.2],14.4,120,
      ticks=[9.3+i*.55 for i in range(3)]+[15.0+i*.4 for i in range(3)],stamps=[0.3],coins=[14.4,17.6],alerts=[4.6,5.1])
print('ok')
