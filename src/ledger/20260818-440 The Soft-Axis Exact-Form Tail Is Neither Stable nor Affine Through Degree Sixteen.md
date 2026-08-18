---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Soft-Axis Exact-Form Tail Is Neither Stable nor Affine Through Degree Sixteen

## Record

Status: extended cutoff falsification test following Entry 439.

## Hard-to-vary claim

The cutoff dependence at the soft boundary might be removable by one affine
Hilbert-tail correction. The observed valuations (89,92,95) at exact-form
degrees (8,10,12) suggested the provisional rule
[

u_N=89+rac32(N-8).
]
If that rule survived, it could motivate a relative-index subtraction,
provided the subtraction were subsequently derived from the graded
exact-form tower rather than fitted.

The first finite falsifiers are degrees 14 and 16.

## Frozen probe

Use
[
E=t,qquad X_2=3t^2
]
over
[
mathbf F_{2305843009213693951}[t]/(t^{24}).
]
The transverse unit 3 avoids the frozen algebraic branches
(X_2=pm E^2). The master-image rank remains ten.

## Result

The valuation sequence at exact-form degrees
[
8, 10, 12, 14, 16
]
is
[
89, 92, 95, 97, 99.
]
Equivalently, the excess over the punctured generic valuation 66 is
[
23, 26, 29, 31, 33.
]

The increment sequence is
[
3, 3, 2, 2.
]
Thus the degree-14 value already refutes the affine prediction 98, and the
degree-16 value shows that the raw sequence has still not stabilized.

At degree 14,
[
(r_E,r_{[E,M]})=(224,234),qquad
(delta_E,delta_{[E,M]})=(192,289).
]
At degree 16,
[
(r_E,r_{[E,M]})=(271,281),qquad
(delta_E,delta_{[E,M]})=(222,321).
]
The rank difference remains ten, while the determinant difference changes.

Therefore
[
oxed{
	ext{neither raw cutoff stabilization nor one affine tail subtraction
defines the soft-axis saturation weight through degree 16.}
}
]

## Interpretation

The failure is in the chosen infinite exact-form presentation. It is not a
new exceptional direction and does not alter the frozen carrier. More
sampling of cutoff degrees cannot canonically select a completion: even if a
numerical sequence eventually stabilizes, that would not identify which
graded tail was quotiented.

The next object must therefore be structural. One must construct the
completed or graded exact-form quotient and prove that its discarded tail is
contractible or determinant-trivial. Only then is a renormalized Smith index
admissible.

The stable total-energy excess 27 from Entry 439 remains valid in its tested
scope. It cannot yet be paired with a soft-axis number to produce a global
transition degree.

## Classification

- soft-axis cutoff sequence: coefficient-presentation dependence;
- affine-tail correction: refuted;
- stable total-energy transverse excess: unchanged at 27;
- new carrier datum: none;
- degree-20 compactified Fitting line: still unproved.

## Epistemic boundary

The calculation is finite-field and truncated at (t^{24}). It refutes the
specific affine extrapolation and demonstrates nonstabilization through
degree 16. It does not prove that no canonical completion exists, nor that
the raw sequence diverges indefinitely.

## Next falsifier

Grade the exact-form complex by polynomial degree at (X_2=0). Identify the
eventual tail maps and test whether they form a contractible periodic
complex with a canonically trivial determinant line. If so, quotient that
tail before recomputing the transverse Smith index. If no canonical
contractible tail exists, the present master-image presentation cannot
define the desired compactified Fitting line.

## Evidence

- research/benincasa/dlog-smith-soft-axis-tail-certificate.json
- research/benincasa/marici-gm/src/bin/marked_tangency_support.rs
