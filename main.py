import numpy as np
import matplotlib.pyplot as plt 


def main():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid()
    plt.show()  

if __name__ == "__main__":
    main()

    