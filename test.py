import re
import pandas as pd


data = pd.read_csv(
    'D:\\Rubens_HD\\Git-Clone\\WebScraping-InaClick\\questoes\\1bcb6979-778b-4f29-9ebb-589012c5278d.csv')

new_list = []


for i in data['link']:
    match = re.search(r'/questoes-de-concursos/questoes/\w+', i)
    new_list.append(match.group())

df = pd.DataFrame(new_list)

df.to_csv('your_name.csv', index = False)
