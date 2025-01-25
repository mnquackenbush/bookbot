def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    word_count = word_counter(text)
    character_counts = character_counter(text)
    letter_counts, number_counts, special_char_counts = character_sorter(character_counts)
    
    #Print Final Report on Book
    print(f"--- Begin report of {book_path} ---")

    #Print total word count
    print(f"{word_count} words found in the document")
    print()

    #Print each letter's count
    for letter in letter_counts:
        print(f"The {letter} character was found {letter_counts[letter]} times")

    print("--- End report ---")


# Opens the file @ book_path,
# reads the contents, and returns
# them as book_contents string. 
def get_book_contents(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

# Takes in text and returns total length of text.
def word_counter(text):
    return len(text.split())
     
# Takes in text, and defines a dictionary 
# (letter_count) that tracks each time 
# a letter appears in the text.
def character_counter(text):
    lowercase_contents = text.lower()
    character_count = {}
    for word in lowercase_contents:
        for character in word:
            character_value = character
            if character_value not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1   
    return character_count       

# Takes in a dictionary (specifically character_counts)
# and sorts each character into a respective subdictionary 
# by character type.
def character_sorter(characters):
    #Initializes 3 Separate Dictionaries for Each Character Type
    letters = {}
    numbers = {}
    special_chars = {}

    #Initializes a list to store each character dictionary
    character_list = [
        letters,
        numbers,
        special_chars
    ]
    
    #Sorts characters (and their counts) into respective dictionaries
    for character in characters:
        if character.isalpha():
            if character not in letters:
                letters[character] = characters[character]
        elif character.isnumeric():
            if character not in numbers:
                numbers[character] = characters[character]
        else:
            if character not in special_chars:
                special_chars[character] = characters[character]
    
    #Returns list of sorted dictionaries
    return character_list

main()