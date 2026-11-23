import importlib.util

spec = importlib.util.spec_from_file_location("transpose", "39_transpose_matrix.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_transpose_matrix():
    assert mod.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert mod.transpose_matrix([]) == []