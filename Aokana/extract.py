import clr
clr.AddReference("Assembly-Csharp")
from Aokana import PRead

import os,csv,sys

# make sure input_dat_path contains all dat file
def extract_dat():

    if not os.path.exists('./extract'):
        os.mkdir('./extract')

    for file in os.listdir():

        print(f"Start extracting {file}...")

        dat = PRead('./'+file)
        file = file.replace('.dat', '/')

        for key in dat.ti.Keys:
            full_path = './extract/' + file + key
            file_name = full_path.split("/")[-1]
            dir_name = full_path.replace(file_name, "")
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with open(full_path , "wb+") as f:
                f.write(bytes(dat.Data(key)))

def merge_image():

    print("Start merging image...")

    with open('vcglist.csv','r',encoding='utf-8') as file:

        filereader = csv.reader(file,delimiter=' ')
        os.mkdir("combined")

        for row in filereader:
            cgname = row[0].lower()
            combo = [item + ".webp" for item in row]
            res = os.system("magick " + ' '.join(combo) +  " -mosaic " + "./combined/" + cgname + ".png")
            if res!=0:
                print("Error: " + cgname)

if __name__ == '__main__':

    if "-d" in sys.argv:
        extract_dat()
    elif "-m" in sys.argv:
        merge_image()
    else:
        print("Use the python script AFTER reading readme.md!")
        print("Usage: python extract.py [-d] [-m]")
        print("[-d]: Extract .dat")
        print("[-m]: Merge all cgs")