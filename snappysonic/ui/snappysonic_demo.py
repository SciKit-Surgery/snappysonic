# coding=utf-8


"""SnappySonicdemo module"""

import sys
from PySide2.QtWidgets import QApplication
from sksurgerycore.configuration.configuration_manager import (
        ConfigurationManager
        )
from snappysonic.overlay_widget.overlay import OverlayApp


def run_demo(configfile):
    """ Run the application """

    configurer = ConfigurationManager(configfile)

    app = QApplication([])

    configuration = configurer.get_copy()

    viewer = OverlayApp(configuration)

    viewer.start()

    #start the application
    sys.exit(app.exec_())
