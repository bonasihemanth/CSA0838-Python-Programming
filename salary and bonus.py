grade=input("enter the grade of the employee(A/B) :")
salary= int(input("enter the employee salary :"))
if (grade == 'A') and (salary>10000):
    bonus= salary*(5/100)
    print("salary is:",salary)
    print("bonus is:",bonus)
    print(" total salary is:", bonus+salary)
elif (grade == 'B') and (salary>10000):
    bonus= salary*(10/100)
    print("salary is:",salary)
    print("bonus is:",bonus)
    print("total salary is:",bonus+salary)
elif (grade == 'A') and (salary<=10000):
    bonus= salary*(7/100)
    print("salary is:",salary)
    print("bonus is:",bonus)
    print(" total salary is:",bonus+salary)
elif (grade == 'B') and (salary<=10000):
    bonus=salary*(12/100)
    print("salary is:",salary)
    print("bonus is:",bonus)
    print("total salary is:",bonus+salary)
else:
    print("wrong input")
