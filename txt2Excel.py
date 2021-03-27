import re
import pandas as pd

item = 'eiren2'

regex = re.compile('[0-9]')
path_before = r'/data/%s.txt' % item
path_after = r'/data/after_%s.txt' % item

before = open(path_before, 'r', encoding='UTF8')
after = open(path_after, 'w', encoding='UTF8')

while True:
    line = before.readline()
    if not line:
        break
    removed_space = line.replace(" ", "")
    tmp = regex.search(removed_space, 1)
    if(tmp == None):
        continue
    sperator = tmp.group()
    idx = removed_space.find(sperator, 1)

    front_str = removed_space[0:idx]
    back_str = removed_space[idx:len(removed_space)]

    end = front_str + ' ' + back_str
    print(end, file=after)

before.close()
after.close()
csv = pd.read_csv(path_after, delimiter = ' ', engine='python')
csv.to_excel(r'/data/%s.xlsx' % item, index=False, engine='xlsxwriter')