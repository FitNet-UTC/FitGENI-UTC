#Needs ffmpeg

import os
import sys
import shutil

from os import listdir
from os.path import isfile, join

import glob



loc="C:\Users\Noah\Desktop\Fitnet"                   #Enter your path for video
file="fire_ice1_1080.mp4"                       #Enter your file name
frame='320x240'                     #Enter your frame width and height WxH. Do not change the "x"
out='C:\Users\Noah\Desktop\Fitnet\\b\\'               #output path. Need \\ Move will fail without double

print(glob.glob("C:\Users\Noah\Desktop\Fitnet\*.jpeg"  )) # location for output images


loc="cd "+loc

os.system(loc)
os.system('ffmpeg -i '+file+' -vsync 0 -vf select="eq(pict_type\,PICT_TYPE_I)" -s '+frame+' -f image2 foo-%03d.jpeg')

c=0
for i in glob.glob("C:\Users\Noah\Desktop\Fitnet\*.jpeg"):
    c=c+1
    os.system('move '+i+'   '+out+str(c)+'.jpeg')