from PIL import Image
import os

for file in os.listdir("./"):
    ext=file.split(".")[-1]
    if ext=='bmp':
        img=Image.open(file)
        if img.size!=(1280,720):
            print(file)
            