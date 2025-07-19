pattern = int(input("Enter the size of the pattern:"))

"""use a while loop to iterate through each row of the pattern.
Inside the while loop, use a for loop to print("*", end="").
After completing each row, print a newline character to move to the next row.
Continue until the pattern forms a square of the inputted size."""

i = 1
while i <= pattern :
    for j in range(0, pattern) :
        print("*", end= "")
    i += 1
    print()