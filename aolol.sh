#!/usr/bin/env bash

fgFrames=(
  /usr/share/aolol/aol-frame-1.gif
  /usr/share/aolol/aol-frame-2.gif
  /usr/share/aolol/aol-frame-2.gif
  /usr/share/aolol/aol-frame-3.gif
)
bgFrames=(
  /tmp/screen-1.png
  /tmp/screen-2.png
  /tmp/screen-3.png
  /tmp/screen-4.png
)
overlayFrames=(
  /tmp/overlay-1.png
  /tmp/overlay-2.png
  /tmp/overlay-3.png
  /tmp/overlay-4.png
)

tmpbg='/tmp/screen.png'
scrot "$tmpbg"

convert "$tmpbg" -scale 5% -scale 2000% ${bgFrames[0]}
convert "$tmpbg" -scale 10% -scale 1000% ${bgFrames[1]}
convert "$tmpbg" -scale 20% -scale 500% ${bgFrames[2]}
convert "$tmpbg" -scale 50% -scale 200% ${bgFrames[3]}

rm "$tmpbg"

for i in "${!bgFrames[@]}"; do
  convert "${bgFrames[$i]}" "${fgFrames[$i]}" -gravity center -composite -matte "${overlayFrames[$i]}"
done

for frame in "${overlayFrames[@]}"; do
  echo $frame
  i3lock -u -i $frame
  sleep 1
  killall i3lock
done

