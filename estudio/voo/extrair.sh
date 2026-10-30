#!/bin/bash
# Extrai os trechos reais do voo (30/10/2026) em quadros JPG, com desfoque de dados sensíveis.
# Uso: bash extrair.sh <gravação de tela> <clipe da câmera no assento>
SCR="$1"; CAM="$2"; set -e
AT="[0:v]split=2[a][b];[b]crop=200:200:965:1150,boxblur=25[c];[a][c]overlay=965:1150"   # botão flutuante (AssistiveTouch)
seg(){ # nome início duração filtro_extra
  rm -rf "$1"; mkdir -p "$1"
  ffmpeg -v error -y -ss "$2" -t "$3" -i "$SCR" -filter_complex "$AT[x];[x]$4fps=30,scale=840:-2" -q:v 3 "$1/%04d.jpg"
}
# S3a: digitando o stop loss · S3b: "Configuração salva no servidor"
seg s3a 11.0 2.5 ""
seg s3b 14.0 1.4 ""
# S4: "Confira a conexão" (oculta o número da compra)
seg s4 18.0 3.4 "split=2[p][q];[q]crop=620:420:40:280,boxblur=30[r];[p][r]overlay=40:280,"
# S5: órbita perdendo → ganhando (oculta a descrição do item) · S5b: "Nenhuma ação necessária agora"
seg s5 26.0 3.2 "split=3[p][q][u];[q]crop=360:230:90:730,boxblur=30[r];[u]crop=270:830:370:1640,boxblur=28[v];[p][r]overlay=90:730[pr];[pr][v]overlay=370:1640,"
# cartão parado (a tela rola logo depois e mostraria o número da compra): um quadro só
rm -rf s5b; mkdir -p s5b; ffmpeg -v error -y -ss 29.42 -i "$SCR" -frames:v 1 -vf "scale=840:-2" -q:v 2 s5b/0001.jpg
# nuvens: visor da câmera (sem a interface), recortado para 9:16
rm -rf nuvens; mkdir -p nuvens
ffmpeg -v error -y -ss 45.2 -t 2.2 -i "$SCR" -vf "crop=754:1340:0:360,setpts=1.3*PTS,fps=30,scale=1080:1920:flags=lanczos,unsharp=5:5:0.6" -q:v 3 nuvens/%04d.jpg
# celular na mão no assento
rm -rf assento; mkdir -p assento
# só o 1º segundo (Painel): depois a tela mostra o nome do órgão da compra
ffmpeg -v error -y -ss 0 -t 1.0 -i "$CAM" -vf "setpts=2.25*PTS,fps=30,scale=1080:-2,unsharp=5:5:0.8,crop=1080:1920" -q:v 3 assento/%04d.jpg
echo ok
