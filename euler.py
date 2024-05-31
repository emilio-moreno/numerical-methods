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

line_cycler   = cycler(color=["#dadaeb", "#bcbddc", "#9e9ac8", "#807dba", "#6a51a3", "#4a1486"])
plt.rc("axes", prop_cycle=line_cycler)

# Función para scipy
def ode(x, t):
	x, y = x
	derivative = (y, t * x)
	return derivative


# Método de euler
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

def main():

	fig, ax = plt.subplots()
	ax.set(title="Ecuación de Airy con Euler", xlabel="$t$", ylabel="$x(t)$")
	plt.grid(linestyle="--", color="#ddd")

	for N in [25, 30, 50, 250, 500, 1000]:
		tiempos, valores_x, valores_y = metodo_euler(t0 = -10, tfinal = 2.5, N = 1000, x0 = -10, y0 = 0, f = f)
		ax.plot(tiempos, valores_x, label = f"N = {N}")

	tiempos_scipy = linspace(-10, 2.5, 1000)
	solucion_scipy = odeint(ode, [-10, 0], tiempos_scipy)
	ax.plot(tiempos_scipy, solucion_scipy[:,0], label = f"Scipy odeint", color="r")

	plt.legend(loc=2, prop={'size': 13}, markerscale=4)

	# Zoom
	# ax.set(xlim=[-4, 2], ylim=[2, -2])
	plt.savefig('Airy/multi_airy_euler.jpg')

if __name__ == "__main__":
	main()