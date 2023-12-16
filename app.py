# app.py

def greet(name):
    return f"Hello, {name}!"

def main():
    print("Welcome to the Interactive Python App!")
    name = input("What's your name? ")

    greeting = greet(name)
    print(greeting)

if __name__ == "__main__":
    main()
    