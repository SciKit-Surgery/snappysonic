# coding=utf-8

"""Main loop for tracking visualisation"""
#from sksurgerytrackervisualisation.shapes import cone, cylinder
from itertools import cycle
from sys import version_info, exit
from vtk.util import numpy_support
import cv2
import numpy
from PySide2.QtWidgets import QApplication
from sksurgeryutils.common_overlay_apps import OverlayBaseApp
from sksurgerynditracker.nditracker import NDITracker
from sksurgeryarucotracker.arucotracker import ArUcoTracker
from sksurgerytrackervisualisation.shapes.cylinder import VTKCylinderModel

def configure_tracker (config):
    if "tracker type" not in config:
        raise KeyError ('Tracker configuration requires tracker type')

    tracker_type = config.get("tracker type")
    tracker = None
    if tracker_type in ("vega", "polaris", "aurora", "dummy"):
        tracker = NDITracker(config)
    if tracker_type in ("aruco"):
        tracker = ArUcoTracker(config)

    tracker.start_tracking()
    return tracker

class OverlayApp(OverlayBaseApp):
    """Inherits from OverlayBaseApp,
    adding code to read in video buffers, and display a frame 
    of data that depends on the position of an external tracking system,
    e.g. surgeryarucotracker"""

    def __init__(self, config):
        """Overides overlay base app's init, to initialise the
        external tracking system. Together with a video source"""

        if "ultrasound buffer" in config:
            #and call the constructor for the base class
            if version_info > (3, 0):
                super().__init__(config.get("ultrasound buffer"))
            else:
                #super doesn't work the same in py2.7
                OverlayBaseApp.__init__(self, config.get("ultrasound buffer"))
        else:
            raise KeyError ("Configuration must contain an ultrasound buffer")

        self._video_buffers = []
        #maybe ._video_buffers is a list of dictionary, 
        #each contains a video buffer, a description, and 
        #and an extent
        frame_counter = 0
        
        if "buffer descriptions" in config:
            for usbuffer in config.get("buffer descriptions"):
                start_frame = usbuffer.get("start frame")
                end_frame = usbuffer.get("end frame")
                tempbuffer = []
                if start_frame == frame_counter:
                    while frame_counter < end_frame:
                        ret, image = self.video_source.read()
                        frame_counter = frame_counter + 1
                        tempbuffer.append(image)
                print ("adding frame ", len(tempbuffer), " images to buffer ", usbuffer.get("name"))
                usbuffer.update({"buffer" : tempbuffer})
                
                self._video_buffers.append(usbuffer)
                

        self._tracker = None
        
        if "tracker config" in config:
            tracker_config = config.get("tracker config")
            self._tracker = configure_tracker(config.get("tracker config"))
        
        #this is a bit of a hack. Is there a better way?
        bgimage = self._tracker._capture.read()
        print (numpy.shape(bgimage))
        height, width, channels = numpy.shape(bgimage)
        self._backgroundimage = numpy.zeros((height, width, channels), numpy.uint8)

    def update(self):
        """Update the background renderer with a new frame,
        move the model and render"""
        #add a method to move the rendered models
        image = self._get_image_with_tracking()

        self.vtk_overlay_window.set_video_image(image)
        self.vtk_overlay_window.Render()
        #self.vtk_overlay_window._RenderWindow.Render()

    def _get_image_with_tracking(self):
        """Internal method to move the rendered models in
        some interesting way
        #Iterate through the rendered models
        for actor in \
                self.vtk_overlay_window.get_foreground_renderer().GetActors():
            #get the current orientation
            orientation = actor.GetOrientation()
            #increase the rotation around the z-axis by 1.0 degrees
            orientation = [orientation[0], orientation[1], orientation[2] + 1.0]
            #add update the model's orientation
            actor.SetOrientation(orientation)
        """
        port_handles, _, _, tracking, _ = self._tracker.get_frame()

        if port_handles:
            #these will need working on, need a way to match model names with port handles
            pass
        
        usbuffer = self._video_buffers[0].get("buffer")
        image = usbuffer[0]
        cv2.imshow('tracking',self._backgroundimage)
        return image

#here's a dummy app just to test the class. Quickly
if __name__ == '__main__':
    app = QApplication([])

    configuration = { "ultrasound buffer" : "../../data/glove2.mp4",
                      "buffer descriptions" : (
                                               { "name" : "glove",
                                                 "start frame" : 0,
                                                 "end frame" : 100,
                                                 "x0" : 80 , "x1" : 160,
                                                 "y0" : 20 , "y1" : 200 },
                                               { "name" : "glove2",
                                                 "start frame" : 101,
                                                 "end frame" : 200,
                                                 "x0" : 80 , "x1" : 160,
                                                 "y0" : 20 , "y1" : 200 }
                                               ),

                        "tracker config" :
                        {
                            "tracker type" : "aruco",
                            "video source" : 2,
                            "debug" : True,
                            "capture properties" : 
                            {
                                "CAP_PROP_FRAME_WIDTH" : 1280 ,
                                "CAP_PROP_FRAME_HEIGHT" : 960 
                            }

                        }

                    }

    viewer = OverlayApp(configuration)

    #model_dir = '../models'
    #viewer.add_vtk_models_from_dir(model_dir)

    viewer.start()

   #start the application
    exit(app.exec_())


