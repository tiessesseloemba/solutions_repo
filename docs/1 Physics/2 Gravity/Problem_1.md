# Problem 1


# Orbital Period and Orbital Radius



## Motivation


The relationship between the square of the orbital period and the cube of the orbital radius, known as **Kepler's Third Law**, is fundamental in celestial mechanics.
 This simple yet powerful law provides insights into planetary motion and gravitational interactions, from local satellite orbits to cosmic-scale phenomena.
  Understanding this law enables us to determine planetary masses, distances, and orbital characteristics.

## Theoretical Foundation

### Derivation of Kepler's Third Law for Circular Orbits

Consider a planet or satellite of mass $m$ orbiting a much larger mass $M$ (e.g., a star or planet) in a circular orbit of radius $r$. 
The gravitational force provides the necessary centripetal force for circular motion:

$$
F_g = F_c
$$


From Newton's Law of Gravitation:

$$
F_g = \frac{GMm}{r^2}
$$


From the centripetal force equation:

$$
F_c = \frac{m v^2}{r}
$$


Equating both forces:

$$
\frac{GMm}{r^2} = \frac{m v^2}{r}
$$


Canceling $m$ and solving for velocity:

$$
v^2 = \frac{GM}{r}
$$


Since orbital period $T$ is given by $T = \frac{2\pi r}{v}$, substituting $v$:

$$
T^2 = \frac{4\pi^2 r^3}{GM}
$$


This confirms Kepler's Third Law:

$$
T^2 \propto r^3
$$

where the proportionality constant depends on the central mass $M$.



## Implications for Astronomy


- **Calculating planetary masses**: By measuring $T$ and $r$, astronomers estimate the mass of celestial bodies.

- **Satellite and planetary orbits**: Used in designing stable satellite orbits around Earth.

- **Extrasolar planets**: Kepler’s Law aids in identifying exoplanets through transit and radial velocity methods.



## Computational Model
Below is a Python implementation to verify Kepler’s Third Law for circular orbits:

```python
import numpy as np
import matplotlib.pyplot as plt

# Define gravitational constant and mass of central body (e.g., Sun in kg)
G = 6.67430e-11
M = 1.989e30  # Mass of the Sun

# Define a range of orbital radii (in meters)
radii = np.linspace(1e10, 1e12, 100)

# Compute orbital periods using Kepler's Third Law
periods = np.sqrt((4 * np.pi**2 * radii**3) / (G * M))

# Convert periods to years
periods_years = periods / (60 * 60 * 24 * 365.25)

# Plot T^2 vs r^3
plt.figure(figsize=(8,6))
plt.plot(radii**3, periods_years**2, label="$T^2$ vs $r^3$", color='b')
plt.xlabel("Orbital Radius Cubed ($r^3$) [m^3]")
plt.ylabel("Orbital Period Squared ($T^2$) [years^2]")
plt.title("Verification of Kepler's Third Law")
plt.legend()
plt.grid()
plt.show()
```

![alt text](image.png)


## Discussion


1. **Graphical Representation**: The linear plot of $T^2$ vs. $r^3$ confirms the expected proportionality.


2. **Extension to Elliptical Orbits**: For non-circular orbits, Kepler's Law still holds using the semi-major axis $a$ as the effective radius.


3. **Corrections for Non-Ideal Cases**:
   - Perturbations from other celestial bodies
   - Relativistic effects for strong gravitational fields


[Simulation](Simulation_1.html)


### **Interpretation of the Simulation**  


This interactive simulation visually demonstrates **Kepler’s Third Law**, which states that the square of the orbital period ($T^2$) is proportional to the cube of the orbital radius ($r^3$).
 The simulation consists of:  

1. **A Central Star (Yellow Circle)** 

   - Represents the **Sun** or another massive celestial body exerting gravitational force.  

2. **An Orbiting Planet (Blue Circle)** 

   - Moves in a circular path around the central star, following the laws of planetary motion.  

3. **Orbital Radius Slider**  

   - Allows the user to adjust the orbit size dynamically.
   - When the **radius increases**, the planet's orbit grows larger, and its velocity decreases.
   - When the **radius decreases**, the planet moves faster in its orbit.  

### **Kepler’s Third Law in Action**  

- The planet’s **orbital speed** and **orbital period** adjust according to the equation:  

 $$
  T^2 \propto r^3
  $$

  This means that if the orbital radius increases, the orbital period increases as well, but at a specific cubic rate.  

### **Observations from the Simulation**

1. **Larger Orbits → Longer Periods**  

   - When the orbital radius increases, the planet moves slower, taking more time to complete one revolution.  

2. **Smaller Orbits → Faster Motion** 

   - When the orbit is smaller, the gravitational force is stronger, making the planet move faster and complete an orbit in less time.  

### **Real-World Applications**

- **Planetary Motion:** Explains why outer planets (e.g., Jupiter, Saturn) take longer to orbit the Sun than inner planets (e.g., Mercury, Venus).  

- **Satellite Orbits:** Helps design stable satellite paths around Earth.  

- **Exoplanet Detection:** Used in astronomy to determine the mass and distance of exoplanets based on their orbits.  



## Conclusion


Kepler's Third Law elegantly connects orbital mechanics with fundamental gravitational principles. This computational approach reinforces the relationship between the orbital period and radius, supporting its use in astronomy, satellite deployment, and astrophysical research.

