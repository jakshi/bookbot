import sys

from stats import get_char_count, get_sorted_char_count, get_words_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    book = get_book_text(book_file)
    print(f"Found {get_words_count(book)} total words")
    print("--------- Character Count -------")
    chars_count = get_char_count(book)
    sorted_chars = get_sorted_char_count(chars_count)
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
