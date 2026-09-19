# The surviving Clark defect is an exact distributional boundary with a canonical even primitive

## Surviving functional

The Clark projection leaves

\[
D_1(g)
=A_0(g)-\frac12Q_0(g)-M(g),
\]

where

\[
A_0(g)=\int_{-\infty}^0g(x)\,dx,
\quad
Q_0(g)=\int_{\mathbb R}g(x)\,dx,
\quad
M(g)=g'(0).
\]

The first two terms combine as

\[
A_0(g)-\frac12Q_0(g)
=-\frac12\int_{\mathbb R}\operatorname{sgn}(x)g(x)\,dx.
\]

Since

\[
\langle\delta_0',g\rangle=-g'(0),
\]

the defect distribution is

\[
D_1
=-\frac12\operatorname{sgn}(x)+\delta_0'.
\]

## Canonical primitive

Define the even tempered distribution

\[
K_1
=-\frac12|x|+\delta_0.
\]

Distributional differentiation gives

\[
\boxed{
\partial_xK_1=D_1.
}
\]

Thus the sole Clark-visible history/moment mismatch is an exact boundary on
the Schwartz--tempered-distribution complex. No coefficient is fitted from Xi
zeros or from the rung-four residual.

## Rung-five compensator

The common Clark output of the reciprocal defect packet is

\[
(-iD_1,-iD_1).
\]

A canonical degree-minus-one compensator is therefore

\[
H_{D_1}=(-iK_1,-iK_1),
\]

with

\[
\partial_xH_{D_1}=(-iD_1,-iD_1).
\]

This supplies a source-derived local null-homotopy for the surviving
six-channel port defect.

## Qualification

The primitive `K_1` is tempered but is not an ordinary Hilbert history state:
`|x|` grows and `delta_0` is singular. Hence the construction lives naturally
in the rigged boundary complex. Promotion to the completed rung-five Green
system requires:

- continuity in the chosen strong-dual/graph rung;
- compatibility with moving-seam transport;
- prime and cutoff naturality after arithmetic loading;
- preservation by the Clark/Grushin chain maps;
- proof that adjoining `K_1` does not identify the vanishing residue stratum
  with the nonzero retained pair energy.

## Consequence

At the fixed-seam algebraic core, the history-to-moment Clark obstruction is
not a nontrivial cohomology class. It is exact. The remaining difficulty is
analytic admission and natural transport of its primitive, not construction
of a local homotopy.