import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

data = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.qconcursos.com/questoes-de-concursos/questoes?discipline_ids%5B%5D=4&subject_ids%5B%5D=15446")


for i in range(30):
    time.sleep(2)

    t = driver.find_elements(By.CLASS_NAME, "q-id")

    for x in t:
        data.append(x.get_attribute('innerHTML'))

    #btn = driver.find_element(By.CLASS_NAME, "q-next btn btn-default")
    #btn.click()

    driver.get(f"https://www.qconcursos.com/questoes-de-concursos/questoes?discipline_ids%5B%5D=4&page={i+1}&subject_ids%5B%5D=15446")

    time.sleep(2)

nd = pd.DataFrame(data, columns=['link'])

nd.to_csv("questoes.csv")

    