import pandas as pd
import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import argparse

def ingest_data():
    try:
        print("Connecting")
        engine = create_engine(URL(user = args.user,\
            password = args.password,\
                account = args.account,\
                    database = args.database,\
                        schema=args.schema,\
                            role= args.role,\
                                warehouse = args.warehouse))
        conn = engine.connect()
        one_row = conn.execute("SELECT current_version()").fetchone()
        print(one_row[0])
        print("Connection Succesfull \n")
        print("Inserting Data")
        df_chunks = pd.read_csv('./data/train_dataset.csv',chunksize=1000)
        for i,df_chunk in enumerate(df_chunks):
            if i == 0:
                print(f"Creating {args.table} table")
                df_chunk.to_sql('smoking',con=conn,index=False,if_exists='replace')
                print(f"Inserted Chunk{i+1}")
            else:

                df_chunk.to_sql(f'{args.table}',con=conn,index=False,if_exists='append')
                print(f"Inserted Chunk{i+1}")
    
    except Exception as e:
        raise e
       


if __name__=="__main__":

    parser = argparse.ArgumentParser(
                    prog = 'FirstLoad',
                    description = 'Loads the Data from \
                    https://www.kaggle.com/datasets/gauravduttakiit/smoker-status-prediction',
                    epilog = 'For further help go to\
                    https://github.com/sivachandanc/SmokerStatusPrediction')

    parser.add_argument('-u','--user',required=True,help='User name for your snowflake')
    parser.add_argument('-p','--password',required=True,help='Password for your snowflake account')
    parser.add_argument('-a','--account',required=True,\
        help='account Identifier for you snowflake account')
    parser.add_argument('-d','--database',required=True,help='Snowflake Database')
    parser.add_argument('-s','--schema',required=True,help='Snowflake Schema')
    parser.add_argument('-t','--table',required=True,help='Snowflake target table')
    parser.add_argument('-r','--role',default='accountadmin')
    parser.add_argument('-w','--warehouse',default='compute_wh',help='Snowflake Compute warehouse')
    parser.add_argument('-fp','--filepath',required=True)
    args = parser.parse_args()
    ingest_data()

