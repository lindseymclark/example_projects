import pandas as pd
import logging
from data.make_dataset import MakeDataSet
from features.build_features import FeatureBuild
from models.train_model import LinearTrain
from models.predict_model import LinearPredict

#set up log
logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', \
                    level=logging.INFO, filename='linear_log.log')

#import and combine intial data
data = MakeDataSet.load_train_data('train_FD001.txt')
data = MakeDataSet.transform_train_data_headers(data)
final_dataset = MakeDataSet.combine_engine_failure_data(data, 'RUL_FD001.txt')
logging.info("The number of rows processed is %s", len(data))

#Build Features
dataforregression1 = FeatureBuild.build_inital_feature_set(final_dataset)
dataforregression_final = FeatureBuild.build_sensor_change(dataforregression1)
print(dataforregression_final)

#Train and Save Model
LinearTrain.train_ols_model(dataforregression_final)

#Run Model
LinearPredict.predict_unseen_data('../models/jet_engine_prediction_model.pkl', dataforregression_final)
