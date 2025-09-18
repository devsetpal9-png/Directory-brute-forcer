# Directory-brute-forcer
A Python tool that scans websites for hidden directories using a wordlist and HTTP requests.

# 🕵️ Directory Brute-Forcer

A Python-based tool for discovering hidden directories and files on web servers using brute-force techniques. This is a lightweight alternative to tools like `dirb`, `gobuster`, and `dirbuster`, built for educational and ethical penetration testing.

---

## 🚀 Features

- 🔍 Scans target URLs for hidden directories
- 📂 Supports custom wordlists
- ✅ Filters valid paths using HTTP status codes
- 🧱 Simple, modular code structure
- 🛠️ Easy to extend with threading, logging, or export features

---

## 🧠 How It Works

The script reads a list of potential directory names from a wordlist file, appends each to the target URL, and sends an HTTP GET request. If the server responds with a `200 OK` status, the directory is considered valid and printed to the console.

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests

## ⚠️ Ethical Disclaimer
This tool is intended strictly for educational and ethical use. Do not use it to scan websites or servers without explicit permission from the owner. Unauthorized scanning may violate laws, terms of service, and ethical guidelines. The author is not responsible for any misuse of this tool.

git clone https://github.com/devsetpal9-png/Directory-brute-forcer
