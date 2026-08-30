# Triplet-quintet stabilizer obstruction: WP648

## Question

Is one dynamical real triplet (n) plus one real symmetric-traceless quintet
(Q) sufficient to replace WP647's imported orientation by a faithful
source-generated flavor frame?

## Source-authorized orientation terms

Through degree four, relative orientation enters an (SO(3))-invariant
potential through \(n^\top Qn\) and \(n^\top Q^2n\). Its orientation equation
therefore has the form

\[
n\mathbin\times(aQ+bQ^2)n=0.
\]

When \(aQ+bQ^2\) has nondegenerate spectrum, stationarity makes \(n\) an
eigenvector of (Q). Put it along the third axis and diagonalize (Q). The
proper half-turn

\[
R=\operatorname{diag}(-1,-1,1)
\]

is nontrivial and satisfies \(Rn=n\) and \(RQR^\top=Q\). The generic stationary
vacuum retains at least a (\mathbb Z_2) stabilizer; degenerate cases retain an
equal or larger stabilizer.

## Consequence

The carrier can break and rigidify the original symmetry, but it does not
construct a faithful oriented frame. Choosing a residual branch by hand would
add the undeclared reference excluded by WP647. The smallest exact falsifier
is a generic stationary nondegenerate one-triplet/one-quintet vacuum with
trivial (SO(3)) stabilizer.

A progressive successor needs an independently sourced second noncollinear
vector or tensor, a positive action deriving its relative vacuum, and the
messenger matching and detector readout.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp648_triplet_quintet_stabilizer_obstruction.py
```

Generated result: `results/wp648_triplet_quintet_stabilizer_obstruction.json`.
