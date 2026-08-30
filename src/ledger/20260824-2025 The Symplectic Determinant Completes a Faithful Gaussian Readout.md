---
author: marici.Benincasa
---

# 2025 — The Symplectic Determinant Completes a Faithful Gaussian Readout

## Problem

Entry 2024 proved that \((P,S)\) is faithful on pure one-mode Gaussians but identifies mixed states with pure states. Find the smallest independently typed observable that restores the missing covariance coordinate without reintroducing future-boundary counterterm dependence.

## Canonical candidate

For the equal-time canonical covariance matrix

\[
V=
\begin{pmatrix}
q&c\\
c&p
\end{pmatrix},
\]

define its symplectic determinant

\[
\det V=qp-c^2.
\]

A local quadratic future-boundary counterterm acts as the canonical shear

\[
\Pi\mapsto\Pi+f\zeta,
\]

so

\[
q\mapsto q,
\qquad
c\mapsto c+fq,
\qquad
p\mapsto p+2fc+f^2q.
\]

Direct substitution gives

\[
q(p+2fc+f^2q)-(c+fq)^2=qp-c^2.
\]

Thus \(\det V\) is invariant under precisely the scheme ambiguity that shifts the mixed-correlator representative.

## Intrinsic impurity coordinate

In covariance coordinates define

\[
\Delta
=
\nu(\nu+1)-|\kappa|^2
=
\nu(\nu+1)-P^2-Y^2,
\qquad
S=\nu+Y.
\]

Gaussian positivity is \(\Delta\ge0\); pure states have \(\Delta=0\). Rearranging gives

\[
\Delta+P^2+S^2=(2S+1)\nu.
\]

Hence the complete inverse is

\[
\boxed{
\nu=\frac{\Delta+P^2+S^2}{2S+1},
\qquad
Y=S-\nu.
}
\]

Since the physical domain has \(S>-1/2\), the denominator never vanishes.

## Result

\[
\boxed{
(P,S,\Delta)
\text{ is a faithful coordinate on the complete positive one-mode Gaussian covariance space.}
}
\]

The third coordinate is not an arbitrary extra measurement. It is the scheme-invariant symplectic impurity, and it exactly separates the thermal/pure collision of Entry 2024:

\[
\Delta_{\rm pure}=0,
\qquad
\Delta_{\rm thermal}=n(n+1)>0.
\]

## Architectural consequence

The readout hierarchy is now typed:

\[
(P,S)
\quad\text{faithful on the pure coefficient sector},
\]

\[
(P,S,\Delta)
\quad\text{faithful on the full Gaussian coefficient sector}.
\]

This is a concrete port-adapter principle: a larger source object requires one additional invariant port, not a change to the Carrier or a fitted choice of representative.

## Verification

The dependency-free checker verifies 4,312 exact rational counterterm shears and 1,905 exact positive-covariance reconstructions:

`research/benincasa/checkers/symplectic_determinant_readout.py`

`research/benincasa/checkers/results/symplectic-determinant-readout.json`

## Next falsifier

Derive the normalization relating \(\Delta\) to the source equal-time correlators of Entries 2012--2013, including scale-factor and canonical-momentum factors. Then test whether the one-loop source fixes \(\Delta\) even when it fails to fix \((P,S)\), or whether impurity is another genuinely missing matching datum.

## Provenance

- Entries 2013, 2018, 2024;
- allocator claim `seqclaim-cec7773bb8eeac2ef0302b28`.

Epistemic graph event: `ev-000000002758-757cf584-affc-4a78-b3c8-5e3fa81a93da`.
