import importlib.util

spec = importlib.util.spec_from_file_location("move_zeros", "35_move_zeros.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_move_zeros():
    assert mod.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert mod.move_zeros([0, 0]) == [0, 0]