import pandas as pd
import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import argparse
import logging

# Gets the version
def check_coneection():
    """
    This function checks the connection to the database.
    It prints the current version of the database and
    a message that the connection was succesfull.
    """
    logger.info("Creating Engine")

    engine = create_engine(URL(user = args.user,\
        password = args.password,\
            account = args.account))

    logger.debug("Engine Created Sucessfully")
    logger.info("Creating a Connection Object")
    conn = engine.connect()
    logger.debug("Sucessfully Created a Connection Object")

    try:
        one_row = conn.execute("SELECT current_version()").fetchone()
        logger.info(one_row[0])
        logger.debug("Connection Succesfull")
    finally:
        logger.info("Closing connection")
        conn.close()
        engine.dispose()

if __name__=="__main__":
    
    parser = argparse.ArgumentParser(
                    prog = 'SnowflakeConnectionTest',
                    description = 'Checks wether your snowflake credentials are working',
                    epilog = 'For further help go to\
                    https://github.com/sivachandanc/SmokerStatusPrediction')

    parser.add_argument('-u','--user',required=True,help='User name for your snowflake')
    parser.add_argument('-p','--password',required=True,help='Password for your snowflake account')
    parser.add_argument('-a','--account',required=True,\
        help='account Identifier for you snowflake account')
    args = parser.parse_args()

    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler('Connection_Test.log',mode='w')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to fh
    fh.setFormatter(formatter)

    # add fh to logger
    logger.addHandler(fh)
    logger.debug("Invoking ingest_data() function")

    #Calling the Funtion
    check_coneection()