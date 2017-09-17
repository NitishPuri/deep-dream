import numpy as np
import os
import glob


INPUT_IMAGES = '../test_data/nd/*.jpg'

index = 0
for file in glob.iglob(INPUT_IMAGES):
    newName = '../test_data/nd/{}.jpg'.format(index)
    while os.path.isfile(newName) :
        index += 1
        newName = '../test_data/nd/{}.jpg'.format(index)

    print("{} --> {}".format(file, newName))        
    os.rename(file, newName)
