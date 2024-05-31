import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace
from cycler import cycler

# Style
plt.rcParams['figure.dpi'] = 160
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15
rc = {"font.family": "serif",
      "mathtext.fontset": "stix"}
plt.rcParams.update(rc)
plt.rcParams["legend.markerscale"] = 20.0
plt.rcParams["font.serif"] = ["Times New Roman"] + plt.rcParams["font.serif"]

line_cycler_2 = cycler(color=["#c7e9c0", "#a1d99b", "#74c476", "#41ab5d", "#238b45", "#005a32"])
plt.rc("axes", prop_cycle=line_cycler_2)

"""
inputs:
t_0) float: inital time
t_f: final time
x_0) type: float, initial condition for the variable to solve.
y_0) type: float, initial condition for the 1st order derivative.
N) type: float, number of steps.

Outputs:
x) type: list, contains all the x values to build the solution curve.
"""
def runge_kutta(t_0:float, t_f:float, N:float , x_0:float, y_0:float, f):
    dt = (t_f - t_0) / N
    time = [t_0 + k * dt for k in range(N + 1)]
    x, y = [x_0], [y_0]

    for i in range(0, N):
        f_1 = f(time[i], y[i], x[i])
        f_2 = f(time[i] + (dt/2), y[i] + (dt/2)*f_1, x[i] + (dt/2)*y[i])

        y_j = y[i] + dt*f_2
        y.append(y_j)
        x_j = x[i] + dt*y[i+1]
        x.append(x_j)

    return (time, x, y)

# \ddot{x} =  g(t, x, \dot{x})
def Hooke(t, y, x):
    return -0.1 * y - x

def Legendre(t, y, x):
    a = 2
    return (2*t*y/(1-t**2))-(a*(a+1)*x/(1-t**2))

def Airy(t, y , x):
    return t*x

def Bessel(t, y, x):
    n = 5
    return ((n**2-t**2)*x - t*y)/(t**2)

def ode(x, t):
    x, y = x
    derivative = (y, t * x)
    return derivative

def main():
    fig, ax = plt.subplots()
    ax.set(title="Ecuación de Airy con Método de Runge-Kutta", xlabel="$t$", ylabel="$x(t)$")
    plt.grid(linestyle="--", color="#ddd")

    for N in [25, 30, 50, 250, 500, 1000]:
        tiempos, valores_x, valores_y = runge_kutta(t_0 = -10, t_f = 2.5, N = N, x_0 = -10, y_0 = 0, f = Airy)
        ax.plot(tiempos, valores_x, label = f"N = {N}")

    # tiempos_scipy = linspace(-10, 2.5, 1000)
    # solucion_scipy = odeint(ode, [-10, 0], tiempos_scipy)
    # ax.plot(tiempos_scipy, solucion_scipy[:,0], label = f"Scipy odeint", color="r")

    plt.legend(loc=2, prop={'size': 13}, markerscale=4)
    # plt.show()

    plt.savefig('Airy/airy_rk.jpg')

if __name__ == "__main__":
    main()
