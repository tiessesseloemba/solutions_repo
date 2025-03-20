# Problem 3

Below is an overview of the problem along with a discussion of the trajectories and an example computational tool using Python to simulate the payload’s motion under Earth’s gravity.

---

## 1. Overview

When a payload is released from a moving rocket near Earth, its path is determined by both the initial conditions (position, velocity magnitude, and direction) and the gravitational pull of Earth. Depending on these parameters, the trajectory can take one of several forms:
 
- **Elliptical Orbit:** The payload remains bound to Earth if its specific orbital energy is negative. Such a case can occur when the release velocity is below the local escape speed.

- **Parabolic Trajectory:** This is the boundary case where the payload’s energy is exactly zero. The trajectory is marginally unbound, representing the minimum energy required for escape.

- **Hyperbolic Trajectory:** If the payload has excess energy (i.e., its velocity exceeds the escape speed), the path becomes hyperbolic, indicating an unbound orbit and escape from Earth’s gravitational influence.


These scenarios are crucial for mission design. For instance, a payload intended for orbital insertion must achieve an elliptical orbit, while a payload meant for interplanetary transfer might require a hyperbolic escape trajectory. Conversely, a payload with an excessively high release velocity might reenter Earth’s atmosphere or follow a dangerously steep path.

---

## 2. Numerical Analysis and Simulation Approach

### Equations of Motion

The motion of the payload under Earth's gravity is governed by Newton’s law of universal gravitation. In a two-dimensional plane, the acceleration is given by:


$$
\mathbf{a} = -\frac{GM}{r^3} \mathbf{r}
$$


where:

- $G$ is the gravitational constant,

- $M$ is Earth’s mass,

- $\mathbf{r}$ is the position vector of the payload relative to Earth’s center, and

- $r = \|\mathbf{r}\|$ is its magnitude.



### Numerical Integration

To simulate the motion, we solve the second-order differential equations by converting them into a system of first-order equations. A common approach is to use the fourth-order Runge–Kutta (RK4) method, which offers a good balance between accuracy and computational efficiency.



### Simulation Goals

The simulation aims to:

- Compute the trajectory given an initial position (usually specified by altitude above the Earth’s surface) and initial velocity (both magnitude and direction).
- Visualize the trajectory to determine if the payload enters a bound elliptical orbit, follows a parabolic escape trajectory, or departs on a hyperbolic path.

---

## 3. Computational Tool Example

Below is a Python code example that sets up and solves the differential equations for the payload’s trajectory. The code uses standard libraries such as NumPy and Matplotlib for numerical computations and visualization.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11         # Gravitational constant, m^3 kg^-1 s^-2
M_earth = 5.972e24      # Mass of Earth, kg
R_earth = 6.371e6       # Radius of Earth, m

def acceleration(r):
    """Compute the gravitational acceleration at position r."""
    norm_r = np.linalg.norm(r)
    return -G * M_earth * r / norm_r**3

def rk4_step(r, v, dt):
    """Perform one RK4 step for position r and velocity v."""
    # k1
    k1_r = v
    k1_v = acceleration(r)
    
    # k2
    k2_r = v + 0.5 * dt * k1_v
    k2_v = acceleration(r + 0.5 * dt * k1_r)
    
    # k3
    k3_r = v + 0.5 * dt * k2_v
    k3_v = acceleration(r + 0.5 * dt * k2_r)
    
    # k4
    k4_r = v + dt * k3_v
    k4_v = acceleration(r + dt * k3_r)
    
    r_next = r + dt * (k1_r + 2*k2_r + 2*k3_r + k4_r) / 6.0
    v_next = v + dt * (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6.0
    return r_next, v_next

def simulate_trajectory(r0, v0, dt, total_time):
    """Simulate the trajectory given initial position r0 and velocity v0."""
    num_steps = int(total_time / dt)
    r = r0
    v = v0
    trajectory = [r.copy()]
    
    for _ in range(num_steps):
        r, v = rk4_step(r, v, dt)
        trajectory.append(r.copy())
    return np.array(trajectory)

# Example initial conditions:
# Start at an altitude of 300 km above Earth's surface
altitude = 300e3
r0 = np.array([R_earth + altitude, 0.0])  # starting on the x-axis
# Initial velocity magnitude and direction
# For a circular orbit at this altitude: v = sqrt(G*M/(R_earth+altitude))
v_circular = np.sqrt(G * M_earth / (R_earth + altitude))
# We give the payload a slight delta to see different trajectories
v0 = np.array([0.0, 1.05 * v_circular])  # 5% above circular speed

# Simulation parameters
dt = 1.0       # time step in seconds
total_time = 6000.0  # total simulation time in seconds

trajectory = simulate_trajectory(r0, v0, dt, total_time)

# Plotting the trajectory
plt.figure(figsize=(8,8))
plt.plot(trajectory[:,0], trajectory[:,1], label='Payload trajectory')
# Plot Earth for reference
theta = np.linspace(0, 2*np.pi, 100)
x_earth = R_earth * np.cos(theta)
y_earth = R_earth * np.sin(theta)
plt.fill(x_earth, y_earth, 'b', alpha=0.3, label='Earth')
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Trajectory of a Freely Released Payload Near Earth')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()
```


### Explanation

- **Initialization:**  
  The payload starts at a specified altitude above the Earth’s surface. The initial velocity is set to be 5% above the circular orbit speed to illustrate a case that might transition from a bound orbit to an escape scenario if increased further.
  
- **Numerical Integration:**  
  The RK4 method is implemented in the `rk4_step` function to update the position and velocity at each time step.
  
- **Visualization:**  
  The resulting trajectory is plotted against a representation of Earth. An elliptical path would indicate a bound orbit; if the payload were to have exactly the escape velocity, the trajectory would be parabolic, while a higher velocity would yield a hyperbolic escape path.

---

## 4. Trajectory Analysis

- **Orbital Insertion:**  
  For a payload to be inserted into a stable orbit, its speed must be below the escape velocity, resulting in an elliptical (or circular) orbit. The simulation helps adjust the velocity vector to achieve the desired orbit.

- **Reentry Scenarios:**  
  If the payload’s trajectory intersects Earth’s surface (or if aerodynamic drag is considered in more advanced models), it may result in reentry. This typically requires a lower perigee in an elliptical orbit or an incorrect initial velocity direction.

- **Escape Trajectories:**  
  If the payload’s speed exceeds the local escape velocity, the simulation will show a hyperbolic path, meaning the payload will eventually leave Earth’s gravitational influence.

---
[Simulation](PayloadSimualtion.html)

## 5. Conclusion

By numerically integrating the equations of motion using a method such as RK4, we can simulate the trajectory of a payload released near Earth. Adjusting the initial conditions (position, velocity magnitude, and direction) allows exploration of different orbital regimes—from bound elliptical orbits to escape trajectories. This analysis is essential for mission planning in spaceflight, whether for orbital insertion, reentry, or escape missions.

