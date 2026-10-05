from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.11_vowels_consonants")
test_func = module.count_vowels_consonants

assert test_func("hello") == (2, 3)
assert test_func("Python") == (1, 5)
assert test_func("AEIOU") == (5, 0)
assert test_func("123!") == (0, 0)

print("All test cases passed.")
