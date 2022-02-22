SnappySonic
===============================

.. image:: https://github.com/SciKit-Surgery/snappysonic/raw/master/snappysonic.gif
   :height: 134px
   :target: https://github.com/SciKit-Surgery/snappysonic
   :alt: Logo

|

.. image:: https://github.com/SciKit-Surgery/snappysonic/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/SciKit-Surgery/snappysonic/actions
   :alt: GitHub Actions CI status

.. image:: https://coveralls.io/repos/github/SciKit-Surgery/snappysonic/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/SciKit-Surgery/snappysonic?branch=master 
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/snappysonic/badge/?version=latest
    :target: http://snappysonic.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/DOI-10.5334%2Fjors.289-blue
    :target: http://doi.org/10.5334/jors.289
    :alt: The SnappySonic Paper

.. image:: https://api.codeclimate.com/v1/badges/78440062319f61c55177/maintainability
   :target: https://codeclimate.com/github/SciKit-Surgery/snappysonic/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/badge/-Video%20Tutorial-blueviolet?style=flat&logo=youtube
   :target: https://www.youtube.com/watch?v=BI4qyg9NEOk
   :alt: Tutorial on YouTube

.. image:: https://img.shields.io/twitter/follow/scikit_surgery?style=social
   :target: https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw
   :alt: Follow scikit_surgery on twitter


Author: Stephen Thompson

SnappySonic can be used as an ultrasound acquisition simulator. The output from a tracking system (NDI or AruCo tags) is to select a frame of pre-recorded video to show. A suitable video of ultrasound data is included in the data directory, however the user can select a video of their choosing. The software and its use is described in the `SnappySonic paper`_. 

SnappySonic is part of the `SciKit-Surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

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

    git clone https://github.com/SciKit-Surgery/snappysonic


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

    pip install git+https://github.com/SciKit-Surgery/snappysonic

How to Cite
-----------
If you use this software in your research or teaching, please cite:

Thompson, S., Dowrick, T., Xiao, G., Ramalhinho, J., Robu, M., Ahmad, M., Taylor, D. and Clarkson, M.J., 2020. SnappySonic: An Ultrasound Acquisition Replay Simulator. Journal of Open Research Software, 8(1), p.8. DOI: http://doi.org/10.5334/jors.289

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
.. _`source code repository`: https://github.com/SciKit-Surgery/snappysonic
.. _`here`: https://github.com/SciKit-Surgery/snappysonic/config.json
.. _`source code repository data directory`: https://github.com/SciKit-Surgery/snappysonic/data
.. _`Documentation`: https://snappysonic.readthedocs.io
.. _`SciKit-Surgery`: https://github.com/SciKit-Surgery/scikit-surgery
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/SciKit-Surgery/snappysonic/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/SciKit-Surgery/snappysonic/blob/master/LICENSE
.. _`SnappySonic paper`: http://doi.org/10.5334/jors.289
