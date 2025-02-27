import os
import pathlib
import logging


def setting_up_recording(rec_dir=None) -> None:
    """Default rec dir is '<project_root>/recordings'"""
    if rec_dir is None:
        rec_dir = (
            pathlib.Path(__file__)
            .parent.parent.parent.parent.resolve()
            .joinpath("recordings")
        )

    if not os.path.exists(rec_dir):
        os.mkdir(rec_dir)
