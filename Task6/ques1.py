def reverse_words(s):
    words = []
    word = ""
    for char in s + " ":  
        if char != " ":
            word += char
        else:
            if word:
                words.insert(0, word)  
                word = ""    
    return " ".join(words)  
s = "Hello World"
print(reverse_words(s))