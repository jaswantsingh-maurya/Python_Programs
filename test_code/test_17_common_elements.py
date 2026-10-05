from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.17_common_elements")
test_func = module.common_elements

assert test_func([1, 2, 3], [2, 3, 4]) == [2, 3]
assert test_func([1, 2, 2, 3], [2, 4]) == [2]
assert test_func([1, 2], [3, 4]) == []

print("All test cases passed.")
