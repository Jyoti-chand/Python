list1=[1,2,1]
list2=[1,2,7]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list2):
    print("palindrome")
else:
    print("Not palindrome")
    