def is_palindrome(ss):
    if len(ss) < 2:
        return True
    elif ss[0].lower() not in "qwertyuiopasdfghjklzxcvbnm":
        return is_palindrome(ss[1:])
    elif ss[-1].lower() not in "qwertyuiopasdfghjklzxcvbnm":
        return is_palindrome(ss[:-1])
    elif ss[0] != ss[-1]:
        return False
    substr = ss[1:-1]
    return is_palindrome(substr)

def is_palindrome2(ss, n=0):
    if len(ss) < 2:
        return True
    elif n >= len(ss)//2:
            return True
    elif ss[n] != ss[-(n+1)]:
        return False
    else:
        return is_palindrome2(ss, n+1)

# best example which accounts for non characters
def is_palindrome3(ss):
  print(ss)
  if len(ss) < 2:
    return True
  if ss[0].lower() not in "asdfghjklqwertyuiopzxcvbnm":
    return is_palindrome3(ss[1:])
  if ss[-1].lower() not in "asdfghjklqwertyuiopzxcvbnm":
    return is_palindrome3(ss[:-1])
  if ss[0].lower() != ss[-1].lower():
    return False
  mid = ss[1:-1]
  return is_palindrome3(mid)

print("palindrome1")
print("", is_palindrome(""))
print("a", is_palindrome("a"))
print("ab", is_palindrome("ab"))
print("aa", is_palindrome("aa"))
print("aba", is_palindrome("aba"))
print("abba", is_palindrome("abba"))
print("eddie", is_palindrome("eddie"))
print("racecar", is_palindrome("racecar"))
print("aaebb", is_palindrome("aaebb"))
print("!'A,,a'!", is_palindrome("!'A,,a'!"))
print("!'Ab,,ba'!", is_palindrome("!'Ab,,ba'!"))
print("!'Abc,,ba'!", is_palindrome("!'Abc,,ba'!"))
print("!'Abc,,dba'!", is_palindrome("!'Abc,,dba'!"))
print()

print("palindrome2")
print("", is_palindrome2(""))
print("a", is_palindrome2("a"))
print("ab", is_palindrome2("ab"))
print("aa", is_palindrome2("aa"))
print("aba", is_palindrome2("aba"))
print("abba", is_palindrome2("abba"))
print("eddie", is_palindrome2("eddie"))
print("racecar", is_palindrome2("racecar"))
print("aaebb", is_palindrome2("aaebb"))
print("!'A,,a'!", is_palindrome2("!'A,,a'!"))
print("!'Ab,,ba'!", is_palindrome2("!'Ab,,ba'!"))
print("!'Abc,,ba'!", is_palindrome2("!'Abc,,ba'!"))
print("!'Abc,,dba'!", is_palindrome2("!'Abc,,dba'!"))
print()

print("palindrome3")
print("", is_palindrome3(""))
print("a", is_palindrome3("a"))
print("ab", is_palindrome3("ab"))
print("aa", is_palindrome3("aa"))
print("aba", is_palindrome3("aba"))
print("abba", is_palindrome3("abba"))
print("eddie", is_palindrome3("eddie"))
print("racecar", is_palindrome3("racecar"))
print("aaebb", is_palindrome3("aaebb"))
print("!'A,,a'!", is_palindrome3("!'A,,a'!"))
print("!'Ab,,ba'!", is_palindrome3("!'Ab,,ba'!"))
print("!'Abc,,ba'!", is_palindrome3("!'Abc,,ba'!"))
print("!'Abc,,dba'!", is_palindrome3("!'Abc,,dba'!"))
print()
