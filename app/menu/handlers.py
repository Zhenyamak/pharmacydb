from sys import exit
from app.services import component as component_service


def crete_component_handler():
    name = input('Enter name')
    try:
        price = input('Enter price')
    except (ValueError, TypeError):
        print('Wrong price')
        return
    try:
        amount = input('Enter amount')
        return
    except (ValueError, TypeError):
        print('Wrong amount')
    component_service.crete_component(name=name, price=price, amount=amount)


def shut_down():
    print("Bye")
    exit()


def help_handler():
    print("""You are using pharmacy database 
                 You can enter:
                 
                 hekp - (but you are here)
                 exit - to close the program""")


COMMANDS = {
    'create_order': crete_component_handler,
    'exit': shut_down,
    'help': help_handler,
}
