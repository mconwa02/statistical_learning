import numpy as np
import matplotlib.pyplot as plt


def plot_least_squares(df, x, y):
    x = df[x]
    y = df[y]
    m ,c = np.polyfit(x, y, 1)
    plt.plot(x, y, 'o', color='red')
    plt.plot(x, m*x + c)