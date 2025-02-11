# Double Check Number
number = int(input("Enter a Number To Check : "))

if number>50:
    print("Number Is Greater Than 50")
    if number%2==0 :
        print("And It is even too")
    else:
        print("Add it is odd")
else:
    print("Number Is Less Than 50")