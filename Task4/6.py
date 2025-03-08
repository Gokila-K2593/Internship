from collections import Counter
def most_frequent(lst):
    most_common = Counter(lst).most_common(1)[0][0]
    return most_common
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Most frequent element:", most_frequent(lst))