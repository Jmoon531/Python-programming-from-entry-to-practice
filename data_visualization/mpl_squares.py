#!usr/bin/env python
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#plt.plot(x_values, y_values, linewidth=1)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=10)

plt.title('Square Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of value', fontsize=14)

plt.tick_params(axis='both', labelsize=14)


plt.axis([0, 1000, 0, 1000000])
#plt.show()
plt.savefig('square_plot.png', bbox_inches='tight')
