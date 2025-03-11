bookstore = {
    "name": "The Cozy Corner",
    "location": "Main Street, NY",
    "books": [
        {"id": 101, "title": "Harry Potter", "author": "J.K. Rowling", "price": 15.99},
        {"id": 102, "title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 12.50},
        {"id": 103, "title": "1984", "author": "George Orwell", "price": 10.99}
    ],
    "staff": [
        {"name": "Alice", "role": "Manager"},
        {"name": "Bob", "role": "Cashier"}
    ]
}
title_book=[]
print("1.The name of the bookstore is:",bookstore["name"])
# or
# print(bookstore.get("name")) 
print("2.The list of titles in book:")
for book_details in bookstore["books"]:
     print(book_details["title"])
print("3.If there is a book written by George Orwell:")
if book_details["author"] =="George Orwell":
    print("Yes")
else:
    print("No")
      
    
