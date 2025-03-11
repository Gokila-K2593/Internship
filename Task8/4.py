products = [
    {"Name": "Laptop", "Price": 1200, "Stock": 10, "Category": "Electronics"},
    {"Name": "Phone", "Price": 800, "Stock": None, "Category": "Electronics"},
    {"Name": "Shoes", "Price": 50, "Stock": 30, "Category": "Fashion"},
    {"Name": "Headphones", "Price": 150, "Stock": 15, "Category": "Electronics"},
    {"Name": "T-shirt", "Price": 20, "Stock": 50, "Category": "Fashion"}
]
for product in products:
    if product['Category'] == 'Electronics':
        product['Price'] *= 1.10
print("1.Increased price:",products)
count={}
for product in products:
    category=product['Category']
    if category in count:
        count[category]+=1
    else:
        count[category]=1
print("2.product count :",count)
total_stock=0
for product in products:
    if product["Stock"] is not None:
        total_stock+=product["Stock"]
print("3.Total stock:",total_stock)
most_expensive = products[0]
cheapest = products[0]
for product in products:
    if product['Price'] > most_expensive['Price']:
        most_expensive = product
    if product['Price'] < cheapest['Price']:
        cheapest = product
print("4.Most Expensive Product:", most_expensive,"Cheapest Product:", cheapest)
