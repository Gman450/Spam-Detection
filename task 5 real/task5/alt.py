import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from numpy import loadtxt
from pylab import show

data = loadtxt('dataset.txt', delimiter=',')
X = data[:, 0:2]
y = data[:, 2]

clf = LogisticRegression().fit(X[:], y[:])

xx, yy = np.mgrid[0:9000:50, 0:9000:50]
print xx
print yy
grid = np.c_[xx.ravel(), yy.ravel()]
probs = clf.predict_proba(grid)[:, 1].reshape(xx.shape)

f, ax = plt.subplots(figsize=(12, 8))
ax.contour(xx, yy, probs, levels=[.4], cmap="Greys", vmin=0, vmax=.6)

ax.scatter(X[:,0], X[:, 1], c=y[:], s=50,
           cmap="RdBu", vmin=-.2, vmax=1.2,
           edgecolor="white", linewidth=1)

ax.set(aspect="equal",
       #xlim=(-5, 5), ylim=(-5, 5),
       xlabel="Total word count", ylabel="Spam word count")
show()

