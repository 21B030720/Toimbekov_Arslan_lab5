import re

#logic = r"\b\w+.?\d+\b"
logic = r'a+b*'
with open('row.txt', 'r') as f:
    p = f.read()
    l = re.findall(logic, p)
    for i in l:
        print(i, end = " ")