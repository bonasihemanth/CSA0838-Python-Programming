s=input("enter the first string")
p=input("enter the seconf string")
import re
p=r"{}".format(p)
p=re.compile(p)
if p.fullmatch(s):
    print("true")
else:
    print("false")

