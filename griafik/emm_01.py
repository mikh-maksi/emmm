import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(0, 10, 100)

x1 = []
for i in range(100):
    x1.append(3)
y1 = np.linspace(0, 10, 100)


f1 = 2*x



# вказуємо в аргументі label текст легенди
plt.plot(x, f1, '--y', label='$x_2>2x_1$')

plt.xlabel(r'$x1$', fontsize=16)
plt.ylabel(r'$x2$', fontsize=16)

plt.xlim([0, 2])
plt.ylim([0, 2])

plt.legend(fontsize=14)
plt.grid()
plt.tight_layout()
plt.show()