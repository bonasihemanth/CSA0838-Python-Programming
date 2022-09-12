year=int(input("enter the year"))
mod=year%4
if (year%4==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
    print("the next leap year is:",year+(4-mod))
    
