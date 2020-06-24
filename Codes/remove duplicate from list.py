def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)




t = [1, 2, 3, 1, 2, 5, 6, 7, 8]

a = list(set(t))

print(a)
