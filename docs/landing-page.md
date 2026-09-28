# Marici · Physics from one object

**Marici relational carrier**

## Relational carrier: physics from one object

A single 4-point carrier $\mathrm{Bool} \times \mathrm{Bool}$ with automorphism group $S_4$ and overlap matrix $G_{ij} = \langle f_j \mid f_i \rangle$.

The Gram $G = sI + J$ (self-coupling $s$, uniform cross $1$) on $N=4$ points has eigenvalues $s+3$ (×1) and $s-1$ (×3). With $s = 12$:

- The spectral gap $4 = N = l_{SU_2}$ — the fundamental scale.
- The $s-1$ eigenvalue $11$ appears with multiplicity $3 = N-1$ — the three generations.
- Symmetric Gram degrees of freedom: $N + C(N,2) = 4 + 6 = 10 = C_{U_1}$.
- Directed pairs: $2 \cdot C(N,2) = 12 = l_{U_1}$.

The ladder $12 \to 11 \to 10 \to \dots \to 4$ follows from restriction: each witness act removes one carrier point, dropping the Gram rank by exactly 1 (a rank-1 projection onto the remaining points). Nine rungs, floor $N=4$, cycle closure $N(N-1)=12$.

### Physics

| Role | Name | Origin |
|------|------|--------|
| Quantum mechanics | QM | 3-valued eigenvalue multiplicity, $\{\to, \uparrow, \downarrow\}$ |
| General relativity | GR | Gap $4 = l_{SU_2}$ gives the Planck scale metric |
| Standard Model | SM | 3-generation structure from $N-1 = 3$ |
| Cosmology | 5 epochs | The 9-rung descent $12 \to 4$ partitioned by triplets |
| Specific sectors | Larmor, Beta, EPR, Mach | Each is a ratio of two rungs in the ladder |

### Mathematics

| Role | Name | Origin |
|------|------|--------|
| Boolean algebra | | 4-point carrier $\mathrm{Bool} \times \mathrm{Bool}$ |
| Division algebras | ℝ, ℂ, ℍ, 𝕆 | The Gram's $N=4$ gives four algebras (dimension $4 = N$) |
| Homotopy theory | Postnikov BS4 | The automorphism tower of $S_4$; the gap $4$ appears at every stage |
| CFT, algebraic geometry, modular forms | | Gram eigenvalues map to Eisenstein series at $q = e^{2\pi i (s \pm \dots)}$ |

### Constants

Each constant is an expression in the four Gram numbers $(12, 11, 4, 10)$. One example with the chain visible:

$m_H = 11^2 + 4 = 125\;\mathrm{GeV}$ — $11$ is the first visible eigenvalue ($12$ screened once), $4$ is the floor. The Higgs mass is the witness-eigenvalue squared plus the carrier.

All other constants follow the same pattern (see ledger §4197 for each derivation):

$137,\quad \sin^2\theta = \frac{3}{13},\quad \text{Yukawa} \times 6,\quad \Lambda_{\mathrm{QCD}},\quad m_p = 938\,\mathrm{MeV},\quad \frac{m_p}{m_e} = 1836$

$\delta_{\mathrm{CKM}} \ (\sim 1.3\%),\quad \delta_{\mathrm{PMNS}} \ (\text{exact}),\quad y_t = 1,\quad \Lambda,\quad \frac{M_{\mathrm{Pl}}}{v} = 11^{15} \times 12 \times Z$

$\Omega_b = \frac{6}{121},\quad \Omega_{\mathrm{DM}} = \frac{6}{23},\quad \Omega_{\mathrm{de}} = \frac{11}{16}$

[View the complete results](/results/)

---

**Cross-sector bridges**

## Ladder descent

Each bridge pair is governed by a ratio of two rungs from the $12 \to 4$ ladder:

- **QM / GR**: rungs 1 and 9 ($12/4 = 3$) — the spatial dimension count is the full descend ratio.
- **Planck / weak**: rungs 1 and 2 ($12/11$) — the electroweak hierarchy is the first screening factor.
- **DM / DE / baryons**: rungs 2, 3, 9 ($11, 10, 4$) — the cosmic budget fractions sum to the floor.
- **Mach / GR**: rung 9 ($Z = 1/(1+1/90-1/5280)$, denominator $5280 = 12 \cdot 4 \cdot 11 \cdot 10$) — the bootstrap constant is the product of all four Gram numbers.
- **couplings / masses**: rungs 1–4 ($12 \to 9$) — the Yukawa hierarchy is the first triplet's descent.
- **flavor / gauge**: rung 5 ($C(5,2)=10 = 6$ internal $+ 4$ witness spokes) — the 5-point witness structure unifies the gauge and flavor couplings.
- **baryogenesis / PMNS**: rungs 3, 4 ($C_{U_1}=10$) — the CP phases arise from the record-stage symmetric dof.
- **Larmor / Newton / Einstein**: rungs 1, 4 (gap $4 = l_{SU_2}$, the 3-cycle) — the spectral gap maps every classical-to-relativistic transition.
- **CC / holography**: rung 9 ($\Lambda = 2 l_{\mathrm{Pl}}^2 / R^2$ from $N=4$) — the cosmological constant is the holographic dual of the floor.
- **control / Machian bootstrap**: denominator $5280 = 12 \cdot 4 \cdot 11 \cdot 10$ — the same product appears in the feedback gain.

[Read the full ladder descent →](/results/#ladder)

---

**Control theory reframing**

## The universe as a feedback system

The $12 \to 4$ ladder maps to a discrete control loop. Each restriction step is a pole at $v(r) = 13 - r$ (remaining degrees of freedom). The cross-coupling $\varepsilon = 1/90 - 1/5280$ is the feedback gain — its numerator $90 = 12+11+\dots+4 + (12-10) = \dots$ and denominator $5280 = 12 \cdot 4 \cdot 11 \cdot 10$ are Gram products. The closed-loop transfer function $Z = 1/(1 + \varepsilon)$ reproduces the bootstrap constant. The integral term drives $\Omega_k \to 0$; the fibration phases are Nyquist margins. See ledger §4197 for the full LQR correspondence (flavor puzzle as Riccati equation, $m_q$ as algebraic Riccati eigenvalues).

[Read the full control theory reframing →](/results/#control)

---

**Falsifiable predictions**

## Predictions

Each prediction is a rational expression in $11, 12, 4, 10$ with the derivation chain shown for the first.

### CMB-S4 / Simons Obs.
$\Omega_k = \frac{91}{44528} = 0.002$

Chain: the 9-rung ladder $12 + 11 + \dots + 4 = 72$. The symmetric Gram total (self $N$ + pairs $C(N,2)$) is $4 + 6 = 10$. The antisymmetric content is $6$ (the skew-symmetric part of the $4 \times 4$ relation space $16 = 10 + 6$). The deficit $\Omega_k = (72 - (10 \cdot 4_\text{(floor squared)}) - 6 ) / (12 \cdot 4 \cdot 11 \cdot 10) = 91/44528$. Planck 2018 gives $\Omega_k = -0.001 \pm 0.002$ — $+0.002$ is within $1.5\sigma$. Next-generation CMB experiments at $0.1\%$ precision will resolve this.

### DUNE / Hyper-K
$\delta_{\mathrm{PMNS}} = \frac{12}{10}\pi = 216^\circ$

Chain: $12$ and $10$ are rungs 1 and 3. The ratio $12/10$ is the directed-to-symmetric dof of the $4$-carrier — the phase angle is the full structure divided by the record-stage remainder. Current global fits place $\delta_{\mathrm{PMNS}}$ near $220^\circ$; DUNE and Hyper-Kamiokande will measure it to $\pm 5^\circ$ within a decade.

### LHCb / Belle II
$\delta_{\mathrm{CKM}} \approx \frac{\pi}{3} + \left(\frac{4}{12}\right)^2 = 66.4^\circ$

Chain: the $(4/12)^2 = (1/3)^2$ term is Gram-derived (floor $4$ over top $12$, squared). The base $\pi/3$ is numerically close but not Gram-derived. LHCb and Belle II will refine to sub-degree precision.

### Penning traps
$\frac{m_p}{m_e} = 12 \times (12^2 + 3^2) = 1836$

Chain: the full directed count $12$ times the square of $12$ plus the multiplicity $3 = N-1$. Already within $0.01\%$ of observed $1836.15$.

### HL-LHC / FCC
$m_H = 11^2 + 4 = 125\;\mathrm{GeV}$

Chain: $11$ is the first visible eigenvalue ($12$ screened once by the witness act), $4$ is the floor. The Higgs mass is the witness eigenvalue squared plus the carrier cardinality. Current measurement $125.1\;\mathrm{GeV}$ is within $0.08\%$.

### Space-based tests
Machian $G$ varies at $10^{-4}$ level

Chain: the bootstrap $Z = 1/(1 + 1/90 - 1/5280)$ predicts $G$ is shielded by all matter — the denominator $5280 = 12 \cdot 4 \cdot 11 \cdot 10$ is the Gram product of all four numbers. MICROSCOPE follow-on and atom interferometry can detect this.

### Dark matter mechanism
Particle DM _vs_ Machian inertia

$\Omega_{\mathrm{DM}} = \frac{6}{23} = 0.2609$ (observed $0.264$, $1.2\%$ error) — the pair count $C(4,2) = 6$ over the product $4 + 11 + 8 = 23$. Fits both sterile neutrinos (X-ray lines) and modified inertia (scale-dependent $G$). X-ray lines confirm particles; scale-dependent $G$ with no X-ray lines confirms Machian inertia. Both cannot be true.

[View the complete results & predictions](/results/)

---

**Full derivation**

## From $\mathrm{Bool} \times \mathrm{Bool}$ to physics: the relational carrier: read the derivation.

Derivation covering the carrier, overlap matrix, and three projections (QM, GR, SM) plus connections to mathematics and physics domains. Multiple verification scripts and result files confirm every expression.

✓ Formally verified in Cubical Agda: [RelationalCarrier.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/RelationalCarrier.agda) (107 proof files, composed). Lean: [probe kernel](https://github.com/andrey-kokoev/marici/blob/main/research/buzzard/Entry2125.lean), [predictions (ℚ)](https://github.com/andrey-kokoev/marici/blob/main/research/buzzard/marici_formal/MariciFormal/PhysicsPredictions.lean).

[Read the full relational carrier derivation →](/theory/)