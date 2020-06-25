def reverse(x: int):
    if x < -2**(31) or x > (2**(31)-1):
        return 0
    revnum = ''
    if x >= 0:            
        for i in reversed(str(x)):
            revnum += i
        if int(revnum) > 2**(31)-1:
            return 0 
        else:
            return int(revnum)
    if x < 0:
        x = abs(x)
        revnum = '-'
        for i in reversed(str(x)):
            revnum += i
        if int(revnum) < -2**(31):
            return 0 
        else:
            return int(revnum)


print(reverse(5673))
print(reverse(-2321))