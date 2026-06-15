# Числа
integer_num = 10
float_num = 3.5

# Строки
greeting = 'Привет'
name = 'Python'

# Булевые значения
is_active = True
is_admin = False

# Арифметические операции с числами
sum_result = integer_num + float_num
diff_result = integer_num - float_num
product_result = integer_num * float_num
quotient_result = integer_num / float_num
power_result = integer_num ** 2
mod_result = integer_num % 3

print('=== Переменные разных типов ===')
print(f'Число (int): {integer_num}, тип: {type(integer_num).__name__}')
print(f'Число (float): {float_num}, тип: {type(float_num).__name__}')
print(f'Строка: {greeting}, тип: {type(greeting).__name__}')
print(f'Строка: {name}, тип: {type(name).__name__}')
print(f'Булево: {is_active}, тип: {type(is_active).__name__}')
print(f'Булево: {is_admin}, тип: {type(is_admin).__name__}')

print('\n=== Арифметические операции ===')
print(f'{integer_num} + {float_num} = {sum_result}')
print(f'{integer_num} - {float_num} = {diff_result}')
print(f'{integer_num} * {float_num} = {product_result}')
print(f'{integer_num} / {float_num} = {quotient_result:.2f}')
print(f'{integer_num} ** 2 = {power_result}')
print(f'{integer_num} % 3 = {mod_result}')

print('\n=== Операции со строками ===')
full_message = greeting + ', ' + name + '!'
print(f'Конкатенация: {full_message}')
print(f'Повтор строки: {name * 3}')

print('\n=== Операции с булевыми значениями ===')
print(f'is_active and is_admin = {is_active and is_admin}')
print(f'is_active or is_admin = {is_active or is_admin}')
print(f'not is_admin = {not is_admin}')
