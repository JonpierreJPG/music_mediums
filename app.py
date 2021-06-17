import requests
import os
import flask
from flask import request
from dotenv import load_dotenv, find_dotenv
import random

rand_item = random.randint(0, 6)
# item_id = 2    
BASE_URL = 'https://my-music-medium-api.herokuapp.com/mediums/{}'.format(rand_item)
# print(BASE_URL)
response = requests.get(BASE_URL)
data = response.json()
medium = data['name']
link = data['web']
# print(data)
print(medium)
print(link)
