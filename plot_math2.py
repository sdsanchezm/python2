import pylab as pl
import numpy as np

X = np.linspace(0, 2*np.pi, 360, endpoint=True)
Y = np.sin(X)

pl.plot(X,Y)

pl.show()

