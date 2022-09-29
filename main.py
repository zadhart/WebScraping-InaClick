from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import getQuestions, getInfo
import json

f = open("config.json")

jdata = json.load(f)

f.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

print(getInfo(driver, "/questoes-de-concursos/questoes/af72bd38-3a"))

