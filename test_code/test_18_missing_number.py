from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.18_missing_number")
test_func = module.find_missing_number

assert test_func([1, 2, 3, 5], 5) == 4
assert test_func([1, 2, 4, 5], 5) == 3
assert test_func([2, 3, 4, 5], 5) == 1

print("All test cases passed.")
