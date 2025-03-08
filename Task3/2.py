def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
s= input("Enter a string: ")
print("Number of vowels in", s, "is", count_vowels(s))