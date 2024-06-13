import numpy as np
import matplotlib.pyplot as plt

# Define the range of step lengths
s_values = np.linspace(0.1, 10, 1000)

# Define different values of beta
beta_values = [0.5, 1.0, 1.5, 2.0]

# Plot the function for each value of beta
for beta in beta_values:
    L_s = np.abs(s_values)**(-1 - beta)
    plt.plot(s_values, L_s, label=f'β = {beta}')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('x^(-1-β)')
plt.title('Neskalirana razdioba duljine koraka u Lévyjevom letu')
plt.legend()
plt.yscale("log")
plt.grid(True)
plt.show()