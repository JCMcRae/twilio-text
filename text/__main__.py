import sys

import typer
from text.interfaces import cli, desktop

app = typer.Typer()


def main(start_mode):
    select_start_mode(start_mode)


def select_start_mode(start_mode):
    if start_mode is not None and start_mode == 'cli':
        run_cli()
    else:
        run_desktop()


@app.command()
def run_cli():
    cli.menu()


def run_desktop():
    desktop.launch()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    argument = None
    if len(sys.argv) >= 2:
        argument = sys.argv[1]
    main(argument)
