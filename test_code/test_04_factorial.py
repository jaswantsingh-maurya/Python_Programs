from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.04_factorial")
test_func = module.factorial

assert test_func(0) == 1
assert test_func(1) == 1
assert test_func(5) == 120
assert test_func(7) == 5040

print("All test cases passed.")
