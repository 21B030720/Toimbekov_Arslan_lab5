import re
logic = r"а+[а-я]+б"
with open('row.txt', 'r') as f:
    p = f.read()
    print(re.findall(logic, p))
