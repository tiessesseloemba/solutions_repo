# Problem 1



### 1. Theoretical Foundation

#### Deriving the Equations of Motion

Projectile motion is governed by Newton’s laws under constant gravitational acceleration, assuming no air resistance for now. We start with the basic setup: a projectile is launched from the origin (x₀ = 0, y₀ = 0) with an initial velocity $v_0$ at an angle $\theta$ above the horizontal. Gravity acts downward with acceleration $g$.

The initial velocity has components:
- $v_{0x} = v_0 \cos\theta$ (horizontal)
- $v_{0y} = v_0 \sin\theta$ (vertical)

Since there’s no horizontal acceleration (ignoring air resistance), the horizontal motion is:
- $x(t) = v_{0x} t = v_0 \cos\theta \cdot t$

Vertically, gravity accelerates the projectile downward:

- Acceleration: $a_y = -g$
- Velocity: $v_y(t) = v_{0y} - g t = v_0 \sin\theta - g t$
- Position: $y(t) = v_{0y} t - \frac{1}{2} g t^2 = v_0 \sin\theta \cdot t - \frac{1}{2} g t^2$

This comes from solving the differential equation
 $\frac{d^2 y}{dt^2} = -g$, with initial conditions $y(0) = 0$ and $$\frac{dy}{dt}(0) = v_0 \sin\theta$$. The solution is a parabola, which makes sense—projectiles trace parabolic paths.

#### Family of Solutions

The parameters $v_0$, $\theta$, and $g$ define a family of trajectories. For a fixed $g$ (e.g., 9.8 m/s² on Earth), varying $v_0$ scales the size of the parabola, while $\theta$ adjusts its shape and orientation. If we include initial height $h$ (i.e., $y_0 = h$), the vertical equation becomes:
- $$y(t) = h + v_0 \sin\theta \cdot t - \frac{1}{2} g t^2$$
This shifts the parabola upward, affecting the range, as we’ll see.

---

### 2. Analysis of the Range

#### Range as a Function of Angle
The range $R$ is the horizontal distance traveled when the projectile returns to $y = 0$ (assuming it lands at the same height as launch). Set $y(t) = 0$:
- $$0 = v_0 \sin\theta \cdot t - \frac{1}{2} g t^2$$
- Factor out $t$: $$t (v_0 \sin\theta - \frac{1}{2} g t) = 0$$

Solutions:
- $t = 0$ (launch)
- $t = \frac{2 v_0 \sin\theta}{g}$ (landing time)

Plug this time into the horizontal equation:

- $R = x\left(\frac{2 v_0 \sin\theta}{g}\right) = v_0 \cos\theta \cdot \frac{2 v_0 \sin\theta}{g}$
- $R = \frac{2 v_0^2 \sin\theta \cos\theta}{g}$


Using the identity $\sin 2\theta = 2 \sin\theta \cos\theta$:
- $$R = \frac{v_0^2 \sin 2\theta}{g}$$

This is the range equation. It’s maximized when $\sin 2\theta = 1$, so $2\theta = 90^\circ$, or $\theta = 45^\circ$. Thus, the maximum range is:
- $$R_{\text{max}} = \frac{v_0^2}{g}$$

The range is symmetric: $$R(\theta) = R(90^\circ - \theta)$$, e.g., $\theta = 30^\circ$ and $60^\circ$ yield the same range.

#### Influence of Parameters
- **Initial Velocity ($v_0$)**: Range scales with $v_0^2$. Double $v_0$, and $R$ quadruples.
- **Gravity ($g$)**: Range is inversely proportional to $g$. On the Moon ($g \approx 1.62 \, \text{m/s}^2$), range is about 6 times greater than on Earth.
- **Launch Height**: If $y_0 = h$, the time to land comes from the quadratic $$h + v_0 \sin\theta \cdot t - \frac{1}{2} g t^2 = 0$$. Solving this adjusts $R$, typically increasing it for $h > 0$.

---

### 3. Practical Applications

#### Uneven Terrain
If the projectile lands at a different height (e.g., $y = -H$ for a cliff), adjust the range calculation. Solve:
- $$-H = v_0 \sin\theta \cdot t - \frac{1}{2} g t^2$$
This gives a quadratic in $t$, and the range depends on both $\theta$ and $H$, often favoring steeper angles for downward trajectories.

#### Air Resistance
With drag (proportional to velocity, say $F_d = -k v$), the equations become nonlinear differential equations:
- $m \frac{d v_x}{dt} = -k v_x$
- $m \frac{d v_y}{dt} = -m g - k v_y$
Analytic solutions are complex, but numerically, drag reduces range and shifts the optimal angle below 45°, depending on $k$.

#### Real-World Examples
- **Sports**: A soccer ball’s range varies with kick angle and spin (Magnus effect adds complexity).
- **Artillery**: Gunners adjust $\theta$ based on terrain and wind.
- **Spacecraft**: Launch angles optimize orbital insertion, though gravity isn’t constant.

---

### 4. Implementation

#### Computational Tool
Here’s a Python script using NumPy and Matplotlib to simulate and visualize the range vs. angle:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
v0 = 20.0  # initial velocity (m/s)
g = 9.8    # gravity (m/s^2)
theta_deg = np.linspace(0, 90, 91)  # angles from 0° to 90°
theta_rad = np.radians(theta_deg)

# Range function
R = (v0**2 * np.sin(2 * theta_rad)) / g

# Plot
plt.figure(figsize=(8, 6))
plt.plot(theta_deg, R, label=f'v₀ = {v0} m/s, g = {g} m/s²')
plt.xlabel('Angle of Projection (degrees)')
plt.ylabel('Range (meters)')
plt.title('Range vs. Angle of Projection')
plt.grid(True)
plt.legend()
plt.show()

# Maximum range
max_idx = np.argmax(R)
print(f"Maximum range: {R[max_idx]:.2f} m at {theta_deg[max_idx]}°")
```

#### Visualization
- Run this with different $v_0$ (e.g., 10, 20, 30 m/s) or $g$ (e.g., 1.62 m/s² for the Moon).
- The plot shows a peak at 45°, with range dropping symmetrically on either side.

#### Enhancements
- Add height: Modify $t$ and $R$ calculations.
- Simulate trajectories: Plot $x(t)$ vs. $y(t)$ for various $\theta$.

---

### Conclusion
The range’s dependence on $\theta$ is a beautiful blend of trigonometry and physics, peaking at 45° under ideal conditions. Parameters like $v_0$ and $g$ scale the result, while real-world factors like height or drag enrich the problem. This framework scales from classroom demos to rocket science—pretty cool for a simple parabola