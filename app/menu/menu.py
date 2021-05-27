from app.menu import handlers
from app.menu.handlers import COMMANDS


def menu():
    print('Enter command, help - see all avaliable commands')
    while True:
        command = input('=> ')
        handler = COMMANDS.get(command)
        if handler:
            handler()
        else:
            print('Unknown command')
