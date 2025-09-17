# 💳 Personal Wallet

A simple yet secure command-line personal wallet built with Python.  
It lets you create a wallet, store your balance, and protect everything with AES encryption so your data always stays private.

---

## ✨ Features

- 🔑 **Master Password Protection** – access wallet only with your password  
- 🔒 **Full Database Encryption** – your `wallet.db` is encrypted into `wallet_secure.db` using AES-GCM  
- 🪪 **Unique Wallet Address** – randomly generated, hashed (SHA-256), and stored securely  
- 💰 **Balance Management** – *(coming soon)* view, add, and withdraw funds  
- 🎨 **Rich UI** – colorful CLI interface with smooth text animations  

---

## 🛡️ Security Highlights

- Wallet addresses are hashed with **SHA-256** before storage  
- Database file (`wallet.db`) is encrypted with **AES-GCM** and a key derived from your password using **PBKDF2-HMAC-SHA256**  
- If someone opens your database in a SQLite viewer, they’ll see **gibberish** instead of usable data  
- Only the **correct master password** can decrypt your wallet  

---

## 🚀 Getting Started

Run the following commands in your terminal:

# 1. Clone the repository
git clone https://github.com/your-username/personal-wallet.git
cd personal-wallet

# 2. Install dependencies
pip install rich cryptography

# 3. Run the wallet
python wallet.py

## 🤡 Default Master Password
The demo version uses the following Master Password:

password

_⚠️ I’d suggest you change it before using._

📂 Project Structure

personal-wallet/
│
├── wallet.py            # Main script
├── wallet_secure.db     # Encrypted database (generated after first run)
└── README.md            # Project documentation


## 🛠️ Roadmap

 - [ ] Implement balance viewing
 - [ ] Add funds to wallet
 - [ ] Withdraw funds
 - [ ] Support multiple wallets
 - [ ] Add transaction history

## 🤝 Contributing

Pull requests and feature suggestions are welcome!
Licensed under the MIT License.

## ⚠️ Disclaimer: This project is for learning and demonstration purposes only.
## Do not use it to store real financial data or cryptocurrencies.
