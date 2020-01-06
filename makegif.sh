inputdir=images
out=out.gif
palette=palette.png
filters=fps=24,scale=550:-1:flags=lanczos
ffmpeg -v warning -f image2 -i $inputdir/image%05d.png -vf "$filters,palettegen" -y $palette
ffmpeg -v warning -f image2 -i $inputdir/image%05d.png -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $out