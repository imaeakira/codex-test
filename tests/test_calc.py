"""Test module for calc utilities."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.calc import add


def test_add():
    assert add(2, 3) == 5
