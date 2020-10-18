import pytest
import cellpy_utils as cutil


def test_minimal():
    a = 2
    b = cutil.double(a)
    print(f"{a} -> {b}")

