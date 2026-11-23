import importlib.util

spec = importlib.util.spec_from_file_location("count_words", "32_count_words.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_count_words():
    assert mod.count_words("Hello world from Python") == 4
    assert mod.count_words("   ") == 0