from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.12_reverse_string")
test_func = module.reverse_string

assert test_func("hello") == "olleh"
assert test_func("Python") == "nohtyP"
assert test_func("") == ""
assert test_func("12345") == "54321"

print("All test cases passed.")
