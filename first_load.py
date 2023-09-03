import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from custom_loggin import log
import parameters
import configparser

def ingest_data():
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
    8. table: Snowflake table name
    """

    # Reading the Config File
    config = configparser.ConfigParser()
    config.read('config.ini')
    first_load_log = config['first_load']['first_load_log']
    parameter_user_name = config['parameter_store']['parameter_user_name']
    parameter_snowflake_pass=config['parameter_store']['parameter_snowflake_pass']
    parameter_account_number=config['parameter_store']['parameter_account_number']
    file_to_ingest = config['model']['training_data_location']
    database = config['snowflake']['database']
    schema = config['snowflake']['schema']
    table = config['snowflake']['table']
    role = config['snowflake']['role']
    warehouse = config['snowflake']['warehouse']

    #Creating the Logger
    logger = log(first_load_log)

    try:

        engine = create_engine(URL(user = parameters.get_parameters(parameter_user_name),\
            password = parameters.get_parameters(parameter_snowflake_pass),\
                account = parameters.get_parameters(parameter_account_number),\
                    database = database,\
                        schema=schema,\
                            role= role,\
                                warehouse = warehouse))
        conn = engine.connect()

        
        one_row = conn.execute("SELECT current_version()").fetchone()
        logger.debug(f"Connection Object Created Succesfully -> {one_row[0]}")

        logger.info("Reading Data")
        df_chunks = pd.read_csv(file_to_ingest,chunksize=1000)

        logger.debug("Data Loaded into DataFrame")
        logger.info("Loading Data Chunk wise")


        for i,df_chunk in enumerate(df_chunks):

            if i == 0:
                logger.info(f"Creating {table} table")
                df_chunk = df_chunk[['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'fasting blood sugar',
                                    'Cholesterol', 'hemoglobin', 'Urine protein', 'serum creatinine',
                                    'smoking']]
                # success, nchunks, nrows, _ = write_pandas(conn, df_chunk, 'smoking')
                df_chunk.to_sql(table,con=conn,index=False,if_exists='replace')
                logger.debug(f"Inserted Chunk{i+1}")

            else:
                df_chunk = df_chunk[['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'fasting blood sugar',
                                    'Cholesterol', 'hemoglobin', 'Urine protein', 'serum creatinine',
                                    'smoking']]
                # success, nchunks, nrows, _ = write_pandas(conn, df_chunk, 'smoking')
                df_chunk.to_sql(table,con=conn,index=False,if_exists='append')
                logger.debug(f"Inserted Chunk{i+1}")

        logger.debug("All the data Chunks insterted")

    except Exception as e:
        logger.error(e)
        raise e
    finally:
        conn.close()
        engine.dispose()
       


if __name__=="__main__":

    # Calling the Function 
    ingest_data()

