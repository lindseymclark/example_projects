from imblearn.over_sampling import SMOTE
import statsmodels.api as sm
import pandas as pd


class LinearTrain:
    def __int__(self, name):
        self.name = name

    def apply_smote(X_train: pd.DataFrame, y_train: list):
        """This applies an synthetic minority oversampling technique (SMOTE) for outcomes of low prevelance.

        :param X_train: the independent variables
        :type X_train: pd.DataFrame
        :param y_train: the depdendent variable
        :type y_train: list
        ...
        :return: dataframe of raw data
        :rtype: pd.DataFrame
        """
        os = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=0.3)
        columns = X_train.columns
        os_data_X, os_data_y = os.fit_resample(X_train, y_train)
        os_data_X = pd.DataFrame(data=os_data_X, columns=columns)
        ox_data_y = pd.DataFrame(data=os_data_y, columns=[DepVar])

    def train_ols_model(dataforregression_final: pd.DataFrame) -> object:
        """This applies an an ordinary least squares model to input data.

        :param dataforregression_final: the training dataset
        :type dataforregression_final: pd.DataFrame
        ...
        :return: model object
        :rtype: object
        """
        X = dataforregression_final[
            ["sensor2", "sensor3", "sensor7", "sensor14", "sensor16"]
        ]
        X = sm.add_constant(X)
        y = dataforregression_final[["FailureCycle"]]
        model = sm.OLS(y, X)
        results = model.fit()
        results.save("../models/jet_engine_prediction_model.pkl")
        print(results.summary2())
