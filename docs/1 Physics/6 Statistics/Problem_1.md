# Problem 1


###  **Introduction to the Central Limit Theorem (CLT)**

The **Central Limit Theorem** states that as the sample size increases, the sampling distribution of the sample mean will approximate a normal distribution, regardless of the original population's distribution, provided that the population has a finite mean and variance. 
This is a powerful result in statistics because it allows us to apply inferential statistics techniques even when we don't know the exact distribution of the underlying population.

---

### 1. **Simulating Sampling Distributions**

We will simulate data from three different types of population distributions:

* **Uniform Distribution**: A uniform distribution where all values have equal probability.
* **Exponential Distribution**: A distribution often used for modeling time between events in a Poisson process.
* **Binomial Distribution**: A distribution describing the number of successes in a fixed number of Bernoulli trials.

### 2. **Sampling and Visualization**

We will draw multiple random samples from the population, calculate the sample mean for each sample, and visualize the resulting sampling distributions of the sample means. The sample sizes will vary (e.g., 5, 10, 30, 50).

### 3. **Parameter Exploration**

We will investigate how the **shape of the original distribution** and the **sample size** influence the convergence of the sample means to a normal distribution. Additionally, we will explore how the **population variance** affects the spread of the sampling distribution.

### 4. **Practical Applications**

The CLT has practical implications in:

* **Estimating population parameters**: The sample mean is a consistent estimator of the population mean.
* **Quality control in manufacturing**: Small sample sizes from a large population can be used to estimate the population mean with high accuracy.
* **Predicting outcomes in financial models**: Using sample data to estimate expected returns and risks in finance.

---

###  **Python Code for Simulations**

We will use Python with the libraries `numpy`, `matplotlib`, and `seaborn` for simulation and visualization. Below is the Python code for the entire process.

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate samples from different distributions
def generate_population(distribution_type, size):
    if distribution_type == "uniform":
        return np.random.uniform(0, 1, size)
    elif distribution_type == "exponential":
        return np.random.exponential(1, size)
    elif distribution_type == "binomial":
        return np.random.binomial(n=10, p=0.5, size=size)
    else:
        raise ValueError("Unsupported distribution type")

# Function to generate sampling distributions
def generate_sampling_distribution(population, sample_size, num_samples):
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=False)
        sample_means.append(np.mean(sample))
    return sample_means

# Parameters
population_size = 100000
sample_sizes = [5, 10, 30, 50]
num_samples = 1000

# Generate populations
uniform_population = generate_population("uniform", population_size)
exponential_population = generate_population("exponential", population_size)
binomial_population = generate_population("binomial", population_size)

# Plot histograms of sample means for each sample size
fig, axes = plt.subplots(3, 4, figsize=(15, 12))

for i, dist in enumerate(["uniform", "exponential", "binomial"]):
    population = globals()[f"{dist}_population"]
    
    for j, sample_size in enumerate(sample_sizes):
        sample_means = generate_sampling_distribution(population, sample_size, num_samples)
        ax = axes[i, j]
        sns.histplot(sample_means, kde=True, stat="density", ax=ax)
        ax.set_title(f"{dist.capitalize()} - Sample Size {sample_size}")
        ax.set_xlim(-5, 5)

plt.tight_layout()
plt.show()
```

###  **Explanation of the Code:**

1. **Generate Population Data**: The `generate_population()` function creates a population based on the selected distribution type.
2. **Generate Sampling Distributions**: The `generate_sampling_distribution()` function randomly samples from the population, calculates the mean of each sample, and repeats this process multiple times.
3. **Plotting the Results**: Using `matplotlib` and `seaborn`, we plot histograms of the sampling distributions for each distribution type and sample size.

###  **Visual Output:**

Running the above code will generate histograms that show how the sampling distribution of the sample mean approaches a normal distribution as the sample size increases. Each row in the plot corresponds to one of the population distributions (Uniform, Exponential, Binomial), and each column corresponds to a different sample size.

---

### **Results and Discussion**

* **Uniform Distribution**: The sampling distribution starts off as skewed for small sample sizes and becomes more normal as the sample size increases.
* **Exponential Distribution**: The sampling distribution is more skewed compared to the uniform distribution, and it requires a larger sample size to approximate normality.
* **Binomial Distribution**: For large sample sizes, the binomial distribution becomes symmetric and approaches normality, especially when the number of trials is large.

### **The Impact of Sample Size**:

As we increase the sample size, the distribution of the sample means converges to a normal distribution more quickly. This is consistent with the Central Limit Theorem, which states that for sufficiently large sample sizes, the sampling distribution of the sample mean will be approximately normal, regardless of the original population’s distribution.

### **The Role of Variance**:

The variance of the original population affects the spread of the sampling distribution. Populations with high variance (like the exponential distribution) lead to sampling distributions with a larger spread, whereas populations with lower variance (like the binomial) result in narrower sampling distributions.

---

###  **Real-World Applications**

The CLT is essential in many fields, such as:

* **Quality Control**: In manufacturing, we can take small random samples to estimate the average quality of products without inspecting every item.
* **Financial Models**: When predicting stock returns or analyzing risks, the CLT allows for simplifying assumptions about distributions, even if the underlying data is not normally distributed.
* **Surveying**: In polling, a random sample is used to estimate the population’s opinion, and the CLT ensures that we can make accurate predictions.



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

![alt text](<image statistics.png>)

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
