from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.05_fibonacci_series")
test_func = module.fibonacci_series

assert test_func(0) == []
assert test_func(1) == [0]
assert test_func(5) == [0, 1, 1, 2, 3]
assert test_func(7) == [0, 1, 1, 2, 3, 5, 8]

print("All test cases passed.")
