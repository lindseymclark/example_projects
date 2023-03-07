import pandas as pd


class FeatureBuild:
    def __int__(self, name):
        self.name = name

    def build_inital_feature_set(data: pd.DataFrame) -> pd.DataFrame:
        """This function parses the raw data into a subset of indepdendent variables.

        :param data: input data from raw transformed dataset
        :type data: pd.DataFrame
        ...
        :return: dataframe of inital feature set
        :rtype: pd.DataFrame
        """
        dataforregression1 = data.query("Cycle == FailureCycle").reset_index()
        dataforregression1 = dataforregression1[
            [
                "UnitNumber",
                "FailureCycle",
                "SensorMeasurement2",
                "SensorMeasurement3",
                "SensorMeasurement7",
                "SensorMeasurement14",
                "SensorMeasurement16",
            ]
        ]
        tempdata = data.loc[data["Cycle"] == 1]
        tempdata = tempdata[
            [
                "SensorMeasurement2",
                "SensorMeasurement3",
                "SensorMeasurement7",
                "SensorMeasurement14",
                "SensorMeasurement16",
                "FailureCycle",
                "UnitNumber",
            ]
        ]
        dataforregression = tempdata.merge(
            dataforregression1,
            left_on=["FailureCycle", "UnitNumber"],
            right_on=["FailureCycle", "UnitNumber"],
        )
        return dataforregression

    def build_sensor_change(dataforregression: pd.DataFrame) -> pd.DataFrame:
        dataforregression["sensor2"] = (
            dataforregression["SensorMeasurement2_y"]
            - dataforregression["SensorMeasurement2_x"]
        )
        dataforregression["sensor3"] = (
            dataforregression["SensorMeasurement3_y"]
            - dataforregression["SensorMeasurement3_x"]
        )
        dataforregression["sensor7"] = (
            dataforregression["SensorMeasurement7_y"]
            - dataforregression["SensorMeasurement7_x"]
        )
        dataforregression["sensor14"] = (
            dataforregression["SensorMeasurement14_y"]
            - dataforregression["SensorMeasurement14_x"]
        )
        dataforregression["sensor16"] = (
            dataforregression["SensorMeasurement16_y"]
            - dataforregression["SensorMeasurement16_x"]
        )
        dataforregression_final = dataforregression.drop(
            [
                "SensorMeasurement2_x",
                "SensorMeasurement3_x",
                "SensorMeasurement7_x",
                "SensorMeasurement14_x",
                "SensorMeasurement16_x",
                "UnitNumber",
                "SensorMeasurement2_y",
                "SensorMeasurement3_y",
                "SensorMeasurement7_y",
                "SensorMeasurement14_y",
                "SensorMeasurement16_y",
            ],
            axis=1,
        )
        return dataforregression_final
