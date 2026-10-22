# Oral Presentation
## Introduction - Quantum Motion in a Uniform Magnetic Field
Hello, my name is Ali. Today I will talk about the quantum mechanics of a charged particle moving in a magnetic field.

## Why study this problem?
Charged particles in magnetic fields are everywhere:
- The Northern Lights happen because electrons spiral along Earth's magnetic field
- Particle accelerators use magnetic fields to bend particle paths
- MRI machines use strong magnetic fields to image the human body

## Background: What we need to know
A particle with charge $q$ moving at velocity $\vec{v}$ in an electromagnetic field is subject to the general \underline{\textbf{Lorentz Force}}:
\vfill
\[\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})\]\vfill
$E$ the electric field, $B$ the magnetic field, $q$ the charge of the particle and $\vec{v}$ the velocity of the particle.

## Example: Classical Motion
Let's see what this means in practice... [Video]
Classically, the particle performs a cyclotron orbit. The radius depends on the velocity.

## The Question [Unveiling]
Classically, as we saw, the energy is continuous. The particle can orbit at any radius, with any velocity, so it can have any energy it wants.

[CLICK]
But what happens in Quantum Mechanics?

[CLICK]
The central question of this project is: **How does the Magnetic Field quantize energy?**

## The Vector Potential
Since B is divergence free, we can write it as the curl of a vector potential $\vec{A}$
The choice of A is not unique, this is called the gauge freedom.
There are many gauges (Coulomb gauge, Lorenz gauge, etc.) but the one we'll be using today is the Landau gauge.
\[ \vec{A} = (0, Bx, 0) \]

## Deriving the Classical Hamiltonian
We know the total energy of a system is the sum of the kinetic energy and the potential energy. In a general electromagnetic field, this would be the kinetic energy plus the electric potential energy $q\phi$. Note that the magnetic field itself does no work, so it adds no scalar potential term. 

Now, in Hamiltonian mechanics, the momentum $\vec{p}$ is not just mass times velocity ($m\vec{v}$). It is the **canonical momentum**, which includes a contribution from the vector potential: $\vec{p} = m\vec{v} + q\vec{A}$.

Why is this the correct momentum and Hamiltonian?  
We can verify this rigorously using **Hamilton's equations**.

First, we calculate the velocity $\dot{\vec{r}}$ by taking the derivative with respect to momentum ($\nabla_p H$).
Then, we calculate how momentum changes over time $\dot{\vec{p}}$ using the spatial derivative ($-\nabla_r H$).

When we combine these results to find the acceleration ($m\vec{a} = m\ddot{\vec{r}}$), the terms simplify perfectly to give us exactly the Lorentz Force law:
\[ \vec{F} = m\vec{a} = q(\vec{E} + \vec{v} \times \vec{B}) \]

Since it reproduces the correct equation of motion, we know this Hamiltonian is valid.

So, to find the Hamiltonian...
This gives us the general Hamiltonian: $H = \frac{1}{2m}(\vec{p} - q\vec{A})^2 + q\phi$.

## Quantum Mechanics Setup
To move to quantum mechanics, we use a procedure called **Canonical Quantization**. 
The idea is simple but powerful: we take our classical "variables" and promote them to "operators."

1.  The position $\vec{r}$ becomes the position operator $\hat{\vec{r}}$.
2.  The momentum $\vec{p}$ becomes the momentum operator $\hat{\vec{p}}$. In position space, this is the gradient: $\hat{\vec{p}} = -i\hbar\nabla$.

We then take these operators and plug them directly into the Classical Hamiltonian we just proved. This gives us our **Quantum Hamiltonian** Operator $\hat{H}$.

## Hamiltonian under Landau Gauge
Now, how do we solve for the dynamics?
In classical mechanics, we use Newton's laws. In quantum mechanics, the equivalent is the **Schrödinger Equation**:
\[ \hat{H}\psi = E\psi \]
This equation tells us the stationary states of the system—the allowed energy levels $E$ that the electron can occupy.

Substituting our specific Hamiltonian (with the Landau Gauge) into this equation gives us the specific differential equation we need to solve.

## Solving the Equation
We are now looking for solutions to the Schrödinger equation we just derived. Notice something interesting about our Hamiltonian: it contains the operators for $y$ and $z$ derivatives (momentum), but it doesn't contain the coordinates $y$ or $z$ themselves. The magnetic field effect depends only on $x$.

In quantum mechanics, when the Hamiltonian is independent of a coordinate, the corresponding momentum is a **conserved quantity**. This implies that $p_y$ and $p_z$ are constants of the motion.

We can exploit this symmetry using an **ansatz**—an educated guess for the wavefunction's form. We choose a solution that looks like a free plane wave in the $y$ and $z$ directions:
\[ \psi(\vec{r}) = e^{i(p_y y + p_z z)/\hbar} \psi(x) \]

When we plug this ansatz back into the Schrödinger equation, the $y$ and $z$ derivatives turn into simple constants ($p_y$ and $p_z$).


## Result: Landau Levels
Now, let's look at the 1D part of the equation we are left with.
If we map the terms carefully, we see something remarkable.
We have a kinetic energy term $\frac{p_x^2}{2m}$ and an effective potential term $\frac{1}{2}m\omega_c^2(x-x_0)^2$.

Does this combination look familiar? It is exactly the Hamiltonian of a **Quantum Harmonic Oscillator**!
The only difference is that the oscillator is shifted to a center position $x_0$, which is determined by the momentum $p_y$.

Because we know the solution to the harmonic oscillator, we don't need to do any more hard work. We can simply write down the energy eigenvalues immediately.
The total energy is the standard harmonic oscillator spectrum $\hbar\omega_c(n + 1/2)$, plus the free kinetic energy from the motion in the $z$-direction.
\[ E_{n, p_z} = \hbar\omega_c\left(n + \frac{1}{2}\right) + \frac{p_z^2}{2m} \]

These discretized energy levels are called **Landau Levels**.

Crucially, notice that the energy does NOT depend on $x_0$, and therefore it does not depend on the momentum $p_y$. This means that many different states (spiraling around different centers $x_0$) all have the exact same energy. This massive **degeneracy** is a fundamental property of Landau levels and is key to understanding phenomena like the Quantum Hall Effect.

## Energy Levels
Let's visualize the key difference between classical and quantum energy levels.

On the left, we have the **classical** picture. In classical mechanics, the electron can orbit at any radius, and therefore it can have any continuous value of energy. The energy spectrum is a smooth continuum.

On the right, we have the **quantum** picture—the Landau Levels we just derived. The energy is now **quantized** into discrete, evenly-spaced levels separated by $\hbar\omega_c$. The electron can only exist in one of these specific energy states, not in between.

This quantization is a purely quantum mechanical effect. It arises because the cyclotron motion becomes a quantum harmonic oscillator, and harmonic oscillators have discrete energy levels. At low temperatures and strong magnetic fields, this discreteness becomes dominant and leads to dramatic effects like the Quantum Hall Effect.

## The Complete Wavefunction
Here is the full mathematical solution. 
Notice the structure: we have plane waves for the free motion in y and z.
And in the x-direction, we have the harmonic oscillator functions.

The key takeaway here is the **Degeneracy**. The center of the spiral, x0, depends on momentum. But the Energy does not. This means you can slide the spiral anywhere in the sample, and the energy stays the same.

## Outlook & Reflection
Next steps would include checking spin (Zeeman effect) and what happens at the edges of the sample.
A self-criticism: I should have explored the Symmetric Gauge to show that the physics doesn't change.

## Takeaway
1. Magnetic Field makes things go in circles (Cyclotron).
2. Quantum Mechanics turns those circles into discrete steps (Landau Levels).
3. This is the foundation of the Quantum Hall Effect.

## Q&A - Auxiliary Slides

### Q1: Why Landau Gauge?
I chose the Landau gauge (0, Bx, 0) because it simplifies the math by separating the variables. It breaks rotational symmetry but makes the Hamiltonian easy to solve. The Symmetric gauge preserves rotation but requires polar coordinates. The physics is the same.

### Q2: Degeneracy
The degeneracy is massive. It's proportional to the magnetic flux. Basically, you can fit one quantum state for every "flux quantum" that passes through your sample. For a real lab magnet, that's billions of states.

### Q3: Zero Point Energy?
Does the electron stop at absolute zero? No. Just like the harmonic oscillator, there is a zero-point energy of 1/2 h-bar omega_c. The uncertainty principle forbids it from sitting still.

### Q4: Edge States?
At the edges of the sample, the potential shoots up. This bends the energy levels upwards. The electrons there don't spiral in circles; they skip along the wall. These "skipping orbits" conduct electricity even when the bulk is insulating. This is the edge current of the Quantum Hall Effect.
