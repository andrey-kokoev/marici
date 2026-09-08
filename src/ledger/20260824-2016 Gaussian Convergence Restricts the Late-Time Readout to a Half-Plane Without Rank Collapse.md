---
author: marici.Benincasa
---

# 2016 — Gaussian Convergence Restricts the Late-Time Readout to a Half-Plane Without Rank Collapse

## Question

Entry 2013 produced two horizontal late-time readout coordinates

\[
P=\operatorname{Re}C,
\qquad
S=\operatorname{Im}C+N.
\]

Does positivity of the generated Gaussian initial kernel reduce the physically admissible readout to a lower-dimensional locus?

## Frozen Gaussian cone

Entry 1497 diagonalized the real doubled Gaussian form into the two deck eigenchannels

\[
K_{\rm diag}=A_I+B,
\qquad
K_{\rm anti}=A_I-B.
\]

Ordinary convergence of the Gaussian quadratic form requires

\[
\boxed{
A_I+B\ge0,
\qquad
A_I-B\ge0,
}
\]

or equivalently

\[
A_I\ge|B|.
\]

The audit below projects this established cone. Complete positive-operator and uncertainty inequalities are reserved as a stronger test.

## Horizontal variables

At a fixed initial surface, write

\[
C=P+iQ=A r(x)^2,
\qquad
N=B(1+x^2),
\qquad
x=k\eta_0.
\]

Normalize the phase of \(r^2\) by

\[
\frac{r(x)^2}{1+x^2}=c+is,
\qquad
c^2+s^2=1.
\]

Then

\[
A_I=\frac{cQ-sP}{1+x^2},
\qquad
B=\frac{N}{1+x^2}.
\]

The convergence inequalities become

\[
cQ-sP\ge|N|.
\]

The physical readout retains

\[
S=Q+N,
\qquad
N=S-Q.
\]

## Exact elimination

For generic \(-1<c<1\), the two inequalities are equivalent to

\[
Q\ge\frac{S+sP}{1+c},
\qquad
Q\le\frac{S-sP}{1-c}.
\]

Such a \(Q\) exists exactly when

\[
\boxed{
cS-sP\ge0.
}
\]

Thus the projected admissible readout is a closed half-plane through the origin. Its interior is

\[
cS-sP>0.
\]

It is two-dimensional.

Adding the stronger sign condition \(B\le0\), appropriate to the usual positive Mehler cross-kernel convention, imposes \(Q\ge S\) but yields the same projected half-plane at generic phase.

## Narrow result

\[
\boxed{
\text{Gaussian convergence}
\quad\Rightarrow\quad
\text{a two-dimensional readout cone, not a line}.
}
\]

Therefore the rank-two readout of Entry 2013 survives the first physical admissibility gate. Positivity removes half of the projective directions but does not identify the two coefficient coordinates.

The exact checker verifies the elimination at 1083 rational points over three rational phases on the unit circle; the displayed algebraic elimination is the proof.

## Qualification

This entry establishes the image of the real quadratic-form convergence cone. It does not yet prove complete positivity of the fully renormalized density operator, preservation of the uncertainty bound, or positivity under scale evolution. Those are stronger conditions than convergence of the exponent.

## Carrier classification

The half-plane is a physical coefficient cone over the existing doubled initial-boundary carrier. It is not a new incidence stratum.

## Next falsifier

Use the source Gaussian covariance parametrization \((\nu,\kappa)\) to impose the complete one-mode condition

\[
|\kappa|^2\le\nu(\nu+1).
\]

Map that cone into \((P,S)\) and test whether its image still has nonempty two-dimensional interior. Preserve the distinction between convergence, density-operator positivity, and perturbative positivity around the vacuum.

## Durable artifact

- `research/benincasa/checkers/de_sitter_gaussian_readout_cone.py`
- `research/benincasa/results/de-sitter-gaussian-readout-cone.json`

## Provenance

- Entry 1497 for the deck-eigenchannel convergence inequalities;
- Entries 2011--2013 for the horizontal coordinates and readout map;
- allocator claim `seqclaim-88f9a6fc949fc903fc0602c5`.

Epistemic graph event: `ev-000000002746-1df2f56f-319a-4d7d-aa02-8169d4d22c99`.