totalusers=int(input("enter the total no.of users:"))
staffusers=int(input("enter the staff no.of users:"))
defaultusers=int(((staffusers)/3))
studentsusers =totalusers-(staffusers+defaultusers)
print("the student users in the college are:",studentsusers)
 
