import os
from tqdm import tqdm

os.chdir("./evcg")

for item in tqdm(os.listdir("./")):
    ext=item.split(".")[-1]
    newname=item.split(".")[0]+'.png'
    if ext=='bmp':
        os.system("magick "+item+' -quality 100 '+newname)
        os.remove(item)
        