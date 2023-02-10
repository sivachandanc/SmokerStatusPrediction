import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import logging
import parameters

# Gets the version
def check_coneection():
    """
    This function checks the connection to the database.
    It prints the current version of the database and
    a message that the connection was succesfull.
    """
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler('./logs/Connection_Test.log',mode='w')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to fh
    fh.setFormatter(formatter)

    # add fh to logger
    logger.addHandler(fh)

    logger.info("Creating Engine")

    engine = create_engine(URL(user = parameters.get_parameters('user_name'),\
        password = parameters.get_parameters('password'),\
            account = parameters.get_parameters('account_number')))

    logger.debug("Engine Created Sucessfully")
    logger.info("Creating a Connection Object")
    conn = engine.connect()
    logger.debug("Sucessfully Created a Connection Object")

    try:
        one_row = conn.execute("SELECT current_version()").fetchone()
        logger.info(one_row[0])
        logger.debug("Connection Succesfull")
        print("Connection Succesfull")
    finally:
        logger.info("Closing connection")
        conn.close()
        engine.dispose()

if __name__=="__main__":
    #Calling the Funtion
    check_coneection()