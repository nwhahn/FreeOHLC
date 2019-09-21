import datetime as dt
import glob
import logging
import os
from argparse import ArgumentParser

import pandas as pd

nasdaq_symbols = 'ftp://ftp.nasdaqtrader.com/symboldirectory/'
arca_location = 'ftp://ftp.nyxdata.com/ARCASymbolMapping/ARCASymbolMapping.txt'
nyse_location = 'ftp://ftp.nyxdata.com/NYSESymbolMapping/NYSESymbolMapping.txt'
nas_ls_location = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt'
nas_tr_location = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt'


def get_version(path: str, file_name: str) -> int:
    files = glob.glob(f'{path}/{file_name}.*')
    logging.info(files)
    if len(files) == 0:
        return 0
    else:
        return max([int(v.split('.')[-1]) for v in files]) + 1


def make_symlink(df: pd.DataFrame, path: str, sym_name: str, sep: str) -> None:
    today = dt.datetime.today().strftime('%Y_%m_%d')
    creation_file = f'{sym_name}_{today}.csv'
    logging.info(f'Generating file with name: {creation_file}')
    version = get_version(path, creation_file)

    true_path = f'{path}/{creation_file}.{version}'
    df.to_csv(true_path, sep=sep)

    symlink_path = f'{path}/{sym_name}.csv'
    if os.path.exists(symlink_path):
        os.unlink(symlink_path)
    os.symlink(true_path, symlink_path)


def arca_nyse_df(sep: str, f_loc: str) -> pd.DataFrame:
    columns = ['Symbol', 'CQS_Symbol', 'SymbolIndexNumber', 'NYSEMarket', 'ListedMarket', 'TickerDesignation', 'UOT',
               'PriceScaleCode', 'NYSE_SystemID', 'BBG_BSID', 'BBG_GlobalID', '_']
    df = pd.read_csv(f_loc, sep=sep, header=None)
    df.columns = columns
    df = df.drop(columns='_')
    return df


def nasdaq_df(sep: str, f_loc: str) -> pd.DataFrame:
    df = pd.read_csv(f_loc, sep=sep)
    df['CQS_Symbol'] = df['CQS Symbol']
    df['CQS_Symbol'] = df['CQS_Symbol'].fillna(df['Symbol'])

    return df


def main_impl(args) -> int:
    if args.arca:
        logging.info('Gathering arca symbols')
        arca_df = arca_nyse_df(args.sep, arca_location)

        logging.info(f'Got dataframe of size: {arca_df.size}')
        make_symlink(arca_df, args.path, 'symbols_arca', args.sep)

    if args.nyse:
        logging.info('Gathering nyse symbols')
        nyse_df = arca_nyse_df(args.sep, nyse_location)

        logging.info(f'Got dataframe of size: {nyse_df.size}')
        make_symlink(nyse_df, args.path, 'symbols_nyse', args.sep)

    if args.nas_tr:
        logging.info('Gathering nasdaq traded symbols')
        nas_tr_df = nasdaq_df(args.sep, nas_tr_location)

        logging.info(f'Got dataframe of size: {nas_tr_df.size}')
        make_symlink(nas_tr_df, args.path, 'symbols_nasdaq_traded', args.sep)

    if args.nas_ls:
        logging.info('Gathering nasdaq listed symbols')
        nas_ls_df = nasdaq_df(args.sep, nas_ls_location)

        logging.info(f'Got dataframe of size: {nas_ls_df.size}')
        make_symlink(nas_ls_df, args.path, 'symbols_nasdaq_listed', args.sep)

    return 0


def main():
    parser = ArgumentParser(description='Script to download refdata files, will maintain symlinks')
    parser.add_argument('--arca', help='arca ftp', action='store_true')
    parser.add_argument('--nyse', help='nyse ftp', action='store_true')
    parser.add_argument('--nas-tr', help='traded ftp', action='store_true')
    parser.add_argument('--nas-ls', help='listed ftp', action='store_true')
    parser.add_argument('--path', help='path to save the file(s) to', required=True)
    parser.add_argument('--sep', import pandas as pd
from argparse import ArgumentParser
import datetime as dt
import os
import glob
import logging
from logger import LoggingEnv

nasdaq_symbols = 'ftp://ftp.nasdaqtrader.com/symboldirectory/'
arca_location = 'ftp://ftp.nyxdata.com/ARCASymbolMapping/ARCASymbolMapping.txt'
nyse_location = 'ftp://ftp.nyxdata.com/NYSESymbolMapping/NYSESymbolMapping.txt'
nas_ls_location = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt'
nas_tr_location = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt'


def get_version(path: str, file_name: str) -> int:
    files = glob.glob(f'{path}/{file_name}.*')
    logging.info(files)
    if len(files) == 0:
        return 0
    else:
        return max([int(v.split('.')[-1]) for v in files]) + 1


def make_symlink(df: pd.DataFrame, path: str, sym_name: str) -> None:
    today = dt.datetime.today().strftime('%Y_%m_%d')
    creation_file = f'{sym_name}_{today}.csv'
    logging.info(f'Generating file with name: {creation_file}')
    version = get_version(path, creation_file)

    true_path = f'{path}/{creation_file}.{version}'
    df.to_csv(true_path)

    symlink_path = f'{path}/{sym_name}.csv'
    if os.path.exists(symlink_path):
        os.unlink(symlink_path)
    os.symlink(true_path, symlink_path)


def arca_nyse_df(sep: str, f_loc: str) -> pd.DataFrame:
    columns = ['Symbol', 'CQS_Symbol', 'SymbolIndexNumber', 'NYSEMarket', 'ListedMarket', 'TickerDesignation', 'UOT',
               'PriceScaleCode', 'NYSE_SystemID', 'BBG_BSID', 'BBG_GlobalID', '_']
    df = pd.read_csv(f_loc, sep=sep, header=None)
    df.columns = columns
    df = df.drop(columns='_')
    return df


def nasdaq_df(sep: str, f_loc: str) -> pd.DataFrame:
    df = pd.read_csv(f_loc, sep=sep)
    df['CQS_Symbol'] = df['CQS Symbol']
    df['CQS_Symbol'] = df['CQS_Symbol'].fillna(df['Symbol'])

    return df


def main_impl(args) -> int:
    if args.arca:
        logging.info('Gathering arca symbols')
        arca_df = arca_nyse_df(args.sep, arca_location)

        logging.info(f'Got dataframe of size: {arca_df.size}')
        make_symlink(arca_df, args.path, 'symbols_arca')

    if args.nyse:
        logging.info('Gathering nyse symbols')
        nyse_df = arca_nyse_df(args.sep, nyse_location)

        logging.info(f'Got dataframe of size: {nyse_df.size}')
        make_symlink(nyse_df, args.path, 'symbols_nyse')

    if args.nas_tr:
        logging.info('Gathering nasdaq traded symbols')
        nas_tr_df = nasdaq_df(args.sep, nas_tr_location)

        logging.info(f'Got dataframe of size: {nas_tr_df.size}')
        make_symlink(nas_tr_df, args.path, 'symbols_nasdaq_traded')

    if args.nas_ls:
        logging.info('Gathering nasdaq listed symbols')
        nas_ls_df = nasdaq_df(args.sep, nas_ls_location)

        logging.info(f'Got dataframe of size: {nas_ls_df.size}')
        make_symlink(nas_ls_df, args.path, 'symbols_nasdaq_listed')

    return 0


def main():
    parser = ArgumentParser(description='Script to download refdata files, will maintain symlinks')
    parser.add_argument('--arca', help='arca ftp', action='store_true')
    parser.add_argument('--nyse', help='nyse ftp', action='store_true')
    parser.add_argument('--nas-tr', help='traded ftp', action='store_true')
    parser.add_argument('--nas-ls', help='listed ftp', action='store_true')
    parser.add_argument('--path', help='path to save the file(s) to', required=True)
    parser.add_argument('--sep', help='nasdaq and nyse both use this', default='|')
    args = parser.parse_args()

    return main_impl(args)


if __name__ == '__main__':
    main()
default='|')
    args = parser.parse_args()

    return main_impl(args)


if __name__ == '__main__':
    main()
