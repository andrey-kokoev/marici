# Marici · Physics from one object

**Marici relational carrier**

## Relational carrier: physics from one object

A single 4-point carrier $\mathrm{Bool} \times \mathrm{Bool}$ with automorphism group $S_4$ and overlap matrix $G_{ij} = \langle f_j \mid f_i \rangle$ gives quantum mechanics, general relativity, the Standard Model, and connections across mathematics — all from the same overlap structure.

### Physics

| Role | Name |
|------|------|
| Physics | Connected |
| | QM, GR, SM (8 sectors), cosmology (5 epochs), Larmor, Spin, Beta decay, EPR, Mach, $\Omega_b$, $\Omega_{\mathrm{DM}}$, $\Omega_{\mathrm{de}}$ |

### Mathematics

| Role | Name |
|------|------|
| Mathematics | Connected |
| | Boolean algebra, CFT, category theory, algebraic geometry, modular forms, homotopy theory, knot theory, TQFT, division algebras, ML, and more |

### Constants

| Role | Name |
|------|------|
| Constants | Derived |
| | $137, \quad \sin^2\theta = \frac{3}{13}, \quad \text{Yukawa} \times 6, \quad m_H = 125\,\mathrm{GeV}, \quad \Lambda_{\mathrm{QCD}}, \quad m_p = 938\,\mathrm{MeV}, \quad \frac{m_p}{m_e} = 1836$ |
| | $\delta_{\mathrm{CKM}} \ (\sim 1.3\%), \quad \delta_{\mathrm{PMNS}} \ (\text{exact}), \quad y_t = 1, \quad \Lambda, \quad \frac{M_{\mathrm{Pl}}}{v} = 11^{15} \times 12 \times Z$ |
| | $\Omega_b = \frac{6}{121}, \quad \Omega_{\mathrm{DM}} = \frac{6}{23}, \quad \Omega_{\mathrm{de}} = \frac{11}{16}$ |

[View the complete results](/results/)

---

**Cross-sector bridges**

## Postnikov descent

QM ↔ GR, couplings ↔ masses, Planck ↔ weak, DM ↔ DE ↔ baryons, Mach ↔ GR, baryogenesis ↔ PMNS, Larmor ↔ Newton ↔ Einstein, flavor ↔ gauge, CC ↔ holography, control theory ↔ Machian bootstrap. The same carrier descent, the same four Gram numbers, the same Postnikov tower at every bridge.

[Read the full Postnikov descent →](/results/#bridges)

---

**Control theory reframing**

## The universe as a feedback system

The four Gram numbers are pole locations; $\varepsilon = \frac{1}{90} - \frac{1}{5280}$ is the feedback gain; $Z = \frac{1}{1+\varepsilon}$ is the closed-loop transfer function. The integral term drives $\Omega_k \to 0$, the fibration phases are Nyquist margins, and the flavor puzzle is an LQR Riccati equation. The Gram-based constants and dynamics expressed in the language of classical control.

[Read the full control theory reframing →](/results/#control)

---

**Falsifiable predictions**

## Predictions

Each prediction is a rational expression in $11, 12, 4, 10$. Most predictions have no free parameters; $\delta_{\mathrm{CKM}}$ has a $\pi/3$ base angle that is numerically close but not Gram-derived. The experiments that can confirm or falsify them exist or are under construction.

### CMB-S4 / Simons Obs.
$\Omega_k = \frac{91}{44528} = 0.002$

The cosmic budget from Gram ratios leaves a deficit of $\frac{91}{44528}$ for spatial curvature. Planck 2018 gives $\Omega_k = -0.001 \pm 0.002$ — $\Omega_k = +0.002$ is within $1.5\sigma$. Next-generation CMB experiments at 0.1% precision will resolve this.

### DUNE / Hyper-K
$\delta_{\mathrm{PMNS}} = \frac{12}{10}\pi = 216^\circ$

Exact Gram expression. Current global fits place $\delta_{\mathrm{PMNS}}$ near $220^\circ$; DUNE and Hyper-Kamiokande will measure it to $\pm 5^\circ$ within a decade.

### LHCb / Belle II
$\delta_{\mathrm{CKM}} \approx \frac{\pi}{3} + \left(\frac{4}{12}\right)^2 = 66.4^\circ$

Within 1.3% of observed $65.5^\circ$. The $(4/12)^2$ term is Gram-derived; the base $\pi/3$ is numerically close but not Gram-derived. LHCb and Belle II will refine to sub-degree precision.

### Penning traps
$\frac{m_p}{m_e} = 12 \times (12^2 + 3^2) = 1836$

Already within 0.01% of observed $1836.15$. Deviations would reveal new physics in the carrier overlap structure.

### HL-LHC / FCC
$m_H = 11^2 + 4 = 125\,\mathrm{GeV}$

Current measurement $125.1\,\mathrm{GeV}$ is within 0.08%. Future colliders measure to $10\,\mathrm{MeV}$ precision, testing at 0.01%.

### Space-based tests
Machian $G$ varies at $10^{-4}$ level

The bootstrap $Z = \frac{1}{1 + 1/90 - 1/5280}$ predicts $G$ is shielded by all matter. MICROSCOPE follow-on and atom interferometry can detect this.

### Dark matter mechanism
Particle DM _vs_ Machian inertia

$\Omega_{\mathrm{DM}} = \frac{6}{23} = 0.2609$ (observed $0.264$, 1.2% error) fits both sterile neutrinos (X-ray lines) and modified inertia (scale-dependent $G$). X-ray lines confirm particles; scale-dependent $G$ with no X-ray lines confirms Machian inertia. Both cannot be true.

[View the complete results & predictions](/results/)

---

**Full derivation**

## From $\mathrm{Bool} \times \mathrm{Bool}$ to physics: the relational carrier: read the derivation.

Derivation covering the carrier, overlap matrix, and three projections (QM, GR, SM) plus connections to mathematics and physics domains. Multiple verification scripts and result files confirm every expression.

✓ Formally verified in Cubical Agda: [RelationalCarrier.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/RelationalCarrier.agda) (107 proof files, composed). Lean: [probe kernel](https://github.com/andrey-kokoev/marici/blob/main/research/buzzard/Entry2125.lean), [predictions (ℚ)](https://github.com/andrey-kokoev/marici/blob/main/research/buzzard/marici_formal/MariciFormal/PhysicsPredictions.lean).

[Read the full relational carrier derivation →](/theory/)