# coding=utf-8

"""snappy-torso-simulator tests"""

from numpy import uint8, zeros
import pytest
from sksurgerytorsosimulator.overlay_widget.overlay import OverlayApp

def test_init_no_logo(setup_qt):
    """
    Test we can initialise widget
    """
    config = {
                 "default image": "data/logo.png",
        "buffer descriptions": [
                {
                 "name": "xxxx",
                 "start frame": 0,
                 "end frame": 284,
                 "x0": 40, "x1": 240,
                 "y0": 200, "y1": 260,
                 "scan direction": "x"
                }],
     "tracker config": {
                "tracker type": "aruco",
                "video source": "data/aruco_tag.avi",
                "debug": True,
                "capture properties": {
                        "CAP_PROP_FRAME_WIDTH": 640,
                        "CAP_PROP_FRAME_HEIGHT": 480
                }
        }
     }

    with pytest.raises(KeyError):
        overlay_widget = OverlayApp(config)

    config.update({"ultrasound buffer": "data/usbuffer.mp4"})
    overlay_widget = OverlayApp(config)

def test_init_with_logo(setup_qt):
    """
    Test we can initialise widget
    """
    config = {
                "ultrasound buffer": "data/usbuffer.mp4",
        "buffer descriptions": [
                {
                 "name": "xxxx",
                 "start frame": 0,
                 "end frame": 284,
                 "x0": 40, "x1": 240,
                 "y0": 200, "y1": 260,
                 "scan direction": "x"
                }],
     "tracker config": {
                "tracker type": "aruco",
                "video source": "data/aruco_tag.avi",
                "debug": True,
                "capture properties": {
                        "CAP_PROP_FRAME_WIDTH": 640,
                        "CAP_PROP_FRAME_HEIGHT": 480
                }
        }
     }

    overlay_widget = OverlayApp(config)
    overlay_widget.start()
    overlay_widget.update()
    overlay_widget.stop()


   
