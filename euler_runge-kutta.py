import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace
from cycler import cycler


# Estilo
plt.rcParams['figure.dpi'] = 160
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15
rc = {"font.family": "serif",
      "mathtext.fontset": "stix"}
plt.rcParams.update(rc)
plt.rcParams["legend.markerscale"] = 20.0
plt.rcParams["font.serif"] = ["Times New Roman"] + plt.rcParams["font.serif"]

line_cycler_1 = cycler(color=["#dadaeb", "#bcbddc", "#9e9ac8", "#807dba", "#6a51a3", "#4a1486"])
line_cycler_2 = cycler(color=["#c7e9c0", "#a1d99b", "#74c476", "#41ab5d", "#238b45", "#005a32"])
plt.rc("axes", prop_cycle=line_cycler_1)

# Función para scipy
def ode(x, t):
	x, y = x
	derivative = (y, t * x)
	return derivative


# Métodos de Euler y de Runge-Kutta
def f(t, x, y):
	return t * x


def metodo_euler(t0, tfinal, N, x0, y0, f):
	delta_t = (tfinal - t0) / N
	tiempos = [t0]
	valores_x = [x0]
	valores_y = [y0]

	for k in range(1, N + 1):
		tk = t0 + k * delta_t
		tiempos.append(tk)

		xk = valores_x[-1] + valores_y[-1] * delta_t
		valores_x.append(xk)

		yk = valores_y[-1] + f(tk, valores_x[-1], valores_y[-1]) * delta_t
		valores_y.append(yk)

	return tiempos, valores_x, valores_y


def runge_kutta(t_0:float, t_f:float, N:float , x_0:float, y_0:float, f):
    dt = (t_f - t_0) / N
    time = [t_0 + k * dt for k in range(N + 1)]
    x, y = [x_0], [y_0]

    for i in range(0, N):
        f_1 = f(time[i], x[i], y[i])
        f_2 = f(time[i] + (dt/2),x[i] + (dt/2)*y[i] , y[i] + (dt/2)*f_1)

        y_j = y[i] + dt*f_2
        y.append(y_j)
        x_j = x[i] + dt*y[i+1]
        x.append(x_j)

    return (time, x, y)


def main():
	fig, ax = plt.subplots()
	ax.set(title="Ecuación de Airy con Euler y con Runge-Kutta", xlabel="$t$", ylabel="$x(t)$")
	plt.grid(linestyle="--", color="#ddd")

	for N in [25, 30, 500, 1000]:
		tiempos, valores_x, valores_y = metodo_euler(t0 = -10, tfinal = 2.5, N = N, x0 = -10, y0 = 0, f = f)
		ax.plot(tiempos, valores_x, label = f"Euler: N = {N}")
	
	plt.legend(title="Euler", loc=2, prop={'size': 13}, markerscale=4)

	for N, color in zip([25, 30, 500, 1000], ["#c7e9c0", "#a1d99b", "#74c476", "#41ab5d"]):		
		tiempos, valores_x, valores_y = runge_kutta(t_0 = -10, t_f = 2.5, N = N, x_0 = -10, y_0 = 0, f = f)
		ax.plot(tiempos, valores_x, label = f"RK: N = {N}", color=color)
	
	tiempos_scipy = linspace(-10, 2.5, 1000)
	solucion_scipy = odeint(ode, [-10, 0], tiempos_scipy)
	ax.plot(tiempos_scipy, solucion_scipy[:,0], label = f"Scipy odeint", color="r")

	ax.legend(loc=2, prop={'size': 13}, markerscale=4)

	# Zoom
	# ax.set(xlim=[-4, 2], ylim=[2, -2])
	plt.savefig('Airy/airy_euler_rk.jpg')

if __name__ == "__main__":
    main()