# 3012 — NPT Orientation Synchronization Is Robust but Source-Noise Limited

**Status:** exact robustness theorem with experimental boundary  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-2081cbb2923d1d181433636e`

## Scope

Entry 3010 proves relative-orientation synchronization on the ideal tunable downconversion family. The primary source also reports small unwanted \(|HV\rangle\) and \(|VH\rangle\) components and attributes them to analyzer/source-axis misalignment or imperfect source orthogonality. This entry separates coherent frame errors from genuine mixture.

It does not infer a density-matrix error bound from fringe visibility. No source-fixed stochastic noise channel is supplied for that inference.

## Coherent local-frame errors

Let

\[
\rho'=(U\otimes V)\rho(U\otimes V)^\dagger
\]

with \(U,V\in U(2)\). Then

\[
(\rho')^{T_2}
=
(U\otimes V^*)\rho^{T_2}(U\otimes V^*)^\dagger.
\]

Thus local analyzer or source-axis rotations preserve the complete partial-transpose spectrum. They may populate \(|HV\rangle\) and \(|VH\rangle\) coordinates in a chosen frame, but they do not weaken NPT orientation synchronization.

This covers the source’s first proposed explanation when the mismatch is a genuine local basis rotation.

## Arbitrary mixed perturbations

Write

\[
\widetilde\rho=\rho_0+\Delta,
\qquad
\Delta=\Delta^\dagger,
\qquad
\operatorname{Tr}\Delta=0,
\]

where the ideal state \(\rho_0\) has smallest partial-transpose eigenvalue

\[
\lambda_{\min}(\rho_0^{T_2})=-\mathcal N_0.
\]

Weyl’s inequality gives

\[
\lambda_{\min}(\widetilde\rho^{T_2})
\le
-\mathcal N_0+|\Delta^{T_2}\|_{\rm op}.
\]

Partial transpose preserves the Frobenius norm, so

\[
\|\Delta^{T_2}\|_{\rm op}
\le
\|\Delta^{T_2}\|_F
=
\|\Delta\|_F.
\]

Hence the source-independent sufficient condition

\[
\|\Delta\|_F<\mathcal N_0
\]

guarantees that the perturbed state remains NPT and continues to synchronize relative complex orientation.

For the frozen ideal family,

\[
\mathcal N_0
=
\frac{|\varepsilon|}{1+\varepsilon^2}.
\]

The certified noise radius therefore shrinks to zero at the product endpoints, exactly where the ideal synchronization witness disappears.

## What the source does not authorize

The reported high fringe visibility and small off-family coordinates do not by themselves determine \(\|\Delta\|_F\), nor do they specify whether the deviation is coherent, stochastic, local, or correlated. Therefore they cannot be substituted into the bound without an independently derived reconstruction or noise channel.

An isotropic or Werner-like mixture may be used as a hostile toy model, but not as the provenance of the reported experiment unless the source derives it.

## Narrow conclusion

The NPT synchronization mechanism is exactly invariant under coherent local calibration drift and stable in an explicit open Frobenius ball under arbitrary mixture. Its experimentally realized support remains unquantified only because the frozen source does not type the observed imperfections as a definite density-matrix perturbation family.

This is a readout-authority boundary, not a failure of the coefficient architecture.

## Relation to the alternating-carrier comparison

The Flavor alternating determinant requires three independently typed ports and vanishes on repeated inputs. Optical NPT synchronization instead needs two ports plus an entangled positive cone. Both mechanisms reject reflection only after the source supplies an orientation-sensitive relational object; neither obtains handedness from repeated local copies alone.

## Next falsifier

Use the source’s reconstructed experimental density matrices, if machine-readable values can be recovered with equation/table provenance, and compute their partial-transpose spectra directly. If only plots or summary visibilities are available, record the missing matrix data rather than fitting them from the figures.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-2081cbb2923d1d181433636e`, value 3012.
- Exact coherent invariance: partial transpose transforms by unitary similarity under local rotations.
- Mixed-noise certificate: \(\|\Delta\|_F<\mathcal N_0\).
- Provenance boundary: source visibility is not treated as a density-matrix norm bound.
- Epistemic-graph admission: `ev-000000005781-9926e0c0-589d-450d-9217-8a0aff8e063d`.
