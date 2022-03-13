import re
logic1 = r'_[a-z]'
logic2 = r'[A-Z]'
k = "Arslan_barslan"
with open('row_2.txt', 'r') as f:
    p = f.read()
    m = ''.join(i.capitalize() or "_" for i in k.split("_"))
    print(m)