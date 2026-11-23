import importlib.util

spec = importlib.util.spec_from_file_location("most_frequent", "36_most_frequent.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_most_frequent():
    assert mod.most_frequent([1, 3, 2, 3, 4, 3]) == 3
    assert mod.most_frequent([]) is None