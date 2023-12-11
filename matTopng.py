from os import path
import os
from matplotlib import pyplot as plt
import numpy as np
import h5py
from PIL import Image
import re
import sys
from glob import glob

directory = "brainTumorDataPublic_22993064"

for filename in os.listdir(directory):
    filepath = os.path.join(directory,filename)
    
    print(filename[:-4])

    f = h5py.File(filepath, 'r')
    cjdata = f['cjdata']

    image = np.array(cjdata.get('image')).astype(np.float64)
    label = cjdata.get('label')[0,0]

    tumorBorder = np.array(cjdata.get('tumorBorder'))[0]
    tumorMask = np.array(cjdata.get('tumorMask'))

    f.close()

    hi = np.max(image)
    lo = np.min(image)
    image = (((image - lo)/(hi-lo))*255).astype(np.uint8)
    im = Image.fromarray(image)

    if label == 1:
        im.save("meningioma/" + filename[:-4] + ".png")

    elif label == 2:
        im.save("glioma/" + filename[:-4] + ".png")

    else:
        im.save("pituitary/" + filename[:-4] + ".png")
