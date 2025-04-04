try:
        with open("data.txt", "r") as file:
            content = file.read()
            print("File contents:", content)
except FileNotFoundError as e:
        print("File not found.Creating data.txt",e)
        with open("data.txt","w") as file:
            file.write("Hello, World!")
        print("File data.txt created")
        