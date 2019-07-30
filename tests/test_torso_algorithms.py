# coding=utf-8

"""snappysonic tests"""

from math import floor
from numpy import zeros, uint8
import pytest
import snappysonic.algorithms.algorithms as skalg

def test_configure_tracker():
    """
    Test that tracker configures and connects with
    a dummy tracker
    """
    settings = {
        "tracker type" : "dummy",
        }
    _ = skalg.configure_tracker(settings)

    settings = {
        "invalid" : "config"
        }

    with pytest.raises(KeyError):
        _ = skalg.configure_tracker(settings)

    settings = {
        "tracker type" : "aruco",
        "video source" : "data/nofile.xxxx",
        "aruco dictionary" : "DICT_6X6_250"
        }

    with pytest.raises(OSError):
        _ = skalg.configure_tracker(settings)

    settings = {
        "tracker type" : "aruco",
        "video source" : "data/usbuffer.mp4",
        "aruco dictionary" : "DICT_6X6_250"
        }

    _ = skalg.configure_tracker(settings)

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
        if i == 3:
            tbuffer.update({"scan direction" : "x"})

        timagebuffer = []
        timage = zeros((10, 10, 1), uint8)
        for frame in range(100):
            timagebuffer.append(timage)
        tbuffer.update({"buffer" : timagebuffer})
        usbuffers.append(tbuffer)

    #we should return false if image out of bounds
    pts = (67, 250)
    ret, _ = skalg.lookupimage(usbuffers[0], pts)
    assert not ret
    ret, _ = skalg.lookupimage(usbuffers[1], pts)
    assert not ret
    ret, frame = skalg.lookupimage(usbuffers[2], pts)
    assert ret
    assert frame.shape == (10, 10, 1)
    ret, _ = skalg.lookupimage(usbuffers[3], pts)
    assert not ret

    pts = (265, 250)
    ret, _ = skalg.lookupimage(usbuffers[0], pts)
    assert not ret
    ret, _ = skalg.lookupimage(usbuffers[1], pts)
    assert not ret
    ret, _ = skalg.lookupimage(usbuffers[2], pts)
    assert not ret
    ret, frame = skalg.lookupimage(usbuffers[3], pts)
    assert ret
    assert frame.shape == (10, 10, 1)


def test_check_us_buffer():
    """
    tests function to check that ultrasound
    buffer is properly configured.
    """
    tbuffer = {}
    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"name" : "a name"})

    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"start frame" : 0})

    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"end frame" : 0})

    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"x0" : 0})

    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"x1" : 0})

    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"y0" : 0})

    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"y1" : 0})

    with pytest.raises(KeyError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"scan direction" : "z"})

    with pytest.raises(ValueError):
        skalg.check_us_buffer(tbuffer)
    tbuffer.update({"scan direction" : "x"})

    skalg.check_us_buffer(tbuffer)


def test_check_bg_image_size():
    """
    tests function to set up background image size
    """
    configuration = {
        "buffer descriptions":
        [
            {
                "name": "xxxx",
                "start frame": 0,
                "end frame": 284,
                "x0": 40, "x1": 240,
                "y0": 200, "y1": 260,
                "scan direction": "x"
            },
            {
                "name": "xxxxxx",
                "start frame": 285,
                "end frame": 560,
                "x0": 260, "x1": 460,
                "y0": 200, "y1": 260,
                "scan direction": "x"
            },
            {
                "name": "xxx",
                "start frame": 561,
                "end frame": 816,
                "x0": 40, "x1": 240,
                "y0": 280, "y1": 440,
                "scan direction": "x"
            }
        ],
        "border size" : 20,
    }

    offsets, image_size = skalg.get_bg_image_size(configuration)

    assert offsets == (20, 180)
    assert image_size == (280, 460)
