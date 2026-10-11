# Gram Unification of QM, GR, and the Standard Model

**Historical index, not a verified unification.** The continuum-completion claim
and the conclusion that only source admission/precision/inflation remain are
superseded by `continuum-embedding-evidence-boundary.md` (7 October 2026).
The actual finite implementations do not establish the cited metric limit;
the stated interpolant fails even on a constant metric. Accordingly the
all-three-theories completion claim is withdrawn. Other sectors below are
historical assertions, not newly verified results. The original index is
hash-preserved in `quarantine/20261007-continuum-evidence/`.

**S4 correction:** `s4-gram-action-comparison.md` reuses the already completed
witness construction and compares it with the original full operator Gram.
Its conjugation doublet is not the asserted four-state matter decomposition;
the dependent SM/generation claims are withdrawn, not blocked only on admission.

## Historical overview (not current disposition)

One mathematical object—the Gram matrix \(G_{ij} = \langle f_j | f_i \rangle\) of a finite carrier \(X_N\) with automorphism group \(S_N\)—produces all three layers of fundamental physics through sector decomposition.

## Core chain

| Step | Result | Artifact |
|---|---|---|
| Foundation | Carrier from Bool×Bool, probes, Gram, automorphism group, fibration rotation | `foundational-derivation-boolxbool-to-gram.md` |
| Gram selection principle | N-path interference from Gram overlaps, Born rule as rank-1 factorization | `gram-selection-principle.md`, `checkers/check_gram_selection_principle.py` |
| LQG connection | Holonomy-flux algebra matches, SU(2) promotion forced by cocycle | `lqg-structural-analogy.md`, `checkers/check_holonomy_flux_algebra.py` |
| Machian metric | \(g_{ab}(p) = G_{ab}\) from stabilizer Gram | `machian-metric.md`, `checkers/check_machian_metric.py` |
| ADM constraints | (+++-) signature from 24 S4 elements, constraint algebra closes | `formal-adm-constraint-derivation.md`, `checkers/check_discrete_constraint_algebra.py` |
| Continuum limit | **Withdrawn:** literal interpolation does not even reproduce a constant metric; finite code supplies no replacement | `continuum-embedding-evidence-boundary.md` |
| SM gauge group | **Withdrawn identification.** Natural S4 is 1+3; valid witness and operator doublets have different actions and no selected matter map. | `s4-gram-action-comparison.md`; `weak-doublet-singlet-weight-and-s4-representation-audit.md` |
| CKM mixing | Gram misalignment between up/down bases: \(\theta_{12}\approx13^\circ\) | `checkers/check_gram_entries.py`, `checkers/check_mass_diagonalization.py` |
| PMNS mixing | Gram misalignment in lepton sector: \(\theta_{12}\approx34^\circ\) | `checkers/check_pmns_from_gram.py` |
| 3 generations | **Not selected.** The retained arrow source has a canonical three-matching quotient, not independently derived S4^3 matter factors. The old subgroup count is wrong. | `twelve-arrow-blocks-and-generation-selection.md` |
| Anomaly cancellation | All 6 Ward identities pass per generation (16 states = SO(10) spinor) | `checkers/check_anomaly_cancellation.py` |
| Higgs mechanism | Off-diagonal Gram block between S4 doublet (2) and singlets (1ₐ,1_b) | `checkers/check_higgs_mechanism.py` |
| Dark matter | 3 ν_R sterile neutrinos, 25% of Gram trace → \(\Omega_{\text{DM}}\approx 0.27\) | `dark-matter-as-gram-remainder.md`, `checkers/check_dark_matter_abundance.py` |
| Dark energy | Uniform diagonal Gram entries from transitivity → \(\Lambda\) | `machian-metric.md` |
| Strong CP / axion | U(1) phase mode of Gram, QCD instantons relax \(\theta̅\to0\) | `checkers/check_strong_cp.py` |
| Baryogenesis | Leptogenesis via ν_R decays, n_b/n_γ ∼ 10⁻⁸ | `checkers/check_baryogenesis.py` |
| Entanglement | Gram non-separability → CHSH violation, S = 2√2 | `checkers/check_entanglement.py` |
| Hawking radiation | Thermal Gram at horizon, \(T_H = 1/(8\pi GM)\), unitarity by Gram trace conservation | `checkers/check_hawking_radiation.py` |
| Carrier hierarchy | **Withdrawn physical minimality claim.** The old size tables printed supplied assignments; their evidence entry points are quarantined. | `twelve-arrow-blocks-and-generation-selection.md` |

## Historical carrier hierarchy (not a prediction)

The block/action/count comparison above supersedes this table. Equivalent
relabelled partitions do not count as different physical generations.

| Points | Automorphism | Physics | Minimal for |
|---|---|---|---|
| 4 | S4 | SU(3)×SU(2)×U(1), 1 generation | SM gauge group |
| 8 | S8 | 2 gen + Z2 mirror (twin Higgs) | Mirror symmetry |
| **12** | **S12** | **3 gen, no extra sectors** | **Observed generations** |
| 16 | S16 | 4 gen or SO(10) GUT | GUT |
| 4n | S4n | n SM generations | — |

## Results (JSON, in `results/`)

| File | Content |
|---|---|
| `carrier-minimality.json` | Old output path absent at correction; its producer is quarantined, not a minimality certificate |
| `S7_S8_carrier_structure.json` | S7, S8 irrep decompositions |
| `S9_carrier.json` | S9 branching, twin Higgs lost |
| `S16_carrier.json` | S16 → SO(10) GUT connection |
| `S12-dark-matter-prediction.json` | \(\Omega_{\text{DM}}\) = 25% from Gram trace |
| `dark-sector-portal.json` | 5th point portal coupling |
| `pmns-from-gram-misalignment.json` | PMNS from Gram off-diagonals |
| `higgs-from-gram.json` | Higgs as Gram connector |
| `strong-cp-axion-from-gram.json` | Axion as U(1) Gram phase mode |
| `baryogenesis-from-gram.json` | Leptogenesis from ν_R |
| `hawking-from-gram.json` | Thermal Gram at horizon |
| `entanglement-from-gram.json` | CHSH violation from Gram non-separability |

## Connectivity audit

| Domain | Element | Status |
|---|---|---|
| QM | Born rule, interference, entanglement, uncertainty | ✅ |
| GR | Claimed metric-to-continuum chain | **Not established; continuum construction refuted.** Other listed identifications need independent evidence. |
| SM | Claimed carrier-to-matter chain | **Not derived.** Finite action comparison is constructed; physical representation/kinetic selection is not supplied. |
| Cosmology | Dark matter (ν_R), dark energy (Λ), baryogenesis (leptogenesis) | ✅ |
| QG | Hawking radiation, information paradox, discrete carrier unitarity | ✅ |

## Historical remaining-gate list (superseded)

The missing typed comparison and failed interpolant are mathematical defects,
not merely an admission decision. The following old list was not sufficient:

- **Source admission**: the epistemic graph has not authorized the 12-point carrier as the physical positive pairing
- **Finite-checker precision**: some checkers pass numerically but could benefit from formal proof
- **Inflation mechanism**: the early-universe exponential expansion is not explicitly placed in the carrier