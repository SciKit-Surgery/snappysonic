import pytest
import PySide2

import sys
from sksurgeryutils.common_overlay_apps import OverlayBaseApp
from snappysonic.overlay_widget.overlay import OverlayApp

from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
from sksurgeryvtk.widgets.vtk_overlay_window import VTKOverlayWindow

from sksurgeryvtk.widgets.QVTKRenderWindowInteractor \
        import QVTKRenderWindowInteractor

import vtk
from vtk.util.colors import tomato

def test_overlay_app(setup_qt):
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
            "debug": False,
        }
    }

    # This widget inherits from OverlayBaseApp
    overlay_widget = OverlayApp(config)    
    overlay_widget.update()
    overlay_widget.stop()

# def test_overlay_base_app(setup_qt):
#     _ = setup_qt

#     # This includesa  VTKOverlayWindow()
#     overlay_base_app = OverlayBaseApp("data/usbuffer.mp4")

# def test_vtk_overlay_widget(setup_qt):
#     _ = setup_qt

#     overlay_widget = VTKOverlayWindow()