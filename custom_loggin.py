import logging
def log(log_file:str):
    """
        Initializes and configures a logger for the current module.

        The logger is set to the DEBUG level. A file handler with DEBUG level is also added to the logger.
        Logs are saved in the './logs/' directory with the filename provided in the 'log_file' parameter.
        Each log message will have the format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'.

        Parameters:
        - log_file (str): Name of the log file (without extension) where log messages will be saved.

        Returns:
        None. The function simply adds the file handler to the logger.
    """
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(f'./logs/{log_file}.log',mode='w')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger