from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.15_second_largest")
test_func = module.second_largest

assert test_func([10, 20, 30, 40]) == 30
assert test_func([5, 5, 3, 2]) == 3
assert test_func([1, 10, 5, 8]) == 8

print("All test cases passed.")
