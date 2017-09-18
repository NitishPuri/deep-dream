import numpy as np
import os
import glob
from PIL import Image

INPUT_IMAGES = '../test_data2/g/*.png'

index = 0
for file in glob.iglob(INPUT_IMAGES):
    newName = '../test_data2/g/{}.jpg'.format(index)
    while os.path.isfile(newName) :
        index += 1
        newName = '../test_data2/g/{}.jpg'.format(index)

    print("{} --> {}".format(file, newName))        

    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(newName)

    # os.rename(file, newName)
