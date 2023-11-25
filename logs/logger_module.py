import logging
import os
from datetime import datetime
from datetime import date

class LogGen():
    @staticmethod
    def loggen():
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        path = os.path.abspath(os.curdir) + f'\\automation_{str(today)}_{str(current_time)}.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger