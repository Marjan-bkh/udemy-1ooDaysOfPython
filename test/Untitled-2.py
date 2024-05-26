numbers = [1, 2, 3, 4, 5, 6,]

# Initialize variables to keep track of the current position and line length
position = 0
line_length = 1

# Iterate over the list of numbers
while position < len(numbers):
    # Print the numbers for the current line
    print(" ".join(map(str, numbers[position:position + line_length])))

    # Update the position and line length for the next line
    position += line_length
    line_length += 1
