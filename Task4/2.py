def most_common_word(text):
    word_counts = {}
    word = ""
    for char in text:
        if char.isalnum():
            word += char
        else:
            if word:
                word_counts[word] = word_counts.get(word, 0) + 1
                word = ""
    if word:  
        word_counts[word] = word_counts.get(word, 0) + 1  
    most_common = max(word_counts, key=word_counts.get)
    return most_common
text = input("Enter a paragraph: ").lower()
print("The most common word is:", most_common_word(text))