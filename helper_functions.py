# Function to calculate the max error for given parameters
def calculate_max_error(test_params):
    a_test, b_test, F0_test = test_params
    predicted = [raman_model(E, F, a_test, b_test, F0_test) for E, F in data]
    max_error = np.max(np.abs(predicted - raman_shift))
    return max_error

# Test different conditions
zetas = [0.2, 1.0, 2.0]  # Example test cases for zeta-like parameter
test_results = []

for zeta in zetas:
    print(f"Testing for zeta = {zeta}")
    initial_conditions = [
        [1e-5 * zeta, 1e-5 * zeta, 1e13],
        [1e-5 * zeta, 1e-5 * zeta, 5e13],
        [1e-5 * zeta, 1e-5 * zeta, 7.5e13],
    ]  # Example test initial conditions

    for idx, params in enumerate(initial_conditions):
        max_error = calculate_max_error(params)
        print(f"  Initial conditions: a={params[0]:.3e}, b={params[1]:.3e}, F0={params[2]:.3e}")
        print(f"  Max Error: {max_error:.4f}")
        test_results.append((zeta, params, max_error))
    print()
