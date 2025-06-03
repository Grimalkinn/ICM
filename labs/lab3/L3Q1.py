multupleOf7 = [i for i in range(7,141,7)]

modified = []
for i in range(len(multupleOf7)):
    modified.append((multupleOf7[i]/2)-3)

for a, b in zip(multupleOf7, modified):
    print(f"{a:>5} {b:>5.0f}")