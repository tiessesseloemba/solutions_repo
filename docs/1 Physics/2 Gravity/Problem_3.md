# Problem 3

# Trajectories of a Freely Released Payload Near Earth

Let’s tackle this task comprehensively by analyzing the trajectories of a freely released payload near Earth, performing a numerical analysis, discussing the implications for space missions, and developing a computational tool to simulate and visualize the motion.
 We'll use HTML and JavaScript to create an interactive simulation.

---

### 1. Analysis of Possible Trajectories

When a payload is released from a moving rocket near Earth, its trajectory is determined by its initial position, velocity, and the gravitational force of Earth. 
The possible trajectories can be classified based on the payload’s specific mechanical energy ($\epsilon$):


- **Elliptical Trajectory ($\epsilon < 0$)**:
 If the payload’s energy is negative, it follows a closed, elliptical orbit around Earth. This occurs when the initial velocity is less than the escape velocity but sufficient to maintain an orbit (e.g., greater than the circular orbit velocity at that altitude). 
 This is typical for orbital insertion scenarios, like deploying a satellite into Low Earth Orbit (LEO).

- **Parabolic Trajectory ($\epsilon = 0$)**: 
If the payload’s energy is exactly zero, it follows a parabolic path, just escaping Earth’s gravity to infinity with zero residual speed. 
This occurs at the escape velocity ($v_{\text{esc}} = \sqrt{\frac{2GM}{r}}$).

- **Hyperbolic Trajectory ($\epsilon > 0$)**: 
If the payload’s energy is positive, it follows an open, hyperbolic path, escaping Earth’s gravity with excess speed at infinity. 
This happens when the initial velocity exceeds the escape velocity, common in escape scenarios like interplanetary missions.


The specific energy is given by:


$$\epsilon = \frac{v^2}{2} - \frac{GM}{r} $$


where $v$ is the payload’s speed, $r$ is its distance from Earth’s center, $G$ is the gravitational constant, and $M$ is Earth’s mass. 
The trajectory type depends on whether $\epsilon$ is negative, zero, or positive.

---

### 2. Numerical Analysis to Compute the Path


To compute the payload’s path, we use numerical integration of the equations of motion under Earth’s gravity.
 The gravitational force provides an acceleration:


$$\vec{a} = -\frac{GM}{r^3} \vec{r} $$


where $\vec{r} = (x, y)$ is the position vector from Earth’s center, and $r = |\vec{r}|$.

#### Initial Conditions


- **Position**: The payload is released at an altitude $h$ above Earth’s surface, so its initial distance from Earth’s center is $r_0 = R_{\text{earth}} + h$.
 We’ll assume it starts along the x-axis for simplicity: $(x_0, y_0) = (r_0, 0)$.

- **Velocity**: The initial velocity has components $(v_x, v_y)$, which could be inherited from the rocket’s motion or imparted during release.


- **Altitude**: We’ll allow the user to specify the release altitude.

#### Numerical Integration


We use a simple Euler method for integration:

- Acceleration:
 $a_x = -\frac{GM}{r^3} x$, $a_y = -\frac{GM}{r^3} y$

- Velocity update:
 $v_x \leftarrow v_x + a_x \Delta t$, $v_y \leftarrow v_y + a_y \Delta t$

- Position update:
 $x \leftarrow x + v_x \Delta t$, $y \leftarrow y + v_y \Delta t$


This method approximates the trajectory over small time steps $\Delta t$.

---

### 3. Relation to Orbital Insertion, Reentry, or Escape Scenarios


- **Orbital Insertion**: If the payload’s velocity at release matches the circular orbit velocity ($v_{\text{circ}} = \sqrt{\frac{GM}{r}}$), it enters a circular orbit (e.g., LEO at 400 km requires ~7.67 km/s). 
Slightly lower or higher velocities result in elliptical orbits, useful for satellite deployment.

- **Reentry**: If the velocity is too low, the payload’s orbit decays, intersecting Earth’s surface (or atmosphere), leading to reentry.
For example, a suborbital trajectory with insufficient tangential velocity will fall back.

- **Escape**: If the velocity exceeds the escape velocity ($v_{\text{esc}} = \sqrt{\frac{2GM}{r}}$), the payload escapes Earth’s gravity, following a parabolic or hyperbolic path. 
At 400 km altitude, $v_{\text{esc}} \approx 10.9 \, \text{km/s}$, relevant for missions leaving Earth’s sphere of influence.

---

### 4. Computational Tool: Simulation and Visualization

[Simulation](playloadsimulation.html)



### Explanation of the Enhanced Simulation

1. **Structure**:

   - A larger `<canvas>` (1000x800 pixels) for better visibility of all trajectories.

   - A legend in the top-left corner, matching your provided image.

   - Controls for adjusting altitudes and velocities for LEO, MEO, GEO, and escape trajectory.

   - Checkboxes to toggle visibility of each trajectory.

   - Buttons to update the simulation or reset the escape trajectory.


2. **Trajectories**:

   - **Low Earth Orbit (LEO)**: Green dot orbiting at 400 km altitude (default velocity 7.67 km/s, circular at this altitude).

   - **Medium Earth Orbit (MEO)**: Red dot at 20,000 km (default velocity 3.87 km/s).

   - **Geostationary-like Orbit (GEO)**: Blue dot at 35,786 km (default velocity 3.07 km/s, matching GEO velocity).

   - **Escape Trajectory**: Yellow dot starting at Earth’s surface with escape velocity (default 11.19 km/s), following a hyperbolic path.


3. **Physics**:


   - **Circular Orbits (LEO, MEO, GEO)**: Simplified as circular paths with user-defined velocities. Angular speeds are scaled for visibility.

   - **Escape Trajectory**: Uses numerical integration (Euler method) to compute the path under gravity, with acceleration $a = -\frac{GM}{r^2}$.

4. **Features**:


   - **Adjustable Parameters**: Users can set altitudes (km) and velocities (km/s) for each orbit.

   - **Visibility Toggles**: Checkboxes to show/hide LEO, MEO, GEO, or escape trajectory.

   - **Real-Time Data**: Each dot displays its current speed and altitude.

   - **Reset Escape**: Restarts the escape trajectory without affecting the circular orbits.

   - **Trails**: The escape trajectory has a yellow trail; circular orbits don’t need trails since they’re repetitive.


5. **Interaction**:

   - Default settings produce stable circular orbits for LEO, MEO, and GEO, and an escape trajectory.
   - Change LEO velocity to 5 km/s: The green dot will fall back to Earth (reentry scenario).
   - Increase escape velocity to 15 km/s: The yellow dot escapes faster.
   - Toggle off MEO to focus on other trajectories.

---

### Expected Output

- **Canvas**:
  - A blue Earth at the center.

  - **LEO**: Green dot orbiting quickly at 400 km.

  - **MEO**: Red dot orbiting slower at 20,000 km.

  - **GEO**: Blue dot orbiting slowest at 35,786 km.

  - **Escape**: Yellow dot escaping with a trail, starting at Earth’s surface.

  - Each dot has a label showing speed (km/s) and altitude (km).

- **Controls**:

  - Adjust altitudes and velocities to explore different scenarios (e.g., elliptical orbits, reentry, faster escape).

  - Toggle visibility to focus on specific trajectories.

![alt text](<DALL·E 2025-03-21 09.25.50 - A space simulation illustration featuring Earth as a blue globe in the center against a black space background with stars. Various orbital paths are d.webp>)
---


