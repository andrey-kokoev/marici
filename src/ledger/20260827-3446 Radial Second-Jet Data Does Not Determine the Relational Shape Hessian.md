---
author: marici.Benincasa
date: 2026-08-27
---

# 3446 — Radial Second-Jet Data Does Not Determine the Relational Shape Hessian

## Question

Entry 3441 identifies the quadratic intervention required to activate the
relational (A_2) scalar. Can the existing homogeneous total-energy or radial
normal data determine that intervention coefficient?

## Cyclic Hessian decomposition

At the cyclic homogeneous locus, a symmetric three-site Hessian decomposes
into two independent invariant channels:

\[
\mathbb Q^3=\mathbb Q(1,1,1)\oplus A_2.
\]

Consequently its restriction has one radial eigenvalue and one relational
shape eigenvalue. Cyclic invariance does not identify them.

## Exact hostile pair

Consider the two cyclic Hessians

\[
H_{\rm shape}=I,
\qquad
H_{\rm radial}=\frac13J,
\]

where (J) is the all-ones matrix. For the radial vector
(n=(1,1,1)), both give

\[
n^TH_{\rm shape}n=n^TH_{\rm radial}n=3.
\]

Both have zero radial--shape mixed terms. Yet for either primitive shape root,
for example (b=(1,-1,0)),

\[
b^TH_{\rm shape}b=2,
\qquad
b^TH_{\rm radial}b=0.
\]

Thus two source-compatible cyclic second jets can agree exactly on radial data
while differing maximally on relational activation.

## Result

The total-energy normal jet, including its second radial grade, cannot decide
whether the quadratic (A_2) readout is populated. The missing physical datum is
specifically a logarithmic energy-shape Hessian, not merely higher order in the
total-energy coordinate.

The finite source test is now one directional derivative. For a primitive
shape tangent (b), derive

\[
\lambda_{A_2}=D_b^2\Psi\big|_{X_1=X_2=X_3}
\]

from the source-normalized scalar wavefunction or its relative period. Cyclic
symmetry then determines the complete shape Hessian. A nonzero value activates
Entry 3441's intervention; zero closes it at second order.

This must be computed from the physical scalar family. Neither the total-energy
nearby-cycle data nor the abstract Cartan pairing fixes (\lambda_{A_2}).

## Verification

Checker:
`research/benincasa/checkers/audit_radial_shape_hessian_independence.py`.

Allocator claim: `seqclaim-357fbcddeef7a3721d122291`.

Epistemic graph event:
`ev-000000007380-7bb2611f-9a37-4758-8194-f9205450f606`.
