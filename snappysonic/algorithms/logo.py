"""Functions for snappysonic"""
from math import cos, pi
from numpy import full, int32, uint8
from cv2 import randn, fillConvexPoly, circle

def noisy(image):
    """
    Creates a noise image, based on the dimensions of the
    passed image.
    param: the image to define size and channels of output
    returns: a noisy image
    """
    mean = 0
    stddev = (50, 5, 5)
    randn(image, (mean), (stddev))
    return image


class WeissLogo():
    """Creates a WEISS logo and passes a copy on request"""

    def __init__(self, image_size=331.0):
        """
        Creates a WEISS logo and passes a copy on request
        param: the image size in pixels
        """

        thickness = image_size/8.5

        lblength = image_size/1.4

        sblength = image_size/1.9

        lhlength = image_size/5.5
        shlength = image_size/3.1

        qtr_pi_cos = cos(-pi/4)

        self._background = full((int32(image_size), int32(image_size), 3),
                                [125, 98, 0], dtype=uint8)

        #the ends of each bar, going clockwise from top centre
        end_points = []
        end_points.append(((image_size/2), (image_size-lblength)/2))
        end_points.append((((sblength * qtr_pi_cos + image_size)/2),
                           ((-sblength * qtr_pi_cos + image_size)/2)))
        end_points.append((((image_size+lblength)/2), (image_size/2)))
        end_points.append(((shlength * qtr_pi_cos + image_size/2),
                           (shlength * qtr_pi_cos + image_size/2)))
        end_points.append(((image_size/2), (image_size+lblength)/2))
        end_points.append((((-sblength * qtr_pi_cos + image_size)/2),
                           ((sblength * qtr_pi_cos + image_size)/2)))
        end_points.append((((image_size-lblength)/2), (image_size/2)))
        end_points.append(((-lhlength * qtr_pi_cos + image_size/2),
                           (-lhlength * qtr_pi_cos + image_size/2)))

        vertices = []
        vertices.append((end_points[0][0] - thickness/2, end_points[0][1]))
        vertices.append((end_points[0][0] + thickness/2, end_points[0][1]))
        vertices.append((end_points[4][0] + thickness/2, end_points[4][1]))
        vertices.append((end_points[4][0] - thickness/2, end_points[4][1]))
        fillConvexPoly(self._background, int32(vertices), color=[255, 255, 255])

        vertices = []
        vertices.append(((image_size-lblength)/2,
                         (image_size-thickness)/2))
        vertices.append(((image_size+lblength)/2,
                         (image_size-thickness)/2))
        vertices.append(((image_size+lblength)/2,
                         (image_size+thickness)/2))
        vertices.append(((image_size-lblength)/2,
                         (image_size+thickness)/2))
        fillConvexPoly(self._background, int32(vertices), color=[255, 255, 255])

        vertices = []
        vertices.append((
            (sblength * qtr_pi_cos - thickness * qtr_pi_cos + image_size)/2,
            (-sblength * qtr_pi_cos - thickness * qtr_pi_cos + image_size)/2))
        vertices.append((
            (sblength * qtr_pi_cos + thickness * qtr_pi_cos + image_size)/2,
            (-sblength * qtr_pi_cos + thickness * qtr_pi_cos + image_size)/2))
        vertices.append((
            (-sblength * qtr_pi_cos + thickness * qtr_pi_cos + image_size)/2,
            (sblength * qtr_pi_cos + thickness * qtr_pi_cos + image_size)/2))
        vertices.append((
            (-sblength * qtr_pi_cos - thickness * qtr_pi_cos + image_size)/2,
            (sblength * qtr_pi_cos - thickness * qtr_pi_cos + image_size)/2))
        fillConvexPoly(self._background, int32(vertices), color=[255, 255, 255])

        vertices = []
        vertices.append(
            (-lhlength * qtr_pi_cos + (-thickness * qtr_pi_cos + image_size)/2,
             -lhlength * qtr_pi_cos + (thickness * qtr_pi_cos + image_size)/2))
        vertices.append(
            (-lhlength * qtr_pi_cos + (thickness * qtr_pi_cos + image_size)/2,
             -lhlength * qtr_pi_cos + (-thickness * qtr_pi_cos + image_size)/2))
        vertices.append(
            (shlength * qtr_pi_cos + (thickness * qtr_pi_cos + image_size)/2,
             shlength * qtr_pi_cos + (-thickness * qtr_pi_cos + image_size)/2))
        vertices.append(
            (shlength * qtr_pi_cos + (-thickness * qtr_pi_cos + image_size)/2,
             shlength * qtr_pi_cos + (thickness * qtr_pi_cos + image_size)/2))
        fillConvexPoly(self._background, int32(vertices), color=[255, 255, 255])

        for point in end_points:
            circle(self._background, (int32(point[0]), int32(point[1])),
                   radius=int32(thickness/2 + 1), color=[255, 255, 255],
                   thickness=-1)

    def get_logo(self):
        """
        Returns the WEISS Logo

        :return: The WEISS Logo as a Numpy array
        """
        return self._background

    def get_noisy_logo(self):
        """
        Returns the WEISS Logo with some noise added

        :return: A noisy WEISS Logo as Numpy Array
        """
        noise = noisy(self._background.copy())
        return self._background + noise
