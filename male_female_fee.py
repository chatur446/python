#male female fee
a = int(input("a: "))
g = input("M/F: ")
if ((a == 1 or a== 2) and g == "M"):
    print("fee is 100")
elif (a == 3 or a == 4 or g == "F"):
    print("fee is 200")
elif (a == 5 and g == "M"):
    print("fee is 300")
else:
    print("no fee")    
