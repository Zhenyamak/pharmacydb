from app.data import menu

def Command():
    command = input("You are using pharmacy database \n"
                      "You can enter:\n"
                      "If you wish to stop working with database, enter End\n"
                      "For more information enter Help\n")
    # сюда базовые функции типа вывода или добавления

if __name__ == '__main__':
    while True:
        request = input("Введите команду: ")
        menu(request)