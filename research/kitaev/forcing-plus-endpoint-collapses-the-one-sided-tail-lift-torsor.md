# Forcing plus endpoint collapses the one-sided tail-lift torsor

## Question

Once the theta forcing and Clark endpoint are both frozen, does any
graph-valued ambiguity remain in the one-sided first-order tail lift?

## Frozen tail problem

Let

\[
G'(q)=-sG(q)+g(q),
\qquad
G(0)=p,
\]

on the positive half-line, with

\[
\sigma=\Re s>0.
\]

The exact solution is

\[
G(q)=e^{-sq}p+
\int_0^q e^{-s(q-r)}g(r)\,dr.
\]

Thus the endpoint (p) and forcing (g) determine one tail.

## Uniqueness

If (G_1,G_2) have the same forcing and endpoint, their difference (H)
satisfies

\[
H'=-sH,
\qquad
H(0)=0.
\]

Hence

\[
H(q)=e^{-sq}H(0)=0.
\]

The affine tail-lift torsor therefore collapses to a point after both maps
are specified:

1. the source-to-forcing map;
2. the source-to-endpoint map.

No further local realization choice remains.

## Decay is not an endpoint substitute

For every scalar (c),

\[
H_c(q)=ce^{-sq}
\]

solves the homogeneous equation and decays at infinity. Therefore forcing
plus tail decay leaves a one-dimensional ambiguity. The endpoint condition
is the anchor that removes it.

This corrects any claim that a stable forward flow selects its own boundary
state merely by decay.

## Completion estimate

For (g\in L^2(\mathbb R_+)), Young's inequality gives

\[
\lVert G\rVert_2
\le
\frac{|p|}{\sqrt{2\sigma}}
+\frac{\lVert g\rVert_2}{\sigma}.
\]

Since

\[
G'=g-sG,
\]

the graph norm is bounded by the same endpoint and forcing data, with a
constant depending on (s) and (sigma^{-1}).

On every parameter set satisfying

\[
\Re s\ge\delta>0
\]

and with bounded (s), the lift is uniformly continuous. The estimate
degenerates as (delta\) tends to zero. Therefore one-sided completion is
stable on compact off-seam sectors, but this argument supplies no uniform
seam limit.

## Consequence for the theta programme

The local tail evolution is not the remaining constructor once Grothendieck
supplies the exact Clark endpoint and forcing. The unresolved information is
upstream and global:

1. whether the forcing map is derived in one common labelled source frame;
2. whether the reciprocal forcing is its authorized Fourier--Tate mate;
3. how the two one-sided lifts sew across the bilateral seam;
4. whether those maps remain continuous in the chosen completion;
5. whether the resulting pulled-back alternating Green form annihilates the
   source-observation kernel.

The scalar completed section cannot supply the forcing map. But after that
map is supplied, the one-sided ODE introduces no extra lift torsor.

## Minimal falsifiers

- Same endpoint and forcing, but distinct one-sided tails: impossible for the
  frozen first-order equation.
- Forcing and decay claimed to determine the endpoint: falsified by
  (ce^{-sq}).
- Uniform completion claimed while (Re s\) approaches zero: unsupported by
  the resolvent estimate and falsified whenever the inverse constants escape.
- A residual ambiguity attributed to local evolution after endpoint and
  forcing are fixed: mistyped; it belongs to forcing incidence, seam sewing,
  or completion.

## Disposition

The one-sided tail-lift torsor is exactly one-dimensional when only forcing
and decay are fixed, and exactly trivial when the endpoint is also fixed.
The research frontier moves to source-authorized forcing incidence and
bilateral sewing.

## Claim boundary

This theorem covers the frozen scalar first-order tail flow for fixed
(s) with positive real part. It does not prove that the theta forcing map is
source-authorized, that reciprocal sewing is unique, or that the estimates
remain uniform at the seam or under the full arithmetic completion.
