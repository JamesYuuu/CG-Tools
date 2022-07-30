import os
import py7zr

files=os.listdir("./")
currentpath=os.getcwd()
for file in files:
    if os.path.isdir(file):
        os.chdir(file)
        pictures=os.listdir("./")[1:]
        with py7zr.SevenZipFile(file+'.7z', 'w') as zip:
            for picture in pictures:
                print("zipping "+picture)
                zip.write(picture)
                os.remove(picture)
        os.chdir(currentpath)
