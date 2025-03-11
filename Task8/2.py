people = { 
          'Alice': 
              {'products': ['Laptop', 'Phone', 'Tablet']}, 
          'Bob': 
              {'products': ['Phone']},
          'Charlie': 
              {'products': ['Laptop', 'Tablet', 'Smartwatch', 'Phone']} 
         }
max_person=max(people,key= lambda person:len(people[person]["products"]))
print("1.The person who owns most product:",max_person)
product_name="Phone"
count=0
for person in people:
    if product_name in people[person]["products"]:
        count+=1
print("2.Number of people owns phone:",count)
required_product={"Laptop","Phone"}
owners=[person for person in people if required_product.issubset(set(people[person]["products"]))]
print("3.A list who onws the given product:",owners)
product_count = {}
for person in people:
    for product in people[person]["products"]:
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1
max_product = None
max_count = 0
for product in product_count:
    if product_count[product] > max_count:
        max_product = product
        max_count = product_count[product]
print("4.Most owned product:", max_product)
