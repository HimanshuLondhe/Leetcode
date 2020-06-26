def isPalindrome(x: int):
        revnum = ''
        for i in reversed(str(x)):
            revnum += i 
        if revnum == str(x):
            return True
        return False
        # return str(x) == str(x)[::-1]     #python 1 liner

print(isPalindrome(123321))