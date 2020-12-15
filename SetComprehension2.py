numbers = [1, 2, 3, 4, 3, 2, 1, 4, 5]

set = set(numbers)
print("Set: " + str(set))

Evennumbers = {item for item in set if item % 2 == 0}
print(Evennumbers)
