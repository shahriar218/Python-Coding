
def factorial(y):
    if y == 1:
        return 1
    else:
        return (y * factorial(y-1))


num = int(input("Enter number:"))
print("The factorial of", num, "is", factorial(num))