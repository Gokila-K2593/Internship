with open('File1.txt','r') as source_file,open('File2.txt','w') as destination_file:
    content = source_file.read()
    destination_file.write(content)
print("File copied successfully!")