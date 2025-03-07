# Problem 1
1. Theoretical Foundation

To analyze the projectile motion, we begin with the fundamental equations of motion in a uniform gravitational field. The goal is to derive the horizontal range R as a function of the launch angle $\theta$ for a projectile.

1.1 Equations of Motion

A projectile is launched with an initial velocity $v_0$ at an angle $\theta$ from the horizontal. The motion can be broken down into horizontal (x) and vertical (y) components:

•	Horizontal motion (constant velocity in the absence of air resistance):

$x(t) = v_0 \cos(\theta) t$



•	Vertical motion (with acceleration due to gravity g):

$y(t) = v_0 \sin(\theta) t - \frac{1}{2} g t^2$


1.2 Time of Flight

To find the time $t_{\text{flight}}$ it takes for the projectile to hit the ground, set y(t) = 0 (assuming the projectile lands at the same height from which it was launched). So,

$$0 = v_0 \sin(\theta) t - \frac{1}{2} g t^2$$

Factoring out t:

$$t \left( v_0 \sin(\theta) - \frac{1}{2} g t \right) = 0$$

We get two solutions: t = 0 (at launch) and $t = \frac{2 v_0 \sin(\theta)}{g}$ (when the projectile hits the ground). The time of flight is therefore:

$$t_{\text{flight}} = \frac{2 v_0 \sin(\theta)}{g}$$

1.3 Horizontal Range

The range R is the horizontal distance the projectile travels during its flight. It can be found by substituting the time of flight into the horizontal motion equation:

$$R = x(t_{\text{flight}}) = v_0 \cos(\theta) \left( \frac{2 v_0 \sin(\theta)}{g} \right)$$

Simplifying:

$$R = \frac{v_0^2 \sin(2\theta)}{g}$$

This is the classic equation for the range of a projectile on flat ground with no air resistance. It shows that the range depends on:
•	The initial velocity $v_0$,
•	The angle of projection $\theta$,
•	The gravitational acceleration g.

2. Analysis of the Range

2.1 Dependence of Range on Launch Angle

The equation $R = \frac{v_0^2 \sin(2\theta)}{g}$ clearly indicates that the range is a function of the angle $\theta$. 
To understand this further, we can analyze the behavior of $\sin(2\theta)$:

•	The function $\sin(2\theta)$ reaches its maximum value of 1 when $\theta$ = $45^\circ$.
•	This means the range is maximized when the launch angle is $45^\circ$, which is a key result in projectile motion.

At angles less than $45^\circ$, $\sin(2\theta)$ decreases, reducing the range. Similarly, at angles greater than $45^\circ$, the sine function starts to decrease again.

2.2 Effect of Initial Velocity and Gravitational Acceleration
•	Initial velocity $v_0$: The range increases quadratically with the initial velocity. Doubling $v_0$ will quadruple the range.
•	Gravitational acceleration g: The range decreases as gravity increases. In regions with stronger gravity (e.g., on planets with higher gravity), the range is shorter for the same initial velocity and launch angle.

2.3 Numerical Simulation

We can now simulate the range as a function of the launch angle for different initial velocities and gravitational accelerations.

3. Practical Applications

In real-world scenarios, the model described above is idealized and assumes no air resistance. However, in practical cases, air resistance and other factors like uneven terrain can significantly affect the projectile’s range.
•	Air resistance: For higher velocities or longer flight times, air resistance becomes significant. The range will be less than predicted by the ideal model.
•	Uneven terrain: If the projectile lands at a different height, the equations need to be modified to account for the change in height between launch and landing points.

4. Implementation

We can implement the simulation in Python using the following code. This code calculates the range as a function of the launch angle for different initial velocities and gravitational accelerations.
pip install numpy matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Function to calculate the range for a given initial velocity and angle
def calculate_range(v0, theta_deg):
    theta_rad = np.radians(theta_deg)  # Convert angle to radians
    return (v0**2 * np.sin(2 * theta_rad)) / g

# Parameters
v0 = 20  # Initial velocity in m/s
angles = np.linspace(0, 90, 100)  # Angles from 0 to 90 degrees

# Calculate the range for each angle
ranges = calculate_range(v0, angles)

# Plot the results
plt.figure(figsize=(8, 6))  # Optional: for better figure size
plt.plot(angles, ranges, label=f'Initial velocity = {v0} m/s')

# Add title and labels
plt.title('Projectile Range vs Launch Angle')
plt.xlabel('Launch Angle (degrees)')
plt.ylabel('Range (meters)')

# Add grid for better readability
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.show()
python nom_du_fichier.py

5. Limitations of the Idealized Model

While this model provides a good approximation in the absence of air resistance and for horizontal launch and landing points, there are several limitations:
•	Air resistance: The idealized model assumes no air resistance, but in reality, air resistance will reduce the range, especially at high velocities.
•	Wind: Wind can alter the trajectory significantly, making the range much harder to predict without considering wind speed and direction.
•	Launch height differences: If the launch and landing heights are not the same, the model needs modification to account for this difference in height.
•	Coriolis effect: On large distances (such as with missiles or space objects), the Coriolis effect may slightly alter the trajectory.

6. Extensions for Realistic Factors

To incorporate more realistic factors like air resistance, the equations of motion would need to include drag forces. The projectile motion equations would then become more complex and require numerical methods (such as solving differential equations) to compute the trajectory.

Additionally, terrain modeling can be included by modifying the landing condition y(t) = 0 to reflect the terrain profile.

7. Conclusion

The theoretical and practical analysis of projectile motion reveals several important insights, especially the relationship between launch angle and range. The model can be extended to real-world applications by incorporating additional factors like air resistance and uneven terrain. The Python simulation provides a powerful tool to visualize these relationships and can be extended further to model more complex situations.