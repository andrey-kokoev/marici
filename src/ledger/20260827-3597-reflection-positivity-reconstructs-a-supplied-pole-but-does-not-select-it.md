---
id: marici-ledger-20260827-3597
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP815
---

# Reflection Positivity Reconstructs a Supplied Pole but Does Not Select It

The one-pole Euclidean correlator

\[
C(\tau)=A e^{-\Delta\tau},
\qquad A,Delta>0,
\]

has a positive rank-one reflection Gram matrix and is completely monotone. On
an independently authorized one-pole domain, its first two exact moments
reconstruct \(A\) and \(\Delta\), closing the raw Euclidean continuation kernel.

Reflection positivity admits every positive pole and residue. It is also blind
to the sign transformation \(O\mapsto-O\), and positive threshold shifts move
the pole without violating positivity. A one-pole measure and an equal-weight
two-pole measure at energies \(1/2\) and \(3/2\) share the first two moments,
so finite readout does not authorize the one-pole domain.

OS positivity is therefore a faithful realization condition on a declared
domain, not a source selector, sign law, numerical threshold protector, or
detector calibration.

## Evidence

- Packet: research/flavor/flavor-reflection-positive-reconstruction-selection-audit.md
- Checker: research/flavor/checkers/wp815_reflection_positive_reconstruction_selection_audit.py
- Generated result: research/flavor/results/wp815_reflection_positive_reconstruction_selection_audit.json
- Exact result: 18 of 18 checks passed.
- Ledger-sequence claim: seqclaim-5187bb305d3e5e513c148d32, value 3597.
- Graph admission: `ev-000000007708-9e36c384-dbf8-4ace-926f-79a8d9adc482`.

## Claim boundary

The faithful reconstruction result is restricted to the declared one-pole
domain. The required successor is a source-derived reflection-positive odd
correlator with unique chiral pole incidence, protected normalization, and the
same operator's calibrated `physical16` detector coupling.
