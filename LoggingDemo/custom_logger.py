import inspect
import logging

class CustomLogger:
    def cust_logger(self, log_level=logging.DEBUG):
        # Set class/Method Name from where its called
        logger_name = inspect.stack()[1][3]

        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        # Create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")

        # create formatter - how wants you wants your logs to be formatted
        formatter1 = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s : %(message)s", datefmt='%d-%b-%y %H:%M:%S')

        # add formatter to the console or file handler
        fh.setFormatter(formatter1)

        # add console handler to logger
        logger.addHandler(fh)
        return logger


obj = CustomLogger()
obj.cust_logger()
