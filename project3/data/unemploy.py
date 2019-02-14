import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
df=pd.read_csv('unemployment.csv');
df=df[df['Month']==12]
df.to_csv('unemployment.csv')