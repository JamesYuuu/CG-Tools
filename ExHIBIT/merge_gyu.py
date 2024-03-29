import os,struct,sys

def decode():
    print("Start decoding...")
    os.system("fixipgyu.exe def.rld")

def gyu_to_bmp():
    print("Start transforming gyu to bmp...")
    for files in os.listdir("./"):
        if os.path.isdir(files):
            for file in os.listdir(files):
                file=os.path.join(files,file)
                ext=file.split(".")[-1]
                if ext=='gyu':
                    os.system("gyu2bmp.exe "+file)

def delete_gyu():
    print("Start deleting original gyu...")
    for files in os.listdir("./"):
        if os.path.isdir(files):
            for file in os.listdir(files):
                file=os.path.join(files,file)
                ext=file.split(".")[-1]
                if ext=='gyu':
                    os.remove(file)

def merge():
    print("Start merging...")
    for files in os.listdir("./"):
        if os.path.isdir(files):
            for file in os.listdir(files):
                file=os.path.join(files,file)

                ext=file.split(".")[-1]
                file_name=file.split(".")[0]+".bmp"
                if ext=="gyu":
                    gyu=open(file,"rb")
                    data=gyu.read()
                    
                    x,y=struct.unpack("<2I",data[16:24]) #得到差分尺寸

                    length=len(data)
                    num=length-1
                    while data[num]==0: #判断末尾有多少0
                        num=num-1
                    if length-num-1<=3: #此时不是差分
                        continue
            
                    current_num=num
                    while data[current_num]!=0:
                        current_num=current_num-1 

                    try:
                        location=data[current_num:num+1].decode(encoding="utf8").split(",") #得到覆盖坐标信息
                    except Exception:   #此时不是差分
                        continue
            
                    base_file=os.path.join(location[0][-4:-2],location[0][-4:]+".bmp")
                    size=str(x)+"x"+str(y)+"+"+location[1]+"+"+location[2]

                    os.system("magick "+base_file+" -compose over "+file_name+" -geometry "+size+" -composite "+file_name)

if __name__=='__main__':
    if list(set(['-d','-g','-m','-del']) and set(sys.argv)):
        if '-d' in sys.argv:
            decode()
        if '-g' in sys.argv:
            gyu_to_bmp()
        if '-m' in sys.argv:
            merge()
        if '-del' in sys.argv:
            delete_gyu()
    else:
        print("Usage: python merge_gyu.py [-d][-g][-m][-del]")
        print("[-d]: decode key in def.rld")
        print("[-g]: transform gyu to bmp")
        print("[-m]: merge bmp from location in gyu")
        print("[-del]: delete all gyu")
