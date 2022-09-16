s=str(input("enter the string:"))
s=s.split()[::-1]
l=[]
for i in s:
    l.append(i)
    print(" ".join(l))
