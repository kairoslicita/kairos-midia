#!/bin/bash
# R10 opção A: tomada contínua da câmera (assento → janela), com rampas de velocidade e desfoque leve na tela do celular filmado.
# Uso: bash tomada.sh <clipe da câmera 02b2d623...mp4>
CAM="$1"; set -e; rm -rf tomada; mkdir -p tomada
B="split[o][s];[s]crop=478:620:0:230,boxblur=2:2[bl];[o][bl]overlay=0:230"
ffmpeg -v error -y -i "$CAM" -filter_complex "\
[0:v]trim=10:30,setpts=(PTS-STARTPTS)/2,$B[a];\
[0:v]trim=30:48,setpts=(PTS-STARTPTS)/7,$B[b];\
[0:v]trim=48:52.8,setpts=(PTS-STARTPTS)/1.2[c];\
[a][b][c]concat=n=3:v=1,fps=30,scale=1080:1920:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.05:saturation=1.08" -q:v 3 tomada/%04d.jpg
ls tomada | wc -l
