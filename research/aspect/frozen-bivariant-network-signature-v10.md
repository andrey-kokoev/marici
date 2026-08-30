# Frozen normalized joint spectral-cover signature v10

## Status

Version 10 is the successor to the already-created and falsified v9. v9 remains unchanged.

v10 retains mode identity on the normalized joint control–spectral cover before taking any aggregate quotient.

## Repair of the v9 hostile

For (A(t)=\begin{pmatrix}0&1\\t&0\end{pmatrix}), the incidence equation is

\[
\lambda^2=t.
\]

On the normalization (t=s^2), v10 retains the two eigenvalue sheets and their Riesz projectors

\[
P_\pm=\frac12\left(I\pm\frac{A(s^2)}s\right).
\]

The deck turn (s\mapsto-s) exchanges both eigenvalues and projectors. The total resolvent is reconstructed only after this labelled transport is checked:

\[
(A-zI)^{-1}=\frac{P_+}{s-z}+\frac{P_-}{-s-z}.
\]

Aggregate closure is therefore a quotient of labelled closure, not its replacement.

## Required cover data

v10 declares the external control base, the joint incidence space, its normalization, branch and ramification strata, sheetwise eigenvalues and projectors, the deck groupoid, and labelled specialization maps.

At branch strata, colliding sheets survive as vanishing-cycle transport. Sheet relabelling is gauge; a nontrivial deck permutation of observed channels is physical transport.

## First unused hostile

The companion family

\[
A_3(t)=\begin{pmatrix}0&1&0\\0&0&1\\t&0&0\end{pmatrix}
\]

has incidence equation

\[
\lambda^3=t.
\]

Its deck generator cyclically permutes three sheets and has order three. v10 requires the general deck-groupoid relations and forbids hardcoding the two-sheet repair.

## Next falsifier

Use multiple branch points with noncommuting braid generators. Pairwise sheet permutations may each pass while their ordered composites differ. That attacks whether the deck groupoid must be upgraded to a braid-groupoid representation with higher coherence.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v10.py
```
