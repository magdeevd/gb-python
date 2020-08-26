def main():
    """
    4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
    Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
    """
    string = input("Введите строку: ")

    for i, word in enumerate(string.split(" ")):
        print(f"{i + 1} - {word[0:10]}")


if __name__ == '__main__':
    main()
