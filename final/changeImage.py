#!/usr/bin/env python3
from PIL import Image
import os

path = 'supplier-data/images/'
size = (600, 400)
for filename in os.listdir(path):
    if filename[0].isdigit():
        im = Image.open(os.path.join(path, filename))
        im = im.resize(size)
        im = im.convert('RGB')
        basename = filename[:3]
        im.save(path + basename + '.jpeg', 'JPEG')
        print(filename)
