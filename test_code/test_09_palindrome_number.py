from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.09_palindrome_number")
test_func = module.is_palindrome

assert test_func(121) is True
assert test_func(1221) is True
assert test_func(123) is False
assert test_func(-121) is False

print("All test cases passed.")
