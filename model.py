import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from custom_loggin import log
import configparser


def create_model() -> bool:

    """ This function creates a Random Forest Classifier model and saves it as tree_model.joblib
    Args:
        None
    Returns:
        True: If the model is created and saved successfully
        False: If the model is not created and saved successfully
    """
    # Reading the Cofig File
    config = configparser.ConfigParser()
    config.read('config.ini')
    model_taining_log = config['model']['model_training_log']
    model_file_name = config['model']['model_file']
    training_data_location = config['model']['training_data_location']

    # Creating the Logger
    logger = log(model_taining_log)

    try:
        # Loading the data
        logger.debug(f"Loading the CSV file from {training_data_location}")
        df_raw = pd.read_csv(training_data_location)
        df_raw = df_raw[['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'fasting blood sugar',
       'Cholesterol', 'hemoglobin', 'Urine protein', 'serum creatinine',
       'smoking']]
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
        logger.debug("Saving the model")
        joblib.dump(model, model_file_name)
        logger.info(f"Model saved at {model_file_name}")

        return True

    except Exception as e:
        logger.error(e)
        raise e

def load_predict(df:pd.DataFrame) -> int:

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
    # Reading the Cofig File
    config = configparser.ConfigParser()
    config.read('config.ini')
    model_predict_log = config['model']['model_predict_log']
    model_file_name = config['model']['model_file']

    # Creating a Logger
    logger = log(model_predict_log)

    try:
        # Loading the model
        logger.debug("Loading the Model")
        loaded_model = joblib.load(model_file_name)
        logger.info("Model Loaded sucesfully")

        # Prdicting the data
        logger.debug("Doing Prediction")
        prediction = loaded_model.predict(df)
        logger.info("Prediction Done")

        if prediction[0] == 0:
            return 0
        elif prediction[0] == 1:
            return 1
    except Exception as e:
        logger.error(e)
        raise e

if __name__ == "__main__":

    create_model()
