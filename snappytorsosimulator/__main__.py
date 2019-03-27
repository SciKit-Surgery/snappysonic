#!/usr/bin/python
#  -*- coding: utf-8 -*-
"""snappytorsosimulator"""

import sys

if __name__ == "__main__" and not __package__:
    # To allow the package's main function to be executed without the -m switch,
    # i.e. "python snappytorsosimulator", we have to explicitly set the
    # module name and append the parent directory to the sys.path (see PEP 366)
    from os import path
    __package__ = "snappytorsosimulator"  # pylint: disable=redefined-builtin
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.dirname(path.dirname(__file__)))

# pylint: disable=wrong-import-position
from snappytorsosimulator.ui.snappytorsosimulator_command_line import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
