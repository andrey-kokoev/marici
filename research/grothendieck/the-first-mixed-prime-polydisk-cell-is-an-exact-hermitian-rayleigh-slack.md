# The First Mixed-Prime Polydisk Cell Is an Exact Hermitian Rayleigh Slack

## Setup

The smallest prime-labelled multiaffine object is

\[
F(u,v)=a+bu+cv+duv,
\qquad a,b,c,d\ge 0.
\]

The coefficients label the vacuum, the two singleton prime sectors, and their
mixed incidence. This is the first cell not visible to either one-prime axis
alone.

## Exact reduction

For fixed `u`, a zero satisfies

\[
v=-\frac{a+bu}{c+du}.
\]

Therefore no zero can have `|v|<1` precisely when

\[
|a+bu|^2-|c+du|^2\ge0
\]

for every `|u|<1`, apart from the separately exposed case in which numerator
and denominator vanish together.

Writing `u=r exp(i theta)`, minimization over the phase gives the radial slack

\[
q(r)=A+Cr^2-2|B|r,
\]

where

\[
A=a^2-c^2,
\qquad B=ab-cd,
\qquad C=b^2-d^2.
\]

Thus bidisk stability of the biaffine cell is decided by one real quadratic on
`0<=r<=1`, plus the common-factor gate. Its minimum is exact:

- if `C>0` and `|B|<=C`, it is `A-B^2/C`;
- otherwise it is the smaller endpoint value
  `min(A,A+C-2|B|)`.

The common-factor gate is necessary. If `ad=bc`, then the two affine rows are
proportional. A shared zero `u=-a/b` inside the disk makes `F(u,v)=0` for every
`v`, even though the Hermitian slack vanishes rather than becoming negative.

## Interaction curvature

The determinant

\[
\Delta=ad-bc
\]

is the first mixed-prime interaction curvature. Exact independent Fock
formation gives `d=bc/a`, hence `Delta=0` and

\[
F(u,v)=(a+bu)(1+(c/a)v).
\]

In that case stability reduces to the two local contraction walls. Completion
or sewing can deform `Delta`, and the radial slack measures whether that
deformation has pushed a zero into the bidisk.

This connects two previously separate pieces of the programme:

- the mixed-prime rectangle determinant measures failure of tensor
  factorization;
- the prime-polydisk test measures whether that failure changes zero
  location.

The determinant alone is not sufficient, but it is the typed interaction
coordinate entering the exact stability calculation.

## Hostile and benign cells

For `F=1+4uv`, the one-prime restrictions are both the constant `1`, while

\[
q(r)=1-16r^2.
\]

The slack becomes negative past `r=1/4`, and the exact zero `u=v=i/2` lies in
the bidisk.

For the independent cell

\[
F=(1+u/2)(1+v/3),
\]

the mixed curvature vanishes and both local factors are zero-free in the open
disk.

The common-factor hostile `(1+2u)(1+v)` shows why nonnegative slack alone is
not enough: its shared factor vanishes at `u=-1/2`.

## Consequence for the theta attack

The next source calculation should extract the four coefficients of each
finite two-prime theta/Tate cell before diagonal restriction and compute:

1. the local singleton walls;
2. the interaction curvature `Delta`;
3. the exact radial minimum of `q`;
4. the common-factor locus.

This is the smallest finite theorem that can distinguish independent prime
formation from completion-induced mixed interaction while remaining directly
relevant to polydisk zero exclusion.

## Falsifier

The proposed multivariate stability route fails at the first source-derived
two-prime cell for which the exact radial slack is negative, or for which the
two affine rows acquire a common zero in the open disk. Passing all separate
one-prime tests does not repair either failure.
