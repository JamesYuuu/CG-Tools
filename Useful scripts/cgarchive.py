import os
import shutil
import tqdm

os.chdir("./fgimage")
files=os.listdir("./")
currentname=files[0].split("_")[0]
list=[]
currentpath=os.getcwd()
for file in files:
    name=file.split("_")[0]
    if name==currentname:
            list.append(file)
    else:
        os.mkdir("./"+currentname)
        for picture in tqdm(list):
            shutil.move(picture,"./"+currentname)
            print("moving %s" %picture)
        list=[file]
        currentname=name
os.mkdir("./"+currentname)
for picture in tqdm(list):
    shutil.move(picture,"./"+currentname)
    print("moving %s" %picture) 