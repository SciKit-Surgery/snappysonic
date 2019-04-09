# coding=utf-8

"""snappy-torso-simulator tests"""

import pytest
from sksurgerytorsosimulator.ui.sksurgerytorsosimulator_demo import run_demo

def test_demo_with_bad_config():
    """ test with an invalid config """

    configfile = "nullfile.nullfile"
    with pytest.raises(ValueError):
        run_demo(configfile)
