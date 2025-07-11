def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


def main():
    BOOK_PATH = "./books/frankenstein.txt"
    book_text = get_book_text(BOOK_PATH)
    print(book_text)


main()
