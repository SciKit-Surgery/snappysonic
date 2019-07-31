# coding=utf-8

"""Command line processing"""


import argparse
from snappysonic import __version__
from snappysonic.ui.snappysonic_demo import run_demo


def main(args=None):
    """Entry point for snappysonic application"""

    parser = argparse.ArgumentParser(
        description='snappysonic')

    ## ADD POSITIONAL ARGUMENTS
    parser.add_argument(
        "-c",
        "--config",
        required=True,
        type=str,
        help="A file containing the configuration."
        )


    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='snappysonic version ' +
        friendly_version_string
        )

    args = parser.parse_args(args)

    run_demo(args.config)
