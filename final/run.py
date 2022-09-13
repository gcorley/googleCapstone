#! /usr/bin/env python3
import os
import requests
import json


txt_source = 'supplier-data/descriptions/'
image_source = 'supplier-data/images/'
post_url = 'http://[external-IP]/fruits'
i = 1
files = os.listdir(txt_source)
for filename in sorted(files):
    fruit_dict = {}
    with open(txt_source + filename, 'r') as txt:
        txt_lines = txt.readlines()
        fruit_dict['name'] = txt_lines[0].replace('\n', '')
        weight_str = txt_lines[1].split()
        fruit_dict['weight'] = int(weight_str[0])
        fruit_dict['description'] = txt_lines[2]
        image_name = f'{i:03}.jpeg'
        fruit_dict['image'] = image_name
        print(fruit_dict['name'], filename, fruit_dict['image'])
        i += 1
        json_fruit = json.dumps(fruit_dict)
        response = requests.post(post_url, json=json_fruit)
        print(response.status_code)

'''
{"name": "Apple", "weight": 500, "description": "Apple is one of the most nutritious and healthiest fruits. It is very rich in antioxidants and dietary fiber. Moderate consumption can not only increase satiety, but also help promote bowel movements. Apple also contains minerals such as calcium and magnesium, which can help prevent and delay bone loss and maintain bone health. It is good for young and old.\u00a0\n", "image_name": "001.jpeg"}

{"name": "Avocado", "weight": 200, "description": "Avocado contains large amount of oleic acid, a type of monounsaturated fat that can replace saturated fat in the diet, which is very effective in reducing cholesterol levels. Avocado is also high in fiber. Its soluble fiber can remove excess cholesterol from the body, while its insoluble fiber helps keep the digestive system functioning and prevent constipation.\n", "image_name": "002.jpeg"}

{"name": "Blackberry", "weight": 150, "description": "Blackberries have high nutritional value and are excellent fruit for health. It\u2019s rich in nutrients, various amino acids and trace elements necessary for the human body. They are good at promoting blood coagulation, delaying aging, improving immunity and reducing blood pressure and blood lipids. Blackberries can be consumed directly as fruit or made into jam and fruit wine.\n", "image_name": "003.jpeg"}

{"name": "Grape", "weight": 200, "description": "Grapes have up to 30% of sugar. A large amount of fruit acid in grapes helps digestion. Eating proper amount of grapes can strengthen the spleen and stomach. Grapes also contain the minerals calcium, potassium, phosphorus, iron, glucose, fructose, protein, tartaric acid, and various vitamins, which have strong nutritional functions and improve the function of the human body.\n", "image_name": "004.jpeg"}

{"name": "Kiwifruit", "weight": 250, "description": "Kiwifruit contains rich vitamin C, which can strengthen the immune system and supplement the nutrients consumed by the brain. Its perfect ratio of low sodium and high potassium can replenish the energy lost by working long hours.\n", "image_name": "005.jpeg"}

{"name": "Lemon", "weight": 300, "description": "Lemon is rich in vitamin C, which can improve immunity, accelerate wound healing and prevent colds. In the long run, it can lower the chance of developing cancer. Lemon juice helps reduce the burden on the digestive system and promotes the release of toxins from the body.\n", "image_name": "006.jpeg"}

{"name": "Mango", "weight": 300, "description": "Mango contains higher levels of vitamin C than ordinary fruits. Eating mango can also reduce cholesterol and triglycerides, and help prevent cardiovascular disease. Due to its high level of vitamins, regular consumption of mango play an important role in improving body function and moisturizing the skin.\n", "image_name": "007.jpeg"}

{"name": "Plum", "weight": 150, "description": "Plums are rich in sugar, vitamins, fruit acids, amino acids and other nutrients. With high nutritional value, Plums have outstanding health-care functions, which includes refreshing and nourishing liver, relieving depression and poisoning, and clearing dampness and heat of the human body.\n", "image_name": "008.jpeg"}

{"name": "Strawberry", "weight": 240, "description": "Strawberries are rich in carotene and vitamin A, which can alleviate night blindness, maintain the health of epithelial tissues, nourish the liver, and promote body growth and development. Strawberries contains large amount of dietary fiber as well, which can promote gastrointestinal motility and food digestion in the gastrointestinal tract.\n", "image_name": "009.jpeg"}

{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.\n", "image_name": "010.jpeg"}
'''