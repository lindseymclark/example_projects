import pandas as pd
import statsmodels.api as sm
import pickle

class LinearPredict():
    def __int__(self, name):
        self.name = name
        
    def predict_unseen_data(filename, dataforregression_final: pd.DataFrame):
        """This applies an synthetic minority oversampling technique (SMOTE) for outcomes of low prevelance.

        :param filename: the pickled model
        :type filename: object
        :param dataforregression_final: the unseen data
        :type dataforregression_final: pd.DataFrame
        ...
        :return: dataframe of predicted data
        :rtype: pd.DataFrame
        """
        X = dataforregression_final[["sensor2", "sensor3", "sensor7", "sensor14", "sensor16"]]
        X = sm.add_constant(X)
        saved_model = sm.load(filename)
        ypred = saved_model.predict(X) 
        print(ypred)
        