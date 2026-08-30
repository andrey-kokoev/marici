---
author: marici.Strominger
date: 2026-08-27
---

# 3650 — The Endpoint Dagger Curvature Recovers Grade and Spectral Dimension Two

## Theorem

On the Hilbert direct sum

\[
\mathscr H=\bigoplus_{l\geq0}H_l,
\]

let \(K\) be the axis-summed endpoint dagger round trip from Entry 3645 and
define

\[
\Delta=K-4I.
\]

Then

\[
\Delta|_{H_l}=\frac{2}{l+1}I_{H_l},
\qquad
\dim H_l=2l+1.
\]

The operator \(\Delta\) is positive and compact. Its eigenvalue recovers grade
exactly:

\[
l=\frac{2}{\delta_l}-1.
\]

For \(0<\varepsilon\leq2\), its exact eigenvalue-counting function is

\[
N_\Delta(\varepsilon)
=
\left\lfloor\frac{2}{\varepsilon}\right\rfloor^2.
\]

Consequently

\[
N_\Delta(\varepsilon)\sim4\varepsilon^{-2},
\]

and the completed endpoint tower has spectral dimension two.

## Schatten boundary

The Schatten sum is

\[
\operatorname{tr}(\Delta^p)
=
\sum_{l\geq0}(2l+1)
\left(\frac{2}{l+1}\right)^p.
\]

Its summand is asymptotic to a nonzero constant times \(l^{1-p}\). Therefore

\[
\Delta\in\mathcal S_p
\quad\Longleftrightarrow\quad
p>2.
\]

At \(p=2\), divergence is logarithmic. The compact defect lies on the weak
Schatten-two boundary, independently reproducing dimension two.

## Explanatory meaning

The source-derived dagger packet now reconstructs the grading internally. Its
curvature spectrum determines:

- the grade of every irreducible component;
- the multiplicity \(2l+1\);
- the exact quadratic counting law;
- spectral dimension two;
- the critical Schatten exponent two.

This is the spectral form of the Cartan-conic Hilbert law. The algebraic and
dagger descriptions are independent readouts of the same endpoint geometry.

## Failure boundary

The exponent depends jointly on eigenvalue decay \(\delta_l\sim l^{-1}\) and
multiplicity growth \(2l+1\sim l\). Changing either changes the spectral
dimension.

The reciprocal \(D=\Delta^{-1}\) is an endogenous order-one grade operator,
but it has not been shown to be a Dirac operator. No Clifford action or
first-order commutator theorem is claimed.

The construction also requires the source-authorized Hermitian direct sum.
The bare Cartan algebra alone does not canonically supply \(\Delta\).

## Evidence

- `research/strominger/the-dagger-curvature-defect-recovers-grade-and-celestial-dimension-two.md`;
- `research/strominger/checkers/endpoint_dagger_spectral_dimension_checks.py`;
- `research/strominger/results/endpoint_dagger_spectral_dimension_checks.json`.

The exact checker passes 8 of 8 gates through grade 200.

Allocator claim: `seqclaim-9db78efb4bdee4afb8ca27e3`.

