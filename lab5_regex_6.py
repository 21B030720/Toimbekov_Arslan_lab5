import re

logic1 = r'[ |,|.]'
#logic1 = r'С'
logic2 = ':'
with open('row.txt', 'r') as f:
    p = f.read()
    m = re.sub(logic1, logic2, p)
    print(m)
