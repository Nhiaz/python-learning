operations = ["Сложение", "Вычитание", "Умножение", "Деление"]

for i in range(len(operations)):
    print(f"{i + 1}. {operations[i]}")


    
def get_operation_choice():
        x = int(input("Выберите операцию (1-4): "))
        if x == 1:
            print(add())
        elif x == 2:
            print(subtract())
        elif x == 3:
            print(multiply())
        elif x == 4:
            print(divide())

def add(a = 0, b = 0):
    print("Вы выбрали сложение.")
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return a + b

def subtract(a = 0, b = 0):
    print("Вы выбрали вычитание.")
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return a - b

def multiply(a = 0, b = 0):
    print("Вы выбрали умножение.")
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return a * b

def divide(a = 0, b = 0):
    print("Вы выбрали деление.")
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if b == 0:
        return "Ошибка: Деление на ноль"
    return a / b

while True:
    get_operation_choice()
