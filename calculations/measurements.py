import matplotlib.pyplot as plt


def create_table(x, y):
    result = []
    for xi, yi, i in zip(x, y, range(len(x))):
        s = "${}$ & ${}$ & ${:.2e}$ \\\\ \\hline".format(i+1, xi, yi)
        result.append(s)
    print("\n".join(result))


def plot(x, ys):
    maximum = max(ys)
    y = [i / maximum for i in ys]
    fig, ax = plt.subplots()
    ax.grid(True, which='both')
    plt.plot(x, y, ".")
    plt.xlabel("Угол поворота источника, ${}^\\circ$")
    plt.ylabel("Оптическая мощность на фотодиоде, абс. знач.")
    plt.xticks([i for i in x if i % 2 == 0])
    plt.show()


def main():
    xs = [i for i in range(20)]
    # DATA FOR 10 W AND 20 MM BETWEEN LD AND PD
    with_lens = [1.8197E-01, 8.4686E-02, 3.4186E-02,
                 2.7405E-02,  2.4069E-02, 1.5040E-02, 3.4227E-03, *[0 for i in range(20-7)]]
    no_lens = [1.1332E-02, 1.1320E-02, 1.1306E-02,
               1.1294E-02, 1.1288E-02, 1.1288E-02, 1.1262E-02, 1.1252E-02, 1.1206E-02, 1.1182E-02, 1.1172E-02, 1.1124E-02, 1.1092E-02, 1.1020E-02, 1.0984E-02, 1.0944E-02, 1.0884E-02, 1.0840E-02, 6.6160E-03, 0]
    plot(xs, with_lens)

    # create_table(xs, no_lens)


if __name__ == "__main__":
    main()
