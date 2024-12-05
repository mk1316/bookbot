def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letters(text)
    chars_list = dict_to_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words were found in the document", "\n")
    for c in chars_list:
        print(f"The {c['char']} character was found {c['num']} times")
    print("--- End Report ---")

# Putiing them in a list
def dict_to_list(num_chars_dict):
    chars = []
    for c in num_chars_dict:
        if c.isalpha() == True:
            chars.append({"char": c, "num": num_chars_dict[c]})
        else:
            continue
    chars.sort(reverse=True, key=sort_on)
    return chars

# Gets text content
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Counts number of words in text
def count_words(text):
    words = text.split()
    return len(words)

# Creates dict of character frequency
def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# Sort
def sort_on(dict):
    return dict["num"]



    
main()