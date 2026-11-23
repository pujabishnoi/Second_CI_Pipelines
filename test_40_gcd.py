import importlib.util

spec = importlib.util.spec_from_file_location("gcd_mod", "40_gcd.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_compute_gcd():
    assert mod.compute_gcd(48, 18) == 6
    assert mod.compute_gcd(17, 13) == 1