from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)
s = ''
for i in contacts_list:
    s += '\n'
    for l in i:
        s += (l + ',')
p = re.compile('(\,)*')
res = re.sub(p, r'\1', s)
p = re.compile('([А-Я][а-я]+)\s*\,*([А-Я][а-я]+)\s*\,*')
res = re.sub(p, r'\1,\2,', res)
p = re.compile('(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})')
res = re.sub(p, r'+7(\2)\3-\4-\5', res)
p = re.compile('\s*\(*(доб.)\s*(\d+)\)*\s*')
res = re.sub(p, r' \1\2', res)
l = res.split('\n')
l.pop(0)
a = []
for i in l:
    s = (i.split(','))
    s.remove('')
    a.append(s)
for i in a:
    for s in a:
        try:
            if i[0] == s[0]:
                if i != s:
                    print(i, s)
                    for q in range(1, 10):
                        for z in i:
                            if z in s:
                                i.remove(z)
                            else:
                                s.append(z)
                                i.remove(z)
        except:
            pass
text = ''
for i in a:
    if len(i) == 0:
        a.remove(i)
a.sort()

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(a)
