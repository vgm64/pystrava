import pandas as pd
import os
#from collections import Counter


def load_StravaSampleI(data_path):
  files = [data_path + f for f in os.listdir(data_path)]
  total_data = [pd.read_json(f, convert_dates=['start_date_local']) for f in files]
  for i, df in enumerate(total_data):
    filename = os.path.basename(files[i])
    df['uid'] = int(filename.split(".")[0])
  strava = pd.concat(total_data)
  return strava

def pkl_StravaSampleI(data, data_path):
  import cPickle as pickle
  pickle.dump(data, data_path)

#def load_strava(data_path):

def load_demographics(data_path):
  df = pd.read_csv(data_path)
  df['uid'] = range(len(df))
  return df

def load_efforts(data_path):
  files = [data_path + f for f in os.listdir(data_path)]
  total_data = [pd.read_json(open(f)) for f in files]
  for i, df in enumerate(total_data):
    filename = os.path.basename(files[i])
    df['uid'] = int(filename.split(".")[1])
  efforts = pd.concat(total_data)
  return efforts

def load_streams(data_path):
  pass
  
