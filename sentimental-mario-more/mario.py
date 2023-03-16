# Prompt user for the height of the grid
height = 0
while True:
    try:
        height = int(input("Height: "))
        if height < 1 or height > 8:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 8.")

# Build the grid
for i in range(1, height + 1):
    # Build empty space for each line
    for j in range(height - i):
        print(" ", end="")
    # Build grid on left side
    for k in range(i):
        print("#", end="")
    # Add gap between the two sides of the grid
    print("  ", end="")
    # Build grid on right side
    for k in range(i):
        print("#", end="")
    # Move to the next line for the next row of the grid
    print()
