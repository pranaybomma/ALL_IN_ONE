import os
o = open ("output.txt","w+")
with open("fil1") as f1, open("fil2") as f2, open("fil3") as f3:
  for x, y, z in zip(f1, f2, f3):
    zone = x.strip()
    domain = y.strip()
    answer = z.strip()
    os.system("curl "+ zone)






     #print("{0}\n{1}".format(x.strip(), y.strip()))
