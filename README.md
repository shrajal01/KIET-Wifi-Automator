# KIET Wi-Fi Automator

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python automation tool to bypass the manual login process of the **KIET Group of Institutions** Wi-Fi captive portal (Sophos/FortiGate).

---

## Why this project?

In college hostels, Wi-Fi sessions often expire, requiring users to manually log in via a browser repeatedly.
This script automates that process using direct HTTP POST requests, saving time and effort.

---

## Features

* **Instant Login** – Authenticates in milliseconds
* **Error Handling** – Detects connection timeouts and gateway errors
* **Secure Usage** – Designed to be used with environment variables or manual entry (do not push your passwords)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shrajal01/KIET-Wifi-Automator.git
cd KIET-Wifi-Automator
```

---

### 2. Install dependencies

```bash
pip install requests
```

---

### 3. Usage

Open `main.py` and update your credentials:

```python
EMAIL_ID = "your.email@kiet.edu"
PASSWORD = "your_password"
```

Then run the script:

```bash
python main.py
```

---

## ⚠️ Disclaimer

This tool is intended for educational purposes only.
Please ensure you comply with the IT policies of the KIET Group of Institutions while using this script.

---

## 👤 Author

Shrajal

GitHub: https://github.com/shrajal01

Role: Backend Developer | Python | FastAPI
