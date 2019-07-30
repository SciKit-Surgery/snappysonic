"""Functions for snappysonic"""
from numpy import iinfo, int16
from PySide2.QtGui import QPixmap, QImage
from sksurgerynditracker.nditracker import NDITracker
from sksurgeryarucotracker.arucotracker import ArUcoTracker

def configure_tracker(config):
    """
    Configures a scikit-surgery tracker based on the passed config
    param: a tracker configuration dictionary
    returns: The tracker
    raises: Key Error
    """

    if "tracker type" not in config:
        raise KeyError('Tracker configuration requires tracker type')

    tracker_type = config.get("tracker type")
    tracker = None
    if tracker_type in ("vega", "polaris", "aurora", "dummy"):
        tracker = NDITracker(config)
    if tracker_type in "aruco":
        tracker = ArUcoTracker(config)

    if tracker_type not in "dummy":
        tracker.start_tracking()
    return tracker


def lookupimage(usbuffer, pts):
    """
    determines whether a coordinate (pts) lies with an area defined by
    a usbuffer, and returns an image from the buffer if appropriate
    param: usbuffer, a dictionary containing bounding box information (x0,y0,
    x1,y1) and image data
    returns: True if point in bounding box. Image.
    """
    if pts[0] > usbuffer.get("x0"):
        if pts[0] < usbuffer.get("x1"):
            if pts[1] > usbuffer.get("y0"):
                if pts[1] < usbuffer.get("y1"):
                    pdiff = 0
                    if usbuffer.get("scan direction") == "x":
                        diff = pts[0] - usbuffer.get("x0")
                        pdiff = int(diff /
                                    (usbuffer.get("x1") - usbuffer.get("x0")) *
                                    len(usbuffer.get("buffer")))
                    else:
                        diff = pts[1] - usbuffer.get("y0")
                        pdiff = int(diff /
                                    (usbuffer.get("y1") - usbuffer.get("y0")) *
                                    len(usbuffer.get("buffer")))

                    return True, usbuffer.get("buffer")[pdiff]

    return False, None

def check_us_buffer(usbuffer):
    """
    Checks that all ultrasound buffer contains all required key values.
    :param the buffer to check
    :raises Exception: KeyError, ValueError
    """
    if "name" not in usbuffer:
        raise KeyError("Buffer configuration must contain a name.")
    if "start frame" not in usbuffer:
        raise KeyError("Buffer configuration must contain a start frame.")
    if "end frame" not in usbuffer:
        raise KeyError("Buffer configuration must contain an end frame.")
    if "x0" not in usbuffer:
        raise KeyError("Buffer configuration must contain x0")
    if "x1" not in usbuffer:
        raise KeyError("Buffer configuration must contain x1")
    if "y0" not in usbuffer:
        raise KeyError("Buffer configuration must contain y0")
    if "y1" not in usbuffer:
        raise KeyError("Buffer configuration must contain y1")
    if "scan direction" not in usbuffer:
        raise KeyError("Buffer configuration must contain a scan direction.")

    direction = usbuffer.get("scan direction")
    if direction not in ("x", "y"):
        raise ValueError("scan direction must be either x or y")

def get_bg_image_size(config):
    """
    Reads the geometry from a configuration and
    returns the extents of the buffer
    """
    min_x = iinfo(int16).max
    max_x = iinfo(int16).min
    min_y = iinfo(int16).max
    max_y = iinfo(int16).min

    if "buffer descriptions" in config:
        for usbuffer in config.get("buffer descriptions"):
            if usbuffer.get("x0") > max_x:
                max_x = usbuffer.get("x0")
            if usbuffer.get("x1") > max_x:
                max_x = usbuffer.get("x1")
            if usbuffer.get("x1") < min_x:
                min_x = usbuffer.get("x1")
            if usbuffer.get("x0") < min_x:
                min_x = usbuffer.get("x0")
            if usbuffer.get("y0") > max_y:
                max_y = usbuffer.get("y0")
            if usbuffer.get("y1") > max_y:
                max_y = usbuffer.get("y1")
            if usbuffer.get("y1") < min_y:
                min_y = usbuffer.get("y1")
            if usbuffer.get("y0") < min_y:
                min_y = usbuffer.get("y0")
    border_size = 60
    if "border size" in config:
        border_size = config.get("border size")

    max_x = max_x + border_size
    min_x = min_x - border_size

    max_y = max_y + border_size
    min_y = min_y - border_size

    offsets = (min_x, min_y)
    image_size = (max_y - min_y, max_x - min_x)

    return offsets, image_size

def numpy_to_qpixmap(np_image):
    """
    Converts the input numpy array to a qpixmap
    """
    height, width = np_image.shape
    q_image = QImage(np_image, width, height, QImage.Format_Grayscale8)
    return QPixmap.fromImage(q_image)
