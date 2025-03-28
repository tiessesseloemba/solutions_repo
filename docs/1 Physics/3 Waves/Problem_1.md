# Problem 1


## Chapter: Wave Interference

### Introduction to Wave Interference

**Definition of Interference**  

Wave interference occurs when two or more waves overlap in space, combining to form a new wave pattern. This phenomenon arises from the **superposition principle**, which states that the total displacement at any point is the sum of the displacements of the individual waves at that point. 

Interference can result in regions where waves reinforce each other (constructive interference) or cancel each other out (destructive interference).


**Key Concepts**  

1. **Superposition Principle**: 

For $N$ waves, the total displacement is:

   $$
   \eta_{\text{sum}}(x, y, t) = \sum_{i=1}^N \eta_i(x, y, t)
   $$


   where $\eta_i(x, y, t)$ is the displacement due to the $i$-th wave.


2. **Types of Interference**:


   - **Constructive Interference**: Occurs when waves are in phase (phase difference is an integer multiple of $2\pi$), leading to increased amplitude.


   - **Destructive Interference**: Occurs when waves are out of phase (phase difference is an odd multiple of $\pi$), leading to cancellation.



3. **Coherence**: Stable interference patterns require coherent waves, meaning they have the same frequency and a constant phase relationship.


4. **Wave Parameters**:


   - **Amplitude ($A$)**: Maximum displacement of the wave.

   - **Wavelength ($\lambda$)**: Distance between consecutive crests.

   - **Frequency ($f$)**: Number of cycles per second.

   - **Wave Number ($k$)**: $k = \frac{2\pi}{\lambda}$.

   - **Angular Frequency ($\omega$)**: $\omega = 2\pi f$.

   - **Phase ($\phi$)**: Initial offset of the wave cycle.


5. **Circular Waves in 2D**:
 For a point source on a water surface, the wave propagates as a circular wave, with amplitude decreasing as $\frac{1}{\sqrt{r}}$ due to energy spreading in two dimensions.
  The displacement is:

   $$
   \eta(x, y, t) = \frac{A}{\sqrt{r}} \cos(kr - \omega t + \phi)
   $$
   
   where $r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$ is the distance from the source at $(x_0, y_0)$.


**Applications**  
Interference is crucial in:

- **Optics**: Young’s double-slit experiment shows light’s wave nature.

- **Acoustics**: Sound wave interference affects audio design.

- **Water Waves**: Ripples from multiple sources create visible patterns.

- **Quantum Mechanics**: Interference of probability amplitudes.


---

## Problem: Interference Patterns on a Water Surface


### Problem Statement
Analyze the interference patterns on a water surface due to circular waves from point sources at the vertices of a regular polygon. 
The wave equation for a source at $(x_0, y_0)$ is:

$$
\eta(x, y, t) = \frac{A}{\sqrt{r}} \cos(kr - \omega t + \phi)
$$

where:

- $\eta(x, y, t)$: Displacement at $(x, y)$ at time $t$.

- $A$: Amplitude.

- $r$: Distance from the source.

- $k = \frac{2\pi}{\lambda}$: Wave number.

- $\omega = 2\pi f$: Angular frequency.

- $\phi$: Initial phase.


**Steps**:
1. Select a regular polygon.

2. Position the sources.

3. Write the wave equations.

4. Apply superposition.

5. Analyze the interference pattern.

6. Visualize the pattern (using Python and HTML/JavaScript).



**Considerations**:

- All sources have the same $A$, $\lambda$, and $f$.

- Waves are coherent ($\phi = 0$).

- Deliverables include a Python script, explanation, and graphical representation.


---

### Solution

#### Step 1: Select a Regular Polygon

Choose a **square** with 4 vertices:

- Side length $2a$, centered at the origin.

- Set $a = 1$:

  - $S_1 = (1, 1)$
  - $S_2 = (1, -1)$
  - $S_3 = (-1, 1)$
  - $S_4 = (-1, -1)$


#### Step 2: Position the Sources


Sources are at:

- Source 1: $(1, 1)$

- Source 2: $(1, -1)$

- Source 3: $(-1, 1)$

- Source 4: $(-1, -1)$


#### Step 3: Wave Equations


Set parameters:

- $A = 1$

- $\lambda = 1$, so $k = 2\pi$

- $f = 1$, so $\omega = 2\pi$

- $\phi = 0$


For each source:

- Source 1: $r_1 = \sqrt{(x - 1)^2 + (y - 1)^2}$, $\eta_1 = \frac{1}{\sqrt{r_1}} \cos(2\pi r_1 - 2\pi t)$

- Source 2: $r_2 = \sqrt{(x - 1)^2 + (y + 1)^2}$, $\eta_2 = \frac{1}{\sqrt{r_2}} \cos(2\pi r_2 - 2\pi t)$

- Source 3: $r_3 = \sqrt{(x + 1)^2 + (y - 1)^2}$, $\eta_3 = \frac{1}{\sqrt{r_3}} \cos(2\pi r_3 - 2\pi t)$

- Source 4: $r_4 = \sqrt{(x + 1)^2 + (y + 1)^2}$, $\eta_4 = \frac{1}{\sqrt{r_4}} \cos(2\pi r_4 - 2\pi t)$


#### Step 4: Superposition of Waves


$$
\eta_{\text{sum}}(x, y, t) = \sum_{i=1}^4 \frac{1}{\sqrt{r_i}} \cos(2\pi r_i - 2\pi t)
$$


At $t = 0$:


$$
\eta_{\text{sum}}(x, y, 0) = \sum_{i=1}^4 \frac{1}{\sqrt{r_i}} \cos(2\pi r_i)
$$


#### Step 5: Analyze Interference Patterns


- **Constructive Interference**: Where phases align (e.g., $2\pi (r_i - r_j) \approx 2\pi n$).


- **Destructive Interference**: Where phases differ by $\pi$ (e.g., $2\pi (r_i - r_j) \approx (2n+1)\pi$).


- **At the origin $(0, 0)$**:


  - $r_1 = r_2 = r_3 = r_4 = \sqrt{2}$

  - $\frac{1}{\sqrt{r_i}} \approx 0.841$

  - $2\pi r_i \approx 8.885$, $\cos(2\pi \sqrt{2}) \approx -0.266$

  - Total: $4 \times 0.841 \times (-0.266) \approx -0.895$ (destructive).


- **Symmetry**: The square creates a grid-like pattern with nodes along $x = 0$, $y = 0$, and diagonals.

---

## Python Simulation (Static Visualization)

Below is a Python script using Matplotlib to generate a static 2D heatmap of the interference pattern at $t = 0$. This can be included in a Jupyter Notebook or Markdown document.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1  # Amplitude
lambda_ = 1  # Wavelength
k = 2 * np.pi / lambda_  # Wave number
f = 1  # Frequency
omega = 2 * np.pi * f  # Angular frequency
t = 0  # Time snapshot

# Source positions (square vertices)
sources = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Create a grid for plotting
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Compute total displacement using superposition
for (sx, sy) in sources:
    r = np.sqrt((X - sx)**2 + (Y - sy)**2)
    # Avoid division by zero at source points
    r = np.where(r < 0.01, 0.01, r)
    Z += (A / np.sqrt(r)) * np.cos(k * r - omega * t)

# Plot the interference pattern
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=50, cmap='seismic')
plt.colorbar(label='Displacement')
plt.title('Interference Pattern from Square Sources (Python)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```
![alt text](Figure_1.png)

### Explanation of the Python Code
- **Parameters**: Set $A = 1$, $\lambda = 1$, $f = 1$, and $t = 0$.
- **Sources**: Defined as the vertices of a square.
- **Grid**: A 2D grid over $[-5, 5] \times [-5, 5]$ with 200 points in each direction.
- **Superposition**: Compute the displacement at each point by summing the contributions from all sources.
- **Visualization**: Use `contourf` to create a heatmap, with the `seismic` colormap (red for positive, blue for negative).

### Output
The script generates a static heatmap showing the interference pattern, with:
- **Red regions**: Constructive interference (positive displacement).
- **Blue regions**: Destructive interference (negative displacement).
- **White regions**: Near-zero displacement.

This plot can be embedded in a Jupyter Notebook or saved as an image for a Markdown document.



---

### Conclusion
This chapter introduced the concept of wave interference, explained the superposition principle, and demonstrated how to analyze interference patterns from multiple sources on a water surface.
 The problem was solved by choosing a square, deriving the wave equations, applying superposition, and analyzing the resulting pattern. 
 The interactive simulation provides a hands-on way to explore how changes in wavelength, frequency, and amplitude affect the interference pattern, reinforcing the theoretical concepts.

