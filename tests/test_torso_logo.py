# coding=utf-8

"""snappysonic tests"""

from numpy import uint8, zeros
from snappysonic.algorithms.logo import WeissLogo, noisy

def test_logo():
    """
    Test that we can make a nice looking logo
    """
    logo = WeissLogo()

    image = logo.get_logo()

    assert image.shape == (331, 331, 3)
    assert image.dtype == uint8

    logo = WeissLogo(400)
    image = logo.get_noisy_logo()

    assert image.shape == (400, 400, 3)
    assert image.dtype == uint8


def test_noisy():
    """
    tests function to add noise to a colour image.
    """
    timage = zeros((10, 10, 1), uint8)
    _ = noisy(timage)
