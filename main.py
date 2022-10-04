from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import getQuestions, getInfo, remTag, getData
import json
import pandas as pd
import re
import time

f = open("config.json")

jdata = json.load(f)

f.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

data = pd.read_csv(
    'questoes/0eba07d7-5798-4685-bae4-9efe48445994.csv')

new_list = []

for i in data['link']:
    match = re.search(r'/questoes-de-concursos/questoes/\w+.\w+', i)
    new_list.append(match.group())

d = []

for x in new_list:
    d.append(getData(x, driver))
    time.sleep(4)

df = pd.DataFrame.from_dict(d) 

df.to_csv("teste.csv")

