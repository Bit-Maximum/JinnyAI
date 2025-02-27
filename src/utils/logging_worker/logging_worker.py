import os
import pathlib
import logging


def setting_up_logging(log_level=logging.DEBUG, logs_dir=None) -> None:
    """Default logs dir is '<project_root>/logs'"""
    if logs_dir is None:
        logs_dir = (
            pathlib.Path(__file__)
            .parent.parent.parent.parent.resolve()
            .joinpath("logs")
        )

    if not os.path.exists(logs_dir):
        os.mkdir(logs_dir)

    logger = logging.getLogger("discord")
    logger.setLevel(log_level)
    handler = logging.FileHandler(
        filename=pathlib.Path.joinpath(logs_dir, "discord.log"),
        encoding="utf-8",
        mode="w",
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)
