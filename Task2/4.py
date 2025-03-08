a=int(input("Enter the first number:"))
b=int(input("Enter second number:"))
print("The range between",a,"and",b)
count=0
for i in range(a,b+1):
        for j in range(1,i+1):  
            if i%j==0:
                count=count+1
        if count==2:
             print(i)
        count=0  
        