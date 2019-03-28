from sksurgerynditracker.nditracker import NDITracker
from sksurgeryarucotracker.arucotracker import ArUcoTracker
from cv2 import randn


def configure_tracker (config):
    """
    Configures a scikit-surgery tracker based on the passed config
    param: a tracker configuration dictionary
    returns: The tracker
    """

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


def lookupimage (usbuffer, pt):
    """
    determines whether a coordinate (pt) lies with an area defined by
    a usbuffer, and returns an image from the buffer if appropriate
    param: usbuffer, a dictionary containing bounding box information (x0,y0,
    x1,y1) and image data
    returns: True if point in bounding box. Image.
    """
    if pt[0] > usbuffer.get("x0"):
        if pt[0] < usbuffer.get("x1"):
            if pt[1] > usbuffer.get("y0"):
                if pt[1] < usbuffer.get("y1"):
                    #do it by x, as in general we have more pixels that way
                    pdiff=0
                    if usbuffer.get("scan direction") == "x":
                        diff=pt[0] - usbuffer.get("x0")
                        pdiff = int(diff / (usbuffer.get("x1") - usbuffer.get("x0")) * len(usbuffer.get("buffer")))
                    else:
                        diff=pt[1] - usbuffer.get("y0")
                        pdiff = int(diff / (usbuffer.get("y1") - usbuffer.get("y0")) * len(usbuffer.get("buffer")))

                    return True, usbuffer.get("buffer")[pdiff]

    return False, None


def noisy(image):
    """
    Creates a noise image, based on the dimensions of the 
    passed image.
    param: the image to define size and channels of output
    returns: a noisy image
    """
    row,col,ch= image.shape
    mean = 0
    stddev = (50,5,5)
    randn(image,(mean),(stddev))
    return image


def check_us_buffer(usbuffer):
    """
    Checks that all ultrasound buffer contains all required key values.
    :param the buffer to check
    :raises Exception: KeyError, ValueError
    """
    if "name" not in usbuffer:
         raise KeyError ("Buffer configuration must contain a name.")
    if "start frame" not in usbuffer:
         raise KeyError ("Buffer configuration must contain a start frame.")
    if "end frame" not in usbuffer:
         raise KeyError ("Buffer configuration must contain an end frame.")
    if "x0" not in usbuffer:
         raise KeyError ("Buffer configuration must contain x0")
    if "x1" not in usbuffer:
         raise KeyError ("Buffer configuration must contain x1")
    if "y0" not in usbuffer:
         raise KeyError ("Buffer configuration must contain y0")
    if "y1" not in usbuffer:
         raise KeyError ("Buffer configuration must contain y1")
    if "scan direction" not in usbuffer:
         raise KeyError ("Buffer configuration must contain a scan direction.")
    else:
         direction = usbuffer.get("scan direction")
         if direction not in ("x","y"):
             raise ValueError ("scan direction must be either x or y")
