import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x tenhleg')
plt.ylabel('y tenhleg')
plt.title('Amaraas graph')
plt.legend(['sinus', 'cosinus'])
#plt.show()
print(str(plt.show()))