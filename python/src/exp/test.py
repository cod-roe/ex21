#%% aaa
print('hello')
a = 1

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib
sns.set(font='IPAexGothic')
# %matplotlib inline
import ydata_profiling as pdp


# %%
import os
os.getcwd()
# %%
df_train = pd.read_csv('train.csv')


# %%
df_train.describe().T

# %%
df_train.info()
# %%
df_train.head()
# %%


# %%
sns.countplot(data=df_train, x='Sex', hue='Survived')

# %%
print(plt.rcParams['font.family'])

# %%