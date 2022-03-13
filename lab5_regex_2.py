import re
"""logic = r'а+ббб?'
with open("row.txt", 'r') as f:
    p = f.read()
    m = re.findall(logic, p)
    print(m)"""
logic = r'a+bbb?[^b]'
l = input()
m = re.findall(logic, l)
print(m)