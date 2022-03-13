import re
k = 'а_я   а_а    ф_Ф'
logic = r'[а-я]+_+[а-я]+'
with open('row.txt', 'r') as f:
    p = f.read()
    m = re.findall(logic, k)
    print(m)