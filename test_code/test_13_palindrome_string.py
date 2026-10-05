from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.13_palindrome_string")
test_func = module.is_palindrome_string

assert test_func("madam") is True
assert test_func("level") is True
assert test_func("Python") is False
assert test_func("Madam") is True

print("All test cases passed.")
