# IRL amplitude-result replication status

## Scope

This directory now contains executable exact-arithmetic replications of selected results from:

1. N. Arkani-Hamed, Y. Bai, S. He, G. Yan, *Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet*, arXiv:1711.09102.
2. N. Arkani-Hamed et al., *The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM*, arXiv:1008.2958.

These are replications of specific formulas and structural identities, not a claim to reproduce either paper in full.

## ABHY results

Arbitrary-multiplicity proofs now establish:

- the complete planar tree-level biadjoint amplitude, Catalan graph support, dihedral symmetry, and factorization on every planar channel;
- projectivity of the planar scattering form under a common local rescaling;
- realization of the positive ABHY associahedron and equality of the pulled-back planar scattering form with its canonical form.

The universal proofs are:

- `arbitrary-n-planar-biadjoint-amplitude-proof.md`;
- `arbitrary-n-planar-scattering-form-projectivity-proof.md`;
- `arbitrary-n-abhy-associahedron-canonical-form-pullback-proof.md`.

An additional arbitrary-order theorem proves support and unit-coefficient channel factorization of tree-level double-partial functions:

- `arbitrary-order-double-partial-biadjoint-factorization-proof.md`.

For cyclic orders `alpha,beta`, a pole occurs exactly on a split that is an interval in both orders, and its residue is the product of the induced lower double-partial functions. This does not construct a positive geometry for arbitrary order pairs or fix convention-dependent relative signs.

Exact finite computations remain as regression evidence. Largest cases include:

- 14 points: 208,012 cubic trees and 77 planar channels;
- the 14-point scattering form: 208,012 oriented degree-11 terms with zero projective variation;
- the 10-point associahedron: dimension 7, 35 facets, and 1,430 vertices;
- 542 selected double-partial channel factorizations through nine points, plus an exhaustive census of 66,894 inequivalent order pairs and 205,149 channels through seven points.

## Momentum-twistor NMHV results

Arbitrary-multiplicity proofs now establish:

- boundary counts
  \[
  N_{\mathrm{BCFW}}=\frac{(n-3)(n-4)}2,\qquad
  N_{\mathrm{physical}}=\frac{n(n-3)}2,\qquad
  N_{\mathrm{spurious}}=(n-5)(n-3);
  \]
- the incidence identity
  \[
  5N_{\mathrm{BCFW}}=N_{\mathrm{physical}}+2N_{\mathrm{spurious}};
  \]
- cancellation of every internal facet with opposite orientation;
- generic survival of every physical pole;
- independent supertwistor projectivity, `SL(4)` invariance, `GL(4)` weight, and five-bracket antisymmetry;
- cyclic and reflection invariance;
- equality of any two finite simplicial five-bracket chains with the same oriented boundary.

The universal proofs are:

- `arbitrary-n-nmhv-bcfw-boundary-cancellation-proof.md`;
- `arbitrary-n-nmhv-physical-pole-survival-proof.md`;
- `arbitrary-n-nmhv-spurious-pole-cancellation-proof.md`;
- `arbitrary-n-nmhv-momentum-supertwistor-covariance-proof.md`;
- `arbitrary-n-nmhv-cyclic-invariance-from-chain-homology.md`;
- `arbitrary-n-nmhv-reflection-invariance-from-chain-homology.md`;
- `nmhv-five-bracket-chain-depends-only-on-its-oriented-boundary.md`.

Exact finite computations remain as regression evidence: residue checks through nine points, generic rational-kinematics dihedral checks through ten points, coefficient-level symmetry checks through twelve points, and oriented boundary censuses through fifty points.

## One-loop MHV results

The locally acquired source formulas now support arbitrary-multiplicity pre-integration results for the planar one-loop MHV Kermit representation:

- the four-point rational box form equals its four-`dlog` canonical form exactly;
- the general sum contains `(n-2)(n-3)/2` Kermit cells;
- every term has zero external projective weight and zero total loop-line `GL(2)` weight;
- every anchor-type nonlocal pole cancels under an explicit pairwise cell involution;
- every cyclic physical propagator has incidence `n-3` and a generically nonzero residue;
- the complete rational integrand is cyclically and reflectively invariant.

The universal proofs are:

- `arbitrary-n-one-loop-mhv-kermit-count-and-covariance.md`;
- `arbitrary-n-one-loop-mhv-kermit-spurious-pole-cancellation-proof.md`;
- `arbitrary-n-one-loop-mhv-physical-pole-survival-proof.md`;
- `arbitrary-n-one-loop-mhv-kermit-cyclic-invariance-proof.md`;
- `arbitrary-n-one-loop-mhv-kermit-reflection-invariance-proof.md`.

No integrated box value, infrared regulator, subtraction scheme, or loop-level NMHV claim is included.

## Reproducibility

Run:

```bash
python research/nima/run_irl_amplitudes_replication_closure.py
```

The current closure executes 22 top-level checkers. The durable machine-readable summaries are:

- `research/nima/results/irl-amplitudes-replication-manifest.json`
- `research/nima/results/irl-amplitudes-replication-closure.json`

## Claim boundary

The computations use exact integer or rational arithmetic except where a result artifact explicitly says otherwise. Arbitrary-multiplicity claims above rely on the cited proofs, not promotion from finite checks. No claim is made here about nonplanar or indefinite-sign ABHY geometries, normalized multiparticle factorization of NMHV physical residues, general `N^kMHV` sectors, loop-integrand completeness beyond one-loop MHV, regulated or integrated loop amplitudes, Yangian invariance beyond the proved covariance identities, gravity amplitudes, cosmological polytopes, or experimental scattering data. Remaining source requirements are recorded in `n2mhv-and-loop-integrand-source-acquisition-gate.md`.
