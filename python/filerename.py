import os,sys
folder = '/mnt/c/Users/Robne/Downloads/SG_GN-MD-32X/FULL Sega Genesis -- Mega Drive -- 32X (GoodGen 3.00)[GoodMerged]'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.bin', '.md')
       output = os.rename(infilename, newname)