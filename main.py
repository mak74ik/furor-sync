#!/usr/bin/env python3
"""
furor-sync: Local-first encrypted vault and key management tool.
"""

import sys
from cli.main_cli import run_cli

if __name__ == '__main__':
    sys.exit(run_cli() or 0)
