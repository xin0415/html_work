import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('finaltest.csv')



df.corr().to_csv('corrtest.csv')
