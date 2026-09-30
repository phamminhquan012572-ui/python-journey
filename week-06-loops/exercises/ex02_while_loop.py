"""Exercise 02: while, break and continue."""

remaining = 5

# Count down to 1 and update remaining on every pass.
while remaining >= 1:
    print(remaining)
    remaining -= 1

# Loop through 1..10, skip multiples of 3 and stop after 8.
for number in range(1, 11):
    if number % 3 == 0:
        continue
    if number > 8:
        break
    print(number)

print(remaining)
