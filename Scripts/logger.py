import logging
import datetime as dt
import os
import getpass


class LoggingEnv:
    def __init__(self, application: str):
        self.verify_path()
        logging.basicConfig(filename=f'/home/jack/log/{application}_{dt.datetime.now().strftime("%Y-%m-%d_%H_%m_%S")}.log',
                            filemode='w',
                            format='(%(asctime)s) (%(funcName)-8s) [%(levelname)-5s] [%(processName)-8s]: %(message)s',
                            level=logging.INFO)
        logging.info('%%%%%%%%%%%%%%%%%%%%%%%%%')
        logging.info(f'{application}')
        logging.info(f'%%%%%%%%%%%%%%%%%%%%%%%%%')
        logging.info(f'Started at: {dt.datetime.now()}')

    @staticmethod
    def verify_path() -> None:
        user = getpass.getuser()
        log_dir = f'/home/{user}/log'
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)


def main():
    LoggingEnv('TestApplication')

    logging.info('test this shit out')
    logging.warning('How about this')
    logging.error('Jere we go again')


if __name__ == '__main__':
    main()