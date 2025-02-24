import sys

from stats import count_words


def read_file(file_path):
    """Reads a file and returns its content"""
    with open(file_path, encoding="utf8") as f:
        return f.read()


def count_characters(text):
    """Counts the number of characters in a text"""
    count = {}

    for char in text.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count


def sort_on(dict_to_sort):
    """Sorts a dictionary based on its values"""
    return dict_to_sort[1]


def convert_dict_to_list(dict):
    """Converts a dictionary to a list"""
    return list(dict.items())


def generate_report(book_path, word_count, char_count):
    """Prints a report of the book"""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")

    char_list = convert_dict_to_list(char_count)
    char_list.sort(reverse=True, key=sort_on)

    for char, count in char_list:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = read_file(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)

    generate_report(book_path, word_count, char_count)


main()
