# search for x in the tuple using loop
#  (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
x = 49
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
        break
    idx += 1

# or


num = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter number x: "))
for el in num:
    if (el == x):
        print(x,"is found")
        break
    else:
        print("still finding..")
