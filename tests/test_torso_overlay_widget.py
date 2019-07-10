# coding=utf-8

"""snappy-torso-simulator tests"""

from time import time
import pytest
from sksurgeryutils.common_overlay_apps import OverlayBaseApp
from sksurgerytorsosimulator.overlay_widget.overlay import OverlayApp


def test_overlay_app(setup_qt):
    """Test that OverlayBaseApp is working, I'm not sure why
    but doing this seems to avoid time out errors on the mac
    CI server
    """
    print("Starting test: ", time())
    _ = setup_qt
    _ = OverlayBaseApp('data/aruco_tag.avi')
    print("Ending test: ", time())


def test_overlay_app_with_mp4(setup_qt):
    """Test that OverlayBaseApp is working, I'm not sure why
    but doing this seems to avoid time out errors on the mac
    CI server
    """
    print("Starting test: ", time())
    _ = setup_qt
    _ = OverlayBaseApp('data/usbuffer.mp4')
    print("Ending test: ", time())


def test_error_on_ultrasound_buffer(setup_qt):
    """
    Test we get a key error if no usbuffer
    """
    print("Starting test: ", time())
    _ = setup_qt

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
        _ = OverlayApp(config)
    print("Ending test: ", time())

def test_error_on_invalid_buffer(setup_qt):
    """
    Test we get a value error if we can't read the us buffer
    """
    print("Starting test: ", time())
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
        _ = OverlayApp(config)
    print("Ending test: ", time())


def test_init_no_logo(setup_qt):
    """
    Test we can initialise widget, and run with default image set
    """
    print("Starting test: ", time())
    _ = setup_qt
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
    #overlay_widget.update()
    overlay_widget.stop()
    print("Ending test: ", time())


def test_and_run_with_logo(setup_qt):
    """
    Test we can initialise widget and run update,
    when we haven't set default image.
    """
    print("Starting test: ", time())
    _ = setup_qt
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
    #overlay_widget.update()
    overlay_widget.stop()
    print("Ending test: ", time())


def test_and_run_with_buffer_data(setup_qt):
    """
    Test we can initialise widget and run update,
    getting an image from the usbuffer
    """
    print("Starting test: ", time())
    _ = setup_qt
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
    #overlay_widget.update()
    overlay_widget.stop()
    print("Ending test: ", time())
