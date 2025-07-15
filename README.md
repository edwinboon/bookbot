# Bookbot Text Analyzer 📚

BookBot is my first [Boot.dev](https://www.boot.dev) project! and its Python command-line tool that analyzes
text files (books) and provides detailed statistics about character frequency and word count.

## Features

- **Word Count**: Get the total number of words in your text
- **Character Analysis**: Count frequency of each character
- **Sorted Results**: View character statistics sorted by frequency
- **Clean Reports**: Get formatted output with all statistics

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd book-text-analyzer
```

2. Ensure you have Python 3.6+ installed:

```bash
python3 --version
```

## Usage

Run the analyzer with a path to your text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

### Sample Output

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
...
--- End report ---
```

## Project Structure

```
book-text-analyzer/
├── main.py          # Main application entry point
├── stats.py         # Statistics calculation functions
├── README.md        # This file
└── books/          # Directory for text files (optional)
    └── sample.txt
```

## Functions

### `main.py`

- `get_book_text(book_path)`: Reads and returns the content of a text file
- `main()`: Main application logic and argument validation

### `stats.py` (imported functions)

- `get_number_of_words(text)`: Counts total words in the text
- `get_character_count(text)`: Counts frequency of each character
- `get_sorted_character_count(char_count)`: Sorts character counts by frequency
- `print_report(book_path, word_count, sorted_chars)`: Formats and prints the analysis report

## Error Handling

The application includes proper error handling for:

- Missing command-line arguments
- Invalid file paths
- File reading errors

## Requirements

- Python 3.6+
- No external dependencies required

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Examples of Books to Analyze

You can test this tool with:

- Project Gutenberg books (free public domain texts)
- Any `.txt` file containing text
- Programming documentation
- Articles or essays saved as text files

## Tips

- For best results, use plain text files (`.txt`)
- Large files may take a moment to process
- The tool works with any UTF-8 encoded text file

---

_Happy analyzing! 🔍📖_
