from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.19_find_duplicates")
test_func = module.find_duplicates

assert test_func([1, 2, 2, 3, 1]) == [2, 1]
assert test_func([5, 5, 5]) == [5]
assert test_func([1, 2, 3]) == []

print("All test cases passed.")
