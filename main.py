from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import getQuestions, getInfo, remTag, getData
import json
import pandas as pd

f = open("config.json")

jdata = json.load(f)

f.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

d = []
links = ["/questoes-de-concursos/questoes/97095657-34",
"/questoes-de-concursos/questoes/157f4905-32",
"/questoes-de-concursos/questoes/157c6275-32"]

for x in links:
    d.append(getData(x, driver))

df = pd.DataFrame.from_dict(d) 

df.to_csv("teste.csv")

driver.quit()