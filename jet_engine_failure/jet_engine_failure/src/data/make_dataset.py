import pandas as pd
import numpy as np

class MakeDataSet:
    def __int__(self, name):
        self.name = name
        
    def load_train_data(file: str) -> pd.DataFrame:
        """This function loads the raw data into a dataframe.
        
        :param file: the file name
        :type file: str
        ...
        :return: dataframe of raw data
        :rtype: pd.DataFrame
        """
        filename = '../data/external/' + file
        data = pd.read_csv(filename, sep=" ", header=None)
        return data
    
    def transform_train_data_headers(data: pd.DataFrame) -> pd.DataFrame:
        """This function loads the raw data into a dataframe.
        
        :param file: the file name
        :type file: str
        ...
        :return: dataframe of raw data
        :rtype: pd.DataFrame
        """
        data = data.rename(columns={0: "UnitNumber", 1: "Cycle", 2: "OperationalSetting1", 
                     3: "OperationalSetting2", 4: "OperationalSetting3", 5: "SensorMeasurement1", 
                     6: "SensorMeasurement2", 7: "SensorMeasurement3", 8: "SensorMeasurement4",
                     9: "SensorMeasurement5", 10: "SensorMeasurement6", 11: "SensorMeasurement7",
                     12: "SensorMeasurement8", 13: "SensorMeasurement9", 14: "SensorMeasurement10",
                     15: "SensorMeasurement11", 16: "SensorMeasurement12", 17: "SensorMeasurement13",
                     18: "SensorMeasurement14", 19: "SensorMeasurement15", 20: "SensorMeasurement15",
                     21: "SensorMeasurement16", 22: "SensorMeasurement17", 23: "SensorMeasurement18",
                     24: "SensorMeasurement19", 25: "SensorMeasurement20"})
        data = data.drop([26, 27], axis=1)
        return data
        
    def combine_engine_failure_data(data: pd.DataFrame, failure_data: str) -> pd.DataFrame:
        """This function loads the outcome data for failure cycle and combines it with the sensor measurements.
        
        :param data: the sensor data 
        :type data: pd.DataFrame
        :param file: the file name and path for jet engine failure cycle
        :type file: str
        ...
        :return: dataframe of the combined raw data
        :rtype: pd.DataFrame
        """
        filename = '../data/external/' + failure_data
        failure_cycle_data = pd.read_csv(filename, sep=" ", header=None)
        failure_cycle_data = failure_cycle_data.drop([1], axis=1)
        failure_cycle_data = failure_cycle_data.rename(columns={0: "FailureCycle"})
        failure_cycle_data.index = np.arange(1, len(failure_cycle_data) + 1)
        failure_cycle_data['Unit'] = failure_cycle_data.index
        failure_cycle_data = failure_cycle_data.reset_index()

        final_dataset = data.merge(failure_cycle_data, left_on='UnitNumber', right_on='Unit')
        final_dataset = final_dataset.drop(['index', 'Unit'], axis=1)
        return final_dataset