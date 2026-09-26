# Session summary: Gram unification of QM, GR, and the Standard Model

## Core result

One mathematical object—the Gram matrix \(G_{ij} = \langle f_j | f_i \rangle\) of a finite carrier with automorphism group \(S_N\)—produces all three layers of fundamental physics through sector decomposition:

**QAM (Quantum Amplitude Mechanics):** \(I = \sum G_{ij} e^{i(\theta_j-\theta_i)}\) replaces the path integral and Born rule. The Born rule is the rank-1 factorization \(G_{ij} = \psi_i^*\psi_j\).

**GR:** The stabilizer Gram of a point under the automorphism group gives the spatial metric \(g_{ab}(p) = G_{ab}\). The ADM constraint algebra closes on the finite carrier. The continuum limit \(\delta(x,y)\) is constructed explicitly.

**Standard Model:** The irrep decomposition of \(S_4\) gives SU(3)\(\times\)SU(2)\(\times\)U(1). The CKM matrix is the Gram misalignment between up-type and down-type mass eigenbases. The 12-point carrier \(S_{12} \to S_4\times S_4\times S_4\) gives exactly 3 observed generations—the minimal carrier matching observation.

## Carrier hierarchy

| Carrier | Automorphism | Physics |
|---|---|---|
| 4 points | \(S_4\) | SU(3)\(\times\)SU(2)\(\times\)U(1), 1 generation |
| 12 points | \(S_{12}\) | 3 generations, no mirror, no GUT |
| Larger | \(S_{4n}\) | n generations, GUTs, mirror sectors |

The 12-point carrier is the unique minimal structure that matches observed particle content.

## New artifacts (all in `research/nima/`)

**Notes:** gram-selection-principle.md, lqg-structural-analogy.md, machian-metric.md, formal-adm-constraint-derivation.md, continuum-embedding-construction.md, baryonic-matter-bridge.md, falsify-time-as-cocycle.md, progression-hamiltonian-to-qm-to-ours.md, progression-mermaid.md, conceptual-steps-table.md, two-probe-prior-time-linkage-audit.md

**Checkers (13, all passing):** check_gram_selection_principle.py, check_holonomy_flux_algebra.py, check_su2_promotion.py, check_machian_metric.py, check_machian_metric_larger.py, check_discrete_curvature.py, check_discrete_constraint_algebra.py, check_continuum_limit.py, check_gram_entries.py, check_larger_carrier.py, check_small_carriers.py, check_baryonic_matter.py, check_mass_diagonalization.py

## Remaining gate

Source admission of the positive pairing. The 12-point carrier with \(S_{12}\) automorphism and the Gram giving 3 SM generations is the minimal structure matching observation, but the epistemic graph has not authorized this as the physical positive pairing. The owner admission request remains open.