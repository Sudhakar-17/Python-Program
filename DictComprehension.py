Cities = ["Chennai", "Trivandrum", "Hyderabad"]
States = ["Tamilnadu", "Kerala", "Andhra Pradesh"]

# Method 1:
Combination = zip(States, Cities)
for segragate in Combination:
    print(segragate)

# Method 2:
Consolidate = {States: Cities for States, Cities in zip(States, Cities)}
print(Consolidate)
