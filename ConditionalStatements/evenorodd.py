# WAP to check if a number entered by the user is odd or even .

number = int(input("enter a no :"))
rem=(number%2)
if(rem==0):
    print("number is even")
else:
    print("number is odd")