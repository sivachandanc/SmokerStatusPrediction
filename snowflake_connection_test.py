import pandas as pd
import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import argparse

# Gets the version
def check_coneection():
    engine = create_engine(URL(user = args.user,\
        password = args.password,\
            account = args.account))
    conn = engine.connect()
    try:
        one_row = conn.execute("SELECT current_version()").fetchone()
        print(one_row[0])
        print("Connection Succesfull")
    finally:
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
    check_coneection()