def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


# run test
if is_palindrome('racecar'):
    print('pass')
else:
    print('fail')

if is_palindrome('mom'):
    print('pass')
else:
    print('fail')

if is_palindrome('noon'):
    print('pass')
else:
    print('fail')

if is_palindrome('Kennebunkport'):
    print('pass')
else:
    print('fail')

a = str(input("Enter string:"))
if (is_palindrome(a) == True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")