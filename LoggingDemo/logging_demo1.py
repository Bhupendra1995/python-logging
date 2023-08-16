# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# By default the priority is warning
import logging


logging.basicConfig(level=logging.DEBUG, filename="..\logs\demoLogging.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - - %(name)s : %(message)s", datefmt='%d-%b-%y %H:%M:%S')


class DemoLogging:
    def add_numbers(self, a, b):
        return a+b

    def multiply_numbers(self, a, b):
        return a*b


ob = DemoLogging()
sum_result = ob.add_numbers(2,5)
logging.debug("Debug: Addition of numbers {}".format(sum_result))
logging.info("Info: Addition of numbers {}".format(sum_result))
logging.warning("warning: Addition of numbers {}".format(sum_result))
multiply_result = ob.multiply_numbers(2,8)
logging.error("error: Multiply of numbers {}".format(multiply_result))
logging.critical("Critical : Multiply of numbers {}".format(multiply_result))
