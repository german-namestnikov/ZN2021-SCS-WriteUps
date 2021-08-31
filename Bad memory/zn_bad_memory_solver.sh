#!/bin/bash

if [[ $# -ne 1 ]]; then
echo "Provide the image file as argument";
exit
fi

sudo dd if=$1 of=part1 skip=$((0x598000)) bs=1 count=$((0x1000))
sudo dd if=$1 of=part2 skip=$((0x593000)) bs=1 count=5262
cat part1 part2 > archive.rar
echo "Ra" | dd conv=notrunc count=2 bs=1 of=archive.rar
unrar e archive.rar -p'5up3r5eCURE!'

sudo rm part1 part2 archive.rar
