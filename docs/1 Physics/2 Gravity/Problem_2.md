# Problem 2

# **Escape Velocities and Cosmic Velocities**  


Let’s explore the fascinating concepts of escape velocity and the first, second, and third cosmic velocities, derive their mathematical foundations, calculate them for Earth, Mars, and Jupiter, visualize the results, and discuss their significance in space exploration.


### Definitions and Physical Meaning

1. **First Cosmic Velocity ($v_1$) - Orbital Velocity**:


   - **Definition**: 
   The minimum speed required for an object to achieve a stable circular orbit around a celestial body at a low altitude (near the surface, neglecting atmospheric drag).

   - **Physical Meaning**:
    This is the speed at which the centrifugal force balances the gravitational pull, allowing an object to circle the body without falling back or escaping.



2. **Second Cosmic Velocity ($v_2$) - Escape Velocity**:


   - **Definition**:
    The speed needed to completely escape a celestial body’s gravitational influence, starting from its surface, without further propulsion.

   - **Physical Meaning**:
    At this velocity, an object’s kinetic energy equals the gravitational potential energy binding it to the body, allowing it to reach infinity with zero residual speed.



3. **Third Cosmic Velocity ($v_3$) - System Escape Velocity**:


   - **Definition**: 
   The speed required to escape the gravitational influence of a star system (e.g., the Solar System), typically starting from a planet’s surface or orbit.

   - **Physical Meaning**:
    This velocity accounts for escaping both the planet’s gravity and the star’s gravity, relevant for interstellar travel.

### Mathematical Derivations

#### First Cosmic Velocity ($v_1$)


For a circular orbit near the surface (radius $R$), the gravitational force provides the centripetal force:


$$ \frac{G M m}{R^2} = \frac{m v_1^2}{R} $$


Cancel $m$ and simplify:


$$ v_1^2 = \frac{G M}{R} $$


$$ v_1 = \sqrt{\frac{G M}{R}} $$


- $G$: Gravitational constant ($6.6743 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$)


- $M$: Mass of the celestial body


- $R$: Radius of the body



#### Second Cosmic Velocity ($v_2$)


Escape velocity comes from energy conservation. At the surface, total mechanical energy is:



$$ E = K + U = \frac{1}{2} m v_2^2 - \frac{G M m}{R} $$



To escape, energy must be zero at infinity (where $U = 0$, $v = 0$):


$$ \frac{1}{2} m v_2^2 - \frac{G M m}{R} = 0 $$



$$ \frac{1}{2} v_2^2 = \frac{G M}{R} $$



$$ v_2 = \sqrt{\frac{2 G M}{R}} $$


Notice: $v_2 = \sqrt{2} \cdot v_1$.



#### Third Cosmic Velocity ($v_3$)



This is more complex, as it involves escaping the star’s gravity (e.g., the Sun) from a planet’s orbit.

 Assuming launch from the planet’s surface to escape the Solar System:


- Escape from the planet to infinity relative to the planet.

- Then, escape the Sun’s gravity from the planet’s orbital distance ($r$) from the Sun.

Total energy must overcome both potentials:


$$ \frac{1}{2} m v_3^2 - \frac{G M m}{R} - \frac{G M_{\text{Sun}} m}{r} = 0 $$


$$ v_3 = \sqrt{\frac{2 G M}{R} + \frac{2 G M_{\text{Sun}}}{r}} $$


For simplicity, if starting from Earth’s orbit (1 AU), we often compute it from Earth’s orbital velocity around the Sun 
($v_{\text{orb}} = \sqrt{\frac{G M_{\text{Sun}}}{r}} \approx 29.8 \, \text{km/s}$) 
and add the additional speed to reach the Sun’s escape velocity ($\sqrt{2} \cdot v_{\text{orb}} \approx 42.1 \, \text{km/s}$), adjusted for Earth’s gravity.



### Calculations for Earth, Mars, and Jupiter


Using:


- $G = 6.6743 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$


- Earth: $M = 5.972 \times 10^{24} \, \text{kg}$, $R = 6.371 \times 10^6 \, \text{m}$, $r = 1 \, \text{AU} = 1.496 \times 10^{11} \, \text{m}$


- Mars: $M = 6.417 \times 10^{23} \, \text{kg}$, $R = 3.39 \times 10^6 \, \text{m}$, $r = 1.524 \, \text{AU}$


- Jupiter: $M = 1.898 \times 10^{27} \, \text{kg}$, $R = 6.991 \times 10^7 \, \text{m}$, $r = 5.203 \, \text{AU}$


- Sun: $M_{\text{Sun}} = 1.989 \times 10^{30} \, \text{kg}$



#### Earth


- $v_1 = \sqrt{\frac{6.6743 \times 10^{-11} \cdot 5.972 \times 10^{24}}{6.371 \times 10^6}} \approx 7.91 \, \text{km/s}$


- $v_2 = \sqrt{\frac{2 \cdot 6.6743 \times 10^{-11} \cdot 5.972 \times 10^{24}}{6.371 \times 10^6}} \approx 11.19 \, \text{km/s}$


- $v_3$: From surface to Solar System escape: $v_{\text{Sun escape}} = \sqrt{\frac{2 \cdot 6.6743 \times 10^{-11} \cdot 1.989 \times 10^{30}}{1.496 \times 10^{11}}} \approx 42.1 \, \text{km/s}$, combined: 

$v_3 \approx \sqrt{11.19^2 + (42.1 - 29.8)^2} \approx 16.6 \, \text{km/s}$ (approximate, from orbit).

#### Mars


- $v_1 = \sqrt{\frac{6.6743 \times 10^{-11} \cdot 6.417 \times 10^{23}}{3.39 \times 10^6}} \approx 3.55 \, \text{km/s}$


- $v_2 = \sqrt{2} \cdot 3.55 \approx 5.02 \, \text{km/s}$


- $v_3$: Sun escape at 1.524 AU: 

$\sqrt{\frac{2 G M_{\text{Sun}}}{1.524 \cdot 1.496 \times 10^{11}}} \approx 34.1 \, \text{km/s}$, orbital velocity $24.1 \, \text{km/s}$, 
combined:

 $\sqrt{5.02^2 + (34.1 - 24.1)^2} \approx 11.2 \, \text{km/s}$.



#### Jupiter


- $v_1 = \sqrt{\frac{6.6743 \times 10^{-11} \cdot 1.898 \times 10^{27}}{6.991 \times 10^7}} \approx 42.6 \, \text{km/s}$


- $v_2 = \sqrt{2} \cdot 42.6 \approx 60.2 \, \text{km/s}$


- $v_3$: Sun escape at 5.203 AU:

 $\sqrt{\frac{2 G M_{\text{Sun}}}{5.203 \cdot 1.496 \times 10^{11}}} \approx 18.5 \, \text{km/s}$, orbital velocity $13.1 \, \text{km/s}$, combined: 
 
 $\sqrt{60.2^2 + (18.5 - 13.1)^2} \approx 60.5 \, \text{km/s}$.




### Importance in Space Exploration

1. **Launching Satellites**:


   - $v_1$ (e.g., 7.91 km/s for Earth) is critical for low Earth orbit (LEO). Rockets like Falcon 9 exceed this to place satellites in orbit.



2. **Missions to Other Planets**:


   - $v_2$ (11.19 km/s for Earth) is needed to escape Earth. For Mars missions, additional delta-v adjusts for Mars’ lower $v_2$ (5.02 km/s), using Hohmann transfers leveraging orbital mechanics.


3. **Interstellar Travel**:


   - $v_3$ (16.6 km/s from Earth) is the threshold for leaving the Solar System. Voyager probes achieved this via gravity assists, as chemical rockets alone can’t reach it directly from Earth’s surface.



These velocities shape mission design, fuel requirements, and trajectories, making them foundational to exploring our cosmic neighborhood and beyond.



[Simulation](Simulationescape_.html)



**Interpretation of the Escape and Orbital Velocities Simulation**

This simulation illustrates the fundamental concepts of escape and orbital velocities for different celestial bodies, such as Earth, the Moon, and Mars. It provides a visual representation of an orbiting object and a comparative analysis of the velocities required for stable orbit and escape from gravitational influence.

### Key Observations:
1. **Orbital Visualization**: The left panel depicts a simplified representation of an orbiting object around the selected celestial body. The blue (or corresponding color) circle represents the planet or moon, while the green and red circles indicate the first cosmic velocity (orbital velocity) and the second cosmic velocity (escape velocity), respectively.

2. **Velocity Comparison**: The right panel presents a bar chart comparing the first (V1) and second (V2) cosmic velocities. The first cosmic velocity (V1) is the minimum speed required for an object to maintain a stable circular orbit, while the second cosmic velocity (V2) is the speed needed to break free from the celestial body's gravitational pull.

### Interpretation:
- **Higher Mass, Higher Velocities**: More massive celestial bodies, such as Earth, have higher gravitational forces, requiring greater velocities to achieve orbit or escape.
- **Lower Gravity, Lower Velocities**: Smaller bodies like the Moon require significantly lower velocities due to their weaker gravitational fields.
- **Applications in Space Missions**: Understanding these velocities is crucial for designing space missions, satellite launches, and interplanetary travel. Achieving the correct velocity ensures that a payload reaches its intended orbit or successfully escapes into space.

This simulation enhances comprehension of gravitational physics and celestial mechanics, aiding in the visualization of key orbital principles.


