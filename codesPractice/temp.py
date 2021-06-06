import pylab as pl
import numpy as np

X = np.linspace(0, 4*np.pi, 360, endpoint=True)
Y = np.sin(X)
Y2 = np.cos(X)

pl.plot(X,Y)
pl.plot(X,Y2)

pl.show()

