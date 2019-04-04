# coding=utf-8

"""snappy-torso-simulator tests"""

from sksurgerytorsosimulator.algorithms.algorithms import (configure_tracker,
                                                           lookupimage, noisy,
                                                           check_us_buffer)
from math import floor
from numpy import zeros, uint8


def test_configure_tracker():
    """
    Test that tracker configures and connects with
    a dummy tracker
    """
    settings = {
        "tracker type": "dummy",
        }
    tracker = configure_tracker(settings)


def test_lookupimage():
    """
    create dummy ultrasound buffers and test look ups
    """
    usbuffers = []
    for i in range(4):
        tbuffer={}
        tbuffer.update({"x0" : i % 2 * 200})
        tbuffer.update({"x1" : i % 2 * 200 + 100})
        tbuffer.update({"y0" : floor (i/2) * 200})
        tbuffer.update({"y1" : floor (i/2) * 200 + 100})

        timagebuffer=[]
        timage = zeros((10,10,1), uint8)
        for frame in range (100):
            timagebuffer.append(timage)
        tbuffer.update({"buffer" : timagebuffer})
        usbuffers.append(tbuffer)

    #we should return false if image out of bounds
    pts = (67, 250)
    ret, _ = lookupimage(usbuffers[0], pts)
    assert ret == False
    ret, _ = lookupimage(usbuffers[1], pts)
    assert ret == False
    ret, frame = lookupimage(usbuffers[2], pts)
    assert ret == True
    assert frame.shape == (10,10,1)
    ret, _ = lookupimage(usbuffers[3], pts)
    assert ret == False


if __name__ == '__main__':
    test_lookupimage()
