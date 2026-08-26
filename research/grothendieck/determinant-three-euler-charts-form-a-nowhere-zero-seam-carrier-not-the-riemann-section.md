# Determinant-three Euler charts form a nowhere-zero seam carrier, not the Riemann section

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact Schatten-chart theorem and divisor scope boundary

## Reciprocal primitive loops

On the primitive prime space (\ell^2(\mathbb P)\), define

\[
 L_+(s)e_p=p^{-s}e_p,
 \qquad
 L_-(s)e_p=p^{s-1}e_p.
\]

Write (\sigma=\Re s\).  Their third Schatten sums are

\[
 \lVert L_+(s)\rVert_3^3=\sum_p p^{-3\sigma},
\]

\[
 \lVert L_-(s)\rVert_3^3=\sum_p p^{-3(1-\sigma)}.
\]

Consequently

\[
 L_+(s)\in\mathcal S_3
 \quad\Longleftrightarrow\quad
 \sigma>\frac13,
\]

and

\[
 L_-(s)\in\mathcal S_3
 \quad\Longleftrightarrow\quad
 \sigma<\frac23.
\]

The two determinant-three charts overlap on

\[
 \frac13<\sigma<\frac23,
\]

an open strip containing the critical seam.

## The chart determinants are units

For a diagonal Schatten-three operator, the regularized determinant can
vanish only when one eigenvalue equals one.  On the plus chart this would
require

\[
 p^{-s}=1,
\]

which forces (\sigma=0\), outside its domain.  On the minus chart,

\[
 p^{s-1}=1
\]

forces (\sigma=1\), again outside its domain.  Hence

\[
 \det_3(I-L_+(s))\ne0
 \qquad(\sigma>1/3),
\]

and

\[
 \det_3(I-L_-(s))\ne0
 \qquad(\sigma<2/3).
\]

Their ratio on the overlap is therefore a nowhere-vanishing reciprocal
transition unit.  It glues the two regularized Euler determinant lines across
the seam.

## The divisor cannot live in this transition

Because both chart determinants and their transition are units throughout
the overlap, the nontrivial Riemann divisor cannot arise from:

1. failure of the determinant-three carrier;
2. singularity of its reciprocal transition;
3. nontriviality of the underlying line bundle;
4. loss of local Euler invertibility near the critical seam.

The carrier is exactly what reciprocal normalization should provide: a
coherent nowhere-zero comparison background.  The completed theta object is
a distinguished section over that carrier, and the section may vanish even
though every transition remains invertible.

## Where the missing divisor can be hidden

Reconstructing the ordinary Euler determinant requires the omitted cumulants

\[
 \operatorname{Tr}L_+(s),
 \qquad
 \frac12\operatorname{Tr}(L_+(s)^2).
\]

The first converges only for (\sigma>1\), while the second converges for
(\sigma>1/2\) and becomes singular at the seam.  Continuing the primitive
current separately is equivalent to continuing the prime zeta function and
imports the zeta divisor through Möbius inversion.  It therefore cannot be
used as an independent construction of the missing section.

On the reciprocal chart the same obstruction appears with the roles of the
two half-sectors reversed.  The primitive and square coordinates remain
rigged boundary data; they are not scalar holomorphic corrections that turn
the unit carrier into (\Xi\) without already knowing its continuation.

## Consequence for the determinant-line comparison

The desired source comparison must have the form

\[
 \alpha:
 \mathcal L_\theta
 \longrightarrow
 \mathcal L_{\mathrm{Euler},3}
 \otimes\mathcal L_\infty,
\]

but (\alpha\) cannot identify the theta section with either regularized chart
determinant alone.  The latter are units.  It must transport a distinguished
boundary-bearing section whose primitive, square, and Poisson data are still
typed before scalar continuation.

Thus the next theorem is not line-bundle triviality.  It is a construction of
the section and its conservation law inside the already coherent carrier.

## Falsifier

Any proposed determinant proof fails if it does one of the following:

- claims that a zero is a singularity of the local determinant-three
  transition;
- reconstructs (\Xi\) by separately continuing the primitive prime sum;
- infers section nonvanishing from invertibility of the carrier;
- treats the divergent square current at the seam as an ordinary scalar;
- or attaches a divisor-bearing factor to the carrier without a source
  constructor.

## Result

The two reciprocal determinant-three Euler charts give an exact,
source-labelled, nowhere-zero carrier across the critical seam.  That is a
useful normalization theorem, but it cannot itself see the Riemann zeros.
The RH-bearing information lies in the distinguished completed section and
its global boundary conservation, not in the determinant-line transition.
