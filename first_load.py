import pandas as pd

from snowflake.sqlalchemy import URL

from sqlalchemy import create_engine

import argparse

import logging

import parameters




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

    try:
        logger.info("Creating SQL engine with give Credntials")

        engine = create_engine(URL(user = parameters.get_parameters('user_name'),\
            password = parameters.get_parameters('password'),\
                account = parameters.get_parameters('account_number'),\
                    database = args.database,\
                        schema=args.schema,\
                            role= args.role,\
                                warehouse = args.warehouse))

        logger.debug("Engine Created Sucesfully")
        logger.info("Creating a Connection Object")

        conn = engine.connect()
        one_row = conn.execute("SELECT current_version()").fetchone()

        logger.debug(f"Connection Object Created Succesfully -> {one_row[0]}")
        logger.info("Reading Data")

        df_chunks = pd.read_csv('./data/train_dataset.csv',chunksize=1000)

        logger.debug("Data Loaded into DataFrame")
        logger.info("Loading Data Chunk wise")

        for i,df_chunk in enumerate(df_chunks):

            if i == 0:
                logger.info(f"Creating {args.table} table")
                df_chunk = df_chunk[['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'fasting blood sugar',
                                    'Cholesterol', 'hemoglobin', 'Urine protein', 'serum creatinine',
                                    'smoking']]
                df_chunk.to_sql('smoking',con=conn,index=False,if_exists='replace')
                logger.debug(f"Inserted Chunk{i+1}")

            else:
                df_chunk = df_chunk[['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'fasting blood sugar',
                                    'Cholesterol', 'hemoglobin', 'Urine protein', 'serum creatinine',
                                    'smoking']]
                df_chunk.to_sql(f'{args.table}',con=conn,index=False,if_exists='append')
                logger.debug(f"Inserted Chunk{i+1}")

        logger.debug("All the data Chunks insterted")
        conn.close()
        engine.dispose()

    except Exception as e:
        logger.error(e)
        raise e
       


if __name__=="__main__":

    parser = argparse.ArgumentParser(
                    prog = 'FirstLoad',
                    description = 'Loads the Data from \
                    https://www.kaggle.com/datasets/gauravduttakiit/smoker-status-prediction',
                    epilog = 'For further help go to\
                    https://github.com/sivachandanc/SmokerStatusPrediction')


    parser.add_argument('-d','--database',required=True,help='Snowflake Database')

    parser.add_argument('-s','--schema',required=True,help='Snowflake Schema')

    parser.add_argument('-t','--table',required=True,help='Snowflake target table')

    parser.add_argument('-r','--role',default='accountadmin')

    parser.add_argument('-w','--warehouse',default='compute_wh',help='Snowflake Compute warehouse')

    parser.add_argument('-fp','--filepath',required=True)

    args = parser.parse_args()

    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler('./logs/first_load.log',mode='w')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to fh
    fh.setFormatter(formatter)

    # add fh to logger
    logger.addHandler(fh)
    logger.debug("Invoking ingest_data() function")

    # Calling the Function 
    ingest_data()

