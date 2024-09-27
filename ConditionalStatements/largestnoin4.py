#WAP to find the gretest of 4 numbers entered by user .
a= int(input("enter first no :"))
b= int(input("enter second no :"))
c= int(input("enter third no :"))
d= int(input("enter fourth no :"))
if(a>b and a>c and a>d):
    print("a",a)
elif(b>c and b>d):
    print("b",b)
elif(c>d):
    print("c",c)
else:
    print("d",d)