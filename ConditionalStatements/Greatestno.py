#WAP to find the gretest of 3 numbers entered by user .
num1= int(input("enter first no :"))
num2= int(input("enter second no :"))
num3= int(input("enter third no :"))
if(num1>num2 and num1>num3):
    print("Num1",num1)
elif(num2>num3):
    print("Num2",num2)
else:
    print("Num3",num3)