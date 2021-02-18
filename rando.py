import numpy as np
import random as random
import time
import matplotlib.pyplot as plt

# Количество чисел для генерации
qty = 500

random_execution_time = []
for number in range(qty):
    start_time_random = time.time()
    random_list = [random.gauss(0, 1) for i in range(number)]
    end_time_random = time.time()
    execution_time_random = end_time_random - start_time_random
    random_execution_time.append(execution_time_random)

np_execution_time = []
for number in range(qty):
    start_time_np = time.time()
    s = np.random.normal(0, 1, number)
    end_time_np = time.time()
    execution_time_np = end_time_np - start_time_np
    np_execution_time.append(execution_time_np)

x = list(range(1, qty + 1))

plt.grid = True
plt.plot(x, random_execution_time, label="random")
plt.plot(x, np_execution_time, label="numpy")
plt.xlabel("Количество всевдорандомных чисел")
plt.ylabel("Время исполнения")
plt.legend()
plt.show()
