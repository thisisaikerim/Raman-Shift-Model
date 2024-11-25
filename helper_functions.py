

# new test data
new_energies = np.array([200, 400, 1500])  # new energies in keV
new_fluences = np.array([6e12, 5e13, 5e14])  # new fluences in cm^-2
new_raman_shifts = np.array([350.5, 349.8, 348.0])  # new Raman shifts in cm^-1

fluences_range = np.logspace(12, 15, 100)  # fluence values for smooth prediction lines
 
predicted_shifts = [raman_model(E, F, a, b, F0) for E, F in zip(new_energies, new_fluences)]

errors = np.array(predicted_shifts) - new_raman_shifts
absolute_errors = np.abs(errors)
max_error = np.max(absolute_errors)

# acceptable error threshold
ERROR_THRESHOLD = 2.0 

print("Testing on new data:")
for i in range(len(new_energies)):
    print(f"Data Point {i+1}:")
    print(f"  Energy (E): {new_energies[i]} keV")
    print(f"  Fluence (F): {new_fluences[i]:.2e} cm^-2")
    print(f"  Actual Raman Shift: {new_raman_shifts[i]:.2f} cm^-1")
    print(f"  Predicted Raman Shift: {predicted_shifts[i]:.2f} cm^-1")
    print(f"  Absolute Error: {absolute_errors[i]:.4f}")
    result_status = "Test passed successfully" if absolute_errors[i] <= ERROR_THRESHOLD else "Test failed"
    print(f"  Result: {result_status}
")

if max_error <= ERROR_THRESHOLD:
    print(f"All tests passed with maximum error {max_error:.4f} cm^-1.")
else:
    print(f"Some tests failed. Maximum error {max_error:.4f} cm^-1 exceeds threshold.")

plt.figure(figsize=(8, 6))

# predicted lines for the new energies
for energy in [200, 400, 1500]:
    predicted_shifts_line = [raman_model(energy, F, a, b, F0) for F in fluences_range]
    plt.plot(fluences_range, predicted_shifts_line, label=f"Predicted (E = {energy} keV)")

# experimental data points
plt.scatter(new_fluences, new_raman_shifts, label="Experimental Data", color="blue")

plt.xscale("log")
plt.xlabel("Fluence (cm^-2)")
plt.ylabel("Raman Shift (cm^-1)")
plt.title("Raman Shift vs. New Fluence for New Energies")

plt.legend()
plt.grid(which="both", linestyle="--", linewidth=0.5)

plt.show()

