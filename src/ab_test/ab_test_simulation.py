import numpy as np
from scipy import stats

np.random.seed(42)

sample_size = 500

# Baseline model (A)
baseline_accuracy = np.random.binomial(1, 0.78, sample_size)

# New model (B)
new_model_accuracy = np.random.binomial(1, 0.84, sample_size)

baseline_mean = np.mean(baseline_accuracy)
new_model_mean = np.mean(new_model_accuracy)
uplift = new_model_mean - baseline_mean

t_stat, p_value = stats.ttest_ind(new_model_accuracy, baseline_accuracy)

print("A/B Test Simulation Results")
print("---------------------------")
print(f"Baseline Model Accuracy: {baseline_mean:.3f}")
print(f"New Model Accuracy: {new_model_mean:.3f}")
print(f"Uplift: {uplift:.3f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05 and uplift > 0:
    print("Recommendation: Ship the new model because it improves accuracy with statistical significance.")
else:
    print("Recommendation: Run more data because the result is not strong enough.")
