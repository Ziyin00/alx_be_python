"""Draws a square pattern of asterisks of user-specified size using nested loops."""

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
