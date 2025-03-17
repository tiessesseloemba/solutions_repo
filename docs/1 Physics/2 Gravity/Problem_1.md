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


Since orbital period $T$ is given by $T = \frac{2\pi r}{v}$, 

substituting $v$:

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


This simulation visually demonstrates **Kepler's Third Law**, which states that the square of a planet's orbital period is proportional to the cube of its orbital radius.  



#### **How the Simulation Works:** 


1. A **yellow Sun** is fixed at the center.  

2. A **blue planet** orbits around the Sun in a circular trajectory.  

3. The **slider** allows you to adjust the **orbital radius** (the distance from the Sun).  

4. The **planet moves slower in a larger orbit** and faster in a smaller orbit, illustrating Kepler’s law.  


#### **Key Observations:**  


- As the **orbit increases**, the planet’s speed **decreases** because a larger orbit requires a longer period to complete.  

- The relationship between **radius and speed** follows the equation:  

  $$
  T^2 \propto r^3
  $$

- This is the same principle used by astronomers to predict **planetary motion, satellite orbits, and exoplanet detection**.  




## Conclusion


Kepler's Third Law elegantly connects orbital mechanics with fundamental gravitational principles. This computational approach reinforces the relationship between the orbital period and radius, supporting its use in astronomy, satellite deployment, and astrophysical research.

