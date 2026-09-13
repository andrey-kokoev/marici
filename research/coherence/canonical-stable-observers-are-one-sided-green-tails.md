# Canonical stable observers are one-sided Green tails

## From state innovations to dual observers

For ordered contexts, let \(R\) be the lower bidiagonal innovation transform

\[
r_1=k_1,
\qquad
r_i=k_i-\rho_{i-1}k_{i-1}.
\]

It diagonalizes the Green Gram matrix:

\[
RKR^T=D,
\qquad
D=\operatorname{diag}(1,1-\rho_1^2,\ldots).
\]

The canonical dual observer matrix is

\[
B=R^{-T}.
\]

Its rows satisfy

\[
BQ B^T=D^{-1},
\qquad Q=K^{-1}.
\]

After normalization,

\[
A=D^{1/2}B,
\]

one has

\[
AQA^T=I.
\]

Thus these observers have condition number one in the Green state geometry.

## Explicit form

Observer \(i\) vanishes on contexts strictly to its left. On context \(j\ge i\), its coefficient is

\[
B_{ij}
=
\rho_i\rho_{i+1}\cdots\rho_{j-1}
=
e^{-(x_j-x_i)}.
\]

So each canonical observer is a one-sided right Green tail:

\[
B_i=(0,\ldots,0,1,e^{-(x_{i+1}-x_i)},e^{-(x_{i+2}-x_i)},\ldots).
\]

## Interpretation

The stable completion does not require a numerical Gram--Schmidt search. Ordered Green geometry supplies a closed-form causal observer bank:

```text
state innovations:
  subtract the immediate predecessor

stable dual observers:
  integrate the exponentially decaying future tail
```

The observer bank is triangular, local to construct, and exactly dual to the Markov innovation coordinates.

## Boundary orientation

The displayed bank is right-oriented. Reversing context order gives the corresponding left-tail bank. Retaining both orientations recovers reversal closure; choosing one is a causal frame choice analogous to selecting incoming versus outgoing polarization.

## Collision behavior

The unnormalized tail observers remain finite as contexts collide, but normalization uses

\[
\sqrt{1-\rho_i^2}.
\]

This factor tends to zero. Condition number one is measured in the degenerating Green metric; it does not remove physical noise amplification when observers are measured in a fixed ambient norm.

## Verification

```text
python research/coherence/check_canonical_green_dual_observers.py
```

The exact checker verifies the tail formula and dual diagonalization through twelve contexts.

Artifacts:

- `check_canonical_green_dual_observers.py`
- `canonical-green-dual-observers.v1.json`
