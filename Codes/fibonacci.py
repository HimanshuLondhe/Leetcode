FibArray = [0,1]
def fibonacci(n : int ):			#space efficient 
    a = 0
    b = 1 
    arr = [0,1]
    if n > 2:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            arr.append(b)
        print (b)
        return arr 
    else:
        return [0,1]

print(fibonacci(5))


def fibb(x):						# recursive 
    if x<=0:
        return 0 
    elif(x == 1): 
        return 1

    return fibb(x-1) + fibb(x-2)

print(fibb(4))
