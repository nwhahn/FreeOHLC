import pandas as pd
from argparse import ArgumentParser
import logger
from database import Database, DbInfo

__app__ = 'load_sec_universe'
logger = logger.get_logger(__name__, __app__)


def get_symbols(db_info: DbInfo) -> pd.DataFrame:
    query = f"SELECT SYMBOLNYSE, NASDAQSYMBOL, CQSSYMBOL FROM {db_info.schema}.{db_info.table}"
    return db_info.database.get_df(query)


def merge_nyse_arca_rames(path: str) -> tuple:
    arca_df = pd.read_csv(f'{path}/symbols_arca.csv')
    nyse_df = pd.read_csv(f'{path}/symbols_nyse.csv')
    nas_lis = pd.read_csv(f'{path}/symbols_nasdaq_listed.csv')
    nas_trd = pd.read_csv(f'{path}/symbols_nasdaq_traded.csv')

    return nyse_df, arca_df, nas_lis, nas_trd


def main_impl(args):
    db_info = DbInfo(Database(args.database), args.schema, args.table)

    sym_df = get_symbols(db_info)

     



def main():
    parser = ArgumentParser(description="This script will read in the files and "
                                        "append them 'correctly' to the database")
    parser.add_argument('--database', help='database account to use', default='DATABASE_INSERTER')
    parser.add_argument('--schema', help='Schema where the securities are', default='FREEOHLC')
    parser.add_argument('--table', help='name of the table', default='SECURITY')
    parser.add_argument('--path', help='path to all the csv files', default='/tmp')
    args = parser.parse_args()




if __name__ == '__main__':
    main()
