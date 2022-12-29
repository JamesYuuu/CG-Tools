import json,os
from PIL import Image
from tqdm import tqdm

class evcg(object):

    def __init__(self,filename):

        os.chdir(filename)

        with open('atlas.json','r',encoding='utf8') as f:
            self.js = json.load(f)

        self.image = list()     
        for file in os.listdir('./'):
            if file.split('.')[-1]=='png':
                self.image.append(Image.open(file).convert('RGBA'))
        
        self.width = self.js['Canvas']['Width']
        self.height = self.js['Canvas']['Height']
    
    def make_pic(self,subfiles,savename):

        final_pic = Image.new('RGBA',(self.width,self.height))

        for item in self.js['Block']:
            filename = item['filenameOld']
            if not filename in subfiles:
                continue

            canvas = Image.new('RGBA', (int(item['width']), int(item['height'])), (255,255,255,0))
            
            for block in item['Mesh']:
                x = block['viewX']
                y = block['viewY']

                width = block['width']
                height = block['height']

                src_x = block['srcOffsetX']
                src_y = block['srcOffsetY']

                tex_no = block['texNo']

                crop = self.image[tex_no].crop((x,y,x+width,y+height))
                canvas.alpha_composite(crop,(int(src_x),int(src_y)))

            offsetX = item['offsetX']
            offsetY = item['offsetY']
            final_pic.alpha_composite(canvas,(int(offsetX),int(offsetY)))

        final_pic.save(f'../../output/{savename}.png')

if __name__ == '__main__':

    if not os.path.exists('./output'):
        os.mkdir('./output')

    f = open('cglist.lst','r',encoding='utf-8')

    os.chdir('./image')
    
    pre_filename = None

    for line in tqdm(f.readlines()):

        line = line.strip()
        if line and line[0].isalpha():
            line = line.split(',')

            filename = line[0] + 'l' + line[1]
            if not pre_filename or pre_filename != filename:
                if pre_filename:
                    os.chdir('..')
                pre_filename = filename
                ev = evcg(filename)

            subfiles = [line[0] + 'l_' + '0'*index + item for index,item in enumerate(line[1:]) if item != '0']
            savename = ''.join(line)

            try:
                ev.make_pic(subfiles,savename)
            except Exception:
                with open('failed.log','w+') as log:
                    log.write(f'{filename} failed\n')
