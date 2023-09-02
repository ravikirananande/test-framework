import logging
logging.basicConfig(filename='demologs.log', level=logging.DEBUG, filemode='w',format='	%(asctime)s - %(levelname)s: %(message)s')
# logging.info('This is second statement')
# # logging.warning('This is second statement')
# logging.error('This is second statement')
# logging.warning('This is second statement')
# logging.critical('This is critical')
# logging.warning('This is second statement')
# # logging.debug('oooooooooooooooooooooooooooooo')

class cal:
    def add(self,a,b):
        return a+b

    def mul(self, a, b):
        return a * b

c=cal()
sum=c.add(3,5)
logging.debug(f'debug: Addition of two numbers are {sum}')
logging.info(f'info: Addition of two numbers are {sum}')
logging.warning(f'warning: Addition of two numbers are {sum}')
logging.error(f'error: Addition of two numbers are {sum}')
mul=c.mul(3,8)
logging.error(f'error: Addition of two numbers are {mul}')
logging.critical(f'error: Addition of two numbers are {mul}')
