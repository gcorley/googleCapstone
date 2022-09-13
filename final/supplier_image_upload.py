#!/usr/bin/env python3
import requests
import changeImage
import os


image_source = changeImage.path
url = 'http://localhost/upload/'
for filename in os.listdir(image_source):
    if 'jpeg' in filename:
        with open(image_source + filename, 'rb') as image:
            response = requests.post(url, files={'file': image})
