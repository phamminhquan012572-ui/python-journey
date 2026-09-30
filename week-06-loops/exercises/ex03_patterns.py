"""Exercise 03: readable list comprehensions."""

numbers = range(1, 11)

# Build squares for all numbers.
squares: list[int] = [number ** 2 for number in numbers]

# Build even_numbers with one filter.
even_numbers: list[int] = [number for number in numbers if number % 2 == 0]

# The comprehension above is concise and readable.
# Equivalent normal loop:
even_numbers_loop: list[int] = []
for number in numbers:
    if number % 2 == 0:
        even_numbers_loop.append(number)

print(squares, even_numbers)
