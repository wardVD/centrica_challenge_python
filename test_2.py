# Bad Practice Example: can you spot the bad practices and refactor the code?
# We don't want to change the function signatures

numbers = [1, 2, 3, 4, 5]

def calculate_sum():
    global numbers
    return sum(numbers)

def calculate_average():
    global numbers
    total = sum(numbers)
    count = len(numbers)
    return total / count

def add_number(new_number):
    global numbers
    numbers.append(new_number)

# Using the functions
print("Sum:", calculate_sum())
print("Average:", calculate_average())
add_number(6)
print("Updated Sum:", calculate_sum())
