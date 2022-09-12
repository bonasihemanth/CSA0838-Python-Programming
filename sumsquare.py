a=[2,3,4,5,6,7]
def sumsquare(a):
    odd=0
    even=0
for i in a:
    if i%2==0:
        even=even+i**2
    else:
        odd=odd+i**2
a=[odd,even]
print(sumsquare(a))
