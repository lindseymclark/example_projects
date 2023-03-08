import pandas as pd
import statsmodels.api as sm
import pickle

class LinearPredict():
    def __int__(self, name):
        self.name = name
        
    def predict_unseen_data(filename, dataforregression_final: pd.DataFrame):
         """This applies an synthetic minority oversampling technique (SMOTE) for outcomes of low prevelance.

        :param X_train: the independent variables
        :type X_train: pd.DataFrame
        :param y_train: the depdendent variable
        :type y_train: list
        ...
        :return: dataframe of raw data
        :rtype: pd.DataFrame
        """
        X = dataforregression_final[["sensor2", "sensor3", "sensor7", "sensor14", "sensor16"]]
        #print
        X = sm.add_constant(X)
        saved_model = sm.load(filename)
        ypred = saved_model.predict(X) 
        print(ypred)
        