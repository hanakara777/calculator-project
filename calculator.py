def calculator ():
    print("Hi, feel free to use calculator")

    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    operation = input("Enter the operation (+, -, *, /): ")
    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x / y


    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operation!"

    print(f"The result is {result} ")
        
if __name__ == "__main__":
    calculator()