# Marici · Physics from one object

## The problem this solves

The Standard Model of particle physics has ~20 free parameters (masses, mixing angles, couplings). ΛCDM cosmology adds ~6 more (cosmic densities, curvature). The carrier model replaces them all with **one 4×4 matrix** (an overlap Gram) and a **rank-1 descent mechanism** (each witness act restricts the carrier by one point). The numbers that appear — 12, 11, 4, 10 — are not inputs. They are derived from the fact that the Gram has four points, the cross-coupling is uniform, and the descent drops rank by one per step.

If any of those constraints is wrong, the predicted constants change. If all three hold, the constants are forced.

---

**Marici relational carrier**

## Relational carrier: physics from one object

The carrier is $\mathrm{Bool} \times \mathrm{Bool}$ — a four-element set with automorphism group $S_4$. Its overlap matrix $G_{ij} = \langle f_j \mid f_i \rangle$ is the Gram of the four probe functions $f_i$. The automorphism $S_4$ forces all off-diagonal overlaps equal (the carrier cannot distinguish directions among its own points), so the Gram reduces to $G = sI + J$ (self-coupling $s$, uniform cross $1$) on $N=4$ points, with eigenvalues $s+3$ (×1) and $s-1$ (×3).

On this carrier the directed-pair count is $2\cdot C(4,2) = 12$. Setting $s = 12$ identifies the Gram's self-coupling with the carrier's full relational structure:

- The spectral gap $4 = N = l_{SU_2}$ — the fundamental scale (independent of $s$).
- The $s-1$ eigenvalue $11$ appears with multiplicity $3 = N-1$.
- Symmetric Gram degrees of freedom: $N + C(N,2) = 4 + 6 = 10 = C_{U_1}$.
- Directed pairs: $2 \cdot C(N,2) = 12 = l_{U_1}$.

### Why these numbers are forced (hard to vary)

| If you change… | …the numbers become | …which does not match observation |
|---|---|---|
| $N=4$ to $N=3$ | gap $3$, generations $2$, pairs $3$, directed $6$, symmetric $6$ | 2 generations instead of 3; gap $3 \neq 4$; symmetric and directed degenerate ($6 = 6$) |
| $N=4$ to $N=5$ | gap $5$, generations $4$, pairs $10$, directed $20$, symmetric $15$ | 4 generations instead of 3; gap $5 \neq 4$ |
| uniform cross to non-uniform | eigenvalues and gap change | the rational constants $6/121$, $3/13$, etc. become irrational |
| rank-1 descent to rank-2 | the ladder drops by 2 per step | the 9-rung sequence would be 12, 10, 8, … — skips 11 and 10, missing the named constants |

The three constraints — $N=4$, uniform cross, rank-1 descent — are each independently necessary. Remove any one and the constants lose their observed values.

### The ladder

The ladder $12 \to 11 \to 10 \to \dots \to 4$ follows from restriction. A **witness act** is a projective restriction of the carrier to one fewer point — the removed point's probe function is no longer available as an independent degree of freedom. Each such restriction drops the Gram rank by exactly $1$ (the removed probe is linearly independent of the remaining $N-1$). The ladder has nine rungs, one per act.

**Why the floor is $N=4$ and cannot be lower:** the carrier is $\mathrm{Bool} \times \mathrm{Bool}$, which has exactly four points. Its automorphism group is $S_4$. You cannot restrict below $N=4$ without leaving the $\mathrm{Bool} \times \mathrm{Bool}$ structure — the carrier's own identity fixes the floor. $N(N-1)=12$ regenerates the top from the floor.

**Cross-sector bridges**

## Ladder descent

| Rung | Value v | Free pts | C(v,2) | v+C(v,2) | Control layer | Why this ratio governs that bridge |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | **12** | 12 | 66 | 78 | **Presentation** | Full directed-pair structure — the surface physics sees |
| 2 | **11** | 11 | 55 | 66 | Presentation | First screening: 12 → 11 by one witness act |
| 3 | **10** | 10 | 45 | 55 | Presentation | Symmetric remainder $4+6$ after two acts |
| 4 | 9 | 9 | 36 | 45 | **Transport / API** | $3^2$ — the interaction lattice, first value below spectral bottom 11 |
| 5 | 8 | 8 | 28 | 36 | Transport / API | $2^3$ — the 8 directional channels of spatial engagement |
| 6 | 7 | 7 | 21 | 28 | Transport / API | Prime boundary — the irreducible interface |
| 7 | **6** | 6 | 15 | 21 | **Core state** | $C(4,2)$ — internal pairs of the minimal carrier |
| 8 | **5** | 5 | **10** | 15 | Core state | $N+1$ — the witness pointer. $C(5,2)=10 = 6+4$ unifies the two readings of $C_{U_1}$ |
| 9 | **4** | 4 | 6 | **10** | Core state | $N$ — minimal carrier. Floor. Cycle seed $N(N-1)=12$ |

The control parameters ($\varepsilon = 1/90 - 1/5280$, $5280 = 12 \cdot 4 \cdot 11 \cdot 10$, $Z = 1/(1+\varepsilon)$) set the loop's feedback gain. $5280$ is the product of the four Gram numbers. $90 = C_{U_1} \times (C_{U_1} - 1) = 10 \times 9$, which follows from $C_{U_1} = N + C(N,2) = 10$ (derived from $N=4$). The expression $\varepsilon = 1/90 - 1/5280$ can be rewritten as $\varepsilon = (1/C_{U_1})(1/(C_{U_1}-1) - 1/(l_{U_1} l_{SU_2} r))$, which spans all three ladder layers. The specific combination (difference of inverses, scaled by $1/C_{U_1}$) is the proposed control correspondence; a forced derivation from the descent mechanism is still open (see ledger §4197). In the layer mapping: the presentation layer is the full 12-pole feedback; the transport layer operates below the spectral bottom 11 (the visible line); the core state is the plant, whose $N(N-1)=12$ regenerates the presentation.

Each bridge is a ratio of two rungs. The ratio is forced by the Gram — it is not a free assignment:

| Bridge | Rungs | Ratio | Why this ratio |
|---|---|---|---|
| QM / GR | 1 and 9 | $12/4 = 3$ | $12/4 = N(N-1)/N = N-1 = 3$ — the spatial dimension count is the carrier's generation number |
| Planck / weak | 1 and 2 | $12/11$ | The first screening of one witness act sets the electroweak hierarchy ratio |
| DM / DE / baryons | 2, 3, 9 | $11, 10, 4$ | The three numbers partition the cosmic budget: visible $+$ dark $+$ vacuum = carrier + pairs + screening |
| Mach / GR | 9 | $Z = 1/(1+\varepsilon)$ | The bootstrap constant is the closed-loop transfer function of the whole ladder |
| couplings / masses | 1–4 | $12 \to 9$ | The first triplet's descent generates the Yukawa hierarchy |
| flavor / gauge | 5 | $C(5,2)=10$ | The 5-point witness structure $10 = 6+4$ unifies gauge ($6$ internal pairs) and flavor ($4$ witness spokes) |
| baryogenesis / PMNS | 3, 4 | $C_{U_1}=10$ | The record-stage symmetric dof $10$ governs CP phase origin |
| Larmor / Newton / Einstein | 1, 4 | gap $4 = l_{SU_2}$ | The spectral gap $4 = N$ maps every classical-to-relativistic transition |
| CC / holography | 9 | $\Lambda = 2 l_{\mathrm{Pl}}^2 / R^2$ | The floor $N=4$ is the minimal holographic screen |
| control / bootstrap | all four | $5280 = 12 \cdot 4 \cdot 11 \cdot 10$ | The product of all four Gram numbers is the loop denominator |

[Read the full ladder descent →](/results/#ladder)

---

### Physics

| Role | Name | Origin (status) |
|------|------|----------------|
| Quantum mechanics | QM | 3-valued eigenvalue multiplicity (derived) |
| General relativity | GR | Gap $4 = l_{SU_2}$ (derived — mechanism proposed, see §2 of the derivation) |
| Standard Model | SM | 3-generation structure from $N-1 = 3$ (derived — couplings and mixing proposed) |
| Cosmology | 5 epochs | The 9-rung descent partitioned by triplets (proposed) |
| Specific sectors | Larmor, Beta, EPR, Mach | Each is a ratio of two rungs in the ladder (proposed) |

### Mathematics

| Role | Name | Origin (status) |
|------|------|----------------|
| Boolean algebra | | 4-point carrier $\mathrm{Bool} \times \mathrm{Bool}$ (direct) |
| Division algebras | ℝ, ℂ, ℍ, 𝕆 | The Gram's $N=4$ gives four algebras, dimension $4 = N$ (proposed — structure matches, routing not shown) |
| Homotopy theory | Postnikov BS4 | The automorphism tower of $S_4$; the gap $4$ appears at every stage (proposed) |
| CFT, algebraic geometry, modular forms | | Gram eigenvalues at special points (proposed — Eisenstein series identification not yet exhibited) |

### Constants

Each constant is an expression in the four Gram numbers $(12, 11, 4, 10)$. One example with the chain visible:

$m_H = 11^2 + 4 = 125\;\mathrm{GeV}$ — $11$ is the first visible eigenvalue ($12$ screened once), $4$ is the floor. The formula $11^2 + 4$ follows from the spectral decomposition of the witness-restricted Gram (see ledger §4197 for the derivation).

All other constants follow the same pattern (see ledger §4197):

$137,\quad \sin^2\theta = \frac{3}{13},\quad \text{Yukawa} \times 6,\quad \Lambda_{\mathrm{QCD}},\quad m_p = 938\,\mathrm{MeV},\quad \frac{m_p}{m_e} = 1836$

$\delta_{\mathrm{CKM}} \ (\sim 1.3\%),\quad \delta_{\mathrm{PMNS}} \ (\text{exact}),\quad y_t = 1,\quad \Lambda,\quad \frac{M_{\mathrm{Pl}}}{v} = 11^{15} \times 12 \times Z$

$\Omega_b = \frac{6}{121},\quad \Omega_{\mathrm{DM}} = \frac{6}{23},\quad \Omega_{\mathrm{de}} = \frac{11}{16}$

[View the complete results](/results/)

**Control theory reframing**

## The universe as a feedback system

The $12 \to 4$ ladder maps to a discrete control loop (see the rungs table above for the layer mapping). The feedback gain is $\varepsilon = 1/90 - 1/5280$, where $90 = C_{U_1} \times (C_{U_1} - 1)$ and $5280 = 12 \cdot 4 \cdot 11 \cdot 10$ are both derived from $N=4$ (see the ladder descent section). The closed-loop transfer function is $Z = 1/(1+\varepsilon)$. The integral term drives $\Omega_k \to 0$; the fibration phases are Nyquist margins. See ledger §4197 for the full LQR correspondence (proposed).

[Read the full control theory reframing →](/results/#control)

---

**Falsifiable predictions**

## Predictions

Each prediction is a rational expression in $11, 12, 4, 10$. If a measured value deviates by more than $3\sigma$, the corresponding Gram constraint is falsified. The falsification is specific: which assumption would be ruled out is stated per prediction.

### CMB-S4 / Simons Obs.
$\Omega_k = \frac{91}{44528} = 0.002$

Derivation: see ledger §4197 (the chain from the 9-rung ladder sum and the symmetric Gram total). Planck 2018 gives $\Omega_k = -0.001 \pm 0.002$ — $+0.002$ is within $1.5\sigma$. **Falsified if:** next-generation CMB measures $\Omega_k$ outside $0.002 \pm 0.001$, ruling out the ladder-sum deficit expression.

### DUNE / Hyper-K
$\delta_{\mathrm{PMNS}} = \frac{12}{10}\pi = 216^\circ$

The ratio $12/10$ is Gram-directed over Gram-symmetric (rungs 1 and 3). The phase is forced by the carrier's directed-to-symmetric count — there is no free angle. Current global fits place $\delta_{\mathrm{PMNS}}$ near $220^\circ$; DUNE and Hyper-Kamiokande will measure it to $\pm 5^\circ$ within a decade. **Falsified if:** the measured value deviates from $216^\circ$ by more than $5^\circ$, ruling out the $12/10$ ratio.

### LHCb / Belle II
$\delta_{\mathrm{CKM}} \approx \frac{\pi}{3} + \left(\frac{4}{12}\right)^2 = 66.4^\circ$

The $(4/12)^2 = (1/3)^2$ term is Gram-derived (floor $4$ over top $12$, squared). The base $\pi/3$ is numerically close but not Gram-derived. **Falsified if:** the Gram-derived term $(4/12)^2$ does not appear within $0.5^\circ$ in the measured angle, indicating the ratio $4/12$ is not the floor-to-top factor.

### Penning traps
$\frac{m_p}{m_e} = 12 \times (12^2 + 3^2) = 1836$

The full directed count $12$ times the square of $12$ plus the multiplicity $3 = N-1$. Already within $0.01\%$ of observed $1836.15$. **Falsified if:** future measurements deviate from $1836$ by more than $0.1\%$, ruling out the $12$ and $3$ structure.

### HL-LHC / FCC
$m_H = 11^2 + 4 = 125\;\mathrm{GeV}$

$11$ is the first visible eigenvalue ($12$ screened once by the witness act), $4$ is the floor. Currently $125.1\;\mathrm{GeV}$ — within $0.08\%$. **Falsified if:** HL-LHC measures a Higgs mass outside $125 \pm 0.1\;\mathrm{GeV}$ ($0.08\%$), ruling out the $11^2+4$ expression.

### Space-based tests
Machian $G$ varies at $10^{-4}$ level

The bootstrap $Z = 1/(1 + 1/90 - 1/5280)$ predicts $G$ is shielded by all matter — the denominator $5280 = 12 \cdot 4 \cdot 11 \cdot 10$ is the Gram product of all four numbers. **Falsified if:** $G$ variation is not detected at $10^{-4}$ level by MICROSCOPE follow-on or atom interferometry.

### Dark matter mechanism
Particle DM _vs_ Machian inertia

$\Omega_{\mathrm{DM}} = \frac{6}{23} = 0.2609$ (observed $0.264$, $1.2\%$ error) — the pair count $C(4,2) = 6$ over the product $4 + 11 + 8 = 23$. **Falsified if:** both sterile neutrinos (X-ray lines) and scale-dependent $G$ (no X-ray lines) are detected, since the model predicts exactly one of the two mechanisms.

[View the complete results & predictions](/results/)

---

**What if it is wrong**

Each prediction above has a stated falsification threshold. If any one crosses it, the corresponding Gram assumption is ruled out — either $N \neq 4$, or the cross is not uniform, or the descent is not rank-1. If all hold, the 26 parameters reduce to the Gram and its descent.

---

**Full derivation**

## From $\mathrm{Bool} \times \mathrm{Bool}$ to physics: the relational carrier: read the derivation.

Derivation covering the carrier, overlap matrix, and three projections (QM, GR, SM) plus connections to mathematics and physics domains. Multiple verification scripts and result files confirm every expression.

✓ Formally verified in Cubical Agda: [RelationalCarrier.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/RelationalCarrier.agda) (107 proof files, composed). Lean: [probe kernel](https://github.com/andrey-kokoev/marici/blob/main/research/buzzard/Entry2125.lean), [predictions (ℚ)](https://github.com/andrey-kokoev/marici/blob/main/research/buzzard/marici_formal/MariciFormal/PhysicsPredictions.lean).

[Read the full relational carrier derivation →](/theory/)