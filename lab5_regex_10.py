import re
logic1 = r'_[a-z]'
logic2 = r'[A-Z]'
k = "ArslanBarslan"
with open('row_2.txt', 'r') as f:
    p = f.read()
    #m = ''.join("_" + i[0].lower() + i[1:] for i in re.findall(r'[A-Z]+[^A-Z]*', k))
    m = re.findall(r'[A-Z]+[^A-Z]*', k)
    d = 0
    for i in m:
        if d != 0:
            print("_", end = "")
        print(i[0].lower()+i[1:], end = "")
        d += 1
    #print(m)