# IRL amplitude-result replication status

## Scope

This directory now contains executable exact-arithmetic replications of selected results from:

1. N. Arkani-Hamed, Y. Bai, S. He, G. Yan, *Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet*, arXiv:1711.09102.
2. N. Arkani-Hamed et al., *The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM*, arXiv:1008.2958.

These are replications of specific formulas and structural identities, not a claim to reproduce either paper in full.

## ABHY benchmarks

- Four-point interval associahedron, canonical form, amplitude, residues, and projectivity.
- Planar tree-level biadjoint amplitudes from 5 through 14 points.
- Complete Catalan graph support, cyclic/reflection symmetry, and every planar factorization channel.
- Explicit positive ABHY associahedra and canonical-form pullbacks from 5 through 10 points.
- Projectivity of planar scattering forms from 5 through 14 points.

Largest exact cases:

- 14 points: 208,012 cubic trees and 77 planar channels.
- 14-point scattering form: 208,012 oriented degree-11 terms with zero projective variation.
- 10-point associahedron: dimension 7, 35 facets, and 1,430 vertices.

## Momentum-twistor NMHV benchmarks

- Six-term five-bracket identity.
- Equality of distinct six-point BCFW triangulations.
- Cyclic and reflection symmetry through 12 points on positive data.
- Generic rational-kinematics dihedral checks through 10 points.
- Independent supertwistor projectivity, SL(4) invariance, GL(4) weight, and total antisymmetry.
- Exact spurious-residue cancellation through 9 points.
- Exact survival of every physical pole through 9 points.
- Boundary-count and oriented-chain cancellation checks for every multiplicity from 6 through 50.

The boundary census verifies

\[
N_{\mathrm{BCFW}}=\frac{(n-3)(n-4)}2,\qquad
N_{\mathrm{physical}}=\frac{n(n-3)}2,\qquad
N_{\mathrm{spurious}}=(n-5)(n-3),
\]

and

\[
5N_{\mathrm{BCFW}}=N_{\mathrm{physical}}+2N_{\mathrm{spurious}}.
\]

Every tested physical facet has incidence one; every tested spurious facet has incidence two with opposite orientations.

## Reproducibility

Run:

```bash
python research/nima/run_irl_amplitudes_replication_closure.py
```

The current closure executes 13 top-level checkers. The durable machine-readable summaries are:

- `research/nima/results/irl-amplitudes-replication-manifest.json`
- `research/nima/results/irl-amplitudes-replication-closure.json`

## Claim boundary

The computations use exact integer or rational arithmetic except where a result artifact explicitly says otherwise. Finite-range checks are not arbitrary-multiplicity proofs. Numerical or symbolic checks on sampled kinematics are not substitutes for a general algebraic proof. No claim is made here about loop-integrand completeness, Yangian invariance beyond the tested covariance identities, gravity amplitudes, cosmological polytopes, or experimental scattering data.
