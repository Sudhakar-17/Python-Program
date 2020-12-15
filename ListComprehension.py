numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Method 1:
even1 = []
for i in numbers:
    if i % 2 == 0:
        even1.append(i)
print("Method 1: "+str(even1))

# Method 2:
even2 = [i for i in numbers if i % 2 == 0]
print("Method 2: "+str(even2))

# Expression - Method 2:
sqr_root = [i * i for i in numbers]
print("Expression: "+str(sqr_root))
