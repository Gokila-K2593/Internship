names=(["Alice", "Bob", "Charlie"])
try:
        with open("names.txt","w") as file:
            for name in names:
                file.write(name)
        print("Successfully wrote")
except Exception as e:
        print("Error writing to file:",e)

