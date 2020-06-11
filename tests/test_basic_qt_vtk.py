import pytest
import PySide2

import sys

from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
from sksurgeryvtk.widgets.vtk_overlay_window import VTKOverlayWindow

from sksurgeryvtk.widgets.QVTKRenderWindowInteractor \
        import QVTKRenderWindowInteractor

import vtk
from vtk.util.colors import tomato

@pytest.fixture(scope="session")
def setup_qt():

    """ Create the QT application. """
    app = QApplication([])
    return app

def test_qapp(setup_qt):

    app = setup_qt
    dialog = QDialog()
    dialog.show()

def test_vtk_cylinder(setup_qt):
    
    #Copied from https://vtk.org/Wiki/VTK/Examples/Python/Cylinder

    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)

    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(tomato)
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)

    # Create the graphics structure. The renderer renders into the render
    # window. The render window interactor captures mouse events and will
    # perform appropriate camera or actor manipulation depending on the
    # nature of the events.
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size
    ren.AddActor(cylinderActor)
    ren.SetBackground(0.1, 0.2, 0.4)
    renWin.SetSize(200, 200)

    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    iren.Initialize()

    # We'll zoom in a little by accessing the camera and invoking a "Zoom"
    # method on it.
    ren.ResetCamera()
    ren.GetActiveCamera().Zoom(1.5)
    renWin.Render()

    # Start the event loop.
    #iren.Start()

# This should pass
def test_qvtkrenderwindowinteracto_dont_start(setup_qt):
    app = setup_qt
    widget = QVTKRenderWindowInteractor()

# This should fail/crash
def test_qvtkrenderwindowinteractor(setup_qt):
    app = setup_qt
    widget = QVTKRenderWindowInteractor()
    widget.Start()

def test_vtkoverlaywindow(setup_qt):
    app = setup_qt
    widget = VTKOverlayWindow()

