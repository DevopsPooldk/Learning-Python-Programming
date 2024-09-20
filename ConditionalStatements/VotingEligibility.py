# Wap to check Person is eligible for voting or not .

age = int(input("Enter Your Age : "))
if(age >= 18 and age <= 110):
    print("Person is eligible for voting")
elif(age < 18 or age > 110 ): #invalid age for voting 110 i just casualy write .
    print("invalid person")
else:
    print("invalid input") #for any negative number input