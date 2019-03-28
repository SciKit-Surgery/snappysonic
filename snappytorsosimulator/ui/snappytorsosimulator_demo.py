# coding=utf-8


"""Hello world demo module"""
from PySide2.QtWidgets import QApplication
from snappytorsosimulator.overlay_widget.overlay import OverlayApp

def run_demo(configfile):
    """ Run the application """
    app = QApplication([])

    configuration = { "ultrasound buffer" : "data/usbuffer.mp4",
                      "default image"     : "data/logo.png",
                      "buffer descriptions" : (
                                               {
                                                "name" : "glove",
                                                "start frame" : 0,
                                                "end frame" : 284,
                                                "x0" : 20 , "x1" : 200,
                                                "y0" : 20 , "y1" : 160,
                                                "scan direction" : "x"
                                               },
                                               {
                                                "name" : "caterpillar",
                                                "start frame" : 285,
                                                "end frame" : 560,
                                                "x0" : 220 , "x1" : 460,
                                                "y0" : 20 , "y1" : 160,
                                                "scan direction" : "x"
                                               },
                                               {
                                                "name" : "unknown",
                                                "start frame" : 561,
                                                "end frame" : 816,
                                                "x0" : 20 , "x1" : 200,
                                                "y0" : 200 , "y1" : 360,
                                                "scan direction" : "x"
                                               },
                                               {
                                                "name" : "orange",
                                                "start frame" : 817,
                                                "end frame" : 1060,
                                                "x0" : 220 , "x1" : 460,
                                                "y0" : 200 , "y1" : 360,
                                                "scan direction" : "y"
                                               }
                                              ),
                        "tracker config" :
                        {
                            "tracker type" : "aruco",
                            "video source" : 2,
                           # "video source" : 0,
                            "debug" : True,
                            "capture properties" :
                            {
                                "CAP_PROP_FRAME_WIDTH" : 640 ,
                                "CAP_PROP_FRAME_HEIGHT" : 480
                            }

                        }

                    }

    viewer = OverlayApp(configuration)

    #model_dir = '../models'
    #viewer.add_vtk_models_from_dir(model_dir)

    viewer.start()

   #start the application
    exit(app.exec_())


