import re
logic = r'[А-Я][а-я]+'
with open("row.txt", 'r') as f:
    p = f.read()
    print(re.findall(logic, p))
