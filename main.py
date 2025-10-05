import sys
from stats import count_words, count_caracter, informe

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    caracter_words = count_caracter(text)
    informe_caracter = informe(text, book_path, num_words, caracter_words)
    print(informe_caracter)

main()

