def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    word_count = word_counter(text)
    letter_counts = letter_counter(text)
    print(letter_counts)

    
def get_book_contents(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

def word_counter(text):
    num_words = len(text.split())
    return f"There are {num_words} words in Frankenstein."

def letter_counter(text):
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