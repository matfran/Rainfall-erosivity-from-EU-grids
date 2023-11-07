# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:25:01 2023

@author: u0133999
"""


import os
import pandas as pd
import geopandas as gpd
from Rfactor_functions import ei30_from_ts

f_dir_in = 'C:/Users/u0133999/OneDrive - KU Leuven/PhD/WaTEM_SEDEM_preprocessing/WS_inputs_EUSEDcollab'
emo5_path = os.path.join(f_dir_in, 'EUSEDcollab_timeseries_pr6.csv')
id_ = str(6)
EnS = 'ATC4'

alpha_p = os.path.join(f_dir_in, 'alpha_params_v2.shp')
beta_p = os.path.join(f_dir_in, 'beta_params_v2.shp')
emo5_pr = pd.read_csv(emo5_path)
emo5_pr.index = pd.to_datetime(pd.to_datetime(emo5_pr['Date'], dayfirst = True, format='%Y-%m-%d %H:%M:%S'))
alpha_m = gpd.read_file(alpha_p)
beta_m = gpd.read_file(beta_p)
station_name = 'Station_Id ' + id_
emo5_pr_st = pd.DataFrame(emo5_pr[station_name])
r_events = ei30_from_ts(emo5_pr_st, EnS, station_name, alpha_m, beta_m, time_resolution = 6)

