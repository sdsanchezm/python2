import matplotlib.pyplot as plt 
import numpy as np 
period = 80
frec = 1 
Amp = 5
x = np.arange(period)
y = [ Amp*np.sin(2*np.pi*frec* (i/period)) for i in x]
plt.stem(x,y, 'g', )
plt.plot(x,y)
plt.show()