
def dup(x):
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                return True
    return False        

def dup1(x):
    h = {}
    for i in x:
        if i in h:
            return True
        else:
            h[i] = i
    return False

print(dup("panda"))
print(dup1("panda"))

