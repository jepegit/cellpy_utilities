from cellpy_utils import gutils


def test_minimal():
    """Minimal test to see if imports work"""
    a = 2
    b = gutils.double(a)
    print(f"{a} -> {b}")

