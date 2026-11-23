import importlib.util

spec = importlib.util.spec_from_file_location("first_non_repeating", "33_first_non_repeating.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_first_non_repeating():
    assert mod.first_non_repeating("swiss") == "w"
    assert mod.first_non_repeating("aabb") is None