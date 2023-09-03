import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import configparser
import parameters
from custom_loggin import log




def inserting_data(df) -> bool:

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
     # Reading the Cofig File
    config = configparser.ConfigParser()
    config.read('config.ini')
    insert_data_log = config['insert_data']['insert_data_log']
    parameter_user_name = config['parameter_store']['parameter_user_name']
    parameter_snowflake_pass=config['parameter_store']['parameter_snowflake_pass']
    parameter_account_number=config['parameter_store']['parameter_account_number']
    database = config['snowflake']['database']
    schema = config['snowflake']['schema']
    table = config['snowflake']['table']
    role = config['snowflake']['role']
    warehouse = config['snowflake']['warehouse']

    # Creating the Logger
    logger = log(insert_data_log)

    try:
        logger.info("Creating SQL engine with give Credntials")

        engine = create_engine(URL(user = parameters.get_parameters(parameter_user_name),\
            password = parameters.get_parameters(parameter_snowflake_pass),\
                account = parameters.get_parameters(parameter_account_number),\
                    database = database,\
                        schema= schema,\
                            role= role,\
                                warehouse = warehouse))

        logger.debug("Engine Created Sucesfully")
        logger.info("Creating a Connection Object")

        conn = engine.connect()
        one_row = conn.execute("SELECT current_version()").fetchone()

        logger.debug(f"Connection Object Created Succesfully -> {one_row[0]}")

        logger.info("Loading Data")

        df.to_sql(table,con=conn,index=False,if_exists='append')


        logger.debug("Data Entry Inserted")
        conn.close() 
        engine.dispose()
        return True

    except Exception as e:
        logger.error(e)
        raise e
       


if __name__=="__main__":

    # Testing
    
    df_series = pd.read_csv('./data/train_dataset.csv').iloc[0][['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'fasting blood sugar',
       'Cholesterol', 'hemoglobin', 'Urine protein', 'serum creatinine',
       'smoking']]
    
    
    df = pd.DataFrame(columns=['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'fasting blood sugar',
       'Cholesterol', 'hemoglobin', 'Urine protein', 'serum creatinine',
       'smoking'])
    df = df.append(df_series,ignore_index = True)

    inserting_data(df)



