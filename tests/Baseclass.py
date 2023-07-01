import inspect

import pytest
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        # To create logging file
        filehandler = logging.FileHandler("logfile.log")
        logger.addHandler(filehandler)  # filehandler object

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)

        # We can set level here if you want to see perticular logs
        logger.setLevel(logging.DEBUG)

        # logger.debug("write your logs")
        # logger.info("write your logs")
        # logger.warning("write your logs")
        # logger.error("write your logs")
        # logger.critical("write your log")
        return logger


