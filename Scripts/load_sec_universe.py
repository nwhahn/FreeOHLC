import pandas as pd
from argparse import ArgumentParser
import logger

app = 'load_sec_universe'
logger = logger.get_logger(__name__, app)




def main():
    parser = ArgumentParser(description="This script will read in the files and "
                                        "append them 'correctly' to the database")
    parser.add_argument('--database', help='database account to use', default='DATABASE_INSERTER')
    parser.add_argument('--path', help='path to all the csv files', default='/tmp')
    args = parser.parse_args()

    logger.info("hey")


if __name__ == '__main__':
    main()
