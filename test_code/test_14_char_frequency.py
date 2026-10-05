from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.14_char_frequency")
test_func = module.character_frequency

assert test_func("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert test_func("aaa") == {"a": 3}
assert test_func("") == {}

print("All test cases passed.")
