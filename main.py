import string

def count_words(file_contents):
    """
    Counts the number of words in the file.
    """
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    """
    Counts the number of lettes in the file.

    Returns a ditionary of 26 english characters
    """
    alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}

    for char in file_contents.lower():
        if char in alphabet_dict:
            alphabet_dict[char] += 1
        
    return alphabet_dict

def main():
    file = 'books/frankenstein.txt'
    with open(file) as f:
        file_contents = f.read()

    print(f'--- Begin report of {file} ---')
    word_count=count_words(file_contents)
    print(word_count)
    print()
    character_count = count_letters(file_contents)
    for key, value in character_count.items():
        print(f'The {key} character was found {value} times')
    print('--- End report ---')
main()