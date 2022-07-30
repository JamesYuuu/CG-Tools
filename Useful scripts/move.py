import os
import shutil
from tqdm import tqdm

files=os.listdir("./")
currentpath=os.getcwd()
for file in tqdm(files):
    if os.path.isdir(file):
        os.chdir(file)
        for member in os.listdir("./"):
            shutil.move(member,currentpath)
        os.chdir(currentpath)
        os.rmdir(file)