import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

energy = np.array([200, 200, 200, 400, 400, 400, 1500, 1500, 1500])  # Energies in keV
fluence = np.array([3e12, 1e13, 1e14, 3e12, 1e13, 1e14, 3e12, 1e13, 1e14])  # Fluence in cm^-2
raman_shift = np.array([350, 350, 349, 349, 349.72, 348.73, 348, 348.9, 348])  # Raman shift in cm^-1

data = np.column_stack((energy, fluence))

def raman_model(E, F, a, b, F0):
    return 350.0 - a * E - b * (1 - np.exp(-F / F0))

# Loss function
def loss_function(params):
    a, b, F0 = params  # parameters to optimize
    predicted = [raman_model(E, F, a, b, F0) for E, F in data]
    return np.sum((predicted - raman_shift) ** 2)

# Initial guess for parameters
initial_params = [1e-5, 1e-5, 1e13]

# Perform optimization
result = minimize(loss_function, initial_params, method="BFGS")
a, b, F0 = result.x

# energies for which to plot predicted lines
energies = [200, 400, 1500]
energy_fixed = 200  # Fix energy to 200 keV
# fluence range for predictions
fluence_query = np.logspace(12, 15, 100)
predicted_shifts = [raman_model(energy_fixed, F, a, b, F0) for F in fluence_query]


# predictions for each energy
for energy_fixed in energies:
    predicted_shifts = [raman_model(energy_fixed, F, a, b, F0) for F in fluence_query]
    plt.plot(fluence_query, predicted_shifts, label=f"Predicted (E = {energy_fixed} keV)")

# experimental data (all energies)
plt.scatter(fluence, raman_shift, label="Experimental Data", color="blue")

# Log scale and labels
plt.xscale("log")
plt.xlabel("Fluence (cm^-2)")
plt.ylabel("Raman Shift (cm^-1)")
plt.legend()
plt.title("Raman Shift vs. Fluence for Different Energies")
plt.show()