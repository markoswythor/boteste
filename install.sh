#!/usr/bin/bash

apt-get update
apt-get upgrade
apt-get install nodejs
apt-get install webp
apt-get install ffmpeg
apt-get install wget
apt-get install tesseract
apt-get install python3
apt-get install python3-pip
python3 -m pip install youtube_search
python3 -m pip install googletrans==3.1.0a0
wget -O ~/../usr/share/tessdata/ind.traineddata "https://github.com/tesseract-ocr/tessdata/blob/master/ind.traineddata?raw=true"
npm install image-to-base64
npm install

echo "[*] All dependencies have been installed, please run the command \"node index.js\" to immediately start the script"
