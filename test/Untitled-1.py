def decode(message_file):
    words = []
    lis = []
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to store words

    # Initialize a variable to track the expected number
    expected_num = 1

    # Iterate through each line in the file
    for line in lines:
        # Split the line into number and word
        num, word = line.strip().split(' ')
        lis.append((int(num), word))
    #print(lis)
    # Sort the data based on the numbers
    sorted_data = sorted(lis, key=lambda x: x[0])
    position = 0
    line_length = 1

    # Initialize a list to store the message words
    message_words = []

    # Iterate over the list of numbers
    while position < len(sorted_data):
        # Get the word corresponding to the last number in the current line
        word = sorted_data[position + line_length - 1][1]
        # Append the word to the message words list
        message_words.append(word)
        # Print the numbers for the current line
        #print(" ".join(str(item[0]) for item in sorted_data[position:position + line_length]))

        # Update the position and line length for the next line
        position += line_length
        line_length += 1

    # Join the message words into a string
    decoded_message = ' '.join(message_words)
    return decoded_message

# Example usage:
decoded_message = decode('encoded_message.txt')
print(decoded_message)
