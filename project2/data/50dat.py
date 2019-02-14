import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances
import sys
import numpy as np

df = pd.read_csv('finaltest.csv')
ed = euclidean_distances(df,df)
np.savetxt('test.txt', ed, fmt='%.4f')
with open('test1.txt','w') as out_file:
        with open('finaltest.csv','r') as in_file:
                for line in in_file:
                        out_file.write('['+line.rstrip('\n')+'],'+'\n')
# ed.to_csv('mdstest.csv')