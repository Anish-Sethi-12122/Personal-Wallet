💳 **Personal Wallet**

A simple yet secure command-line personal wallet built with Python.
It lets you create a wallet, store your balance, and protect everything with AES encryption so your data always stays private.


✨ **Features**

🔑 _Master Password Protection –_ access wallet only with your password.
🔒 _Full Database Encryption –_ your wallet.db is encrypted into wallet_secure.db using AES-GCM.
🪪 _Unique Wallet Address –_ randomly generated, hashed (SHA-256), and stored securely.
💰 _Balance Management –_ (coming soon) view, add, and withdraw funds.
🎨 _Rich UI –_ colorful CLI interface with smooth text animations.


🛡️ **Security Highlights**

Wallet addresses are hashed with SHA-256 before storage.
Database file (wallet.db) is encrypted with AES-GCM and a key derived from your password using PBKDF2-HMAC-SHA256.
If someone opens your database in a SQLite viewer, they’ll see gibberish instead of usable data.
Only the correct master password can decrypt your wallet.


**🚀 Getting Started**

Run the following commands in your terminal-

_1. Clone the repository_
git clone https://github.com/your-username/personal-wallet.git
cd personal-wallet

_2. Install dependencies_
pip install rich cryptography

_3. Run the wallet_
python wallet.py

**🤡 Default Master Password**

The demo version uses the following Master Password:

password

_⚠️ I'd suggest you to change it before using_

**📂 Project Structure**

personal-wallet/
│
├── wallet.py            # Main script
├── wallet_secure.db     # Encrypted database (generated after first run)
└── README.md            # Project documentation


**🛠️ Roadmap**

- [ ] Implement balance viewing  
- [ ] Add funds to wallet  
- [ ] Withdraw funds  
- [ ] Support multiple wallets  
- [ ] Add transaction history  


**🤝 Contributing**

Pull requests and feature suggestions are welcome!
Licensed under the MIT License

**This project is for learning and demonstration purposes only.
Do not use it to store real financial data or cryptocurrencies.**
