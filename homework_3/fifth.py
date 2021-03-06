def main():
    """
    5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
    сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
    символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
    то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
    """
    q = 'q'
    result = 0

    while True:
        string = input()
        numbers = string.split(' ')
        q_index = numbers.index(q) if q in numbers else None

        if q_index is None:
            result += sum(map(int, numbers))
            print(result)
        else:
            result += sum(map(int, numbers[0:q_index]))
            print(result)
            return


if __name__ == '__main__':
    main()
