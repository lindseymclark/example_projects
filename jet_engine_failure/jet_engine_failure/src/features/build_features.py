import pandas as pd

class FeatureBuild:
    def __int__(self, name):
        self.name = name
        
    def test():
        """This function loads the raw data into a dataframe.
        
        :param file: the file name
        :type file: str
        ...
        :return: dataframe of raw data
        :rtype: pd.DataFrame
        """
        dataforreg = data3.query('Cycle == FailureCycle').reset_index()
        dataforreg = dataforreg[['FailureCycle', 'SensorMeasurement2', 'SensorMeasurement3', 
                         'SensorMeasurement7', 'SensorMeasurement14', 'SensorMeasurement16']]
        data5 = data3.loc[data3['Cycle'] == 1]
        data5 = data5[['SensorMeasurement2', 'SensorMeasurement3', 
                         'SensorMeasurement7', 'SensorMeasurement14', 'SensorMeasurement16', 'FailureCycle', 'UnitNumber']]
        result = data5.merge(dataforreg, left_on=['FailureCycle', 'UnitNumber'], right_on=['FailureCycle','UnitNumber'])
        
    def build_sensor_change():
        result['sensor2'] = result['SensorMeasurement2_y'] - result['SensorMeasurement2_x']
        result['sensor3'] = result['SensorMeasurement3_y'] - result['SensorMeasurement3_x']
        result['sensor7'] = result['SensorMeasurement7_y'] - result['SensorMeasurement7_x']
        result['sensor14'] = result['SensorMeasurement14_y'] - result['SensorMeasurement14_x']
        result['sensor16'] = result['SensorMeasurement16_y'] - result['SensorMeasurement16_x']
        result = result.drop(['SensorMeasurement2_x', 'SensorMeasurement3_x', 'SensorMeasurement7_x',
                     'SensorMeasurement14_x', 'SensorMeasurement16_x', 'UnitNumber', 
                      'SensorMeasurement2_y', 'SensorMeasurement3_y', 'SensorMeasurement7_y', 
                      'SensorMeasurement14_y', 'SensorMeasurement16_y'], axis=1)




    