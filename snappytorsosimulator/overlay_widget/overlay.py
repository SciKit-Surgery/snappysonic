# coding=utf-8

"""Main loop for tracking visualisation"""
from sys import version_info, exit
from cv2 import (rectangle, putText, circle, imread, imshow)
from numpy import zeros, uint8
from sksurgeryutils.common_overlay_apps import OverlayBaseApp
from snappytorsosimulator.algorithms.algorithms import (configure_tracker,
                                                        lookupimage, noisy,
                                                        check_us_buffer)


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
                check_us_buffer(usbuffer)
                start_frame = usbuffer.get("start frame")
                end_frame = usbuffer.get("end frame")
                tempbuffer = []
                if start_frame == frame_counter:
                    while frame_counter <= end_frame:
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
        _, bgimage = self._tracker._capture.read()

        self._backgroundimage = zeros((bgimage.shape), uint8)
        if "buffer descriptions" in config:
            for usbuffer in config.get("buffer descriptions"):
                pt0=(usbuffer.get("x0"),usbuffer.get("y0"))
                pt1=(usbuffer.get("x1"),usbuffer.get("y1"))
                rectangle(self._backgroundimage,pt0,pt1,[255,255,255])
                putText(self._backgroundimage, usbuffer.get("name"),pt0, 0, 1.0, [255,255,255])

        self._defaultimage = None
        if "default image" in config:
            self._defaultimage = imread(config.get("default image"))
        else:
            self._defaultimage = self._backgroundimage.copy()

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

        tempimg = self._backgroundimage.copy()

        pt=None
        if port_handles:
            for i in range(len(port_handles)):
                if port_handles[i] == 0:
                    pt=(tracking[i][0,3],tracking[i][1,3])
                    circle(tempimg,pt,5,[255,255,255])

        imshow('tracking',tempimg)

        if pt:
            for usbuffer in self._video_buffers:
                inframe, image = lookupimage (usbuffer, pt)
                if inframe:
                    return image

        temping2 = self._defaultimage.copy()
        temping3 = self._defaultimage.copy()
        noise = noisy(temping2)
        return noise + temping3

