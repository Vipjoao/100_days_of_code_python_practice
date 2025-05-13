def greet():
    print("Hello!")
    print("How do you do?")
    print("Isn't the weather nice?\n")

greet()

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?\n")

greet_with_name("John")

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How is it like in {location}?\n")

greet_with("John", "São Paulo, Brasil")