from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.20_word_frequency")
test_func = module.word_frequency

assert test_func("hello world hello") == {"hello": 2, "world": 1}
assert test_func("Python python PYTHON") == {"python": 3}
assert test_func("") == {}

print("All test cases passed.")
