import click
from src.db import create_table, seed_db
from src.app import App


@click.group()
def main():
    pass

@main.command()
def init_db():
    """Creates table and seeds it"""
    create_table()
    seed_db()
    

@main.command()
def run():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()