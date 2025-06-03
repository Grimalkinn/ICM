a = 0.0 #input("Enter firsf value for x: ")
b = 20 #input("Enter number of intervals: ")
c = 5.0 #inut("Enter last value for x: ")

temp = []
for i in range(int(a),int(b)+1):
    temp.append((i)*0.25)


modified = []
for i in range(len(temp)):
    x = temp[i]
    x1 = x**2
    x2 = -(3*x)
    x3=2
    modified.append(x1+x2+x3)

for a, b in zip(temp, modified):
    print(f"{a:>5} {b:>5.0f}")