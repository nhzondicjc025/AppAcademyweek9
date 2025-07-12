def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def add(x, y):
    return x + y

result = add(5, 3)
print(f"The sum is: {result}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Bob", "good Morning")