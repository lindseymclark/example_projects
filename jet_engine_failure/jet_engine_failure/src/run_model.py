import pandas as pd
from data.make_dataset import MakeDataSet
from features.build_features import FeatureBuild

#import and combine intial data
data = MakeDataSet.load_train_data('train_FD001.txt')
data = MakeDataSet.transform_train_data_headers(data)
final_dataset = MakeDataSet.combine_engine_failure_data(data, 'RUL_FD001.txt')

#Build Features
dataforregression1 = FeatureBuild.build_inital_feature_set(final_dataset)
dataforregression_final = FeatureBuild.build_sensor_change(dataforregression1)
print(dataforregression_final)


#Run and Save Model