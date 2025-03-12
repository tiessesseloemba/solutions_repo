# Problem 1
### 1. Theoretical Foundation

#### Deriving the Equations of Motion

Projectile motion can be analyzed by breaking it into horizontal and vertical components. Assuming no air resistance, the only acceleration is due to gravity, which acts downward.

- **Horizontal Motion:**
  - Acceleration: $a_x = 0$
  - Velocity: $v_x = v_0 \cos(\theta)$
  - Position: $x(t) = v_0 \cos(\theta) \cdot t$

- **Vertical Motion:**
  - Acceleration: $a_y = -g$
  - Velocity: $v_y = v_0 \sin(\theta) - g \cdot t$
  - Position: $y(t) = v_0 \sin(\theta) \cdot t - \frac{1}{2} g t^2$

#### Time of Flight

The time of flight $T$ is the time it takes for the projectile to return to the ground. This occurs when $y(T) = 0$:

$$
0 = v_0 \sin(\theta) \cdot T - \frac{1}{2} g T^2
$$

Solving for $T$:

$$
T = \frac{2 v_0 \sin(\theta)}{g}
$$

#### Range

The horizontal range $R$ is the distance traveled during the time of flight:

$$
R = v_x \cdot T = v_0 \cos(\theta) \cdot \frac{2 v_0 \sin(\theta)}{g} = \frac{v_0^2 \sin(2\theta)}{g}
$$

### 2. Analysis of the Range

#### Dependence on Angle of Projection

The range $R$ is given by:

$$
R = \frac{v_0^2 \sin(2\theta)}{g}
$$

- **Maximum Range:** The maximum range occurs when $\sin(2\theta) = 1$, which happens at $\theta = 45^\circ$.

- **Symmetry:** The range is the same for angles $\theta$ and $90^\circ - \theta$.

#### Influence of Initial Velocity and Gravitational Acceleration

- **Initial Velocity $v_0$:** The range is proportional to the square of the initial velocity. Doubling $v_0$ quadruples the range.

- **Gravitational Acceleration $g$:** The range is inversely proportional to $g$. On a planet with lower gravity, the range would be greater.

### 3. Practical Applications

#### Uneven Terrain

If the projectile is launched from a height $h$ above the ground, the range equation becomes more complex. The time of flight and range would need to account for the additional height.

#### Air Resistance

In real-world scenarios, air resistance cannot be ignored. It introduces a drag force that opposes the motion, reducing the range. The equations of motion would need to include a drag term, making them more complex and typically requiring numerical methods for solution.

### 4. Implementation

#### Computational Tool

A simple Python script can be used to simulate and visualize projectile motion:

```python
import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, theta, g=9.81, h=0):
    theta_rad = np.radians(theta)
    t_flight = (v0 * np.sin(theta_rad) + np.sqrt((v0 * np.sin(theta_rad))**2 + 2 * g * h)) / g
    t = np.linspace(0, t_flight, num=500)
    x = v0 * np.cos(theta_rad) * t
    y = h + v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    return x, y

def plot_trajectory(v0, angles, g=9.81, h=0):
    plt.figure(figsize=(10, 5))
    for angle in angles:
        x, y = projectile_motion(v0, angle, g, h)
        plt.plot(x, y, label=f'{angle}°')
    plt.title('Projectile Motion')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
v0 = 50  # initial velocity in m/s
angles = [30, 45, 60]  # angles in degrees
plot_trajectory(v0, angles)
```

#### Visualization

This script plots the trajectory of a projectile for different angles of projection. You can adjust the initial velocity, angles, and other parameters to see how they affect the range and trajectory.

### Conclusion

By deriving the equations of motion and analyzing the range as a function of the angle of projection, we gain a deeper understanding of projectile motion. This foundational knowledge can be extended to more complex scenarios, such as accounting for air resistance or uneven terrain, and can be effectively visualized using computational tools.