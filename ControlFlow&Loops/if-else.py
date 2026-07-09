num = int(input("Enter a number:"))
if num > 90 and num <= 100:
    print("A+")
elif num > 80  and num <= 90:
    print("A")
elif num > 70 and num <= 80:
    print("B+")
elif num > 60 and num <= 70:
    print("C+")
elif num >= 30 and num <=60:
    print("D")
else:
    print("fail")