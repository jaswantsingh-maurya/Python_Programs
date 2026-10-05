from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.10_sum_of_digits")
test_func = module.sum_of_digits

assert test_func(12345) == 15
assert test_func(100) == 1
assert test_func(0) == 0
assert test_func(-123) == 6

print("All test cases passed.")
