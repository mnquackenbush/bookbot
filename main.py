def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    word_count = word_counter(text)
    character_counts = character_counter(text)
        

    
def get_book_contents(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

def word_counter(text):
    return len(text.split())
     

def character_counter(text):
    lowercase_contents = text.lower()
    letter_count = {}
    for word in lowercase_contents:
        for letter in word:
            letter_value = letter
            if letter_value not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1   
    return letter_count       

main()