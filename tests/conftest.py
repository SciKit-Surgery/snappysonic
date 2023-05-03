# -*- coding: utf-8 -*-

""" Creates the QT app """
import pytest
from PySide6.QtWidgets import QApplication

@pytest.fixture(scope="session")
def setup_qt():

    """ Create the QT application. """
    # Check if already an instance of QApplication is present or not
    if not QApplication.instance():
        _pyside_qt_app = QApplication([])
    else:
        _pyside_qt_app = QApplication.instance()

    return _pyside_qt_app
