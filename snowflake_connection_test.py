import pandas as pd
import snowflake.connector
from custom_loggin import log
import configparser
import parameters

# Gets the version
def check_conection():
    """
    This function checks the connection to the database.
    It prints the current version of the database and
    a message that the connection was succesfull.
    """
    # create logger
    config = configparser.ConfigParser()
    config.read('config.ini')
    snowflake_connection_test_log = config['snowflake_connection_test']\
                                            ['snowflake_connection_test_log']
    parameter_user_name = config['parameter_store']['parameter_user_name']
    parameter_snowflake_pass=config['parameter_store']['parameter_snowflake_pass']
    parameter_account_number=config['parameter_store']['parameter_account_number']
    logger = log(snowflake_connection_test_log)

    logger.info("Creating Connection object")
    con = snowflake.connector.connect(
    user=parameters.get_parameters(parameter_user_name),
    password=parameters.get_parameters(parameter_snowflake_pass),
    account=parameters.get_parameters(parameter_account_number),
    session_parameters={
        'QUERY_TAG': 'CheckingSnowFlakeConnection',
    }
)
    logger.debug("Sucessfully Created a Connection Object")

    try:
        one_row = con.cursor().execute("SELECT current_version()").fetchone()
        logger.info(one_row[0])
        logger.debug("Connection Succesfull")
        logger.info("Connection Succesfull")
    finally:
        logger.info("Closing connection")
        con.close()

if __name__=="__main__":
    #Calling the Funtion
    check_conection()