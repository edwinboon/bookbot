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
    BOOK_PATH = "./books/frankenstein.txt"
    book_text = get_book_text(BOOK_PATH)
    number_of_words = get_number_of_words(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = get_sorted_character_count(character_count)

    print_report(BOOK_PATH, number_of_words, sorted_character_count)


main()
