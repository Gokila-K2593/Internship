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
print("Increased price:",products)
count={}
for product in products:
    category=product['Category']
    if category in count:
        count[category]+=1
    else:
        count[category]=1
print("product count :",count)
total_stock=0
for product in products:
    if product["Stock"] is not None:
        total_stock+=product["Stock"]
print("Total stock:",total_stock)
