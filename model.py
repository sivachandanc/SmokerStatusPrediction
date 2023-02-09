import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import logging

def create_model() -> bool:

    """ This function creates a Random Forest Classifier model and saves it as tree_model.joblib
    Args:
        None
    Returns:
        True: If the model is created and saved successfully
        False: If the model is not created and saved successfully
    """
    
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler('Model_Creation.log',mode='w')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to fh
    fh.setFormatter(formatter)

    # add fh to logger
    logger.addHandler(fh)
    try:
        # Loading the data
        logger.debug("Loading the CSV file")
        df_raw = pd.read_csv("./data/train_dataset.csv")
        logger.info("Sucessfully loaded the csv file")

        #Loadng the Classifier
        logger.debug("Creating the Random Forest Classifier model")
        model = RandomForestClassifier(n_estimators=100)
        logger.info("Sucesfully created the forest model object")

        # Trianing model
        logger.debug("Training the model")
        model.fit(df_raw.iloc[:,:-1],df_raw['smoking'])
        logger.info("Training Done")

        # Saving the model
        filename = 'tree_model.joblib'
        logger.debug("Saving the model")
        joblib.dump(model, filename)
        logger.info("Model saved as tree_model.joblib")

        return True

    except Exception as e:
        logger.error(e)
        raise e

def load_predict(df:pd.DataFrame) -> bool:

    """        
        Loads the model and predicts the data.
        Parameters
        ----------
        df : pd.DataFrame
            The dataframe to be predicted.
        Returns
        -------
        bool
            True if the prediction is 1 else False.
        Raises
        ------
        Exception
            If any error occurs.
    """


    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler('load_predict.log',mode='w')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to fh
    fh.setFormatter(formatter)

    # add fh to logger
    logger.addHandler(fh)
    try:
        # Laoding the model
        filename = 'tree_model.joblib'
        logger.debug("Loading the Model")
        loaded_model = joblib.load(filename)
        logger.info("Model Loaded sucesfully")

        # Prdicting the data
        logger.debug("Doing Prediction")
        prediction = loaded_model.predict(df)
        logger.info("Prediction Done")

        if prediction[0] == 0:
            return False
        elif prediction[0] == 1:
            return True
    except Exception as e:
        logger.error(e)
        raise e

if __name__ == "__main__":
    pass
    