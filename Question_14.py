'''Word Counter: Create a program that counts the number of words, characters, and 
lines in a text document.'''

# Defining function which accepts file path or paragraph for counting
def count_words_characters_lines(input_data):
    if input_data.startswith("file:"):
        # If input is a file path
        file_path = input_data[5:].strip()
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
            return
    else:
        content = input_data # If input is a paragraph

    word_count = len(content.split()) # Count the number of words
    char_count = len(content) # Count the number of characters
    line_count = content.count('\n') + 1 # Count the number of lines

    return word_count, char_count, line_count

# Defining main function
def main():
    input_data = input("Enter the file path (starting with 'file:') or a paragraph: ")

    # Count words, characters, and lines based on input type
    word_count, char_count, line_count = count_words_characters_lines(input_data)

    print("Word count:", word_count)
    print("Character count:", char_count)
    print("Line count:", line_count)

if __name__ == "__main__":
    main()
