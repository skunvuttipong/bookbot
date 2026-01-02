from stats import get_book_text, count_words, count_alphabets
import sys
        
def main():
    # Check if the user provided a path argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the path from command line arguments
    path = sys.argv[1]
    
    book = get_book_text(path)
    alphabets = count_alphabets(book)
    sorted_alphabets = dict(sorted(alphabets.items(), key=lambda item: item[1], reverse=True))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")
    for k,v in sorted_alphabets.items():
        print(f"{k}: {v}")
    
if __name__ == "__main__":
    main()