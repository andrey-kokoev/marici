## 1920s: the step-by-step progression from Hamiltonian to QM

| Step | Year | What was added | Key formula | Conceptual leap |
|---|---|---|---|---|
| **Hamiltonian mechanics** | 1833 | Phase space \((q,p)\), Poisson bracket, generating functions | \(\{q_i,p_j\}=\delta_{ij}\), \(H(q,p,t)\) | State = point in phase space. Dynamics = Hamiltonian flow. |
| **Bohr–Sommerfeld quantization** | 1913–1924 | Action quantization on periodic orbits | \(\oint p\,dq = n\hbar\) | Not all actions are allowed—only discrete multiples of \(\hbar\). |
| **Heisenberg matrix mechanics** | 1925 | Observables as matrices; non-commutativity | \(pq - qp = \frac{\hbar}{i}\) | Position and momentum cannot be simultaneously numbers. The Poisson bracket becomes a commutator. |
| **Schrödinger wave mechanics** | 1926 | Wavefunction \(\psi(q,t)\); complex amplitude | \(i\hbar\frac{\partial\psi}{\partial t}=H\psi\) | The state is not a point—it is a complex field. Dynamics is linear. |
| **Born rule** | 1926 | Probability = \(|\psi|^2\) | \(P(a)=|\langle a|\psi\rangle|^2\) | The wavefunction does not describe reality directly—it gives probabilities for measurement outcomes. |
| **Dirac transformation theory** | 1927 | Unification: canonical quantization | \(\{,\}\to\frac{[,]}{i\hbar}\) | Matrix and wave mechanics are the same formalism. Quantization is a rule for turning classical into quantum. |
| **von Neumann axiomatization** | 1932 | Hilbert space, spectral theorem, measurement | \(\rho\), projectors \(E_i\) | QM is a closed mathematical system: Hilbert space + Hermitian operators + Born rule + projection postulate. |
| **Feynman path integral** | 1948 | Amplitude = sum over paths | \(\langle b|a\rangle=\int\mathcal Dq\;e^{iS/\hbar}\) | The action itself becomes the exponent of the fundamental amplitude. No operator needed. |

## Our path: what is kept, what is skipped, what is removed

| Our step | What we add | Analogue in the 1920s | What we **do not** add |
|---|---|---|---|
| **Declared Clifford algebra** | \(e_1^2=e_2^2=1,\;J^2=-1\) | Phase space (real, no probability) | No non-commutativity; our algebra is still a matrix algebra, not an abstract operator algebra. |
| **Connection \(\alpha = d\varphi-\beta/\kappa\)** | Geometric extension of phase space | Feynman's \(e^{iS/\hbar}\) (both are exponentials of action-like integrals) | No complex amplitude; \(\int\alpha\) is a real geometric quantity. |
| **\(\kappa\) as action–phase scale** | Conversion factor (like \(\hbar\)) | Planck's constant | \(\kappa\) is not Planck's constant—it is uncalibrated and geometric. |
| **Finite discrete carrier (4-point source)** | Exact algebraic skeleton | No analogue in QM | QM starts from continuous Hilbert space. We start from a finite set. |
| **Retained histories** | Full typed composition record | No analogue | QM replaces history with wavefunction collapse. We keep every step. |
| **4\(\pi\) minimal period** | Spinor structure from cocycle | Spinor in QM (Dirac 1928) | Both have 4\(\pi\) spinor period. But we derive it from the cocycle, not from representation theory. |
| **Complementarity \(V^2+D^2=1\)** | From positive Gram alone | Born's probability interpretation | We get the **same mathematical relation** as QM, but from counting, not from probability amplitudes. |
| **No probability** | ... | Born rule (1926) | **We stop here.** Probability is not derived, not assumed, not needed. The carrier is deterministic. Uncertainty only enters if we forget information. |

**The key divergence:** in 1926, Born added probability as a primitive postulate. We do not. Our complementarity relation comes from the Gram determinant—the same algebraic source as \(V^2+D^2=1\) in QM—but we interpret it geometrically, not statistically. The "probability" in QM is replaced by rational counting ratios when coarse-graining, and by nothing at all when the full typed history is retained.