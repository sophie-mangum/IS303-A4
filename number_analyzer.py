'''
Sophie Mangum
IS 303 - A04

Number Analyzer
This program collects numbers from the user and displays
statistical analysis including mean, minimum, maximum,
range, and numbers above average.

Inputs:
- How many numbers to enter (int)
- Numbers entered by the user (float)

Processes:
- get_positive_int(prompt): keeps asking until user enters a valid positive integer
- get_valid_float(prompt): keeps asking until user enters a valid decimal number
- collect_numbers(count): returns a list of numbers from the user
- calculate_mean(numbers): returns the average using math library
- count_above_average(numbers, average): returns count of numbers above average
- display_report(numbers, average, minimum, maximum, number_range, above_avg): prints formatted statistics

Outputs:
- Mean
- Minimum value
- Maximum value
- Range
- Count of numbers above average
'''

import math

# Functions

def get_positive_int(prompt):
    """Get a valid positive integer."""
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_float(prompt):
    """Get a valid decimal number."""
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("Invalid input. Please enter a number.")


def collect_numbers(count):
    """Collect numbers from the user."""
    numbers = []

    for i in range(count):
        number = get_valid_float(f"Enter number #{i + 1}: ")
        numbers.append(number)

    return numbers


def calculate_mean(numbers):
    """Return the average of the numbers."""
    return math.fsum(numbers) / len(numbers)


def count_above_average(numbers, average):
    """Return how many numbers are above average."""
    count = 0

    for number in numbers:
        if number > average:
            count += 1

    return count


def display_report(numbers, average, minimum, maximum, number_range, above_avg):
    """Display formatted statistics."""
    print("\n=== Number Analysis Report ===")

    print(f"Numbers Entered: {numbers}")
    print(f"Mean: {average:.2f}")
    print(f"Minimum: {minimum:.2f}")
    print(f"Maximum: {maximum:.2f}")
    print(f"Range: {number_range:.2f}")
    print(f"Numbers Above Average: {above_avg}")


# Main Flow

print("=== Number Analyzer ===")

count = get_positive_int("How many numbers would you like to enter? ")

numbers = collect_numbers(count)

average = calculate_mean(numbers)
minimum = min(numbers)
maximum = max(numbers)
number_range = maximum - minimum
above_avg = count_above_average(numbers, average)

display_report(
    numbers,
    average,
    minimum,
    maximum,
    number_range,
    above_avg
)