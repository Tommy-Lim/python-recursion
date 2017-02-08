def is_palindrome(ss):
    if len(ss) <= 1:
        return True
    elif ss[0] != ss[-1]:
        return False


print(is_palindrome(""))
print(is_palindrome("a"))
print(is_palindrome("ab"))
