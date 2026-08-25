# Reciprocal circles are the two sectors; half-planes are their Mellin shadows

## Bounded question

Does modular inversion act internally on the arithmetic phase circle found in
packet 102, or does it require two complementary geometric sectors?

## Radius-dependent circle heat source

Write

\[
 \Theta(t)=\sum_{n\in\mathbb Z}e^{-\pi t n^2},
 \qquad t>0.
\]

This is the heat trace of the integral winding operator on a circle whose
metric scale is `t`.  Poisson sewing gives

\[
 \Theta(t)=t^{-1/2}\Theta(t^{-1}).
\]

This is not the assertion that a fixed heat operator is invariant.  It
relates two metric presentations: winding at radius scale `t` and phase-dual
winding at reciprocal scale `t^-1`.  Fourier transform is the quarter-turn
that exchanges them.

Put `u=log(t)` and normalize by the half-density:

\[
 \mathcal T(u)=e^{u/4}\Theta(e^u).
\]

Then the modular law becomes the exact reflection

\[
 \boxed{\mathcal T(u)=\mathcal T(-u).}
\]

Thus the completed source is naturally a section over two charts

\[
 U_+=\{u>0\},\qquad U_-=\{u<0\},
\]

sewn at the self-dual circle `u=0`.  The two sectors exist before the complex
Mellin variable is introduced.

## Why analytic half-planes appear

The Mellin character is

\[
 t^{s/2}=e^{su/2}.
\]

On the two source charts it has opposite convergence behavior.  Before
modular completion, the `u>0` and `u<0` integrals therefore define different
analytic half-plane realizations.  Modular reflection identifies their
boundary data and continuation produces one completed relative object.

Consequently the half-planes are not fundamental geometric halves of the
complex `s`-plane.  They are analytic shadows of the reciprocal-radius source
charts:

\[
 \boxed{
 \text{reciprocal circle metrics}
 \longrightarrow
 \text{two Mellin convergence charts}
 \longrightarrow
 \text{one completed function}.}
\]

The critical shift by `1/2` is the modular half-density.  In the centered
coordinate

\[
 z=s-\frac12,
\]

reciprocal reflection acts by `z -> -z`; complex conjugation supplies the
real structure.  The critical line is the fixed seam of their composition,
not a line selected retrospectively by the zero set.

## Meaning of the self-dual circle

At `t=1`, winding and phase polarizations have the same metric normalization.
The circle is therefore the geometric fixed object of the metaplectic
quarter-turn.  It is a circle of arithmetic phase conjugate to integral
winding—not a circle of Riemann zeros.

This sharpens the operator's proposed Explanation:

1. finite-place completion selects integral winding;
2. Pontryagin duality turns integral winding into a compact phase circle;
3. Fourier rotation exchanges winding and phase descriptions;
4. modular half-density centers their reciprocal sewing at `Re(s)=1/2`;
5. the two half-planes record which reciprocal chart supplied the ordinary
   Mellin realization.

The vertical critical line is therefore displaced from `Re(s)=0` because the
uncompleted Mellin character carries modular weight one.  Subtracting the
half-density centers the reflection at zero.

## What this does not explain

This construction explains why the seam is canonical and why the offset is
exactly one half.  It does not force completed zeros onto the seam.  An even
source in `u` can still have a transform with off-axis zeros; the previously
constructed hostile polynomial--Gaussian carriers demonstrate precisely this
gap.

The missing RH law must therefore constrain the reciprocal-circle
correspondence beyond:

- integrality projection;
- Fourier self-duality;
- positivity of the heat source;
- modular reflection.

## Next theorem-shaped gate

Let `C_+` and `C_-` denote the two radius-polarized trace-class families.  The
next object is their relative comparison at the self-dual seam, before scalar
trace compression.  A successful construction must:

1. be derived from the adelic vacuum and metaplectic transport;
2. retain winding labels and seam boundary terms;
3. have scalar Mellin readout equal to completed `Xi` up to an explicit unit;
4. possess an off-seam coercivity law not shared by hostile self-Fourier
   carriers.

The falsifier is a hostile source satisfying the same operator-level
reciprocal-circle correspondence while retaining an off-critical Mellin zero.
If it exists, this geometric Explanation locates the line but cannot orient
the divisor.
