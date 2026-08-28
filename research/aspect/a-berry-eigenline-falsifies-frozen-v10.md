# A Berry eigenline falsifies frozen v10

## Result

Version 10 is falsified. A global projector and trivial sheet permutation do not imply a globally trivial eigenframe.

## Hostile packet

Take the positive eigenspace of the spin-half Hamiltonian over the control sphere. On the equator, write (q=e^{i\phi}). North and south eigenframes may be chosen as

\[
u_N=\frac1{\sqrt2}\begin{pmatrix}1\\q\end{pmatrix},
\qquad
u_S=\frac1{\sqrt2}\begin{pmatrix}q^{-1}\\1\end{pmatrix}.
\]

They obey

\[
u_S=q^{-1}u_N.
\]

The transition function has winding minus one.

## What v10 sees

Both frames define the same projector:

\[
P_N=u_Nu_N^*=u_Su_S^*=P_S.
\]

The positive and negative projectors are globally defined, disjoint, and resolve the identity. Their eigenvalues are fixed at (+1) and (-1). There is no branch point and no sheet permutation. The total resolvent reconstructed from those projectors is globally single-valued.

Every v10 cover, projector, deck, and aggregate-resolvent gate therefore passes.

## What v10 loses

The phase transition (q^{-1}) is invisible after passing from an eigenframe to its projector. Its nonzero winding means the positive eigenline has nontrivial first Chern class. No single global eigenvector frame exists, and parallel transport carries Berry holonomy.

This is directly optical: a polarization mode can return to the same ray and projector while acquiring a measurable referenced geometric phase.

## Required successor

A successor must place a phase-framed eigenline or determinant line above every projector sheet. It must retain:

- chartwise eigenframes and their phase-transition cocycle;
- Berry connection and loop holonomy;
- characteristic-class or winding data;
- compatibility with deck permutation, branch specialization, and the aggregate quotient.

Projector transport is the ray-level quotient of this framed transport.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v10_berry_line_falsifier.py
```
