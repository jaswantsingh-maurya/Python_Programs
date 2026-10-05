from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.06_prime_number")
test_func = module.is_prime

assert test_func(2) is True
assert test_func(7) is True
assert test_func(1) is False
assert test_func(10) is False
assert test_func(0) is False

print("All test cases passed.")
