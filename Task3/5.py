def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]
s = input("Enter a string: ")
if is_palindrome(s):
    print("It is a palindrome")
else:
    print("It is not a palindrome") 