
def square(arr):
    temp = []
    for i in range(len(arr)):
        temp.append(arr[i]**2)
    return temp


num = [i for i in range(1,11)]
# print(num)
mod = square(num)
# print(mod)

for x,y in zip(num, mod):
    print(f"{x:>2},{y:>3}")