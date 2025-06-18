

def validateboundedInt(value, bound):
    upperB = bound
    lowerB = -bound
    if type(value) == type(0):
        if lowerB <= value <= upperB:
            return value, "is a valid integer!"
        elif value > upperB:
            return value, "is too large!"
        elif value < lowerB:
            return value, "is too small!"
        else:
            return value
    else:
        return value, "is not an integer!"
    
init = (-101, -100, 0, 1, 101, 100, True, 1.5, "hello")
mod = []

for i in init:
    # print(i)
    mod.append(validateboundedInt(i, 100))

for i in range(len(mod)):
    print(mod[i])


