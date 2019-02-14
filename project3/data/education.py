import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
df=pd.read_csv('education.csv');
df = df.drop(['Rank','Rank.1','Rank.2'], axis=1)
# df=df[df['Rank']==12]
df.to_csv('education.csv')