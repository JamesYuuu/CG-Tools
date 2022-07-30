from tqdm import tqdm
import os
import multiprocessing

def run(file):
    os.system(f'magick ./evcg/{file} -quality 100 ./evcg/{file}')

if __name__ == "__main__":
    pool = multiprocessing.Pool()
    os.chdir("./evcg")
    for file in tqdm(os.listdir("./")):
        pool.apply_async(run,(file,))
 
    pool.close()
    pool.join() 
    
