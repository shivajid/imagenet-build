#This assumes that you have extracted the imagenet tar files which has about 1000 tar files that needs to be extracted.
#This script iterates through the directory and extracts the dataset
import tarfile
import os

#Set this to the location of training directory
TRAIN_DIR='/home/jupyter/imagenet/train'

def extract_tar(tfile,dirname):
  with tarfile.open(TRAIN_DIR+"/" + tfile, 'r') as _tar:
    _tar.extractall(TRAIN_DIR+"/"+dirname)

trainfiles=os.listdir(TRAIN_DIR+"/*.tar")

for f in trainfiles:
   print("Extracting file {}".format(f))
   dirname = f.split(".")[0]
   os.mkdir(TRAIN_DIR+"/"+dirname)
   extract_tar(f,dirname)
