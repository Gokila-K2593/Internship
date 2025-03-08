people = { 
          'Alice': {'products': ['Laptop', 'Phone', 'Tablet']}, 
          'Bob': {'products': ['Phone']},
          'Charlie': {'products': ['Laptop', 'Tablet', 'Smartwatch', 'Phone']} 
         }
max_person=max(people,key= lambda person:len(people[person]["products"]))
print("The person who owns most product:",max_person)
product_name="Phone"
count=0
for person in people:
    if product_name in people[person]["products"]:
        count+=1
print("Number of people owns phone:",count)
required_product={"Laptop","Phone"}
owners=[person for person in people if required_product.issubset(set(people[person]["products"]))]
print("A list who onws the given product:",owners)