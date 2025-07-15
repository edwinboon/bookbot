def get_number_of_words(text: str) -> int:
    return len(text.split())


def get_character_count(text: str) -> dict:
    counts_dict = {}
    for char in text.lower():
        if char in counts_dict:
            counts_dict[char] += 1
        else:
            counts_dict[char] = 1
    return counts_dict


def sort_on(items):
    return items["num"]


def get_sorted_character_count(character_count: dict) -> list:
    sorted_count = []
    for key, value in character_count.items():
        if key.isalpha():
            sorted_count.append({"char": key, "num": value})

    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count


def print_report(book_path: str, number_of_words: int, character_count: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("---------- Character Count -------")
    for item in character_count:
        print(f"{item['char']}: {item['num']}")
