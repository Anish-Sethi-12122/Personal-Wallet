# 💳 Personal Wallet

A secure, animated command-line wallet manager built in Python (with almost two weeks of sleepless nights :) ).  
Create your own wallet, store and update your balance, and keep everything safe with advanced AES encryption and PBKDF2 key derivation.

---

## ✨ Features

- 🔑 **Master Password Protection:** Access and manage your wallet only with your master password.  
- 🔒 **Database Encryption:** Your `wallet.db` is transparently encrypted to `wallet_secure.db` using AES-GCM encryption, ie. <i>industry-grade</i> security.  
- 🪪 **Unique Wallet Address:** Each wallet gets a unique, randomly generated address (of the format: IND-XXXXXXXXXXXXXXXX (I hope that's 16 digits), hashed with SHA-256 for extra security.  
- 💰 **Balance Management:** View your current balance, add funds, or withdraw funds—all from a friendly CLI menu (made using `rich` for colours and `time.sleep()` for typing effect.  
- 🎨 **UI/UX:** Enjoy colorful animated output and a user-friendly experience, powered by the `rich` library.

---

## 🛡️ Security Highlights

- Wallet addresses are stored as **SHA-256 hashes** for privacy and integrity.  
- The wallet database is protected with **AES-GCM encryption**, using a secure key derived by **PBKDF2-HMAC-SHA256** <i>(very powerful encryption)</i> from your password.  
- Any direct inspection of `wallet_secure.db` in a database viewer reveals only encrypted data, ie. random garbage of strings - never your wallet address or balance.  
- Only the correct master password can decrypt and unlock your wallet—your secrets are never stored in plain text.

---

## 🚀 Getting Started

**1. Clone the repository**  
`git clone https://github.com/your-username/personal-wallet.git` <br>
`cd personal-wallet  `


**2. Install Python dependencies**  
`pip install rich cryptography` <br>


**3. Run the wallet application**  
`python wallet.py` <br>


---

## Default Master Password  
The demo version comes with this preset master password:  
<i>password</i>


_⚠️ For demo and testing. **Change it** before using in real scenarios! (Or I'd recommend not using for anything practically at all, as this is only just a demo file made for learning cryptography and hashing !)_

---

## 🛠️ Features & Roadmap

| Feature                    | The Code has it ??        |
|----------------------------|--------------|
| Master password lock        | ✔️✔️ |
| AES-GCM database encryption | ✔️✔️ |
| Unique wallet address       | ✔️✔️ |
| Balance viewing             | ✔️✔️ |
| Add funds to wallet         | ✔️✔️ |
| Withdraw funds              | ✔️✔️ |

---

## 🤝 Contributing

Pull requests and suggestions are always welcome!  
Fork the repo, make your changes, and submit a pull request.

Licensed under the MIT License.

---

## ⚠️ Disclaimer

This project is for learning and demonstration only.  
**Do not use it to store real financial data or cryptocurrencies.**
