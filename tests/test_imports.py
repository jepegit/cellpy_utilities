from cellpy_utils import gutils


def test_minimal():
    a = 2
    b = gutils.double(a)
    print(f"{a} -> {b}")

