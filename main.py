def fizzbuzz(limit):
    """FizzBuzz: цикл for + if/elif/else."""
    print('=== FizzBuzz (1-15) ===')
    for i in range(1, limit + 1):
        if i % 15 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
    print('\n')


def guess_number(secret, attempts):
    """Угадай число: цикл while + if/elif/else."""
    print(f'=== Угадай число (загадано: {secret}) ===')
    attempt_index = 0

    while attempt_index < len(attempts):
        guess = attempts[attempt_index]
        attempt_index += 1
        print(f'Попытка {attempt_index}: {guess}', end=' -> ')

        if guess == secret:
            print('Верно!')
            return
        elif guess > secret:
            print('Больше')
        else:
            print('Меньше')

    print('Попытки закончились.\n')


def multiplication_table(number, up_to):
    """Таблица умножения: цикл for + if/elif/else."""
    print(f'=== Таблица умножения на {number} ===')
    for i in range(1, up_to + 1):
        result = number * i
        if i == 1:
            print(f'{number} x {i} = {result}  (начало таблицы)')
        elif i == up_to:
            print(f'{number} x {i} = {result}  (конец таблицы)')
        else:
            print(f'{number} x {i} = {result}')


if __name__ == '__main__':
    fizzbuzz(15)
    guess_number(secret=42, attempts=[10, 25, 40, 42])
    multiplication_table(number=7, up_to=10)
