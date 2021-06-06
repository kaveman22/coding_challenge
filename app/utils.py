import logging
from const import (
    LOG_FORMAT
)

class Logger():
    def __init__(self):
        self.logger = logging.basicConfig(format=LOG_FORMAT, level=logging.INFO,
                            datefmt='%H:%M:%S')