import boto3
import argparse
import configparser
from custom_loggin import log

def putting_snowflake_creds(user_name: str, 
                            password: str, 
                            account_number: str) -> None:
    
    """
        This function is used to store the Snowflake User Name, Password and Account Identifier in the AWS Parameter Store.

        Parameters
        ----------
        user_name : str
            Snowflake User Name
        password : str
            Snowflake User Password
        account_number : str
            Snowflake Account Identifier

        Returns
        -------
        None

        Raises
        ------
        Exception
            If any error occurs while storing the Snowflake User Name, Password and Account Identifier in the AWS Parameter Store.
    """

    # Reading the Config File
    config = configparser.ConfigParser()
    config.read('config.ini')
    parameter_store_log = config['parameter_store']['parameter_store_log']
    parameter_user_name = config['parameter_store']['parameter_user_name']
    parameter_snowflake_pass = config['parameter_store']['parameter_snowflake_pass']
    parameter_account_number = config['parameter_store']['parameter_account_number']
    aws_region = config['aws']['aws_region']

    # Create logger
    logger = log(parameter_store_log)

    try:
        logger.debug("Creating Boto3 client")
        session = boto3.session.Session(region_name=aws_region)
        ssm = session.client("ssm")
        logger.info("Completed connecting the client")


        # Storing the User name in Parameter Store
        logger.debug("Storing the User name in Parameter Store")
        response_username = ssm.put_parameter(
            Name=parameter_user_name,
            Description="This is Snowflake User name stored in Parameter Store",
            Value=user_name,
            Type="String",
            Overwrite=True
        )
        logger.info("Succesfully Stored the user name")

        # Storing Snowflake User Password in the Parameter Store
        logger.debug("Storing the Snowflake Password")
        response_password = ssm.put_parameter(
            Name=parameter_snowflake_pass,
            Description="This Snowflake user password stored in Parameter Store",
            Value=password,
            Type="String",
            Overwrite=True
        )
        logger.info("Completed Storing the User Password")

        # Storing the account_identifier in the Parameter Store
        logger.debug("Storing the Snowflake Account Identifier")
        response_account_number = ssm.put_parameter(
            Name=parameter_account_number,
            Description="This is Account Identifier Parameter Store",
            Value=account_number,
            Type="String",
            Overwrite=True
        )
        logger.info("Sucesfully Stored the Account Identifier")

        logger.info(f"Successfully stored Snowflake User Name:{response_username}")

        logger.info(f"Successfully stored Snowflake Password: {response_password}")

        logger.info(f"Successfully stored Snowflake Account_identifier: {response_account_number}")

    except Exception as e:
        logger.error(e)
        raise e

def get_parameters(paramter_name: str)-> str:

    """
    This function is used to get the parameters from AWS Parameter Store.

    It takes the parameter name as input and returns the parameter value.
    It uses the boto3 client to connect to AWS Parameter Store.
    It uses the get_parameter method to get the parameter value.
    It returns the parameter value.
    
    """
    
    # Reading the Config File
    config = configparser.ConfigParser()
    config.read('config.ini')
    parameter_getting_log = config['parameter_store']['parameter_getting_log']
    aws_region = config['aws']['aws_region']

    # create logger
    logger = log(parameter_getting_log)

    try:
        session = boto3.session.Session(region_name=aws_region)
        # Create a boto3 client for AWS Systems Manager Parameter Store
        logger.debug("Creating Boto3 client")
        ssm = session.client("ssm")
        logger.info("Completed connecting the client")

        # Retrieve the parameter from Parameter Store
        logger.debug(f"Getting the {paramter_name}")
        response = ssm.get_parameter(
            Name=paramter_name,
            WithDecryption=False
        )
        logger.info(f"Got the {paramter_name}")

        logger.debug("Extracting the Parameter value")
        # Extract the value of the parameter
        param_value = response["Parameter"]["Value"]

        logger.info("Succesfully retrieved the Parameter value")
        return param_value
    
    except Exception as e:
        logger.error(e)
        raise e




if __name__ == "__main__":

    # For Testing
    
    parser = argparse.ArgumentParser(
                    prog = 'Paramter Store',
                    description = 'Stores and retrieves Credentials from Parameter Store',
                    epilog = 'For further help go to\
                    https://github.com/sivachandanc/SmokerStatusPrediction')

    parser.add_argument('-u','--user',required=False,help='User name for your snowflake')
    
    parser.add_argument('-p','--password',required=False,help='Password for your snowflake account')

    parser.add_argument('-a','--account',required=False,\
        help='account Identifier for you snowflake account')
    
    args = parser.parse_args()

    if args.user is not None:
    # Calling the Function 
        putting_snowflake_creds(args.user, args.password, args.account)
    print(get_parameters('user_name'))