import requests
import os
import flask
from flask import request
from dotenv import load_dotenv, find_dotenv
import random

    
BASE_URL = 'https://my-music-medium-api.herokuapp.com/mediums/0'# Create catch error for nothing found
# print(BASE_URL)
response = requests.get(BASE_URL)
data = response.json()
print(data)

