import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration in m/s^2
v0 = 20    # initial velocity in m/s

# Function to calculate the range
def range_of_projectile(v0, theta, g):
    return (v0**2 * np.sin(2 * np.radians(theta))) / g

# Angles of projection (0 to 90 degrees)
angles = np.linspace(0, 90, 100)

# Calculate range for each angle
ranges = range_of_projectile(v0, angles, g)

# Plotting the range as a function of angle
plt.plot(angles, ranges)
plt.title(f"Range of a Projectile vs. Launch Angle\nInitial Velocity: {v0} m/s")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Range (meters)")
plt.grid(True)
plt.show()