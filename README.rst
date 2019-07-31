SnappySonic
===============================

.. image:: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator
   :alt: Logo

.. image:: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/badges/master/build.svg
   :target: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/pipelines
   :alt: GitLab-CI test status

.. image:: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/badges/master/coverage.svg
    :target: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/scikit-surgery-torso-simulator/badge/?version=latest
    :target: http://scikit-surgery-torso-simulator.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: Stephen Thompson

SnappySonic can be used as an ultrasound acquisition simulator. The output from a tracking system (NDI or AruCo tags) is to select a frame of pre-recorded video to show. A suitable video of ultrasound data is included in the data directory, however the user can select a video of their choosing. 

SnappySonic is part of the `SNAPPY`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

SnappySonic supports Python 3.6.

::
 
    pip install snappysonic
    python snappysonic.py --config config.json

The config file defines the tracking parameters and image buffer, e.g.

::

  {
   "ultrasound buffer": "data/usbuffer.mp4",
	 "buffer descriptions": [
		{
		 "name": "glove",
		 "start frame": 0,
		 "end frame": 284,
		 "x0": 20, "x1": 200,
		 "y0": 200, "y1": 260,
		 "scan direction": "x"
		},
    ]
    ....
    "tracker config": {
		"tracker type": "aruco",
		"video source": 2,
		"debug": true,
		"capture properties": {
			"CAP_PROP_FRAME_WIDTH": 640,
			"CAP_PROP_FRAME_HEIGHT": 480
		
   }
  }

An example configuration file can be downloaded from `here`_ and an image buffer from `source code repository data directory`_

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator


Running tests
^^^^^^^^^^^^^
Unit tests are performed in stand alone environments using tox, which also checks coding style.
::

    tox


Installing
----------

You can pip install from pypi with
::

  pip install snappysonic

or You can pip install directly from the repository as follows:
::

    pip install git+https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2019 University College London.
snappysonic is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator
.. _`here`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/config.json
.. _`source code repository data directory`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/data
.. _`Documentation`: https://scikit-surgerytorsosimulator.readthedocs.io
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY/wikis/home
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/blob/master/CONTRIBUTING.rst
.. _`license file`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerytorsosimulator/blob/master/LICENSE

