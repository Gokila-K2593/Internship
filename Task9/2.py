try:
        number=int(input("enter a number: "))
        print(number/100)        
except ValueError as e: 
    print("ValueError",e) 
except TypeError as e:
    print("TypeError",e)
except NameError as e:
    print("NameError",e)  
except Exception as e:
    print("Incorrect",e)
finally:
    print("done")

    