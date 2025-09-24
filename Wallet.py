import sys
import os
from random import randint
import time
from rich.console import Console
from rich.text import Text
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import sqlite3 as sql

COLOR_MAP = {
    "CYAN": "bright_cyan",
    "YELLOW": "bright_yellow",
    "RED": "bright_red",
    "GREEN": "bright_green",
    "WHITE": "white",
    "MAGENTA": "bright_magenta"
}
console = Console()
wallet_address = None
conn = None
cur = None

def Print(message, color_key="WHITE", style=""):
    color = COLOR_MAP.get(color_key, "white")
    for char in message:
        console.print(char, style=f"{style} {color}", end="")
        time.sleep(0.02069)
    console.print("")

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

def pass_check():
    Print("Enter password to authenticate: ", "CYAN")
    return input() == "password"

def hash_wallet_address(wallet_address: str) -> str:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(wallet_address.encode())
    return digest.finalize().hex()

def generate_wallet():
    wallet_addr = 'IND' + str(randint(1000000000000000, 9999999999999999))
    Print(f"Your wallet address is: {wallet_addr}\nSave it for future reference", "MAGENTA")
    print('\n')
    wallet_hash = hash_wallet_address(wallet_addr)
    return wallet_hash, wallet_addr

def create_wallet():
    global wallet_address
    wallet_hash, wallet_address = generate_wallet()
    Print("Enter your name: ", "YELLOW", "bold")
    name = input()
    print('\n')
    cur.execute("INSERT INTO wallet (wallet_address, name, current_balance) VALUES (?, ?, ?)",
                (wallet_hash, name, 0.0))
    conn.commit()

def database_wallet():
    global cur, conn, wallet_address
    conn = sql.connect('wallet.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS wallet
                   (
                       wallet_address TEXT PRIMARY KEY,
                       name TEXT,
                       current_balance REAL DEFAULT 0.0
                   )''')
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM wallet")
    if cur.fetchone()[0] == 0:
        create_wallet()
    else:
        cur.execute("SELECT wallet_address FROM wallet LIMIT 1")
        wallet_address = cur.fetchone()[0]

def balance():
    Print("----- Option to Check Balance chosen -----", 'YELLOW', "bold")
    print('\n')
    if not pass_check():
        Print("Incorrect Master Password..", "RED", "bold")
        print('\n')
        return
    cur.execute("SELECT * FROM wallet WHERE wallet_address = ?", (wallet_address,))
    data = cur.fetchone()
    if data:
        Print(f"Your current balance is: ₹{data[2]:.2f}", "MAGENTA")
        print('\n')
    else:
        Print("Wallet not found!", "RED", "bold")

def add_balance():
    Print("----- Option to Add Balance chosen -----", "YELLOW", "bold")
    print('\n')
    Print("Enter amount to add: ", "YELLOW", "bold")
    amount = float(input())
    print('\n')
    cur.execute("UPDATE wallet SET current_balance = current_balance + ? WHERE wallet_address = ?", (amount, wallet_address))
    conn.commit()
    Print(f"₹{amount:.2f} added to your balance.", "GREEN", "bold")
    print('\n')

def withdraw_balance():
    Print("----- Option to Withdraw Balance chosen -----", "YELLOW", "bold")
    print('\n')
    if not pass_check():
        Print("Incorrect Master Password..", "RED", "bold")
        print('\n')
        return
    cur.execute("SELECT * FROM wallet WHERE wallet_address = ?", (wallet_address,))
    data = cur.fetchone()
    if not data:
        Print("Wallet not found!", "RED", "bold")
        return
    Print(f"Your current balance is: ₹{data[2]:.2f}", "MAGENTA")
    print('\n')
    Print("Enter amount to withdraw: ", "BLUE")
    amount = float(input())
    while amount > data[2] or amount <= 0:
        if amount > data[2]:
            Print(f"Insufficient funds. Your balance is ₹{data[2]:.2f}.", "RED", "bold")
        else:
            Print("Invalid amount. Must be positive.", "MAGENTA")
        print('\n')
        Print("Enter amount to withdraw: ", "BLUE")
        amount = float(input())
    Print(f"Withdrawing: ₹{amount:.2f}.....", "MAGENTA")
    time.sleep(2)
    cur.execute("UPDATE wallet SET current_balance = current_balance - ? WHERE wallet_address = ?", (amount, wallet_address))
    conn.commit()
    Print("Withdrawal successful.", "GREEN", "bold")
    print('\n')

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

def main():
    while True:
        Print("----- Main Menu -----", "YELLOW", "bold")
        print('\n')
        Print("1. View balance", "CYAN")
        Print("2. Add funds", "CYAN")
        Print("3. Withdraw funds", "CYAN")
        Print("4. Exit", "CYAN")
        Print("Enter the number of your choice: ", "YELLOW", "bold")
        user_choice = input()
        while user_choice not in ['1', '2', '3', '4']:
            Print("Invalid choice. Enter 1-4.", "RED", "bold")
            user_choice = input()
        if user_choice == '1':
            balance()
        elif user_choice == '2':
            add_balance()
        elif user_choice == '3':
            withdraw_balance()
        elif user_choice == '4':
            Print("Thank you for using your personal wallet!", "GREEN", "bold")
            print('\n')
            sys.exit()
        if not ask_continue():
            break

if __name__ == "__main__":
    Print("Welcome to INDIA DEMO BANK e-Pay!", "YELLOW", "bold")
    print('\n')
    Print("Enter your master password to access the wallet (Master password is: password -- REMEMBER ME): ", "YELLOW", "bold")
    master_password = input()
    print('\n')
    if master_password != "password":
        Print("Access denied. Wrong master password.", "RED", "bold")
        sys.exit()
    if os.path.exists("wallet_secure.db"):
        decrypt_file("wallet_secure.db", master_password)
    database_wallet()
    main()
    if os.path.exists("wallet.db"):
        encrypt_file("wallet.db", master_password)
