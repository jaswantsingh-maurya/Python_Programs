from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.08_reverse_number")
test_func = module.reverse_number

assert test_func(12345) == 54321
assert test_func(100) == 1
assert test_func(7) == 7
assert test_func(-123) == -321

print("All test cases passed.")
