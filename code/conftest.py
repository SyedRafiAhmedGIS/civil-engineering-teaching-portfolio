"""Pytest path bootstrap: makes the package importable from any CWD."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
