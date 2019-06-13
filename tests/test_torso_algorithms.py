# coding=utf-8

"""snappy-torso-simulator tests"""

from math import floor
from numpy import zeros, uint8
import pytest
from sksurgerytorsosimulator.algorithms.algorithms import (configure_tracker,
                                                           lookupimage,
                                                           check_us_buffer)
from sksurgerytorsosimulator.algorithms.logo import noisy


def test_configure_tracker():
    """
    Test that tracker configures and connects with
    a dummy tracker
    """
    settings = {
        "tracker type" : "dummy",
        }
    _ = configure_tracker(settings)


def test_lookupimage():
    """
    create dummy ultrasound buffers and test look ups
    """
    usbuffers = []
    for i in range(4):
        tbuffer = {}
        tbuffer.update({"x0" : i % 2 * 200})
        tbuffer.update({"x1" : i % 2 * 200 + 100})
        tbuffer.update({"y0" : floor(i/2) * 200})
        tbuffer.update({"y1" : floor(i/2) * 200 + 100})

        timagebuffer = []
        timage = zeros((10, 10, 1), uint8)
        for frame in range(100):
            timagebuffer.append(timage)
        tbuffer.update({"buffer" : timagebuffer})
        usbuffers.append(tbuffer)

    #we should return false if image out of bounds
    pts = (67, 250)
    ret, _ = lookupimage(usbuffers[0], pts)
    assert not ret
    ret, _ = lookupimage(usbuffers[1], pts)
    assert not ret
    ret, frame = lookupimage(usbuffers[2], pts)
    assert ret
    assert frame.shape == (10, 10, 1)
    ret, _ = lookupimage(usbuffers[3], pts)
    assert not ret


def test_noisy():
    """
    tests function to add noise to a colour image.
    """
    timage = zeros((10, 10, 1), uint8)
    _ = noisy(timage)


def test_check_us_buffer():
    """
    tests function to check that ultrasound
    buffer is properly configured.
    """
    tbuffer = {}
    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"name" : "a name"})

    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"start frame" : 0})

    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"end frame" : 0})

    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"x0" : 0})

    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"x1" : 0})

    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"y0" : 0})

    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"y1" : 0})

    with pytest.raises(KeyError):
        check_us_buffer(tbuffer)
    tbuffer.update({"scan direction" : "z"})

    with pytest.raises(ValueError):
        check_us_buffer(tbuffer)
    tbuffer.update({"scan direction" : "x"})

    check_us_buffer(tbuffer)
