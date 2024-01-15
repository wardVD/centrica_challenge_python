# Bad Practice Example: can you spot the bad practices and refactor the code?

from typing import Union


def addNumbers(x, y):
  result = x + y
  return result

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

def checkIfEven(number):
    """checks uneven numbers"""
    if number % 2 == 0:
        return True
    else:
        return False

def square_number(number: Union[int, float, str]):
    """Works with ints, floats and str"""
    return number ** 2


def fizzbuzz(n: int) -> list[str | int]:
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        else:
            result.append(i)
    return result
    
def main():
    numbers = [1, 2, 3, 4, 5]

    average = calculate_average(numbers)
    print("Average is:", average)

    for num in numbers:
        if checkIfEven(num):
            print(num, "is even.")
        else:
            print(num, "is odd.")

    num1 = 10
    num2 = 5
    result = addNumbers(num1, num2)
    print("Sum of", num1, "and", num2, "is", result)
    
    print(f"Square of 5: {square_number(5)}")

    print(fizzbuzz(15))

if __name__ == "__main__":
    main()
