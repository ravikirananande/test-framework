import logging

class LoggerDemo:
    def sample_logger(self):
        #create logger
        logger=logging.getLogger("demolog1")
        logger.setLevel(logging.DEBUG)

        #Create Console Handler or File Handler and set Log level
        ch=logging.StreamHandler()

        #create formatter
        formatter=logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

        #add formatter to console or file handler
        ch.setFormatter(formatter)

        #Add console handler to logger
        logger.addHandler(ch)

        #Application Code
        logger.warning('This is second statement')
        logger.error('This is second statement')
        logger.warning('This is second statement')
        logger.critical('This is critical')
        logger.warning('This is second statement')

l=LoggerDemo()
l.sample_logger()