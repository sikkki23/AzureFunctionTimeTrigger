requirements.txt
pytest

tests/test_hello.py
import pytest

def test_hello():
    assert "hello" == "hello"