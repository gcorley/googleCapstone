#! /usr/bin/env python3
import os
import requests

path = '/data/feedback'
url = 'http://35.223.61.82/feedback'
titles = ['title', 'name', 'date', 'feedback']
for filename in os.listdir(path):
    with open(path + '/' + filename, 'r') as data:
        lines = data.read().splitlines()
        formatted_data = {}
        for i in range(len(titles)):
            formatted_data[titles[i]] = lines[i]
        response = requests.post(url, data=formatted_data)
        print(str(response.status_code))
