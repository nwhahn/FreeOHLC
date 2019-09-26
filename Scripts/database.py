import pymysql
import configparser
import logging
import os
os.path.dirname(os.path.abspath(__file__))

# TODO change this to be compatable with postgres


class DbInfo:
    def __init__(self, database, schema, table):
        self.database = database
        self.schema = schema
        self.table = table


class Database:
    # TODO: fix this config file default it should not be set to prod
    def __init__(self, account, config_file=f'{os.getcwd()}/config/PROD.Database.cfg'):
        config = configparser.ConfigParser()
        config.read(config_file)
        logging.info(config[account])
        self.db_config = config[account]

    def execute(self, sql: str) -> list:
        """This function not good for large queries"""
        logging.info(sql)

        output = None
        config = self.db_config
        connection = pymysql.connect(host=config['HOST'],
                                     user=config['USER'],
                                     password=config['PASSWORD'],
                                     db=config['DATABASE'],
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                output = cursor.fetchall()
            connection.commit()
        except Exception as e:
            logging.error(e)
        finally:
            connection.close()

        return output


def get_default():
    return Database('DATABASE_READER')

