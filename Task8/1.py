data = { 
        'name': 'Alice', 
        'info': { 'age': 25, 'address': { 'city': 'New York', 'zip': 10001 } } 
        }
f = {}
stack = [(data,  '')]
while stack:
    c, p = stack.pop()
    for k, v in c.items():
        new_key = f"{p}.{k}" if p else k
        if isinstance(v, dict):
            stack.append((v, new_key))  
        else:
            f[new_key] = v 
print(f)
