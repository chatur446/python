#write a program to check if a list contains a palindrome of elements(hint:-use copy() and method())

list1 = [1,2,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("pelindrome")
else:
    print("not pelindrome")  
