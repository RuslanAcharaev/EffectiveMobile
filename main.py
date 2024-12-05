import json
import time

# Переменная для хранения названия внешнего файла для хранения данных
DATABASE = 'db.json'

# Функция для загрузки данных из внешнего файла
def load_data():
    try:
        with open(DATABASE, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Основная переменная для хранения данных на время работы приложения
books: dict = load_data()

# Функция сохранения данных во внешний файл
def save_data():
    with open(DATABASE, 'w', encoding='UTF-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

# Функция добавления книги в библиотеку
def add_book():
    title: str = input('Введите название книги: ')
    author: str = input('Введите автора книги: ')
    year: str = input('Введите год издания книги: ')

    # Генерация id
    if books:
        book_id = int(max(books.keys(), key=int)) + 1
    else:
        book_id = 1
    books[str(book_id)] = {'title': title, 'author': author, 'year': year, 'status': True}
    save_data()
    print('-------------------------------------------')
    print(f'В библиотеку добавлена книга с book_id №{"\033[93m"}{book_id}{"\033[00m"}:\n'
          f'Название: {"\033[93m"}{title}{"\033[00m"}\n'
          f'Автор: {"\033[93m"}{author}{"\033[00m"}\n'
          f'Год издания: {"\033[93m"}{year}{"\033[00m"}\n')
    time.sleep(1)

# Функция удаления книги из библиотеки
def delete_book():
    try:
        book_id = input('Введите id книги, которую нужно исключить из библиотеки: ')
        book_to_delete = books[book_id]
        print(f'Вы собираетесь удалить книгу автора {book_to_delete['author']} с названием {book_to_delete["title"]}\n')
        response = input('Вы уверены?(да/нет): ')
        if response == 'да':
            del books[book_id]
            save_data()
        else:
            return
    except KeyError:
        print(f'{"\033[93m"}Книга с данным book_id не найдена.{"\033[00m"}')
        time.sleep(1)

# Отдельная функция для вывода данных в табличной форме
def print_table(books_to_print: dict):
    max_id_str_len: int = max(max(map(lambda x: len(x), books_to_print.keys())), len("id"))
    max_author_str_len: int = max(max(map(lambda x: len(x['author']), books_to_print.values())), len("Автор"))
    max_title_str_len: int = max(max(map(lambda x: len(x['title']), books_to_print.values())), len("Название"))
    max_year_str_len: int = len("Год издания")
    max_status_str_len: int = len("в наличии")
    horizontal_line: str = "-" * (16 + max_id_str_len + max_author_str_len + max_title_str_len + max_year_str_len +
                             max_status_str_len)
    print(f'{horizontal_line}\n'
          f'| {"id":{max_id_str_len}} | {"Автор":{max_author_str_len}} | {"Название":{max_title_str_len}} | '
          f'{"Год издания":{max_year_str_len}} | {"Статус":{max_status_str_len}} |\n'
          f'{horizontal_line}')
    for key, value in books_to_print.items():
        print(f'| {key:{max_id_str_len}} | '
              f'{value["author"]:{max_author_str_len}} | '
              f'{value["title"]:{max_title_str_len}} | '
              f'{value["year"]:{max_year_str_len}} | '
              f'{"в наличии" if value["status"] else "выдана":{max_status_str_len}} |')
    print(f'{horizontal_line}')
    time.sleep(1)

# Функция поиска книг
def search_books():
    print('-------------------------------------------------------------------\n'
          'Поиск может быть осуществлен по одному из представленных критериев:\n'
          '1. Название книги;\n'
          '2. Автор книги;\n'
          '3. Год издания книги.')
    search_parameter = input('Введите номер критерия поиска книг: ')
    if search_parameter == '1':
        query = input('Введите название или часть названия книги для поиска: ')
        result = dict(filter(lambda x: query.lower() in x[1]['title'].lower(), books.items()))
        if result:
            print_table(result)
        else:
            print(f'{"\033[93m"}По данному запросу книги не найдены.{"\033[00m"}')
    elif search_parameter == '2':
        query = input('Введите автора книги для поиска: ')
        result = dict(filter(lambda x: query.lower() in x[1]['author'].lower(), books.items()))
        if result:
            print_table(result)
        else:
            print(f'{"\033[93m"}По данному запросу книги не найдены.{"\033[00m"}')
    elif search_parameter == '3':
        query = input('Введите год издания книги для поиска: ')
        result = dict(filter(lambda x: query == x[1]['year'], books.items()))
        if result:
            print_table(result)
        else:
            print(f'{"\033[93m"}По данному запросу книги не найдены.{"\033[00m"}')
    else:
        print(f'{"\033[31m"}Некорректный ввод, попробуйте еще раз.{"\033[00m"}')

# Функция вывода списка книг
def list_of_books():
    if books:
        print_table(books)
    else:
        print(f'{"\033[93m"}Книги в библиотеке отсутствуют.{"\033[00m"}')

# Функция изменения статуса книги
def change_status():
    try:
        id_to_change = input('Введите id книги для изменения её статуса: ')
        print(f'Выбрана книга "{books[id_to_change]['title']}". '
              f'Статус книги: {"в наличии" if books[id_to_change]['status'] else "выдана"}')
        answer = input('Изменить статус выбранной книги? (да/нет): ')
        if answer == 'да':
            books[id_to_change]['status'] = not books[id_to_change]['status']
            save_data()
        else:
            return
    except KeyError:
        print(f'{"\033[93m"}Книга с данным id не найдена.{"\033[00m"}')
        time.sleep(1)


def main():
    print('Добро пожаловать в приложение для управления библиотекой книг!')
    while True:
        print('--------------------------------\n'
              'Вам доступны следующие действия:\n'
              '1. Добавить книгу.\n'
              '2. Удалить книгу.\n'
              '3. Вывести список всех книг.\n'
              '4. Поиск книги.\n'
              '5. Изменение статуса.\n'
              '--------------------------------')
        action = input('Выберите действие, введя его номер: ')
        print('--------------------------------')
        if action == '1':
            add_book()
        elif action == '2':
            delete_book()
        elif action == '3':
            list_of_books()
        elif action == '4':
            search_books()
        elif action == '5':
            change_status()
        else:
            print(f'{"\033[31m"}Некорректный ввод, попробуйте еще раз.{"\033[00m"}')
            time.sleep(1)
            continue


if __name__ == '__main__':
    main()


