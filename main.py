def read_file(file_path):
    """Reads a file and returns its content"""
    with open(file_path, encoding="utf8") as f:
        return f.read()


def main():
    """Main function"""
    book_path = "books/frankenstein.txt"
    book_text = read_file(book_path)
    print(book_text)


main()
