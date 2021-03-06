import zipfile
import os,sys
folder = '/mnt/c/Users/Robne/Downloads/SNES_777_ROMS/SNES_777_ROMS'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    ext = os.path.splitext(infilename)[-1].lower()
    if ext == ".zip":
        with zipfile.ZipFile(infilename, 'r') as zip_ref:
            zip_ref.extractall(folder)