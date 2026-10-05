from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.03_pos_neg_zero")
test_func = module.check_number

assert test_func(10) == "Positive"
assert test_func(-10) == "Negative"
assert test_func(0) == "Zero"

print("All test cases passed.")
