import mysql.connector
from typing import Tuple
from datetime import datetime
from .env import HOST, USERNAME, PASSWORD, DB_NAME

conn = mysql.connector.connect(host=HOST, user=USERNAME, password=PASSWORD, database=DB_NAME)

def create_table():
    sql = f"""
    CREATE TABLE `{DB_NAME}`.`user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(45) UNIQUE NOT NULL,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `birthday` DATETIME NOT NULL,
    `datesignedup` DATETIME NOT NULL,
    `phonenumber` VARCHAR(20) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    `address` VARCHAR(100) NULL,
    `password` VARCHAR(45) NOT NULL,
    `balance` DECIMAL(10) NOT NULL,
    PRIMARY KEY (`id`));
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def seed_db():
    """seed = inserting database with some fake initial data to play around with."""
    add_user("mary.zonderman", "Mary", "Zonderman", "22/12/1976", "11/04/2023", "(783) 725-1217", "Mary.Zonderman@gmail.com", "505 Hood Rd #1, Markham, Ontario, L3R 5V6, Canada", "testing!",0)
    add_user("john.pip", "John", "Pip", "02/05/1999", "14/03/2023", "(889) 492-6298", "John.Pip@gmail.com", "505 Hood Rd #1, Markham, Ontario, L3R 5V6, Canada", "testing!",1000)
    add_user("craig.fischer", "Craig", "Fischer", "02/07/202", "08/04/2023", "(443) 994-7539", "Craig.Fischer@gmail.com", "505 Hood Rd #1, Markham, Ontario, L3R 5V6, Canada", "testing!",50)
    add_user("john.park", "John", "Park", "09/09/1999", "14/04/2023", "(648) 757-9484", "John.Park@gmail.com", "505 Hood Rd #1, Markham, Ontario, L3R 5V6, Canada", "testing!",20)
    add_user("ash.ketchum", "Ash", "Ketchum", "22/05/1987", "14/04/2023", "(418) 926-1252", "Ash.Ketchum@gmail.com", "505 Hood Rd #1, Markham, Ontario, L3R 5V6, Canada", "testing!",100000)

def update_user_sql(id):
    return f"""
    """

def add_user(username: str, first_name: str, last_name: str, birthday: str, phonenumber: str, email: str, address: str, password: str, balance: str):
    """FYI the date format used is dd/mm/yyyy. Feel free to try changing it.
    """
    sql = f"""INSERT INTO `{DB_NAME}`.`user` (`username`, `first_name`, `last_name`, `birthday`, `datesignedup`, `phonenumber`, `email`, `address`, `password`, `balance`) VALUES ('{username}', '{first_name}', '{last_name}', STR_TO_DATE('{birthday}', '%d/%m/%Y'), STR_TO_DATE('{datetime.now().strftime('%d/%m/%Y')}', '%d/%m/%Y'), '{phonenumber}', '{email}', '{address}', '{password}', {balance});"""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def update_account_balance_sql(id: int, amount: int) -> int:
    pass

def check_account_balance_sql(id: int) -> int:
    pass

def get_user_name(id: int) -> Tuple[str, str]:
    sql = f"""SELECT first_name, last_name FROM `{DB_NAME}`.`user` where id = {id};"""
    cur = conn.cursor()
    cur.execute(sql)
    
    for row in cur:
        print(row)
        return row
    return -1

def validate_login(username: str, password: str) -> int:
    sql = f"""SELECT id FROM `{DB_NAME}`.`user` where username = '{username}' and password = '{password}';"""
    cur = conn.cursor()
    cur.execute(sql)
    
    for row in cur:
        return row[0]
    return -1