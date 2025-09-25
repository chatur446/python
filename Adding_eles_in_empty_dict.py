# question:- write a program to enter marks of three subjects from the user and store them in a dictionary.
#            start with an empty dictionary and add one by one. use subjects name as key and marks as values.

subject = {}
subject.update({"phy":87})
subject.update({"che":90})
subject.update({"maths":91})
print(list(subject.items()))
