import pandas as pd
import numpy as np

from visualization import *
import seaborn as sns

PATH = 'figures/'
penguins = sns.load_dataset('penguins')
show_countplot(penguins, path=PATH)
show_corr_heatmap(penguins, title='corr_penguins', path=PATH + 'penguines_')

planets = sns.load_dataset('planets')
show_countplot(planets, path=PATH)
show_corr_heatmap(planets, path=PATH + 'planets_')

car_crashes = sns.load_dataset('car_crashes')
show_countplot(car_crashes, path=PATH)
show_corr_heatmap(car_crashes, path=PATH + 'car_crashes_')

df1 = pd.DataFrame({
    'c1': np.random.randn(100),
    'c2': np.random.randn(100),
    'c3': np.random.randn(100),
    'c4': np.random.randn(100),
    'c5': np.random.randn(100),
    })


df2 = pd.DataFrame({
    'c1': np.random.randn(100),
    'c2': np.random.randn(100),
    'c5': np.random.randn(100),
    'c6': np.random.randn(100),
    })

show_distplot(train=df1, test=df2, path=PATH + 'dist_graph')
