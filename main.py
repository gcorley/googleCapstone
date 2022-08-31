#!/usr/bin/env python3
from PIL import Image
import os

size = (128, 128)

for filename in os.listdir('images'):
    if filename.startswith('ic_'):
        icon = Image.open(filename).convert('RGB')
        icon.rotate(90).resize(size).save('/opt/icons/' + filename, 'JPEG')
