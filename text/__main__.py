import typer

import cli

app = typer.Typer()


@app.command()
def run_cli():
    cli.menu()


if __name__ == '__main__':
    run_cli()
