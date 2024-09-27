# WAP to check if a number is multiple of 7 or not

num=int(input("enter a no :"))
rem=(num%7)
if(rem==0):
    print("Num is Multiple of 7",num)
else:
    print("Num is not multiple of 7")