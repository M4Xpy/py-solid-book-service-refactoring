from app.book import Book
from app.functionality import display, print_book
from app.serializers import serialize


def main(book: Book,
         commands: list[tuple[str, str]],
         ) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display(book, method_type)
        elif cmd == "print":
            print_book(book, method_type)
        elif cmd == "serialize":
            return serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
