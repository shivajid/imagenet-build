# imagenet-build

This document gives an overview of how to build imagenet tfrecords to be used for classification tasks

-  Browse to https://www.image-net.org
-  Setup an account with image-net
-   Accept the agreement

Once you have accepted the agreement you will be allowed to download the imagenet dataset.

Before you download ensure that you have a large VM or a machine with about 500GB in disk space.

There are 4 files you wll need to download

a) Train files - There are 2 of them
b) Validation files - This is a tar with 50K images
c) Validation Labels -  wget https://raw.githubusercontent.com/tensorflow/models/master/research/slim/datasets/imagenet_2012_validation_synset_labels.txt

To be used with TPUs and tensorflow you will need to convert them to tfrecords

Download the following script
<code>
wget https://raw.githubusercontent.com/tensorflow/tpu/master/tools/datasets/imagenet_to_gcs.py
</code>

Once you have downloaded the script. It expects the data in the following format.

Extract the imagenet files in the following forrmat
It should be extracted and provided in the format:
- Training images: train/n03062245/n03062245_4620.JPEG
- Validation Images: validation/ILSVRC2012_val_00000001.JPEG
- Validation Labels: synset_labels.txt


set IMAGENET_HOME to the location of the home of the imagenet

To generate the tf records you can use:
<code>
python3 imagenet_to_gcs.py \
  --project="TEST_PROJECT" \
  --gcs_output_path="gs://TEST_BUCKET/IMAGENET_DIR" \
  --raw_data_dir="path/to/imagenet"
  
  </code>
  
  



