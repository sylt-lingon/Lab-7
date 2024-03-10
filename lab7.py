from time import perf_counter
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


L = 1000000

# Task 1

rand_list1 = [random.random() for _ in range(L)]
rand_list2 = [random.random() for _ in range(L)]
rand_list1_np = np.array(rand_list1)
rand_list2_np = np.array(rand_list2)

start_time1 = perf_counter()
list1 = [el1*el2 for el1, el2 in zip(rand_list1, rand_list2)]
end_time1 = perf_counter()
print(f'Время поэлементного перемножения обычных массивов: {end_time1 - start_time1}')

start_time2 = perf_counter()
list2 = np.multiply(rand_list1_np, rand_list2_np)
end_time2 = perf_counter()
print(f'Время перемножения массивов numpy: {end_time2 - start_time2}')
print(f'Перемножение массивов numpy быстрее на {(end_time1 - start_time1) - (end_time2 - start_time2)} секунд')

# Task 2

array = np.genfromtxt('data2.csv', delimiter=',', names=True)
carbs = array['Organic_carbon']

plt.hist(carbs, color='orange', edgecolor='black', bins=18)
plt.title('Histogram')
plt.xlabel('amount of organic carbons')
plt.ylabel('number')
plt.show()

plt.hist(carbs, color='orange', edgecolor='black', bins=18, density=True)
plt.title('Normalized histogram')
plt.xlabel('amount of organic carbons')
plt.ylabel('probability density')
plt.show()

print(f'Среднеквадратичное отклонение: {np.std(carbs)}')

# Task 3

x = np.linspace(-3 * np.pi, 3 * np.pi, 50)
y = np.cos(x)
z = x / np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, marker='x', c='orange')
plt.show()

# Additional task

fig = plt.figure()
l, = plt.plot([], [], 'k')

wr = PillowWriter(fps=40)
plt.xlim(0, 15)
plt.ylim(-3, 3)

xl = []
yl = []

with wr.saving(fig, 'y=sin(x).gif', 100):
    for x in np.linspace(0, 15, 80):
        y = np.sin(x)
        xl.append(x)
        yl.append(y)
        l.set_data(xl, yl)
        wr.grab_frame()
