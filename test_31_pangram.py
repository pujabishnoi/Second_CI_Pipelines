import importlib.util

spec = importlib.util.spec_from_file_location("pangram", "31_pangram.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_is_pangram():
    assert mod.is_pangram("The quick brown fox jumps over the lazy dog") is True
    assert mod.is_pangram("Hello world") is False