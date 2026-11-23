import importlib.util

spec = importlib.util.spec_from_file_location("rotate_string", "37_rotate_string.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_rotate_string():
    assert mod.rotate_string("abcdef", 2) == "cdefab"
    assert mod.rotate_string("abc", 4) == "bca"