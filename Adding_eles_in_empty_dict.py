# question:- write a program to enter marks of three subjects from the user and store them in a dictionary.
#            start with an empty dictionary and add one by one. use subjects name as key and marks as values.

subject = {}
x = int(input("enter phy: "))
subject.update({"phy":x})
y = int(input("enter che: "))
subject.update({"che":y})
z = int(input("enter maths: "))
subject.update({"maths":z})
print(list(subject.items()))
