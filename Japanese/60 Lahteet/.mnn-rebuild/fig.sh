#!/bin/bash
# usage: fig.sh <key> <pdfpage NNN> <name> <H> <W> <Y> <X>   (coords in original PNG px)
V="/Users/claude/Claude/dev/learning-center/Japanese/70 Visuaalinen/liitteet"
out="$V/mnn-chukyu1-$1-p$2-$3.png"
sips -c $4 $5 --cropOffset $6 $7 "$1/pages/p$2.png" --out "$out" >/dev/null && echo "$(basename "$out")"
