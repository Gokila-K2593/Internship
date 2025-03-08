with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('merged.txt', 'w') as merged_file:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    max_length = max(len(file1_lines), len(file2_lines))
    for i in range(max_length):
        if i < len(file1_lines):
            merged_file.write(file1_lines[i].strip() + "\n")  
        if i < len(file2_lines):
            merged_file.write(file2_lines[i].strip() + "\n")
    print("Files merged successfully into 'merged.txt'!")