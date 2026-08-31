# The first Adams four-matrix-unit test is specified but not yet evaluable

## Required identity

The quadratic first-Adams theorem asks for

\[
\mathfrak G_p^{\mathrm{St}}(x,y)
=
\mathfrak G_p^\theta
\bigl(Q_p^{\mathrm{lin}}x,Q_p^{\mathrm{lin}}y\bigr)
\]

on the polarized endpoint plane. Since that plane is two-dimensional, testing the four ordered matrix units \(E_{11},E_{12},E_{21},E_{22}\) is sufficient locally.

## Available source data

The repository supplies:

- the linear comparison \(Q_p^{\mathrm{lin}}\);
- exact even-wall and odd-jump normalization;
- the relative Wronskian connecting morphism;
- an exact polarized Green identity on the Stieltjes cyclic window-history subspace.

Thus the left side is source-defined on the cyclic plane, and the vectors entering the right side are fixed.

## Missing target data

The complete target form \(\mathfrak G_p^\theta\) has not been evaluated on those vectors. In particular, the repository does not freeze all of:

1. wall--tail cross pairings;
2. pairings involving the fourth Gaussian grade;
3. the common closed form domain;
4. radical restriction and descent;
5. prime-uniform bounds needed to pass from the core to completion.

Consequently none of the four target matrix entries is presently executable as a source-derived number or closed form.

## Why zero is not a default

Parity can force some pairings to vanish only after the complete form and reflection action are typed on the same domain. Orthogonality in one auxiliary Hilbert metric does not imply Green orthogonality after relative extension. Therefore unspecified wall--tail or grade cross terms must not be filled with zero.

The off-diagonal units are especially decisive: the exact hostile checker shows that one audited vector can agree while \(E_{12}\), \(E_{21}\), and \(E_{22}\) differ.

## Earliest executable construction

The next artifact must provide a Gram table for the target vectors

\[
Q_p^{\mathrm{lin}}e_1,
\qquad
Q_p^{\mathrm{lin}}e_2
\]

inside the complete relative theta-history carrier. It should list every wall, jump, tail, and Gaussian-grade contribution before summation. Once this table exists, the four matrix-unit checker can compare it exactly with the Stieltjes table and then test Schur reduction.

## Verdict

The quadratic test is mathematically finite but its target inputs are incomplete. G1.1 remains open. The machine-readable readiness record is
`research/nima/results/rh-adams-quadratic-readiness.json`.
