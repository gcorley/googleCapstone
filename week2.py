#! /usr/bin/env python3
import os
import requests

path = '/data/feedback'
for filename in os.listdir(path):
    with open(path + '/' + filename, 'r') as data:
        lines = data.read().splitlines()
        formatted_data = {}
        titles = ['title', 'name', 'date', 'feedback']
        for i in range(len(titles)):
            formatted_data[titles[i]] = lines[i]
        response = requests.post('http://34.134.94.14/feedback', data=formatted_data)
        print(str(response.status_code))
