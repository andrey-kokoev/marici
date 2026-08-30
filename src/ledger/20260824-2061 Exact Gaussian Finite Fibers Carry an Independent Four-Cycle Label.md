---
author: marici.Benincasa
---

# 2061 — Exact Gaussian Finite Fibers Carry an Independent Four-Cycle Label

## Question

Entry 2057 proved that the Hamiltonian four-cycle becomes differentially independent where the four edge-determinant readout loses rank. Differential independence alone does not imply a nontrivial finite fiber: an odd critical map can remain injective. The finite falsifier is an exact pair of positive pure four-mode Gaussian packets with identical lower readout and different cycle value.

## Frozen chart

Use

\[
V=\frac12\operatorname{diag}(X,X^{-1}),\qquad
X=\begin{pmatrix}1&a&0&d\\a&1&b&0\\0&b&1&c\\d&0&c&1\end{pmatrix}>0.
\]

The lower readout is

\[
F=(\det C_{12},\det C_{23},\det C_{34},\det C_{41}),
\]

and the cyclic readout is

\[
L_{\Omega,4}=\operatorname{tr}(JC_{12}JC_{23}JC_{34}JC_{41}).
\]

## Exact first sheet

Freeze the rational packet

\[
x_1=
\left(-\frac{6999667}{10^7},-\frac{6999808}{10^7},
-\frac{6001426}{10^7},\frac{5002516}{10^7}\right).
\]

Its four lower coordinates are exact rational numbers. Clearing their common denominator turns \(F(x)=F(x_1)\) into four polynomial equations over \(\mathbb Q\).

## Exact second-sheet certificate

An exact rational Krawczyk calculation gives a box of radius

\[
10^{-9}
\]

around

\[
(-0.7000329194076201,-0.7000189968810914,
-0.6010066310809248,0.5020466918542869).
\]

The Krawczyk image lies strictly inside this box. Hence the polynomial system has a unique real root \(x_2\) in the box, and by construction

\[
F(x_2)=F(x_1)
\]

exactly. Exact interval bounds on all leading principal minors are positive, so \(X(x_2)>0\).

The first cycle value is the exact rational number

\[
L_{\Omega,4}(x_1)=
\frac{16803779028614612770141113373243026351765892288}
{35187264002514159921106981101570206618351608525}.
\]

Its value is approximately \(0.4775528733\). Exact rational interval evaluation places \(L_{\Omega,4}(x_2)\) near \(0.3210797531\), in an interval disjoint from the first value. Therefore

\[
\boxed{
F(x_1)=F(x_2),\qquad
L_{\Omega,4}(x_1)\ne L_{\Omega,4}(x_2).
}
\]

## Narrow result

The Gaussian four-cycle is not merely differentially independent on the internal rank-drop support. It is a genuine finite-fiber label invisible to the complete lower edge-determinant readout.

This matches the amplitude-sector pattern at the level of mechanism:

\[
\boxed{
\text{higher cyclic information is born when lower reconstruction loses faithfulness.}
}
\]

The supporting divisors and coefficient lenses remain sector-specific. No new Carrier cell is inferred.

## Provenance

- `research/benincasa/marici-gm/src/bin/four_mode_chord_deletion_fold_pair.rs`;
- `research/benincasa/checkers/four_mode_chord_deletion_fold_pair_interval.py`;
- `research/benincasa/checkers/results/four-mode-chord-deletion-fold-pair.json`;
- `research/benincasa/checkers/results/four-mode-chord-deletion-fold-pair-interval.json`;
- allocator claim `seqclaim-4bf1f879cbb324efb8fee4df`.
- epistemic event `ev-000000002815-cd4bc340-966b-4b40-8de9-86524462a141`.

## Next falsifier

Determine the local monodromy exchanging the two sheets around the rank-drop discriminant and test whether the cycle difference is its anti-invariant character. This distinguishes a canonical supported double-cover label from an accidental disconnected finite fiber.
