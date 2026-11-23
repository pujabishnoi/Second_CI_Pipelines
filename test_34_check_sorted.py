import importlib.util

spec = importlib.util.spec_from_file_location("check_sorted", "34_check_sorted.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_is_sorted():
    assert mod.is_sorted([1, 2, 3, 4]) is True
    assert mod.is_sorted([1, 3, 2, 4]) is False