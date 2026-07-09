age = int(input("enter your age:"))
citizen = True
if age >= 18:
    if citizen:
        print("you are eligible for voting")
else:
    print("you are not eligible for voting")