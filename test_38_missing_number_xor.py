import importlib.util

spec = importlib.util.spec_from_file_location("missing_xor", "38_missing_number_xor.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_find_missing_number():
    assert mod.find_missing_number([3, 0, 1]) == 2
    assert mod.find_missing_number([0, 1, 3, 4]) == 2