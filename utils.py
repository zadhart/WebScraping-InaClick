import uuid
import os
import time
import pandas as pd
import json
from selenium.webdriver.common.by import By

def getQuestions(driver, jdata):

    name = str(uuid.uuid4())

    jdata["files"].append(name)

    with open("config.json", "w") as outfile:
        outfile.write(json.dumps(jdata))

    data = []

    driver.get("https://www.qconcursos.com/questoes-de-concursos/questoes?discipline_ids%5B%5D=4&subject_ids%5B%5D=15446")

    for i in range(jdata["lastPage"], jdata["lastPage"] + 20):

        if(jdata["lastPage"] == 300):
            os.system("shutdown")

        time.sleep(15)

        t = driver.find_elements(By.CLASS_NAME, "q-id")

        for x in t:
            data.append(x.get_attribute('innerHTML'))

        driver.get(f"https://www.qconcursos.com/questoes-de-concursos/questoes?discipline_ids%5B%5D=4&page={i+1}&subject_ids%5B%5D=15446")

        time.sleep(15)

        nd = pd.DataFrame(data, columns=['link'])

        nd.to_csv(str(name)+".csv")

        print(i)

        jdata["lastPage"] = i

        with open("config.json", "w") as outfile:
            outfile.write(json.dumps(jdata))

def getInfo(driver, href):
    driver.get("https://www.qconcursos.com"+str(href))

    try:
        descricao = driver.find_element(By.CLASS_NAME, "q-question-enunciation").get_attribute('innerHTML')

        a = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[1]/div/div/div/div[1]/div[4]/div[3]/fieldset/div[1]/label/div").get_attribute('innerHTML')

        b = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[1]/div/div/div/div[1]/div[4]/div[3]/fieldset/div[2]/label/div").get_attribute('innerHTML')

        c = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[1]/div/div/div/div[1]/div[4]/div[3]/fieldset/div[3]/label/div").get_attribute('innerHTML')

        d = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[1]/div/div/div/div[1]/div[4]/div[3]/fieldset/div[4]/label/div").get_attribute('innerHTML')

        e = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[1]/div/div/div/div[1]/div[4]/div[3]/fieldset/div[5]/label/div").get_attribute('innerHTML')

        return {"descricao": descricao, "a": a, "b": b, "c": c, "d": d, "e": e}

    except:

        '''descricao = driver.find_element(By.CLASS_NAME, "q-question-enunciation").get_attribute('innerHTML')

        a = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[1]/div/div/div/div[1]/div[4]/div[4]/fieldset/div[1]/label/div").get_attribute('innerHTML')

        b = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[1]/div/div/div/div[1]/div[4]/div[4]/fieldset/div[2]/label/div").get_attribute('innerHTML')
'''
        return {"descricao": "none", "a": "none", "b": "none", "c": "none", "d": "none", "e": "none"}
        

def remTag(tag):
    i = 0
    l = []
    for x in tag:
        if x == "<" or x == ">":
            l.append(i)
        i += 1

    mys = ""
    w = 0
    #print(l)
    try:
        for x in range(len(tag)):
            if len(l) == 0:
                mys = tag
                break
            elif x >= l[w] and x <= l[w+ 1]:
                pass
            elif x >= l[w+ 1]:
                #mys = mys + " "
                mys = mys + tag[x]
                w += 2
            else:
                mys = mys + tag[x]

        mys2 = ""
        for x in mys:
            if x != "<" and x != ">" and x != ";":
                mys2 = mys2 + x

        mys2 = mys2.replace("&nbsp", " ")
        mys2 = mys2.replace("\n", " ")
            
        return mys2

    except:
        return "error"


def getData(src, driver):

    q = getInfo(driver, src)

    data = q

    data["src"] = src

    for x in q:
        if q[x] != "none":
            data[x] = remTag(q[x])

        else:
            data[x] = "none"

    return data

def combinarCSV():

    import os
    import glob
    import pandas as pd
    os.chdir("D:\\Rubens_HD\\testes_python\\questoes_3")

    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    #combinar todos os arquivos da lista
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #exportar para csv
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

