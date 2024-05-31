import matplotlib.pyplot as plt
import scipy 
import numpy as np

"""
inputs:
t) type: iterable, this already contains information about initial, final time and timestep.
x_0) type: float, initial condition for the variable to solve.
y_0) type: float, initial condition for the 1st order derivative.

Outputs:
x) type: list, contains all the x values to build the solution curve.
"""
def runge_kutta(t:iter , x_0:float, y_0:float):
    dt = (t[1] - t[0])
    t_2 = dt/2

    x, y = [x_0], [y_0]

    for i in range(len(t)-1):
        #Calculation of the subinterval required for runge kutta
        alpha = f(t[i], x[i], y[i])

        y_j = y[i] + dt*f(t[i] + t_2, x[i] + t_2 * y[i], y[i] + t_2*alpha)
        y.append(y_j)
        x_j = x[i] + dt*y[i+1]

        x.append(x_j)

    return x


def f(t, x, y):
    a = 2
    # (2*t*y/(1-t**2))-(a*(a+1)*x/(1-t**2))
    return -0.1 * y - x

def main():
    for dt in [0.01, 0.0001, 0.00001]:
        t = np.arange(-.9, 20, dt)
        x = runge_kutta(t, -1, -1)

        print(t)
        
        plt.plot(t, x)
    plt.show()

if __name__ == "__main__":
    main()
