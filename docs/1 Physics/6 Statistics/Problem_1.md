# Problem 1


```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
population_size = 100000
sample_sizes = [5, 10, 30, 50]
n_samples = 1000  # Number of samples to draw for each sample size

# 1. Generate population distributions
distributions = {
    'Uniform': np.random.uniform(low=0, high=10, size=population_size),
    'Exponential': np.random.exponential(scale=2, size=population_size),
    'Binomial': np.random.binomial(n=20, p=0.5, size=population_size)
}

# 2. Simulate sampling distributions and visualize
plt.figure(figsize=(15, 12))

for i, (dist_name, population) in enumerate(distributions.items(), 1):
    # Plot original population distribution
    plt.subplot(len(distributions), len(sample_sizes) + 1, i * (len(sample_sizes) + 1) - len(sample_sizes))
    sns.histplot(population, bins=50, stat='density')
    plt.title(f'{dist_name} Population')
    plt.xlabel('Value')
    plt.ylabel('Density')
    
    # Generate sampling distributions for different sample sizes
    for j, sample_size in enumerate(sample_sizes, 1):
        # Draw samples and calculate means
        sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(n_samples)]
        
        # Plot sampling distribution
        plt.subplot(len(distributions), len(sample_sizes) + 1, i * (len(sample_sizes) + 1) - len(sample_sizes) + j)
        sns.histplot(sample_means, bins=50, stat='density')
        plt.title(f'n={sample_size}')
        plt.xlabel('Sample Mean')
        plt.ylabel('Density')

plt.tight_layout()
plt.show()

# 3. Parameter Exploration - Calculate statistics
for dist_name, population in distributions.items():
    print(f"\n{dist_name} Distribution:")
    print(f"Population Mean: {np.mean(population):.2f}")
    print(f"Population Variance: {np.var(population):.2f}")
    
    for sample_size in sample_sizes:
        sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(n_samples)]
        print(f"\nSample Size: {sample_size}")
        print(f"Mean of Sample Means: {np.mean(sample_means):.2f}")
        print(f"Variance of Sample Means: {np.var(sample_means):.2f}")
        print(f"Expected Variance (σ²/n): {np.var(population)/sample_size:.2f}")
```

![alt text](<Capture d'écran 2025-04-23 184008.png>)

### Explanation of the Code


1. **Population Distributions**:

   - **Uniform**: Values between 0 and 10.
   - **Exponential**: Scale parameter (mean) = 2, representing a skewed distribution.
   - **Binomial**: 20 trials with a success probability of 0.5, representing a discrete distribution.
   - Each population has 100,000 data points to simulate a large population.


2. **Sampling and Visualization**:

   - For each distribution and sample size (5, 10, 30, 50), we draw 1,000 random samples and compute their means.
   - Histograms show the population distribution (leftmost column) and the sampling distributions of the sample means for each sample size.
   - As sample size increases, the histograms of sample means become more bell-shaped, illustrating the CLT.


3. **Parameter Exploration**:

   - The code calculates and prints the population mean and variance.
   - For each sample size, it reports the mean and variance of the sample means and compares the variance to the theoretical value (population variance divided by sample size, σ²/n).
   - Observations:
     - **Shape Influence**: The exponential distribution (highly skewed) converges to normality more slowly than the uniform or binomial distributions.
     - **Sample Size**: Larger sample sizes (e.g., 30 or 50) produce sampling distributions that are closer to normal, even for skewed populations.
     - **Variance Impact**: The variance of the sample means decreases as sample size increases, following the relationship Var(X̄) = σ²/n, where σ² is the population variance.



### 4. Practical Applications of the CLT

- **Estimating Population Parameters**: The CLT allows us to use sample means to estimate population means with confidence intervals, assuming approximate normality for large samples. For example, in survey research, the average opinion from a sample can estimate the population's opinion.
- **Quality Control in Manufacturing**: Manufacturers use the CLT to monitor processes. For instance, the average weight of a sample of products can be assumed to follow a normal distribution, enabling the detection of deviations from quality standards.
- **Predicting Outcomes in Financial Models**: In finance, the CLT underpins risk assessment. Portfolio returns, which aggregate many individual asset returns, are often modeled as normally distributed, facilitating predictions and risk management.


### Expected Observations from the Simulation

- **Uniform Distribution**: The sampling distribution approaches normality quickly, even for small sample sizes, due to the symmetry and lack of skewness in the population.
- **Exponential Distribution**: The sampling distribution is skewed for small sample sizes (e.g., n=5) but becomes increasingly normal as sample size grows (e.g., n=50).
- **Binomial Distribution**: Since the binomial distribution is already somewhat symmetric for n=20 and p=0.5, the sampling distribution approaches normality rapidly.
- **Variance**: The variance of the sample means closely matches the theoretical value (σ²/n), confirming that the spread of the sampling distribution decreases with larger sample sizes.

This simulation provides a hands-on way to visualize and understand the CLT, demonstrating its robustness across different population distributions and its practical significance in statistical inference.
