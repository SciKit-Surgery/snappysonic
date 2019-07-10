# coding=utf-8

"""snappy-torso-simulator tests"""

import pytest
from sksurgerytorsosimulator.overlay_widget.overlay import OverlayApp
import sksurgeryutils.common_overlay_apps as coa

def test_overlay_app(setup_qt):

    _app = setup_qt
    _overlay_widget = coa.OverlayBaseApp('data/aruco_tag.avi')

def test_error_on_ultrasound_buffer(setup_qt):
    """
    Test we get a key error if no usbuffer
    """
    _app = setup_qt

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
        _overlay_widget = OverlayApp(config)

def test_error_on_invalid_buffer(setup_qt):
    """
    Test we get a value error if we can't read the us buffer
    """
    _app = setup_qt
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

    config.update({"ultrasound buffer": "data/aruco_tag.avi"})
    with pytest.raises(ValueError):
        _overlay_widget = OverlayApp(config)


def test_init_no_logo(setup_qt):
    """
    Test we can initialise widget, and run with default image set
    """
    _app = setup_qt
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

    config.update({"ultrasound buffer": "data/usbuffer.mp4"})

    overlay_widget = OverlayApp(config)
    overlay_widget.update()
    overlay_widget.stop()

def test_and_run_with_logo(setup_qt):
    """
    Test we can initialise widget and run update,
    when we haven't set default image.
    """
    _app = setup_qt
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
    overlay_widget.stop()


def test_and_run_with_buffer_data(setup_qt):
    """
    Test we can initialise widget and run update,
    getting an image from the usbuffer
    """
    _app = setup_qt
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
    overlay_widget.stop()
