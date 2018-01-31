import math
import random
import time

#用遗传算法求函数最大值：
#f(x)=10*sin(5x)+7*cos(4x) x∈[0,10]

variafy_probability = 0.01
mutify_probability = 0.5
best_fit = {'best_fit_gnome': [], 'best_fit_value': None}
gnome_length = 10
gnome_size = 10000
gnome_range = (0, 10)
gnome_list = []
selection_rate_per_ecoph = 0.05
ecoph_number = 500
random.seed(time.time())


def cmp(x, y):
    return result(b2d(x)) < result(b2d(y))


def b2d(gnome):
    number = 0
    for x in gnome:
        number=number * 2 + x
    return number / (2**10 - 1) * 10


def result(value):
    return 10 * math.sin(4 * value) + 7 * math.cos(4 * value)




def init_individual_gnome():
    gnome = []
    for x in range(10):
        gnome.append(random.randint(0, 1))
    return gnome[:]


def init_all_gnome(gnome_list, gnome_size):
    for x in range(gnome_length):
        new_gnome = list(init_individual_gnome())
        gnome_list.append(new_gnome)
    return gnome_list


def nature_selection(gnome_list, selection_rate_per_ecoph):
    gnome_list=sorted(gnome_list,key=lambda x: result(b2d(x)))
    for x in range(int(len(gnome_list) * selection_rate_per_ecoph)):
        del gnome_list[0]


def mutate(gnome_list, variafy_probability):
    for x in range(int(len(gnome_list) * variafy_probability * 10 // 1)):
        gnome_list[random.randrange(0, len(gnome_list) - 1)][random.randrange(
            0, 9)] = 1 - gnome_list[random.randrange(0, len(gnome_list) - 1)][random.randrange(0, 9)]


def mutify(gnome_list, mutify_probability):
    for x in range(int(len(gnome_list) * mutify_probability)):
        gnome_1 = gnome_list[random.randrange(0, len(gnome_list) - 1)]
        gnome_2 = gnome_list[random.randrange(0, len(gnome_list) - 1)]
        temp = gnome_1[:4]
        gnome_1[:4] = gnome_2[:4]
        gnome_2[:4] = temp[:]


if __name__ == '__main__':
    for x in range(ecoph_number):
        init_all_gnome(gnome_list,gnome_size)
        nature_selection(gnome_list, selection_rate_per_ecoph)
        mutate(gnome_list, variafy_probability)
        mutify(gnome_list, mutify_probability)
        gnome_list=sorted(gnome_list,key=lambda x: result(b2d(x)))
        print(gnome_list[-1])

    print('***result***')
    gnome_list=sorted(gnome_list,key=lambda x: result(b2d(x)))
    for x in gnome_list:
        print('x = %d, y = %d ' % (b2d(x), result(b2d(x))),end='\n')
