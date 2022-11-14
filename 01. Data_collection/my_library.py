import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.gridspec as grs
# %matplotlib inline
import seaborn as sns
from datetime import datetime


# plt.rc('font', family='Malgun Gothic')
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
# from IPython.display import Image
import plotly.express as px # ploty
import plotly.graph_objects as go

from tqdm import tqdm
import time

import gc, sys
gc.enable() # 자동 가비지 수거 활성화

# Data 기본 정보 확인

def data_check(df):
    from IPython.core.display import display, HTML
    display(HTML("<style>.container { width:100% !important; }</style>"))
    print( f"◆◆◆ {df.shape}: Total shape ◆◆◆" )
    df_num = df.select_dtypes( include='number', exclude=['cfloat','complex64',"complex128"] )
    if df_num.shape[1] > 0:
        print( f"---{df_num.shape}: Numeric Data: only Real Number ↓↓↓ " + "-"*27 )
        df_info = pd.DataFrame(  [[ i for i in range(df_num.shape[1]) ]], columns=df_num.columns, index=["NO"]  )
        df_info.loc["Column"] = df_num.columns
        df_info.loc["null"] = len(df_num) - df_num.count()
        df_info.loc["null(%)"] = round( 100 * (len(df_num)-df_num.count()) / len(df_num), 1)
        df_info.loc["dtype"] = df_num.dtypes
        df_info.loc["n_uniq"] = df_num.nunique()
        df_info.loc["|"] = "|"
        df_info.loc["Mean"] = df_num.mean()
        df_info.loc["Std"] = df_num.std(ddof=0)
        df_info.loc["|max-min|"] = df_num.max() - df_num.min()
        df_info.loc["│"] = "│"
        df_info.loc["min"] = df_num.min()
        df_info.loc["Q1"] = df_num.quantile(0.25)
        df_info.loc["median"] = df_num.median()   
        df_info.loc["Q3"] = df_num.quantile(0.75)
        df_info.loc["max"] = df_num.max() 
        df_info = df_info.T
        df_info["NO"] = df_info["NO"].astype(int)
        df_info["null"] = df_info["null"].astype(int) 
        for i in range(len(df_info)):
            for j in [2,5,7,8,9]+list(range(11,df_info.shape[1])):
                if df_info.iloc[i,j]==int(df_info.iloc[i,j]):
                    df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,}').split(".")[0] 
                elif abs( df_info.iloc[i,j] ) >= 1000:
                    df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,}').split(".")[0] 
                elif abs( df_info.iloc[i,j] ) >= 100:
                    df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,.1f}').rstrip("0") 
                elif abs( df_info.iloc[i,j] ) >= 10:
                    df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,.2f}').rstrip("0") 
                elif abs( df_info.iloc[i,j] ) >= 1:
                    df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,.3f}').rstrip("0")
                else:
                    df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,.4f}').rstrip("0")
        df_info = df_info.astype(str)
        df_col = pd.DataFrame( [df_info.columns], columns=df_info.columns )
        df_info = pd.concat( [df_col,df_info] )
        df_len = df_info.copy()
        for i in range(len(df_len)):
            for j in range(df_len.shape[1]):
                df_len.iloc[i,j]=len(df_len.iloc[i,j])
        for i in range(len(df_info)):
            for j in range(df_info.shape[1]):
                print(df_info.iloc[i,j].rjust(  df_len.max()[j]  ), end="  ")
            print()
    df_time = df.select_dtypes(include='datetime')
    if df_time.shape[1] > 0:
        print( f"---{df_time.shape}: DateTime Data ↓↓↓ " + "-"*44 )
        df_info = pd.DataFrame(  [[ i for i in range(df_time.shape[1]) ]], columns=df_time.columns, index=["NO"]  )
        df_info.loc["Column"] = df_time.columns  
        df_info.loc["null"] = len(df_time) - df_time.count()
        df_info.loc["null(%)"] = round( 100 * (len(df_time)-df_time.count()) / len(df_time), 1)
        df_info.loc["dtype"] = df_time.dtypes
        df_info.loc["n_uniq"] = df_time.nunique()
        df_info.loc["|"] = "|"
        df_info.loc["min"] = df_time.min()
        df_info.loc["max"] = df_time.max() 
        df_info = df_info.T
        df_info["NO"] = df_info["NO"].astype(int) 
        df_info["null"] = df_info["null"].astype(int)
        for i in range(len(df_info)):
            for j in [2,5]:
                df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,}').split(".")[0]
        df_info = df_info.astype(str)
        df_col = pd.DataFrame( [df_info.columns], columns=df_info.columns )
        df_info = pd.concat( [df_col,df_info] )
        df_len = df_info.copy()
        for i in range(len(df_len)):
            for j in range(df_len.shape[1]):
                df_len.iloc[i,j]=len(df_len.iloc[i,j])
        for i in range(len(df_info)):
            for j in range(df_info.shape[1]):
                print(df_info.iloc[i,j].rjust(  df_len.max()[j]  ), end="  ") 
            print()
    df_obj_1 = df.select_dtypes( exclude=['number','datetime'] )
    df_obj_2 = df.select_dtypes( include=['cfloat','complex64',"complex128"] )
    df_obj = pd.concat( [df_obj_1,df_obj_2], axis=1 )
    if df_obj.shape[1] > 0:
        print( f"---{df_obj.shape}: etc Data: Object, Complex Numbers, ... ↓↓↓ " + "-"*19 )
        df_info = pd.DataFrame(  [[ i for i in range(df_obj.shape[1]) ]], columns=df_obj.columns, index=["NO"]  )
        df_info.loc["Column"] = df_obj.columns 
        df_info.loc["null"] = len(df_obj) - df_obj.count()
        df_info.loc["null(%)"] = round( 100 * (len(df_obj)-df_obj.count()) / len(df_obj), 1)
        df_info.loc["dtype"] = df_obj.dtypes
        df_info.loc["n_uniq"] = df_obj.nunique()
        df_info.loc["|"] = "|"
        freq_list = []
        for i in range(df_obj.shape[1]):
            freq_list.append(  list(df_obj.iloc[:,i].value_counts())[0]  )
        df_info.loc["No1_freq_count"] = freq_list
        df_info.loc["rate(%)"] = [ f"{100*x/len(df_obj):.1f}" for x in freq_list ]
        df_info.loc["value"] = list(  df_obj.mode().iloc[0]  )
        df_info = df_info.T
        df_info["NO"] = df_info["NO"].astype(int) 
        df_info["null"] = df_info["null"].astype(int)
        for i in range(len(df_info)):
            for j in [2,5,7]:
                df_info.iloc[i,j]=str(f'{df_info.iloc[i,j]:,}').split(".")[0]
        df_info = df_info.astype(str)
        df_col = pd.DataFrame( [df_info.columns], columns=df_info.columns )
        df_info = pd.concat( [df_col,df_info] )
        df_len = df_info.copy()
        for i in range(len(df_len)):
            for j in range(df_len.shape[1]):
                df_len.iloc[i,j]=len(df_len.iloc[i,j])
        for i in range(len(df_info)):
            for j in range(df_info.shape[1]):
                if j !=9:
                    print(df_info.iloc[i,j].rjust(  df_len.max()[j]  ), end="  ")
                else:
                    print(df_info.iloc[i,j].ljust(  df_len.max()[j]  ), end="  ")
            print()
    print("-"*78,"\n")