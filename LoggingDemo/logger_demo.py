import logging


class LoggerDemo:
    def logger_demo(self):
        # create logger
        logger = logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.DEBUG)

        # Create console handler or file handler and set the log level
        ch = logging.StreamHandler()
        fh = logging.FileHandler("demologfile.log")

        # create formatter - how wants you wants your logs to be formatted
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s : %(message)s")
        formatter1 = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s : %(message)s", datefmt='%d-%b-%y %H:%M:%S')

        # add formatter to the console or file handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)

        # add console handler to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        # application code log msgs
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')


obj = LoggerDemo()
obj.logger_demo()