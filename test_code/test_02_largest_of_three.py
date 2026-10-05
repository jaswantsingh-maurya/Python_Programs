from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.02_largest_of_three")
test_func = module.largest_of_three

assert test_func(10, 20, 30) == 30
assert test_func(30, 20, 10) == 30
assert test_func(10, 10, 5) == 10
assert test_func(5, 10, 10) == 10
assert test_func(10, 10, 10) == 10

print("All test cases passed.")
