import pandas as pd
from data.make_dataset import MakeDataSet


#import and combine intial data
data = MakeDataSet.load_train_data('train_FD001.txt')
data = MakeDataSet.transform_train_data_headers(data)
final_dataset = MakeDataSet.combine_engine_failure_data(data, 'RUL_FD001.txt')
print(final_dataset.head(2))