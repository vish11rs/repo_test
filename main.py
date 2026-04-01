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
import matplotlib.pyplot as plt

import quadratic


def main():
    x = np.array([1, 0 , -1])

    y = quadratic.qaudratic(x)

    c = y[1]
    b = (y[0]-y[2])/2.
    a = y[0] - b -c

    det = b**2 -4*a*c
    if a == 0: 
        print("Not a Quadratic equation")
    else:
        x1 = (-b + np.sqrt(det))/(2*a)
        x2 = (-b - np.sqrt(det))/(2*a)
        print(f"{a = :.3f}, {b = :.3f}, { c= :.3f}")
        print("The roots are:")
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}") 

    x = np.linspace(-5, 5 , 100)
    y = a*x**2 + b*x + c
    plt.plot(x, y, 'r--')
    plt.axhline(0,color='k')
    plt.axvline(0, color='k')
    plt.grid(True)
    plt.legend(['Quadratic'])
    plt.show()


# def main():
#     print("Main function executing")
#     x = np.linspace(0, 2*np.pi , 100 )
#     y = np.sin(x)
#     plt.plot(x, y, 'r--')
#     # plt.axhline(0,color='k')
#     plt.axvline(np.pi, color='k')
#     plt.grid(True)
#     # ax = plt.gca()
#     # ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi/6))
#     plt.legend(['sin(x)'])
#     # plt.savefig('sinus.png')
#     plt.show()



if __name__ == "__main__":
    main()

    
