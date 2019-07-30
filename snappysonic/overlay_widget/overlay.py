# coding=utf-8

"""Main loop for tracking visualisation"""
from PySide2.QtWidgets import QLabel, QWidget
from cv2 import (rectangle, putText, circle, imread)
from numpy import zeros, uint8
from sksurgeryutils.common_overlay_apps import OverlayBaseApp
from snappysonic.algorithms.algorithms import (configure_tracker,
                                               lookupimage,
                                               check_us_buffer,
                                               get_bg_image_size,
                                               numpy_to_qpixmap)
from snappysonic.algorithms.logo import WeissLogo

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
            super().__init__(config.get("ultrasound buffer"))
        else:
            raise KeyError("Configuration must contain an ultrasound buffer")

        self._video_buffers = self._fill_video_buffers(config)

        self._tracker = None

        if "tracker config" in config:
            self._tracker = configure_tracker(config.get("tracker config"))

        self._bgimage_offsets = (0, 0)
        self._backgroundimage = self._create_background_image(config)

        self._weiss = None
        self._defaultimage = zeros(0, dtype=uint8)
        if "default image" in config:
            self._defaultimage = imread(config.get("default image"))
        else:
            self._weiss = WeissLogo()

        self._logger = None

        self._tracking_window = QWidget()
        self._tracking_window.setWindowTitle("Tracker Position")

        self._tracking_viewer = QLabel("Tracking", self._tracking_window)

        height, width = self._backgroundimage.shape
        self._tracking_window.resize(width, height)
        self._tracking_viewer.resize(width, height)
        self._tracking_window.show()
        self._tracking_viewer.setPixmap(numpy_to_qpixmap(self._backgroundimage))

        #we could implement something like this?
        #if "log directory" in config:
        #    self._logger = sksurgerydatasaver(config.get("log directory"))

    def update(self):
        """Update the background renderer with a new frame,
        move the model and render"""
        #add a method to move the rendered models
        image = self._get_image_with_tracking()

        self.vtk_overlay_window.set_video_image(image)
        self.vtk_overlay_window.Render()

    def _get_image_with_tracking(self):
        """
        Internal method to get an image from the video
        buffer based on the tracker position
        """
        port_handles, _, _, tracking, _ = self._tracker.get_frame()

        tempimg = self._backgroundimage.copy()

        pts = None
        if port_handles:
            for index, port_hdl in enumerate(port_handles):
                if port_hdl == 0:
                    pts = (int(tracking[index][0, 3]),
                           int(tracking[index][1, 3]))
                    off_pts = (int(pts[0] - self._bgimage_offsets[0]),
                               int(pts[1] - self._bgimage_offsets[1]))
                    circle(tempimg, off_pts, 5, [255, 255, 255])

        self._tracking_viewer.setPixmap(numpy_to_qpixmap(tempimg))

        if pts:
            for usbuffer in self._video_buffers:
                inframe, image = lookupimage(usbuffer, pts)
                if inframe:
                    return image

        if self._defaultimage.shape == (0,):
            return self._weiss.get_noisy_logo()

        return self._defaultimage

    def _fill_video_buffers(self, config):
        """
        internal method to fill video buffers
        """
        vidbuffers = []
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
                        if not ret:
                            raise ValueError("Failed Reading video file",
                                             config.get("ultrasound buffer"))

                        frame_counter = frame_counter + 1
                        tempbuffer.append(image)
                print("adding frame ", len(tempbuffer), " images to buffer ",
                      usbuffer.get("name"))
                usbuffer.update({"buffer" : tempbuffer})

                vidbuffers.append(usbuffer)

        return vidbuffers

    def _create_background_image(self, config):
        """
        Creates a backgound image on which we can draw tracking information.
        """

        bg_image_size = [480, 640]
        if "buffer descriptions" in config:
            self._bgimage_offsets, bg_image_size = get_bg_image_size(config)

        bgimage = zeros((bg_image_size), uint8)
        if "buffer descriptions" in config:
            for usbuffer in config.get("buffer descriptions"):
                pt0 = (usbuffer.get("x0") - self._bgimage_offsets[0],
                       usbuffer.get("y0") - self._bgimage_offsets[1])
                pt1 = (usbuffer.get("x1") - self._bgimage_offsets[0],
                       usbuffer.get("y1") - self._bgimage_offsets[1])
                rectangle(bgimage, pt0, pt1, [255, 255, 255])
                putText(bgimage, usbuffer.get("name"), pt0, 0,
                        1.0, [255, 255, 255])

        return bgimage
