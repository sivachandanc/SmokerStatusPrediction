import pandas as pd

import snowflake.connector

from snowflake.sqlalchemy import URL

from sqlalchemy import create_engine

import logging

import os




def inserting_data(df):

    """
    This function is used to ingest data into snowflake.
    It uses the following command line arguments:
    1. user: Snowflake user name
    2. password: Snowflake password
    3. account: Snowflake account name
    4. database: Snowflake database name
    5. schema: Snowflake schema name
    6. role: Snowflake role name
    7. warehouse: Snowflake warehouse name
    """    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler('first_load.log',mode='w')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to fh
    fh.setFormatter(formatter)

    # add fh to logger
    logger.addHandler(fh)
    logger.debug("Invoking ingest_data() function")

    try:
        logger.info("Creating SQL engine with give Credntials")

        engine = create_engine(URL(user = os.getenv('SNOWFLAKE_PASSWORD'),\
            password = os.getenv('SNOWFLAKE_PASSWORD'),\
                account = os.getenv('SNOWFLAKE_ACCOUNT'),\
                    database = os.getenv('SNOWFLAKE_DATABASE'),\
                        schema= os.getenv('SNOWFLAKE_SCHEMA'),\
                            role= os.getenv('SNOWFLAKE_ROLE'),\
                                warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')))

        logger.debug("Engine Created Sucesfully")
        logger.info("Creating a Connection Object")

        conn = engine.connect()
        one_row = conn.execute("SELECT current_version()").fetchone()

        logger.debug(f"Connection Object Created Succesfully -> {one_row[0]}")

        logger.info("Loading Data Chunk wise")

        df.to_sql('smoking',con=conn,index=False,if_exists='append')


        logger.debug("Data Entry Inserted")
        conn.close() 
        engine.dispose()

    except Exception as e:
        logger.error(e)
        raise e
       


if __name__=="__main__":
    pass

