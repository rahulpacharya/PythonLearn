# -*- coding: utf-8 -*-

import pandas as pd
import csv
import Constants

data_file_path = Constants.DATA_PATH+'/dataset.csv'

#Data Loading
messages = [line.rstrip() for line in open(data_file_path)]
print(len(messages))
# Our data has two columns without headers and 5574 data rows
# lets add column headers now
#Appending column headers
messages = pd.read_csv(data_file_path, sep='\t', quoting=csv.QUOTE_NONE,names=["label", "message"])
