import os
import sys

import typer

from text import __app_name__, __version__, us_text_warning, messenger


def menu():
    clear_screen()
    typer.echo(typer.style(f"{__app_name__}, version {__version__}", fg=typer.colors.BLUE))
    typer.echo(typer.style("Main Menu", fg=typer.colors.BLUE))

    print("Type: SEND|INFO|EXIT")
    command = input("> ").lower()
    if command == 'send':
        body = input("Input text message: ")
        typer.echo(typer.style(us_text_warning, fg=typer.colors.BLUE))
        to_number = "+1" + input("Enter phone number: ")
        messenger.send_message(body, to_number)
        wait_on_user()
    elif command == 'info':
        typer.echo(typer.style(f"{__app_name__}, version {__version__}", fg=typer.colors.BLUE))
        wait_on_user()
    elif command == 'exit':
        exit_program()


def wait_on_user():
    input(typer.style("Press any key to continue.", fg=typer.colors.GREEN, blink=True))
    to_menu()


def clear_screen():
    os.system('clear')


def to_menu():
    clear_screen()
    menu()


def exit_program():
    clear_screen()
    sys.exit(0)
