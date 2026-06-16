def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number -1 )
def main():
    val = 4
    print(f"Factorial of {val}! = {factorial(val)}")

if __name__ == "__main__":
    main()