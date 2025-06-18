initVel = int(input("Enter the initial velocity in m/s: "))
intervals = int(input("Enter the number of intervals: "))
gravity = 9.81

# debug
# initVel = 2.5
# intervals = 16

# timeArr = [(i*2)/gravity for i in range(int(initVel), intervals)] # s 2*v0/G
timeArr = []
temp = [i for i in range(0, (intervals*2), 2)]
timeArr = [i*(initVel/intervals)*0.1 for i in temp ]

def equation1(arr):
    temp = []
    for i in range(len(arr)):
        temp.append((initVel*timeArr[i]) - (0.5*gravity*(timeArr[i]**2)) )
    return temp

mod = equation1(timeArr)

for i, j in zip(timeArr, mod):
    print(f"{i:>.05} {j:>.005}")

print(f"y(t) = v0*t - 0.5*g*t**2, where v0 is {initVel} m/s")