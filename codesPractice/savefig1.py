import matplotlib.pyplot as plt
plt.axis('off')
plt.plot([1,3,1,2,3])
plt.plot([3,1,1,2,1])
plt.savefig("out.svg", transparent = True)