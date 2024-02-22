import logging
from logging.config import fileConfig
import colorlog

# fileConfig('backend/logs/dev/logging_dev.ini')
def setup_logging(level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s%(reset)s:%(white)-8s %(message)s%(reset)s %(purple)s[%(name)s] - %(asctime)s ',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

def get_logger(name=None, level=logging.DEBUG):
    if name is None:
        name = __name__
    return setup_logging(level=level).getChild(name)
