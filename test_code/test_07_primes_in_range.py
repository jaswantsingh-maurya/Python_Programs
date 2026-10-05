from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.07_primes_in_range")
test_func = module.primes_in_range

assert test_func(1, 10) == [2, 3, 5, 7]
assert test_func(10, 20) == [11, 13, 17, 19]
assert test_func(20, 25) == [23]

print("All test cases passed.")
