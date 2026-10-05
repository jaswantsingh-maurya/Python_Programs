from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.16_remove_duplicates")
test_func = module.remove_duplicates

assert test_func([1, 2, 2, 3, 1]) == [1, 2, 3]
assert test_func([5, 5, 5]) == [5]
assert test_func([]) == []

print("All test cases passed.")
