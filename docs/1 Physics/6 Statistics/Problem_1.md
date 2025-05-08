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


 **Step 1: Simulating Population Distributions**

We generate three distinct population distributions, each with 100,000 data points:  

1. **Uniform Distribution**: `np.random.uniform(0, 1, 100000)`  

2. **Exponential Distribution**: `np.random.exponential(scale=1, size=100000)`  

3. **Binomial Distribution**: `np.random.binomial(n=10, p=0.5, size=100000)`  

---

 **Step 2: Sampling and Visualization**

For each population, we:  

1. **Sample Means Calculation**:  

   - Draw 10,000 random samples for each sample size $n = 5, 10, 30, 50$.  

   - Compute the mean of each sample.  

2. **Histograms**:  

   - Plot histograms of the sample means for each $n$.  

   - Overlay a normal curve with parameters $\mu = \text{population mean}$ and $\sigma/\sqrt{n}$.  


![alt text](<Figure_pb1 statistics.png>)


### 3. **Parameter Exploration**

1. **Original Distribution Shape**:  

   - **Uniform**: Symmetric → Fast convergence to normality (even at $n=5$).  

   - **Exponential**: Skewed → Requires $n \geq 30$ for near-normality.  

   - **Binomial**: Discrete → Approximates normality at $n=30$, but visible discreteness at small $n$.  

2. **Population Variance**:  

   - Higher variance (e.g., exponential) widens the sampling distribution’s spread.  

   - As $n$ increases, spread narrows by $\sigma/\sqrt{n}$, confirming CLT.  

---


### 4. **Practical Applications**


1. **Estimating Population Parameters**: CLT justifies using sample means to infer population $\mu$, even for non-normal data.  

2. **Quality Control**: Control charts assume normality of process averages.  

3. **Financial Models**: Portfolio returns are modeled as normal due to aggregated effects.  

---

### **Key Observations from Simulations**  


| Distribution       | $n=5$          | $n=30$         |  
|---------------------|--------------------|--------------------|  
| Uniform             | Slightly normal    | Fully normal       |  
| Exponential         | Right-skewed       | Nearly symmetric   |  
| Binomial            | Discrete peaks     | Smooth, normal     |  


---

### **The Impact of Sample Size**:

As we increase the sample size, the distribution of the sample means converges to a normal distribution more quickly. This is consistent with the Central Limit Theorem, which states that for sufficiently large sample sizes, the sampling distribution of the sample mean will be approximately normal, regardless of the original population’s distribution.


### **The Role of Variance**:

The variance of the original population affects the spread of the sampling distribution. Populations with high variance (like the exponential distribution) lead to sampling distributions with a larger spread, whereas populations with lower variance (like the binomial) result in narrower sampling distributions.


### **Conclusion**
 
The simulations visually validate the Central Limit Theorem: as $n$ increases, the sampling distribution of the mean converges to normality, regardless of the population’s original shape. This underpins statistical methods like confidence intervals and hypothesis testing.  


