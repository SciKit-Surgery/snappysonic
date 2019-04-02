# coding=utf-8


"""Hello world demo module"""
from PySide2.QtWidgets import QApplication
from sksurgerycore.configuration.configuration_manager import (
        ConfigurationManager
        )
from sksurgerytorsosimulator.overlay_widget.overlay import OverlayApp


def run_demo(configfile):
    """ Run the application """
    app = QApplication([])

    configurer = ConfigurationManager(configfile)

    configuration = configurer.get_copy()

    viewer = OverlayApp(configuration)

    #model_dir = '../models'
    #viewer.add_vtk_models_from_dir(model_dir)

    viewer.start()

   #start the application
    exit(app.exec_())
