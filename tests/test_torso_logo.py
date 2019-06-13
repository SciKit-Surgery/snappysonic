# coding=utf-8

"""snappy-torso-simulator tests"""

from cv2 import imwrite
from sksurgerytorsosimulator.algorithms.logo import WeissLogo

def test_logo():
    """
    Test that we can make a nice looking logo
    """
    logo = WeissLogo()

    #imwrite("cleanlog.png", logo.get_logo())
    imwrite("noisylog0.png", logo.get_noisy_logo())
    imwrite("noisylog1.png", logo.get_noisy_logo())
    imwrite("noisylog2.png", logo.get_noisy_logo())
