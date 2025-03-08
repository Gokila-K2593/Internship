a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
maxnum=a
for i in [b,c]:
    if i>maxnum:
        maxnum=i
print("Largest number is",maxnum)