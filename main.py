#!/usr/bin/env python3
"""
Furor-Sync - Local-First P2P Encrypted Vault
Part of Yoshi Toolchain.
"""

import sys
from cli.main_cli import run_cli

if __name__ == '__main__':
    sys.exit(run_cli() or 0)
