import numpy as np
import matplotlib.pyplot as plt

# para la generacion de los numeros aleatorios
np.random.seed(10584216)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(1000)
n, bins, patches = plt.hist(x, 50, normed=2, facecolor='red', alpha=0.75)

#labels de los ejes de la grafica
plt.xlabel('Productos')
plt.ylabel('probabilidad')
plt.title('histograma')
plt.text(60, .025, r'$ \mu = 100, \sigma = 15 $')
plt.axis([60, 160, -0.02, 0.05])
plt.grid(True)
plt.show()