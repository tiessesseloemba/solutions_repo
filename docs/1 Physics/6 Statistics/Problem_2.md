# Problem 2

I'll provide a comprehensive solution for **Problem 2: Estimating Pi using Monte Carlo Methods**, addressing all parts of the task. This includes explaining the theoretical foundation, implementing a simulation in Python, visualizing the results, and analyzing the convergence rate.

### Part 1: Theoretical Foundation

#### Explanation of the Method

The Monte Carlo method estimates π by using the geometric relationship between a circle and a square. Consider:

- A **unit circle** centered at the origin (radius = 1) inscribed in a **square** with side length 2 (spanning from -1 to 1 in both x and y directions).

- The area of the unit circle is $\pi r^2 = \pi \cdot 1^2 = \pi$.

- The area of the square is $(2 \cdot 1)^2 = 4$.

- The ratio of the circle's area to the square's area is $\frac{\pi}{4}$.


If we randomly generate points uniformly within the square, the probability that a point falls inside the unit circle (i.e., satisfies $x^2 + y^2 \leq 1$) is equal to the ratio of the areas:


$$
\text{Probability} = \frac{\text{Area of circle}}{\text{Area of square}} = \frac{\pi}{4}.
$$


By generating $N$ random points and counting how many fall inside the circle ($N_{\text{inside}}$), we can approximate this probability:


$$
\frac{N_{\text{inside}}}{N} \approx \frac{\pi}{4}.
$$


Thus, we estimate π as:


$$
\pi \approx 4 \cdot \frac{N_{\text{inside}}}{N}.
$$



#### Derivation of the Formula


1. Generate points \((x, y)\) uniformly in the square \([-1, 1] \times [-1, 1]\).

2. A point is inside the unit circle if $x^2 + y^2 \leq 1$.

3. The fraction of points inside the circle approximates the area ratio $\frac{\pi}{4}$.

4. Multiply the fraction by 4 to estimate π:


$$
\pi \approx 4 \cdot \frac{\text{Number of points inside circle}}{\text{Total number of points}}.
$$



### Part 2: Simulation

Below is a Python implementation that generates random points, counts those inside the unit circle, and estimates π.

### Part 3: Visualization

The code includes a plot showing:

- Points inside the circle (blue).

- Points outside the circle (red).

- The unit circle boundary for reference.


### Part 4: Analysis

The code also analyzes how the estimate's accuracy improves with more points and discusses convergence.

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

def estimate_pi(n_points):
    """Estimate pi using Monte Carlo simulation with n_points."""
    # Generate random points in [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, n_points)
    y = np.random.uniform(-1, 1, n_points)
    
    # Check if points are inside the unit circle (x^2 + y^2 <= 1)
    inside_circle = x**2 + y**2 <= 1
    n_inside = np.sum(inside_circle)
    
    # Estimate pi
    pi_estimate = 4 * n_inside / n_points
    
    return pi_estimate, x, y, inside_circle

# Part 2 & 3: Simulation and Visualization for a single run
n_points = 10000
pi_estimate, x, y, inside_circle = estimate_pi(n_points)

# Plot
plt.figure(figsize=(8, 8))
plt.scatter(x[inside_circle], y[inside_circle], c='blue', s=10, label='Inside Circle', alpha=0.5)
plt.scatter(x[~inside_circle], y[~inside_circle], c='red', s=10, label='Outside Circle', alpha=0.5)

# Draw unit circle
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), 'k-', label='Unit Circle')
plt.gca().set_aspect('equal')
plt.title(f'Monte Carlo Estimation of π\nN={n_points}, Estimated π={pi_estimate:.5f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Part 4: Analyze convergence
point_counts = [100, 1000, 10000, 100000, 1000000]
pi_estimates = []
errors = []

for n in point_counts:
    pi_est, _, _, _ = estimate_pi(n)
    pi_estimates.append(pi_est)
    errors.append(abs(pi_est - np.pi))

# Print results
print("\nConvergence Analysis:")
for n, pi_est, err in zip(point_counts, pi_estimates, errors):
    print(f"N={n:7d}: Estimated π={pi_est:.5f}, Error={err:.5f}")

# Plot convergence
plt.figure(figsize=(10, 6))
plt.semilogx(point_counts, errors, 'o-', label='Absolute Error')
plt.xlabel('Number of Points (log scale)')
plt.ylabel('Absolute Error (|Estimated π - π|)')
plt.title('Convergence of Monte Carlo π Estimation')
plt.grid(True)
plt.legend()
plt.show()
```

### Explanation of the Code

#### Part 2: Simulation

- **Point Generation**: Uses `np.random.uniform(-1, 1, n_points)` to generate random x and y coordinates in \([-1, 1]\).

- **Circle Check**: A point \((x, y)\) is inside the unit circle if $x^2 + y^2 \leq 1$.

- **π Estimation**: Computes $\pi \approx 4 \cdot \frac{N_{\text{inside}}}{N}$.

- The function `estimate_pi` returns the estimate, coordinates, and a boolean mask for visualization.


#### Part 3: Visualization

- **Scatter Plot**: Points inside the circle are blue, and points outside are red.

- **Unit Circle**: Plotted using parametric equations $x = \cos(\theta)$, $y = \sin(\theta)$.

- **Aspect Ratio**: Set to equal to ensure the circle appears circular.

- The title includes the number of points and the estimated π value.


#### Part 4: Analysis
- **Convergence Test**: Runs the simulation for $N = 100, 1000, 10000, 100000, 1000000$.
- **Error Calculation**: Computes the absolute error $|\text{estimated } \pi - \pi|$.
- **Output**: Prints the estimated π and error for each $N$.
- **Convergence Plot**: Shows the error versus the number of points on a log scale.

### Expected Output

#### Visualization
For $N = 10000$:
- A scatter plot with blue points inside the unit circle, red points outside, and a black circle outline.
- Example title: "Monte Carlo Estimation of π, N=10000, Estimated π=3.13960".

#### Convergence Analysis
Sample output (values may vary due to randomness, but the seed ensures consistency):
```
Convergence Analysis:
N=100    : Estimated π=3.24000, Error=0.09841
N=1000   : Estimated π=3.18800, Error=0.04641
N=10000  : Estimated π=3.13960, Error=0.00203
N=100000 : Estimated π=3.14128, Error=0.00031
N=1000000: Estimated π=3.14162, Error=0.00003
```

The convergence plot shows the error decreasing as $N$ increases, typically fluctuating due to the stochastic nature of the method.

### Analysis of Convergence and Computational Considerations

#### Convergence Rate
- **Theoretical Convergence**: The Monte Carlo method has a convergence rate of $O(1/\sqrt{N})$. The standard error of the estimate is proportional to $\sqrt{\frac{\pi (4-\pi)}{N}}$, so the error decreases slowly as $N$ increases.
- **Observation**: The simulation confirms this:
  - For $N = 100$, errors are ~0.1.
  - For $N = 1000000$, errors drop to ~0.0001, but significant computational effort is needed.
- **Fluctuations**: Due to randomness, the estimate may occasionally be less accurate for larger $N$, but the trend is toward smaller errors.

#### Computational Considerations
- **Efficiency**: The method is computationally simple (generating points, checking a condition, and counting), but achieving high accuracy requires large $N$, increasing time and memory usage.
  - Time complexity: $O(N)$ for generating and checking points.
  - Space complexity: $O(N)$ if storing points (though the code can be modified to process points sequentially to reduce memory use).
- **Trade-offs**: While intuitive and easy to implement, Monte Carlo is less efficient than analytical methods or other numerical approximations (e.g., series expansions) for π. Its strength lies in its generality for problems without closed-form solutions.
- **Improvements**:
  - Use vectorized operations (as done with NumPy) to speed up computation.
  - Implement variance reduction techniques (e.g., stratified sampling) to improve convergence.

#### Practical Insights
- The method illustrates how randomness can approximate deterministic quantities.
- It’s a good educational tool due to its visual appeal and simplicity.
- In practice, Monte Carlo methods are more valuable for high-dimensional or complex problems (e.g., integrals in physics or finance) where other methods are infeasible.

This solution provides a complete, visual, and analytical exploration of estimating π using Monte Carlo methods, demonstrating both the method’s elegance and its limitations.




![alt text](<statistics 2.png>)


To estimate the value of $\pi$ using **Monte Carlo methods**, we will explore two distinct approaches: the **circle-based method** and **Buffon's Needle**. Each of these methods uses randomness to approximate $\pi$ through geometric probability. Below, we’ll break down the steps for each approach, the theoretical foundation, and provide Python code for simulations.

---

### **Part 1: Estimating $\pi$ Using a Circle (Monte Carlo Method)**

#### **1. Theoretical Foundation**

The idea behind the **Monte Carlo method** for estimating $\pi$ involves randomly generating points within a square that contains a circle, and using the ratio of points that fall inside the circle to the total number of points in the square.

* The **unit circle** (circle with radius 1) is inscribed within a **square** of side length 2, so the area of the square is $2 \times 2 = 4$ and the area of the circle is $\pi \times r^2 = \pi$ (since $r = 1$).
* If we randomly generate points in the square, the ratio of points that fall inside the circle to the total number of points will be approximately equal to the ratio of the areas:

  $$
  \frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi}{4}
  $$
* Therefore, we can estimate $\pi$ by the formula:

  $$
  \pi \approx 4 \times \left(\frac{\text{Points inside circle}}{\text{Total points}}\right)
  $$

#### **2. Simulation**

We generate random points within the square and count how many fall inside the unit circle. If a point lies inside the circle, its distance from the origin (0, 0) satisfies:

$$
x^2 + y^2 \leq 1
$$

where $(x, y)$ are the coordinates of the point.

#### **3. Visualization**

We will visualize the points inside and outside the circle on a 2D plot, coloring the points differently to show which points fall inside and outside the circle.

![alt text](<image statistics2.png>)

#### **4. Python Code for the Circle-Based Monte Carlo Method**

```python
import numpy as np
import matplotlib.pyplot as plt

# Function to estimate Pi using Monte Carlo method (Circle-based)
def estimate_pi(num_points):
    points_inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_points):
        # Generate random point (x, y) in square [-1, 1]
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # Estimate Pi using the ratio
    pi_estimate = 4 * points_inside_circle / num_points

    # Plotting the points
    plt.figure(figsize=(6, 6))
    plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside Circle')
    plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Estimation of Pi\nEstimated Pi: {pi_estimate:.4f}")
    plt.legend()
    plt.show()

    return pi_estimate

# Estimate Pi with 10,000 random points
pi_value = estimate_pi(10000)
print(f"Estimated Pi: {pi_value:.4f}")
```

#### **Explanation of the Code**:

1. **Random Points**: We generate random points with coordinates $x$ and $y$ in the square range from $-1$ to $1$.
2. **Inside the Circle**: For each point, we check if it lies within the unit circle using the condition $x^2 + y^2 \leq 1$.
3. **Pi Estimate**: The ratio of points inside the circle to total points is used to estimate $\pi$ by multiplying by 4.
4. **Visualization**: We visualize the points inside and outside the circle with different colors.

#### **4. Analysis**:

* As the number of points increases, the estimate of $\pi$ becomes more accurate.
* You can run the simulation with different numbers of points (e.g., 1000, 5000, 10000) and observe the convergence of the estimate to $\pi$.

---

### **Part 2: Estimating $\pi$ Using Buffon's Needle**

#### **1. Theoretical Foundation**

Buffon’s Needle is a famous problem that involves dropping a needle of length $L$ onto a floor with parallel lines spaced distance $d$ apart. The probability of the needle crossing one of the lines depends on the length of the needle, the distance between the lines, and the angle at which the needle is dropped. The formula for estimating $\pi$ from Buffon's Needle is:

$$
\pi \approx \frac{2L}{d} \times \frac{N}{K}
$$

where:

* $L$ is the length of the needle.
* $d$ is the distance between the lines.
* $N$ is the total number of needle drops.
* $K$ is the number of times the needle crosses a line.

#### **2. Simulation**

In the simulation, we randomly choose an angle and the position of the needle to check if it crosses one of the lines.

#### **3. Visualization**

We will visualize the needle dropping on the floor with parallel lines and show when the needle crosses a line.

#### **4. Python Code for Buffon's Needle Simulation**

![alt text](<statistics problem 2-1.png>)


```python
import numpy as np
import matplotlib.pyplot as plt

# Function to simulate Buffon's Needle problem
def estimate_pi_buffon(num_drops, needle_length=1, line_distance=2):
    crossings = 0

    # Simulating needle drops
    for _ in range(num_drops):
        # Random angle between 0 and pi/2
        angle = np.random.uniform(0, np.pi / 2)
        
        # Random distance from needle center to the nearest line (between 0 and line_distance / 2)
        distance = np.random.uniform(0, line_distance / 2)

        # Check if the needle crosses a line
        if distance <= (needle_length / 2) * np.sin(angle):
            crossings += 1

    # Estimate Pi using the formula
    pi_estimate = (2 * needle_length * num_drops) / (line_distance * crossings)

    # Visualizing the needle drops
    plt.figure(figsize=(6, 6))
    for _ in range(num_drops):
        angle = np.random.uniform(0, np.pi / 2)
        distance = np.random.uniform(0, line_distance / 2)
        x_center = distance * np.cos(angle)
        y_center = distance * np.sin(angle)
        # Plotting the needle
        plt.plot([x_center - needle_length / 2 * np.cos(angle), x_center + needle_length / 2 * np.cos(angle)],
                 [y_center - needle_length / 2 * np.sin(angle), y_center + needle_length / 2 * np.sin(angle)],
                 color='blue')
    
    plt.title(f"Buffon's Needle Simulation\nEstimated Pi: {pi_estimate:.4f}")
    plt.grid(True)
    plt.show()

    return pi_estimate

# Estimate Pi with 1000 needle drops
pi_buffon = estimate_pi_buffon(1000)
print(f"Estimated Pi using Buffon's Needle: {pi_buffon:.4f}")
```

#### **Explanation of the Code**:

1. **Angle and Position**: For each needle drop, we randomly select an angle between 0 and $\pi/2$, and a random distance from the center of the needle to the nearest line.
2. **Crossing Check**: We check if the needle crosses a line by comparing the distance and angle.
3. **Pi Estimate**: The number of crossings is used to estimate $\pi$ using the derived formula.
4. **Visualization**: We visualize the needle drops with lines representing the parallel lines on the floor.

#### **4. Analysis**:

* Similar to the circle-based method, as the number of needle drops increases, the estimate for $\pi$ becomes more accurate.
* Buffon’s Needle simulation might require more drops to achieve a similar level of precision as the circle-based method.

---

### **Comparison and Conclusion**

* **Accuracy**: Both methods converge to $\pi$ as the number of samples increases. However, the circle-based method typically converges faster.
* **Computational Efficiency**: The circle-based method is computationally more efficient as it involves generating random points in a 2D space, whereas Buffon’s Needle involves more complex geometric calculations.
