# coding=utf-8

"""snappysonic tests"""

import pytest
from snappysonic.ui.snappysonic_demo import run_demo

def test_demo_with_bad_config():
    """ test with an invalid config """

    configfile = "nullfile.nullfile"
    with pytest.raises(ValueError):
        run_demo(configfile)
