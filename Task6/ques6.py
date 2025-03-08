def find_common_and_unique(list1, list2):
    set1, set2 = set(list1), set(list2)
    common = list(set1 & set2)  
    unique = list(set1 ^ set2)
    return common, unique
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements, unique_elements = find_common_and_unique(list1, list2)
print("Common elements:", common_elements)
print("Unique elements:", unique_elements)