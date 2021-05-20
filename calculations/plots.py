import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import tikzplotlib

# x_data = [(i+1)*100 for i in range(5)]
# print(x_data)
# y_data = [26.865, 15.819, 11.841, 9.657, 8.183]


# def func(x, a, b, c):
#     return a/(x+b) + c


# x_range = np.linspace(100, 500, 1000)


# popt, pcov = curve_fit(func, x_data, y_data)
# plt.plot(x_range, func(x_range, *popt), 'g',
#          label='$y = \\frac{%5.3f}{x+%5.3f} + %5.3f$' % tuple(popt))
# plt.plot(x_data, y_data, 'ro',
#          label='data')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()
def inv_r_squared(x, a, b, c):
    return a / (x+b) ** 2+c


def create_table(x, y):
    result = []
    for xi, yi, i in zip(x, y, range(len(x))):
        s = "${}$ & ${}$ & ${:.2e}$ \\\\ \\hline".format(i+1, xi, yi)
        result.append(s)
    print("\n".join(result))


def plot_distance(x, y):
    x_range = np.linspace(.1,2000, 100)
    popt, pcov = curve_fit(inv_r_squared, x, y)
    # print(popt)
    fig, ax = plt.subplots()
    # \frac{0.615}{(x+1.639) ^ 2} - 2.049\cdot10 ^ {-4}

    ax.grid(True, which='both')
    plt.rc("font", size=22)
    plt.rc('axes', titlesize=22)     # fontsize of the axes title
    plt.rc('axes', labelsize=22)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=22)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=22)    # fontsize of the tick labels
    plt.rc('legend', fontsize=22)    # legend fontsize
    plt.rc('figure', titlesize=22)  
    plt.plot(x_range, inv_r_squared(x_range, *popt), "g--")
    plt.plot(x, y, ".")
    plt.xlabel("Расстояние от источника до фотодиода, мм")
    plt.ylabel("Оптическая мощность на фотодиоде, Вт")
    plt.show()
    # tikzplotlib.save("distance.tex")


def plot_divergence(x, y):
    x_range = np.linspace(x[0], x[-1], 100)
    popt, pcov = curve_fit(inv_r_squared, x, y)
    print(popt)
    fig, ax = plt.subplots()
    ax.grid(True, which='both')
    # plt.plot(x_range, inv_r_squared(x_range, *popt), "g--")
    plt.plot(x, y, ".")
    plt.xlabel("Расходимость источника излучения, ${}^\\circ$")
    plt.ylabel("Оптическая мощность на фотодиоде, Вт")
    # plt.show()
    tikzplotlib.save("divergence.tex")


def plot_lens(x, y):
    plt.rc("font", size=22)
    plt.rc('axes', titlesize=22)     # fontsize of the axes title
    plt.rc('axes', labelsize=22)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=22)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=22)    # fontsize of the tick labels
    plt.rc('legend', fontsize=22)    # legend fontsize
    plt.rc('figure', titlesize=22)  
    fig, ax = plt.subplots()
    ax.grid(True, which='both')
    plt.plot(x, y, ".")
    plt.xlabel("Расстояние от линзы до фотодиода, мм")
    plt.ylabel("Оптическая мощность на фотодиоде, Вт")
    # plt.show()
    tikzplotlib.save("lens.tex")


def main():
    distance_x = [.1, 1, 10, 20, 50, 100, 150, 500, 1000, 2000]
    distance_power = [2.03e-1, 8.82e-2, 3.33e-3, 8.97e-4,
                      1.49e-4, 3.7e-5, 1.73e-5, 1.8e-6, 4.8e-7, 6e-8]

    divergence_x = [1, 3, 5, 8, 10, 13, 15, 18, 20, 23, 25, 28, 30]
    divergence_power = [1.15e-2, 1.31e-3, 4.7e-4, 1.88e-4, 1.2e-4,
                        7.4e-5, 5.26e-5, 3.38e-5, 2.78e-5, 2.3e-5, 1.9e-5, 1.47e-5, 1.3e-5]

    lens_x = [5, 10, 15, 15.86, 20, 25, 30, 35, 40]
    lens_power = [7.47e-7, 1.66e-6, 3.5e-4, 1.93e-3,
                  4.37e-4, 3.32e-5, 7.06e-6, 3.52e-6, 2.3e-6]

    # plot_distance(distance_x, distance_power)
    # plot_divergence(divergence_x, divergence_power)
    plot_lens(lens_x, lens_power)
    # create_table(lens_x, lens_power)


if __name__ == "__main__":
    main()
