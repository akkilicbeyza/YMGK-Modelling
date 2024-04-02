import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Get model parameters from user
alpha = float(input("Enter prey growth rate (alpha): "))
beta = float(input("Enter predation rate (beta): "))
gamma = float(input("Enter predator growth rate (gamma): "))
delta = float(input("Enter predator death rate (delta): "))

# Initial conditions
prey_initial = float(input("Enter initial prey population: "))
predator_initial = float(input("Enter initial predator population: "))
y0 = [prey_initial, predator_initial]

# Time points
t = np.linspace(0, 100, 1000)

# Lotka-Volterra differential equations
def model(y, t):
    prey, predator = y
    dydt = [alpha * prey - beta * prey * predator,
            gamma * prey * predator - delta * predator]
    return dydt

# Solve the differential equations
sol = odeint(model, y0, t)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, sol[:, 0], label='Prey Population')
plt.plot(t, sol[:, 1], label='Predator Population')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model: Predator and Prey Populations')
plt.legend()
plt.grid(True)
plt.show()
