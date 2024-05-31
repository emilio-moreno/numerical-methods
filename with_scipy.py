from numpy import linspace
from scipy.integrate import odeint
# import matplotlib.pyplot as plt

# def ode(x, t):
	# x, y = x
	# derivative = (y, t * x)
	# return derivative

# times = linspace(-10, 2.5, 1000)
# solution = odeint(ode, [-10, 0], times)

# plt.plot(times, solution[:,0])
# plt.show()



print(lambda x, y: x^2 + y)