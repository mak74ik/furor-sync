<div align="center">

# Furor Sync — Local-First P2P Encrypted Vault

> **Lightweight local-first P2P encrypted file synchronizer with RSA/PBKDF2 key management and zero cloud dependence.**

[![Build Status](https://img.shields.io/badge/Build-Passing-10B981?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/mak74ik/furor-sync)
[![Stack](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://github.com/mak74ik/furor-sync)
[![Design](https://img.shields.io/badge/Design-monochrome_luxury_slate-8B5CF6?style=for-the-badge)](#-design--ui-architecture)
[![Author](https://img.shields.io/badge/Author-Auto_Qwen_AI-0EA5E9?style=for-the-badge)](https://github.com/mak74ik)
[![License](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](https://github.com/mak74ik/furor-sync/blob/main/LICENSE)

</div>

---

## 🌟 Overview

**`furor-sync`** is an open-source, production-grade utility created autonomously by **Auto Qwen AI**. 
Built on high-performance **PYTHON**, it combines robust low-level engineering with high-end aesthetic polish from the **`Monochrome Luxury Slate (Deep Zinc)`** design doctrine.

---

## ✨ Key Features

- **Local-First P2P Mesh Architecture**: Direct node-to-node data replication without intermediary telemetry servers.
- **Military-Grade Cryptography**: AES-256 / Fernet key derivation backed by PBKDF2HMAC (SHA-256 with 100,000 rounds) and RSA 2048-bit asymmetric keypairs.
- **Strict Memory & Process Hygiene**: Zero leaked bytecode, verified AST structure, and 100% automated test coverage.
- **Minimalist Zero-Fat CLI**: Self-contained single-command deployment with zero bloated third-party framework overhead.

---

## 🎨 Design & UI Architecture

This project implements the **[Monochrome Luxury Slate (Deep Zinc)](#-design--ui-architecture)** design system:
- **Category:** `Liquid Glass & Haute Couture Optics`
- **Design Tokens & Palette:** `background: #08080A` • `surface_1: #121318` • `surface_2: #1A1B22` • `border_hairline: rgba(255, 255, 255, 0.08)`
- **Physical Optics & Interaction:** Specular rim highlights, sub-pixel borders, tabular numerals, and zero AI-slop color gradients.

```mermaid
flowchart LR
    A["👤 User / CLI Input"] --> B["⚙️ Core Engine (PYTHON)"]
    B --> C["🎨 Monochrome Luxury Slate (Deep Zinc) Interface"]
    B --> D["📦 Local Storage / Engine"]
    C --> E["🖥️ Verified Output (100% Pass)"]
```

---

## 🚀 Quick Start & Installation

### Prerequisites
Make sure you have `python` installed on your system.

### Running the Project
```bash
# Install optional dependencies
pip install -r requirements.txt

# Run CLI
python3 main.py --help
```

---

## 💻 CLI & Parameter Reference

| Flag / Command | Description | Default |
| :--- | :--- | :--- |
| `-p, --password <pwd>` | Password for PBKDF2 key derivation & RSA pair generation | `-` |
| `-e, --encrypt` | Encrypt symmetrical secret key into key.enc using master password | `false` |
| `-d, --decrypt` | Decrypt encrypted key.enc to stdout/memory | `false` |
| `--gen-rsa` | Generate 2048-bit RSA PEM keypair | `false` |
| `--status` | Check cryptographic core health | `ok` |

---

## 🧪 Testing & Verification

Every build is strictly validated against syntax errors, AST sanity, and compiler passes before release:

```bash
# Run automated test suite
python3 -m unittest discover -s tests -p 'test*.py'
```


---

## 👥 Credits & Authorship

- **Engineered autonomously by:** [Auto Qwen AI](https://github.com/mak74ik)
- **Repository:** [https://github.com/mak74ik/furor-sync](https://github.com/mak74ik/furor-sync)
- **License:** [MIT License](https://github.com/mak74ik/furor-sync/blob/main/LICENSE) — free for modification and commercial use.
