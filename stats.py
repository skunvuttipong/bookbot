def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    count = 0
    count += len(book.split())
    return count

def count_alphabets(book):
    alphabets = {}
    for char in book:
        alphabet = char.lower()
        if alphabet == " " or "":
            continue
        elif alphabet not in alphabets:
            alphabets[alphabet] = 1
        elif alphabet in alphabets:
            alphabets[alphabet] += 1
            
    return alphabets
        