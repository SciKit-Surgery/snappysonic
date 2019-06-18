# coding=utf-8

"""snappy-torso-simulator tests"""

from PySide2.QtWidgets import QApplication
import pytest
from sksurgerytorsosimulator.overlay_widget.overlay import OverlayApp

APP = QApplication([])

def test_init_no_logo():
    """
    Test we can initialise widget, and run with default image
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

    config.update({"ultrasound buffer": "data/aruco_tag.avi"})
    with pytest.raises(ValueError):
        overlay_widget = OverlayApp(config)

    config.update({"ultrasound buffer": "data/usbuffer.mp4"})

    overlay_widget = OverlayApp(config)
    overlay_widget.update()

def test_and_run_with_logo():
    """
    Test we can initialise widget and run update
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
    overlay_widget.update()


def test_and_run_with_buffer_data():
    """
    Test we can initialise widget and run update,
    getting and image from the usbuffer
    """
    config = {
        "ultrasound buffer": "data/usbuffer.mp4",
        "buffer descriptions": [
            {
                "name": "xxxx",
                "start frame": 0,
                "end frame": 284,
                "x0": 40, "x1": 600,
                "y0": 20, "y1": 460,
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
    overlay_widget.update()
