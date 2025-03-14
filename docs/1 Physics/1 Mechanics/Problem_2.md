# Problem 2

### 1. Theoretical Foundation

#### Differential Equation

The motion of a forced damped pendulum is governed by the following nonlinear second-order differential equation:


$$ \frac{d^2\theta}{dt^2} + b \frac{d\theta}{dt} + \frac{g}{L} \sin\theta = F \cos(\omega t) $$


Where:

- $\theta$ = angular displacement (radians)


- $b$ = damping coefficient (s⁻¹)


- $g$ = gravitational acceleration (9.81 m/s²)


- $L$ = pendulum length (m)


- $F$ = amplitude of the external forcing (s⁻²)


- $\omega$ = driving frequency (rad/s)


- $t$ = time (s)

This equation includes:

- Damping term: $b \frac{d\theta}{dt}$


- Restoring force (nonlinear): $\frac{g}{L} \sin\theta$


- External forcing: $F \cos(\omega t)$


#### Small-Angle Approximation

For small angles ($\theta \ll 1$), 
$\sin\theta \approx \theta$, 
simplifying the equation to a linear forced damped oscillator:

$$ \frac{d^2\theta}{dt^2} + b \frac{d\theta}{dt} + \omega_0^2 \theta = F \cos(\omega t) $$


Where
 $\omega_0 = \sqrt{\frac{g}{L}}$ is the natural frequency.

The general solution is the sum of the homogeneous and particular solutions:

- Homogeneous: 


$$\theta_h(t) = A e^{-\frac{b}{2}t} \cos(\omega_r t + \phi)$$


, where 


$$\omega_r = \sqrt{\omega_0^2 - \left(\frac{b}{2}\right)^2}$$


- Particular: 

$$\theta_p(t) = A_p \cos(\omega t - \delta)$$

, where:

  - $$A_p = \frac{F}{\sqrt{(\omega_0^2 - \omega^2)^2 + (b\omega)^2}}$$

  - $$\delta = \tan^{-1}\left(\frac{b\omega}{\omega_0^2 - \omega^2}\right)$$


#### Resonance Conditions

Resonance occurs when the driving frequency $\omega$ approaches the natural frequency $\omega_0$. 
The amplitude $A_p$ peaks when $\omega = \omega_r$, leading to maximum energy transfer from the driving force to the pendulum. 
For low damping, this is close to $\omega_0$. 
This amplification is critical in systems where energy buildup is desired or must be avoided.

---

### 2. Analysis of Dynamics

#### Parameter Influence

- **Damping Coefficient ($b$)**: Higher $b$ reduces amplitude and prevents chaos by dissipating energy faster. Low $b$ allows sustained oscillations or chaotic behavior.

- **Driving Amplitude ($F$)**: Small $F$ leads to regular motion; large $F$ can push the system into chaos by overcoming the restoring force.

- **Driving Frequency ($\omega$)**: Near $\omega_0$, resonance amplifies motion. Far from $\omega_0$, motion may be quasiperiodic or chaotic depending on $F$ and $b$.


#### Transition to Chaos

- For small $F$ and $b$, motion is periodic or quasiperiodic.

- As $F$ increases, the nonlinear $\sin\theta$ term dominates, leading to bifurcations and eventually chaos.

- Chaos is characterized by sensitivity to initial conditions, visible in phase space as a strange attractor.

---

### 3. Practical Applications

- **Energy Harvesting**: Piezoelectric devices use forced oscillations to convert mechanical energy to electrical energy.

- **Suspension Bridges**: External forces (wind) can drive oscillations; Tacoma Narrows Bridge collapse (1940) is a famous example of resonance gone wrong.

- **Oscillating Circuits**: LC circuits with external driving mimic pendulum dynamics, used in signal processing.

---

### 4. Implementation

Here’s a JavaScript simulation using HTML5 canvas to model and visualize the forced damped pendulum. It includes phase plots and allows parameter adjustment:

[Simulation](Simulation_2.html)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Forced Damped Pendulum Simulator</title>
    <style>
        canvas { border: 1px solid black; }
        .controls { margin: 20px 0; }
        #container { display: flex; }
    </style>
</head>
<body>
    <div class="controls">
        <label>Damping (b): <input type="number" id="damping" value="0.2" min="0" max="2" step="0.1"></label>
        <label>Forcing Amp (F): <input type="number" id="force" value="1.2" min="0" max="5" step="0.1"></label>
        <label>Forcing Freq (ω): <input type="number" id="freq" value="1.0" min="0" max="5" step="0.1"></label>
        <button onclick="startSimulation()">Start</button>
        <button onclick="stopSimulation()">Stop</button>
    </div>
    <div id="container">
        <canvas id="pendulumCanvas" width="400" height="400"></canvas>
        <canvas id="phaseCanvas" width="400" height="400"></canvas>
    </div>

    <script>
        const pendulumCanvas = document.getElementById('pendulumCanvas');
        const phaseCanvas = document.getElementById('phaseCanvas');
        const pCtx = pendulumCanvas.getContext('2d');
        const phCtx = phaseCanvas.getContext('2d');

        const g = 9.81, L = 1.0;
        const scale = 150;
        let theta = 0.1, omega = 0, t = 0;
        let animationFrameId = null;

        class Pendulum {
            constructor(b, F, omega_d) {
                this.b = b;
                this.F = F;
                this.omega_d = omega_d;
            }

            update(dt) {
                const d2theta = -g/L * Math.sin(theta) - this.b * omega + this.F * Math.cos(this.omega_d * t);
                omega += d2theta * dt;
                theta += omega * dt;
                t += dt;
                // Wrap theta to [-π, π]
                if (theta > Math.PI) theta -= 2 * Math.PI;
                if (theta < -Math.PI) theta += 2 * Math.PI;
            }
        }

        function drawPendulum(pendulum) {
            pCtx.clearRect(0, 0, pendulumCanvas.width, pendulumCanvas.height);
            pCtx.save();
            pCtx.translate(200, 50);
            pCtx.beginPath();
            pCtx.moveTo(0, 0);
            const x = scale * Math.sin(theta);
            const y = scale * Math.cos(theta);
            pCtx.lineTo(x, y);
            pCtx.stroke();
            pCtx.beginPath();
            pCtx.arc(x, y, 10, 0, 2 * Math.PI);
            pCtx.fillStyle = 'red';
            pCtx.fill();
            pCtx.restore();
        }

        function drawPhase(pendulum) {
            const x = 200 + 100 * theta / Math.PI;
            const y = 200 + 50 * omega;
            phCtx.fillStyle = 'rgba(0, 0, 255, 0.1)';
            phCtx.beginPath();
            phCtx.arc(x, y, 1, 0, 2 * Math.PI);
            phCtx.fill();
        }

        function startSimulation() {
            if (animationFrameId) cancelAnimationFrame(animationFrameId);
            const b = parseFloat(document.getElementById('damping').value);
            const F = parseFloat(document.getElementById('force').value);
            const omega_d = parseFloat(document.getElementById('freq').value);
            const pendulum = new Pendulum(b, F, omega_d);
            theta = 0.1; omega = 0; t = 0;
            phCtx.clearRect(0, 0, phaseCanvas.width, phaseCanvas.height);
            
            let lastTime = performance.now();
            function animate(currentTime) {
                const dt = (currentTime - lastTime) / 1000;
                pendulum.update(dt);
                drawPendulum(pendulum);
                drawPhase(pendulum);
                lastTime = currentTime;
                animationFrameId = requestAnimationFrame(animate);
            }
            animationFrameId = requestAnimationFrame(animate);
        }

        function stopSimulation() {
            if (animationFrameId) cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }

        // Initial draw
        const initialPendulum = new Pendulum(0.2, 1.2, 1.0);
        drawPendulum(initialPendulum);
    </script>
</body>
</html>
```

#### Features

- **Pendulum Visualization**: Shows the pendulum swinging.

- **Phase Plot**: Displays $\theta$ vs. $\omega$, revealing periodic, quasiperiodic, or chaotic behavior.

- **Controls**: Adjust damping ($b$), forcing amplitude ($F$), and frequency ($\omega$).

- **Numerical Integration**: Uses simple Euler method (for simplicity; Runge-Kutta could be added for accuracy).

#### Observations

- Try $b = 0.2$, $F = 0.5$, $\omega = 1.0$ for periodic motion.

- Increase $F = 1.5$ or more for chaotic behavior (phase plot shows a strange attractor).



6. Conclusion

The forced damped pendulum serves as a powerful model for studying nonlinear dynamics, resonance, and chaos. Through analytical methods and computational simulations, we gain deeper insight into its behavior, with broad applications in engineering, physics, and applied mathematics.


