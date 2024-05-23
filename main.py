print('Задание № 1')
def test_product(txt, *values, type=' ₽'):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}{type}'

print(test_product("Сумма заказа: ", 25, 282, 345,))

print('-------------------')
print('Задание № 2')

print('Первый вариант')
def factorial(n):
    if n == 3:
        return 3
    else:
        return n * factorial(n - 1)

print(factorial(5))

print('-------------------')

print('Второй вариант')
def factorial(n):
    if n == 3:
        return 3
    else:
        return n * factorial(n - 1)

print(factorial(int(input('Введите любое число: '))))