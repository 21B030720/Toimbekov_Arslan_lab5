import re
k = 'АААаааааа оир ва ио лватовламОСРВОЛМ ВОММИ юЛОВМЛы'
with open("row.txt", 'r') as f:
    p = f.read()
    m = re.findall(r'[А-Я]+[^А-Я]*', k)
    m = '\n'.join(m)
    print(m)