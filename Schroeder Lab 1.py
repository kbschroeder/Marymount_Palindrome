def reverse(text):
    result = ""
    for i in range(len(text)-1, -1, -1):
        result += text[i]
    return result

def is_palindrome(word):
    rev = reverse(word)

    if (word == rev):
        return True
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