from sys import argv

from stats import (
    get_character_count,
    get_number_of_words,
    get_sorted_character_count,
    print_report,
)


def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


def main():
    if len(argv) != 2:
        raise ValueError("Usage: python3 main.py <path_to_book>")

    book_path = argv[1]
    book_text = get_book_text(book_path)
    number_of_words = get_number_of_words(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = get_sorted_character_count(character_count)

    print_report(book_path, number_of_words, sorted_character_count)


main()
