# CatSystem2 Decryption Tool

## Introduction

After playing [Yuukyuu no Campanella](https://vndb.org/v30724) from Windmill Oasis, I tried to decrypt the game using tools for CatSystem2. 

Unfortunately, everything changed. 

It start to use atx format instead of hg3 or hg2. I tried to merge all event cgs but I still can't understand everything. 

Hope that more tools will come out after more games being released.

## Some explanations

Currently the .dat file in this new CatSystem2 game is actually .7z file, simply change the format to 7z and unzip it using key 'IrsysPack_CipherKey' which can be found in 'Assembly-CSharp.dll'. 

In the unzipped folder, pictures are named in .atx format which is actually .zip file, aftering unzipping it, it contains serveral png pictures and a json file named 'atlas.json' and a pb file named 'atlas.pb'

I don't really understand what is inside the pb file. But it seems that we only need atlas.json too merge all event cgs.

Inside the atlas.json, it has two big part 'Canvas' and 'Block'. Inside Canvas, it has 'Width' and 'Height' which means the size of the final picture. But there is an exception in some big event cgs, I guess it need to be scaled in the game.

Inside Block, there has 5 main items I understand:

1. 'filenameOld', the name which has the same naming pattern is previous CatSystem2 games
2. 'Height' and 'Width', the size of this block
3. 'OffsetX' and 'OffsetY', the position of this block in the final picture

Besides, there has a lot of Mesh inside one block, which means a block is combined with several small Meshs.  Each Mesh has 6 main parts I understand:

1. 'texNo': the source png it came from
2. 'width' and 'height': the size of this Mesh
3. 'viewX' and 'viewY': the position of this Mesh in the source png
4. 'srcOffsetX' and 'srcOffsetY': the position of this Mesh in the block

Now the question is what blocks we need for diffs in one event cg. I found it in 'cglist.lst', it still use the same combining rules in previous CatSystem2 games.

For example, `ea01,1,1,2` means merging ea01_1 and ea01_01 and ea01_002. If one number is '0', we just skip it.

By the way, every event cg has a 1920x1080 version which is named `ea01l` using the example above and a 1280x720 version, my script extracts the 1920x1080 version only.

## Usage

1. Please put all unzipped file in the folder with the same name and put all folders under the folder named image.

2. Put cglist.lst, this script in the same folder with the folder named image mentioned above.

3. Install pillow and tqdm using pip.

4. run python merge_atx.py then every event cg will be saved in the folder named 'output' and the name of the failed event cgs will be saved in 'failed.log'