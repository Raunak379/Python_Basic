#print number 1 to 6 break = 3.
for i in range (1,7):
    if i == 3:
        break
    print(i)

#print number 1 to 6 continue = 3.
for i in range(1,7):
    if i ==3:
        continue
    print(i)

#pass
for i in range(5):
    pass

print("Done")

#nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)