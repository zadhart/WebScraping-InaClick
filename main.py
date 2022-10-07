from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import getQuestions, getInfo, remTag, getData
import json
import pandas as pd
import re
import time



def main(a):

    f = open("config.json")

    jdata = json.load(f)

    f.close()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    data = pd.read_csv(f'questoes/{a}.csv') #5
        
        

    new_list = []

    for i in data['link']:
        match = re.search(r'/questoes-de-concursos/questoes/\w+.\w+', i)
        new_list.append(match.group())

    d = []

    for x in new_list:
        d.append(getData(x, driver))
        time.sleep(20)

    df = pd.DataFrame.from_dict(d)
    driver.quit() 

    df.to_csv(f"questoes_3/{a}.csv")

def arq():
    with open('config.json') as f: 
        d = json.load(f) 

    a=''
    for i in range(len(d['files'])):
        a=d['files'][i]
        time.sleep(20)
        main(a)

arq()