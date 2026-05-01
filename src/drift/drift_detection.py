import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Reference (training) data
reference_data = np.random.normal(loc=50, scale=5, size=500)

# Production data with drift
production_data = np.random.normal(loc=60, scale=8, size=500)

# Calculate mean difference
reference_mean = np.mean(reference_data)
production_mean = np.mean(production_data)

print("Reference Mean:", reference_mean)
print("Production Mean:", production_mean)
print("Drift (difference):", production_mean - reference_mean)

# Plot distributions
plt.hist(reference_data, bins=30, alpha=0.5, label="Reference Data")
plt.hist(production_data, bins=30, alpha=0.5, label="Production Data")
plt.legend()
plt.title("Data Drift Visualization")

# Save plot
plt.savefig("visualizations/drift_plot.png")
print("Drift plot saved in visualizations/")
