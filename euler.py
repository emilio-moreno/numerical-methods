import matplotlib.pyplot as plt

def f(t, x, y):
	return 3 * y / t + x / t**2

def metodo_euler(t0, tfinal, N, x0, y0, f):
	delta_t = (tfinal - t0) / N
	tiempos = [t0]
	valores_x = [x0]
	valores_y = [y0]

	for k in range(1, N + 1):
		t = t0 + k * delta_t
		tiempos.append(t)

		x = valores_x[-1] + valores_y[-1] * delta_t
		valores_x.append(x)

		y = valores_y[-1] + f(t, valores_x[-1], valores_y[-1]) * delta_t
		valores_y.append(y)

	return tiempos, valores_x, valores_y

fig, ax = plt.subplots()

for N in range(500, 20000, 3000):
	tiempos, valores_x, valores_y = metodo_euler(t0 = 0.1, tfinal = 2.5, N = N, x0 = 0.001, y0 = 2, f = f)

	ax.plot(tiempos, valores_x, label = f"N = {N}")

plt.legend()
plt.show()