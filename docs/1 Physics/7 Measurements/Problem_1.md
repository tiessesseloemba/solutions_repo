# Problem 1

### **Measuring Earth's Gravitational Acceleration with a Pendulum**

#### **Motivation:**

The acceleration due to gravity, denoted $g$, is a fundamental physical constant that influences a wide range of phenomena. 
One way to measure $g$ accurately is through the oscillations of a simple pendulum.
 The period of the pendulum depends on the local gravitational field, and by measuring this period, we can calculate $g$.

#### **Procedure:**

---

### **1. Materials:**

* **String** (1 or 1.5 meters long)
* **Small weight** (e.g., a bag of coins, a key chain, or a small bag of sugar)
* **Stopwatch** (or smartphone timer)
* **Ruler or measuring tape**

---

### **2. Setup:**

1. **Attach the weight** to one end of the string and fix the other end securely to a stable support.
2. **Measure the length of the pendulum** $L$ from the suspension point (where the string is attached) to the center of the weight. Use a ruler or measuring tape for this measurement.

   * Record the **resolution of the measuring tool**. If you're using a ruler, it might have a resolution of 0.1 cm or 1 mm. The uncertainty in the length measurement is half of the resolution of the measuring tool (i.e., $\delta L = \frac{\text{resolution}}{2}$).

---

### **3. Data Collection:**

1. **Displace the pendulum** slightly (less than 15°) and release it, allowing it to swing back and forth.
2. **Measure the time for 10 full oscillations** using a stopwatch or smartphone timer. Record the time for each trial.

   * Repeat the measurement 10 times and record all 10 measurements for consistency.
3. **Calculate the mean time for 10 oscillations** ($T_{\text{mean}}$) and the standard deviation ($\sigma$) of the measurements.
4. **Calculate the uncertainty in the mean time** using the formula for standard deviation:

   $$
   \delta T_{\text{mean}} = \frac{\sigma}{\sqrt{n}}
   $$

   where $n$ is the number of measurements (in this case, $n = 10$).

---

### **4. Calculations:**

1. **Calculate the period of a single oscillation** $T$:

   * The period $T$ is the time taken for one full oscillation, which is the time for 10 oscillations divided by 10:

   $$
   T = \frac{T_{\text{mean}}}{10}
   $$

2. **Determine the gravitational acceleration $g$:**
   The relationship between the period of a simple pendulum and the gravitational acceleration $g$ is given by:

   $$
   T = 2\pi \sqrt{\frac{L}{g}}
   $$

   Rearranging this formula to solve for $g$, we get:

   $$
   g = \frac{4\pi^2 L}{T^2}
   $$

   Plug in the values of $L$ and $T$ to calculate $g$.

3. **Propagate uncertainties:**
   The uncertainty in $g$ is calculated by propagating the uncertainties in $L$ and $T$ using the following formula:

   $$
   \delta g = g \sqrt{\left(\frac{\delta L}{L}\right)^2 + \left(2 \frac{\delta T}{T}\right)^2}
   $$

   where:

   * $\delta L$ is the uncertainty in the length of the pendulum,
   * $\delta T$ is the uncertainty in the period $T$.

---

### **5. Analysis:**

1. **Compare your measured $g$ with the standard value**:

   * The standard value of gravitational acceleration $g$ at the Earth's surface is approximately $9.81 \, \text{m/s}^2$.
   * Compare the calculated value of $g$ with this standard value and discuss the difference.

2. **Discuss the following:**

   * **Effect of measurement resolution** on the accuracy of $g$: Discuss how the precision of the length measurement impacts the final result.
   * **Variability in timing** and its impact on $g$: Discuss how the timing resolution and human reaction time might affect the accuracy of your results.
   * **Assumptions or experimental limitations**: Consider any assumptions made during the experiment, such as the small angle approximation or the assumption that the pendulum swings in a simple harmonic motion. Discuss any potential sources of error (e.g., air resistance, friction at the pivot point).

---

### **Example Data Table:**

| Measurement Trial | Time for 10 Oscillations (s) | Mean Time $T_{\text{mean}}$ (s) | Standard Deviation $\sigma$ (s) | Length $L$ (m) | $T$ (s) | Gravitational Acceleration $g$ (m/s²) |
| ----------------- | ---------------------------- | ------------------------------- | ------------------------------- | -------------- | ------- | ------------------------------------- |
| 1                 | 19.8                         |                                 |                                 | 1.2            |         |                                       |
| 2                 | 20.1                         |                                 |                                 | 1.2            |         |                                       |
| 3                 | 20.0                         |                                 |                                 | 1.2            |         |                                       |
| ...               | ...                          |                                 |                                 | ...            |         |                                       |

---

### **Discussion on Uncertainties:**

* **Measurement Uncertainty**: The uncertainty in length measurement is typically small but can still affect the final result, especially if the string length is not measured precisely.
* **Timing Uncertainty**: The uncertainty in timing can be significant. Human reaction time can add error when starting and stopping the stopwatch, and the resolution of the stopwatch also limits precision.
* **Small Angle Assumption**: This assumption might not be valid for larger angles, which could lead to a slight overestimation of the period and, thus, the gravitational acceleration.

---

### **Deliverables:**

1. A **Markdown document** containing:

   * Tabulated data.
   * Detailed calculations.
   * The uncertainty analysis and discussion.

2. **Python scripts** or **Jupyter Notebooks** implementing the simulations or calculations for pendulum-based measurements and uncertainty propagation.

3. **Plots** showing:

   * The distribution of timing measurements.
   * The convergence of $g$ based on increasing number of measurements.

4. **Analysis** comparing the experimental value of $g$ with the theoretical value and discussing the sources of uncertainty.


