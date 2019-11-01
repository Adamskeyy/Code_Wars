class Book:
    def __init__(self, title, authors, rating, read):
        self.title = title
        self.authors = authors
        self.set_rating(rating)
        self.read = read

    def set_rating(self, rating):
        if 1.0 <= rating <= 10:
            self.rating = rating

    def set_read(self, value):
        if value == 'Tak':
            self.read = True
        else:
            self.read = False


class BookBot:
    def __init__(self):
        self.shelf = []
# add

    def add_book(self, title, authors, rating, read):
        b = Book(title, authors, rating, read)
        self.shelf.append(b)

    def add_book_from_input(self):
        title = input('Tytuł: ')
        authors = input('Autor: ')
        rating = float(input('Ocena: '))
        read = input('Przeczytana? ')
        if read == 'Tak':
            read = True
        else:
            read = False
        self.add_book(title, authors, rating, read)
# set

    def set_book_rating(self, book_index, rating):
        book = self.shelf[book_index]
        book.set_rating(rating)

    def set_book_read(self, book_index, read):
        book = self.shelf[book_index]
        book.set_read(read)
# print

    def print_book(self, index):
        book = self.shelf[index]
        print(f'{index:4} | {book.title:30} | {book.authors:30} | {book.rating:5} | {book.read:5}')

    def print_all_books(self):
        for index in range(len(self.shelf)):
            self.print_book(index)

    def print_all_read_books(self):
        for i in range(len(self.shelf)):
            book = self.shelf[i]
            if book.read:
                self.print_book(i)

    def print_all_rating_books(self, min_rating, max_rating):
        for i in range(len(self.shelf)):
            book = self.shelf[i]
            if min_rating <= book.rating <= max_rating:
                self.print_book(i)

    def save_books(self):
        text_books = []
        for i in range(len(self.shelf)):
            book = self.shelf[i]
            text = f'{book.title};{book.authors};{book.rating};{book.read}'
            text_books.append(text)

        with open('books.csv', 'w') as f:
            for line in text_books:
                f.write(line + '\n')

    def load_books(self):
        with open('books.csv', 'r') as f:
            for line in f:
                book_list = line.split(';')
                if book_list[3] == 'True\n':
                    read = True
                else:
                    read = False
                self.add_book(book_list[0], book_list[1], float(book_list[2]), read)


bot = BookBot()
# bot.add_book('Pan Tadeusz', 'Adam Mickiewicz', 6.0, False)
# bot.add_book('Zbrodnia i Kara', 'Fiodor Dostojewski', 8.5, True)
# bot.add_book('Upadek', 'Albert Camus', 9.0, True)
# bot.add_book('Bracia Karamazow', 'Fiodor Dostojewski', 7.0, True)
# bot.save_books()
bot.load_books()
# bot.print_all_books()

while True:
    command = input('Co mam zrobić? ')
    if command == 'help':
        print('Lista komend: \n'
              'dodaj \n'
              'wszystkie \n'
              'oceń \n'
              'przeczytałem \n'
              'pokaż przeczytane \n'
              'pokaż ocenione \n'
              'zapisz')
    if command == 'dodaj':
        bot.add_book_from_input()
    elif command =='wszystkie':
        bot.print_all_books()
    elif command == 'oceń':
        index = int(input('Indeks: '))
        rating = float(input('Ocena: '))
        bot.set_book_rating(index, rating)
    elif command == 'przeczytałem':
        index = int(input('Indeks: '))
        bot.set_book_read(index, 'Tak')
    elif command == 'pokaż przeczytane':
        bot.print_all_read_books()
    elif command == 'pokaż ocenione':
        min_rating = float(input('Min ocena: '))
        max_rating = float(input('Max ocena: '))
        bot.print_all_rating_books(min_rating, max_rating)
    elif command == 'zapisz':
        bot.save_books()
    else:
        print('Nie wiem co mam zrobić')