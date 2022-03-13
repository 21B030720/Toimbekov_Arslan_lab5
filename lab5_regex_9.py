import re
k = "ArslanAsmanKairat"
#m = "".join(" " + i for i in re.findall(r'[A-Z]+[^A-Z]*', k))
m = re.findall(r'[A-Z]+[^A-Z]*', k)
for i in m:
    print(i, end = " ")