from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import getQuestions, getInfo, remTag
import json

f = open("config.json")

jdata = json.load(f)

f.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

q = getInfo(driver, "/questoes-de-concursos/questoes/97095657-34")

print(q)

print("______________________________________________________________________________")

print(remTag(q["a"]))


driver.quit()