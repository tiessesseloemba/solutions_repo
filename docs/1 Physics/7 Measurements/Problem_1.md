# Problem 1


## 🧪 Measuring the Acceleration Due to Gravity $g$ Using a Simple Pendulum


###  Introduction

This experiment aims to determine the acceleration due to gravity $g$ by analyzing the oscillations of a simple pendulum.
 The method involves timing several oscillations, calculating the period, and applying the theoretical model for simple harmonic motion under small-angle approximation.


This allows us to understand oscillatory systems and develop skills in uncertainty analysis and propagation.



###  Theoretical Background

For small angles (typically < 15°), the period of a simple pendulum is given by:


$$
T = 2\pi \sqrt{\frac{L}{g}}
$$


Solving for $g$:


$$
g = \frac{4\pi^2 L}{T^2}
$$


Where:

* $T$ is the period of one oscillation

* $L$ is the length of the pendulum


The uncertainty in $g$ is calculated using propagation of uncertainty:


$$
\Delta g = g \cdot \sqrt{ \left( \frac{\Delta L}{L} \right)^2 + \left( 2 \cdot \frac{\Delta T}{T} \right)^2 }
$$




###  Materials

* String (1.20 m long)

* Metal keychain (as pendulum mass)

* Ruler (with ±0.5 mm precision)

* Stopwatch (via smartphone)

* Stable stand



###  Procedure

1. Measure the length $L$ of the pendulum from the point of suspension to the center of mass of the weight.

2. Displace the pendulum to a small angle and release it.

3. Measure the time for 10 full oscillations.

4. Repeat the measurement 10 times.

5. Calculate the average time, individual periods, and the uncertainty.

6. Use the theoretical formula to compute $g$.




###  Raw Data


**Measured pendulum length:**

* $L = 1.200 \, \text{m}$,

* Uncertainty: $\Delta L = 0.005 \, \text{m}$


**Times for 10 oscillations:**

| Measurement No. | Time for 10 Oscillations $T_{10}$ (s) |
| --------------- | ------------------------------------- |
| 1               | 21.95                                 |
| 2               | 22.01                                 |
| 3               | 21.90                                 |
| 4               | 22.05                                 |
| 5               | 21.98                                 |
| 6               | 22.03                                 |
| 7               | 21.96                                 |
| 8               | 21.99                                 |
| 9               | 22.00                                 |
| 10              | 22.02                                 |


**Average:**

$\overline{T_{10}} = 21.989 \, \text{s}$


**Standard deviation:**

$\sigma = 0.044 \, \text{s}$


**Uncertainty on average (standard error):**

$\Delta T_{10} = \frac{\sigma}{\sqrt{10}} = 0.014 \, \text{s}$




###  Calculations


**1. Average period:**


$$
T = \frac{21.989}{10} = 2.1989 \, \text{s}, \quad \Delta T = \frac{0.014}{10} = 0.0014 \, \text{s}
$$



**2. Calculated gravitational acceleration:**



$$
g = \frac{4\pi^2 \cdot 1.200}{(2.1989)^2} = 9.80 \, \text{m/s}^2
$$



**3. Propagation of uncertainty:**



$$
\Delta g = 9.80 \cdot \sqrt{ \left( \frac{0.005}{1.200} \right)^2 + \left( 2 \cdot \frac{0.0014}{2.1989} \right)^2 } = 0.04 \, \text{m/s}^2
$$





###  Final Result

$$
\boxed{g = (9.80 \pm 0.04) \, \text{m/s}^2}
$$





###  Table of Periods and Their Uncertainties

| Measurement No. | Time $T_{10}$ (s) | Period $T$ (s) | Uncertainty $\Delta T$ (s) | Relative Uncertainty $\frac{\Delta T}{T}$ |
| --------------- | ----------------- | -------------- | -------------------------- | ----------------------------------------- |
| 1               | 21.95             | 2.195          | ±0.0014                    | 0.000638 (0.0638%)                        |
| 2               | 22.01             | 2.201          | ±0.0014                    | 0.000636 (0.0636%)                        |
| 3               | 21.90             | 2.190          | ±0.0014                    | 0.000639 (0.0639%)                        |
| 4               | 22.05             | 2.205          | ±0.0014                    | 0.000635 (0.0635%)                        |
| 5               | 21.98             | 2.198          | ±0.0014                    | 0.000637 (0.0637%)                        |
| 6               | 22.03             | 2.203          | ±0.0014                    | 0.000636 (0.0636%)                        |
| 7               | 21.96             | 2.196          | ±0.0014                    | 0.000638 (0.0638%)                        |
| 8               | 21.99             | 2.199          | ±0.0014                    | 0.000637 (0.0637%)                        |
| 9               | 22.00             | 2.200          | ±0.0014                    | 0.000636 (0.0636%)                        |
| 10              | 22.02             | 2.202          | ±0.0014                    | 0.000636 (0.0636%)                        |




###  Analysis

* The experimental value of $g$ closely matches the accepted value $9.81 \, \text{m/s}^2$.

* Measurement uncertainty is low, with relative uncertainty below 0.1%.

* Sources of uncertainty include human reaction time when using the stopwatch, length measurement with a ruler, and slight deviations from ideal conditions (friction, air resistance).

* The assumption of small angle oscillation (less than 15°) was respected.


---

###  Conclusion


The experiment provided a precise measurement of the gravitational acceleration using a simple and accessible setup. The uncertainty analysis confirms the reliability of the method. Despite minor experimental limitations, the result is consistent with the theoretical value, demonstrating the effectiveness of pendulum-based measurements.

---




