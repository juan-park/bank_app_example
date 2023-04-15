import click
from src.db import create_table, seed_db

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
    pass

if __name__ == '__main__':
    main()