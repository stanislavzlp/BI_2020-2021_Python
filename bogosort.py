from random import shuffle, randint
import numpy as np
import time
import matplotlib.pyplot as plt


def is_sorted(list_to_chek):
    for i in range(len(list_to_chek) - 1):
        if list_to_chek[i] > list_to_chek[i + 1]:
            return False
    return True


def create_list(size=10, max=50):
    return [randint(0, max) for i in range(size)]


def bogo_sort(list_for_bogo):
    start_time = time.time()
    while not is_sorted(list_for_bogo):
        shuffle(list_for_bogo)
    finish_time = time.time()
    bogo_time = finish_time - start_time

    return bogo_time


quantity_of_repeats = 10
max_len_to_sort = 7
std_all = []
mean_all = []
for i in range(2, max_len_to_sort + 1):
    time_list = []
    for j in range(quantity_of_repeats + 1):
        bogobogo_list = create_list(i)
        execution_time = bogo_sort(bogobogo_list)
        time_list.append(execution_time)
    std = np.std(time_list)
    mean = np.mean(time_list)
    mean_all.append(mean)
    std_all.append(std)

x = list(range(2, max_len_to_sort + 1))
plt.errorbar(x, mean_all, yerr=std_all, fmt='.k')
plt.show()
