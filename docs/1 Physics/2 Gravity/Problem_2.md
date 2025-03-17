# Problem 2

# **Escape Velocities and Cosmic Velocities**  


## **Motivation**  


The concept of **escape velocity** is fundamental in astrophysics and space exploration. 
It determines the minimum speed required for an object to break free from a celestial body's gravitational pull. 

Expanding on this, the **first, second, and third cosmic velocities** define the speed thresholds needed for stable orbit, escape from a planet, and even escape from an entire star system. 
These principles are essential for launching satellites, interplanetary missions, and potential future interstellar travel.  

## **Definitions of Cosmic Velocities**  


1. **First Cosmic Velocity (Orbital Velocity, $v_1$)**  


   - The minimum speed needed for an object to stay in a **stable circular orbit** around a celestial body without propulsion.  

   - Derived from balancing **gravitational force** and **centripetal force**:  


     $$
     v_1 = \sqrt{\frac{GM}{r}}
     $$


   - Example: A satellite in **low Earth orbit** (LEO) must travel at **~7.91 km/s**.  



2. **Second Cosmic Velocity (Escape Velocity, $v_2$)**  


   - The speed required to **escape completely** from a planet’s gravitational influence.  

   - Derived from **energy conservation** (gravitational potential energy vs. kinetic energy):  


     $$
     v_2 = \sqrt{\frac{2GM}{r}}
     $$


   - It is **$\sqrt{2}$ times** the first cosmic velocity. 

   - Example: On Earth, $v_2 \approx 11.2$ km/s, meaning a rocket must reach this speed to leave Earth without further propulsion.  



3. **Third Cosmic Velocity (Stellar Escape Velocity, $v_3$)**  


   - The speed needed to escape **the gravitational pull of the entire solar system** (or another star system).  

   - Depends on **both the Sun’s gravity** and the **planet’s position** in its orbit:  


     $$
     v_3 = \sqrt{v_2^2 + v_s^2}
     $$


     where $v_s$ is the planet’s orbital velocity around the Sun.  


   - Example: To **leave the Solar System from Earth’s orbit**, $v_3 \approx 42.1$ km/s.  


## **Mathematical Analysis & Visualization**  


Below is a Python script to calculate and plot the **first, second, and third cosmic velocities** for different celestial bodies (**Earth, Mars, and Jupiter**).  


[Simulation](Python_simulation.py)

### **Python Simulation**  
```python
import numpy as np
import matplotlib.pyplot as plt

# Define gravitational constant (G) in m³/kg/s²
G = 6.67430e-11 

# Define celestial bodies with (mass in kg, radius in meters)
celestial_bodies = {
    "Earth": (5.972e24, 6.371e6),
    "Mars": (6.417e23, 3.389e6),
    "Jupiter": (1.898e27, 6.9911e7),
}

# Calculate cosmic velocities
velocities = {}
for body, (M, R) in celestial_bodies.items():
    v1 = np.sqrt(G * M / R) / 1000  # First cosmic velocity in km/s
    v2 = np.sqrt(2 * G * M / R) / 1000  # Second cosmic velocity in km/s
    v3 = np.sqrt(v2**2 + (29.78 if body == "Earth" else 24.07 if body == "Mars" else 13.06)**2)  # Third cosmic velocity in km/s
    velocities[body] = (v1, v2, v3)

# Plot results
bodies = list(velocities.keys())
v1_values, v2_values, v3_values = zip(*velocities.values())

x = np.arange(len(bodies))

plt.figure(figsize=(10,6))
plt.bar(x - 0.2, v1_values, width=0.2, label="First Cosmic Velocity (km/s)", color='blue')
plt.bar(x, v2_values, width=0.2, label="Second Cosmic Velocity (km/s)", color='red')
plt.bar(x + 0.2, v3_values, width=0.2, label="Third Cosmic Velocity (km/s)", color='green')

plt.xticks(x, bodies)
plt.ylabel("Velocity (km/s)")
plt.title("Cosmic Velocities for Different Celestial Bodies")
plt.legend()
plt.grid(axis='y')
plt.show()
```

### **Interpretation**  


- **Jupiter has the highest escape velocity** (~60 km/s) due to its massive gravitational field.  


- **Mars has a much lower escape velocity** (~5 km/s), making it easier for spacecraft to launch from its surface. 


- **The third cosmic velocity is highest for Earth** (~42 km/s) because it includes both Earth’s escape velocity and its orbital speed around the Sun.  



## **Space Exploration Applications**  


- **Launching satellites**: The **first cosmic velocity** determines the speed needed for stable orbits (e.g., ISS at ~7.66 km/s).  


- **Interplanetary missions**: The **second cosmic velocity** is crucial for rockets escaping planetary gravity (e.g., Apollo missions).  


- **Leaving the Solar System**: Probes like **Voyager 1 & 2** reached the **third cosmic velocity** to exit the Solar System.  



## **Conclusion**  


The concept of **cosmic velocities** is fundamental for space travel. Understanding these speed thresholds allows engineers to design missions that **place satellites in orbit, send spacecraft to Mars, and even explore beyond the Solar System**. 🚀