import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed
np.random.seed(42)

TRAIN_CSV = '/kaggle/input/random-linear-regression/train.csv'
TEST_CSV = '/kaggle/input/random-linear-regression/test.csv'

# Load csv files and drop rows with nan values
train_df = pd.read_csv(TRAIN_CSV).dropna(axis=0)
test_df = pd.read_csv(TEST_CSV).dropna(axis=0)

# View train data information
train_df.info()
