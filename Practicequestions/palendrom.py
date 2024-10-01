# #Wap to check if a list contains a palindraoms of elements
list1=['a','b','a','b']
copy_list=list1.copy()
copy_list.reverse()
if(copy_list == list1):
    print("Palendrome")
else:
    print("not Palendrome")