# 💳 Personal Wallet

A secure, animated command-line wallet manager built in Python.  
Create your own wallet, store and update your balance, and keep everything safe with advanced AES encryption and PBKDF2 key derivation.

---

## ✨ Features

- 🔑 **Master Password Protection:** Access and manage your wallet only with your master password.  
- 🔒 **Database Encryption:** Your `wallet.db` is transparently encrypted to `wallet_secure.db` using AES-GCM encryption.  
- 🪪 **Unique Wallet Address:** Each wallet gets a unique, randomly generated address, hashed with SHA-256 for extra security.  
- 💰 **Balance Management:** View your current balance, add funds, or withdraw funds—all from a friendly CLI menu.  
- 🎨 **Rich CLI Interface:** Enjoy colorful animated output and a user-friendly experience, powered by the `rich` library.

---

## 🛡️ Security Highlights

- Wallet addresses are stored as **SHA-256 hashes** for privacy and integrity.  
- The wallet database is protected with **AES-GCM encryption**, using a secure key derived by **PBKDF2-HMAC-SHA256** from your password.  
- Any direct inspection of `wallet_secure.db` in a database viewer reveals only encrypted data—never your wallet or balance.  
- Only the correct master password can decrypt and unlock your wallet—your secrets are never stored in plain text.

---

## 🚀 Getting Started

**1. Clone the repository**  
git clone https://github.com/your-username/personal-wallet.git <br>
cd personal-wallet  


**2. Install Python dependencies**  
pip install rich cryptography <br>


**3. Run the wallet application**  
python wallet.py <br>


---

## 🤡 Default Master Password  
The demo version comes with this preset master password:  
<i>password</i>


_⚠️ For demo and testing. **Change it** before using in real scenarios!_

---

## 🛠️ Features & Roadmap

| Feature                    | Status        |
|----------------------------|--------------|
| Master password lock        | ✔️ Implemented |
| AES-GCM database encryption | ✔️ Implemented |
| Unique wallet address       | ✔️ Implemented |
| Balance viewing             | ✔️ Implemented |
| Add funds to wallet         | ✔️ Implemented |
| Withdraw funds              | ✔️ Implemented |

---

## 🤝 Contributing

Pull requests and suggestions are always welcome!  
Fork the repo, make your changes, and submit a pull request.

Licensed under the MIT License.

---

## ⚠️ Disclaimer

This project is for learning and demonstration only.  
**Do not use it to store real financial data or cryptocurrencies.**

---

### Security tips

- Do **not** reuse the master password for anything important.  
- Consider using a password manager for better key management.  
- Don’t commit or share sensitive `.db` files publicly.
