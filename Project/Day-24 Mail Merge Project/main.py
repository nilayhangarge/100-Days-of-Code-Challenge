# Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

# for each name in invited_names.txt
# file.readlines() method reads lines and converts them into list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

    # Replace the [name] placeholder with the actual name.
    # replace() method changes one word to another in a file
    for elements in names:
        new_name = elements.strip()
        new_letter = letter.replace(PLACEHOLDER, new_name)

        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/new_letter_for_{new_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
