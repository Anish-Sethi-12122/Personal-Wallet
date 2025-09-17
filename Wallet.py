import sys
import os
from random import randint
import time
from rich.console import Console
from rich.text import Text
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

COLOR_MAP = {
    "CYAN": "bright_cyan",
    "YELLOW": "bright_yellow",
    "RED": "bright_red",
    "GREEN": "bright_green",
    "WHITE": "white",
    "MAGENTA": "bright_magenta"
}
console = Console()

def Print(message, color_key="WHITE", style=""):
    color = COLOR_MAP.get(color_key, "white")
    styled_text = Text("", style=f"{style} {color}")
    for char in message:
        styled_text.append(char)
        console.print(char, style=f"{style} {color}", end="")
        time.sleep(0.02069)

def ask_continue():
    Print("Would you like to continue? (y/n): ", "YELLOW", "bold")
    choice = input().lower()
    while choice not in ['y', 'n']:
        print('\n')
        Print("Invalid choice. Please enter 'y' or 'n'.", "RED", "bold")
        print('\n')
        Print("Would you like to continue? (y/n): ", "YELLOW", "bold")
        choice = input().lower()
    print('\n')
    return choice == 'y'

def main():
    global choice
    while choice:
        Print("What would you like to do?", "MAGENTA")
        print('\n')
        Print("1. View balance", "CYAN")
        print('\n')
        Print("2. Add funds", "CYAN")
        print('\n')
        Print("3. Withdraw funds", "CYAN")
        print('\n')
        Print("4. Exit", "CYAN")
        print('\n')
        Print("Enter the number of your choice: ", "YELLOW", "bold")
        choice = input()
        print('\n')
        while choice not in ['1', '2', '3', '4']:
            Print("Invalid choice. Please enter a number between 1 and 4.", "RED", "bold")
            print('\n')
            Print("Enter the number of your choice: ", "YELLOW")
            choice = input()
            print('\n')
        if choice == '1':
            balance()
        elif choice == '2':
            add_balance()
        elif choice == '3':
            withdraw_balance()
        elif choice == '4':
            Print("Thank you for using your personal wallet!", "GREEN", "bold")
            print('\n')
            sys.exit()
        choice = ask_continue()

def balance():
    pass  # to implement

def hash_wallet_address(wallet_address: str) -> str:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(wallet_address.encode())
    return digest.finalize().hex()

def generate_wallet():
    wallet_address = 'IND' + str(randint(1000000000000000, 9999999999999999))
    Print(f"Your wallet address is: {wallet_address}\nSave it for future reference", "MAGENTA")
    print('\n')
    wallet_hash = hash_wallet_address(wallet_address)
    return wallet_hash

def create_wallet():
    wallet_hash = generate_wallet()
    Print("Enter your name: ", "YELLOW", "bold")
    name = input()
    print('\n')
    wallet = (wallet_hash, name, 0.0)
    return wallet

def retrieve():
    pass  # to implement

def add_balance():
    pass  # to implement

def withdraw_balance():
    pass  # to implement

def database_wallet():
    import sqlite3 as sql
    conn = sql.connect('wallet.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS wallet
                 (
                     wallet_address TEXT PRIMARY KEY,
                     name TEXT,
                     current_balance REAL DEFAULT 0.0
                 )''')
    conn.commit()
    c.execute("SELECT COUNT(*) FROM wallet")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO wallet (wallet_address, name, current_balance) VALUES (?, ?, ?)", create_wallet())
        conn.commit()
    conn.close()

def encrypt_file(in_file: str, password: str, out_file: str = "wallet_secure.db"):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
    )
    key = kdf.derive(password.encode())
    with open(in_file, "rb") as f:
        data = f.read()
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, None)
    with open(out_file, "wb") as f:
        f.write(salt + nonce + ct)

def decrypt_file(enc_file: str, password: str, out_file: str = "wallet.db"):
    with open(enc_file, "rb") as f:
        blob = f.read()
    salt, nonce, ct = blob[:16], blob[16:28], blob[28:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
    )
    key = kdf.derive(password.encode())
    aesgcm = AESGCM(key)
    data = aesgcm.decrypt(nonce, ct, None)
    with open(out_file, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    Print("Welcome to INDIA DEMO BANK e-Pay!", "YELLOW", "bold")
    print('\n')
    Print("Enter your master password to access the wallet (Master password is: password): ", "YELLOW", "bold")
    master_password = input()
    print('\n')
    if master_password != "password":
        Print("Access denied. Wrong master password.", "RED", "bold")
        print('\n')
        sys.exit()
    if os.path.exists("wallet_secure.db"):
        decrypt_file("wallet_secure.db", master_password)
    choice = 'y'
    database_wallet()
    main()
    if os.path.exists("wallet.db"):
        encrypt_file("wallet.db", master_password)
        os.remove("wallet.db")
