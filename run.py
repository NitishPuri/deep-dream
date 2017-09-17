import glob
import re
import os

from deepdream import *

def generate_layernames():    
    import pandas as pd
    d = {'layers' : layers, "features" : feature_nums}
    ldf = pd.DataFrame(data=d)
    ldf.to_csv('layer.csv')
    print(ldf.head())


def generate_rand_linear_lapnorm():
    count = np.random.choice([1,2,3])

    # tensor to be optimized
    t = None

    layer_idx = np.random.randint(0, len(layers))

    features_idx = []
    features_str = ''

    for i in range(count):
        features_idx.append(np.random.randint(0, feature_nums[layer_idx]))

    features_idx.sort()

    layer = layers[layer_idx]
    layer = layer.split('/')[1]
    
    for i in range(count):
        feature_idx = features_idx[i]

        features_str += '{}'.format(feature_idx)
        if(i<count-1):
            features_str+=','

        if(i == 0):
            t = T(layer)[:,:,:,feature_idx]
        else:
            t += T(layer)[:,:,:,feature_idx]

        print("Mixing ||{}|| Layer {} :: {} :: feature : {}".format(i, layer_idx, layer, feature_idx))

    filename = 'output/dreamTemple/l_{}_f_{}.jpg'.format(layer_idx, features_str)

    if os.path.isfile(filename):
        "Skipping as it already exists"
        return

    render_lapnorm(t , fileToSave=filename, octave_n=4)
    print("Saved to {}".format(filename))    



reg = r'^\.\.\/test_data[\/\\](?P<q>.*)[\/\\](?P<file>.*)\.jpg$'

OUTPUT_IMAGES = 'output/dreams/{d}/{f}.jpg'

def generate_rand_dream(file):

    image = PIL.Image.open(file)
    image = np.float32(image)

    m = re.search(reg, file)    
    dirName = m.group(1)
    fileName = m.group(2)

    count = np.random.choice([1,2,3])

    # tensor to be optimized
    t = None

    layer_idx = np.random.randint(0, len(layers))

    features_idx = []
    features_str = ''

    for i in range(count):
        features_idx.append(np.random.randint(0, feature_nums[layer_idx]))

    features_idx.sort()

    layer = layers[layer_idx]
    layer = layer.split('/')[1]
    
    for i in range(count):
        feature_idx = features_idx[i]

        features_str += '{}'.format(feature_idx)
        if(i<count-1):
            features_str+=','

        if(i == 0):
            t = T(layer)[:,:,:,feature_idx]
        else:
            t += T(layer)[:,:,:,feature_idx]

        print("Mixing ||{}|| Layer {} :: {} :: feature : {}".format(i, layer_idx, layer, feature_idx))

    
    fileName = '{}_l_{}_f_{}'.format(fileName, layer_idx, features_str)
    fileName = OUTPUT_IMAGES.strip().format(d=dirName, f=fileName)

    pattern = '{}_l_{}_f_*'.format(fileName, layer_idx, features_str)
    pattern = OUTPUT_IMAGES.strip().format(d=dirName, f=pattern)

    if len(glob.glob(pattern)) > 0:
        "Skipping as '{}' already exists".format(pattern)
        return

    render_deepdream(t , image, iter_n=15,  filename=fileName, octave_n=8)
    print("Saved to {}".format(fileName))    


# for i in range(5):
#     # generate_rand_lapnorm()
#     generate_rand_linear_lapnorm()



INPUT_IMAGES = '../test_data/*/*.jpg'
images = glob.glob(INPUT_IMAGES)

images = np.random.choice(images, 10)

for file in images:
    print("Generating dreams for : {}".format(file))
    for i in range(10):
        generate_rand_dream(file)




# print (images)

# for i in range(5):
    # Pick a random image from INPUTS
    