

def fx(x):
    if x==0:
        return 0
    elif x%3 == 0:
        return 3
    elif x%2 == 0:
        return 2
    else:
        return 1
    
init = [i for i in range(-6, 7)]
mod = []

for i in init: 
    mod.append(fx(i))

for x,y in zip(init,mod):
    print(f'{x:>2} {y}')

