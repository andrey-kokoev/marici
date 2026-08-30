# Two valuation cones have an exact relative seam norm

## Bounded question

If the source does authorize both integral and inverse-integral valuation
sectors, what is their canonical algebraic sewing and norm?

## One-prime cone pair

Let

\[
 H=\ell^2(\mathbb Z),
 \qquad
 H_+=\ell^2(\mathbb Z_{\ge0}),
 \qquad
 H_-=\ell^2(\mathbb Z_{\le0}),
\]

and let the common seam be

\[
 H_0=\mathbb C e_0.
\]

Valuation reflection `J e_k=e_(-k)` exchanges `H_+` and `H_-` and fixes
`H_0`.

## Relative gluing complex

There is an exact sequence

\[
 0\longrightarrow H_0
 \xrightarrow{\;h\mapsto(h,-h)\;}
 H_+\oplus H_-
 \xrightarrow{\;(f_+,f_-)\mapsto f_++f_-\;}
 H
 \longrightarrow0,
\]

where each cone vector is extended by zero outside its support.  The kernel of
the sum map is exactly the oppositely represented seam.

For a global vector `f`, let `f_plus` and `f_minus` be its two restrictions.
Both contain the common coefficient `f_0`. Inclusion--exclusion gives

\[
 \boxed{
 \|f\|_H^2
 =\|f_+\|_{H_+}^2
 +\|f_-\|_{H_-}^2
 -|f_0|^2.}
\]

The negative seam term is not an instability. It removes the duplicate copy
introduced by the two-chart presentation, leaving the ordinary positive
global norm.

## Relation to the quarter-turn

At each prime, the product--ratio exchange reflects one valuation coordinate.
If both cones are source-authorized, the exact sequence above supplies the
minimal relative object on which that reflection is internal.  The fixed face
has rank one, so the entire one-prime gluing defect is a single seam channel.

This reproduces the recurring architecture

\[
 \boxed{
 \text{two positive local sectors}
 -\text{one duplicated fixed face}
 =\text{one positive global sector}.}
\]

## Source-authority boundary

The algebraic cone theorem is exact but conditional in its application to
theta.  The compact-open additive vacuum `1_Zp` is Fourier-fixed and supports
nonnegative valuations; additive Fourier transform does not automatically
create the inverse-integral cone.  Therefore this packet does not claim that
the local Tate source realizes both `H_plus` and `H_minus` as independent
physical coefficient fibers.

The next source calculation must derive the negative-valuation chart and its
transition map from the local functional equation, including Haar/Jacobian
weights and the local gamma factor.

## Falsifier

At one prime, compute the local Tate zeta integral of `1_Zp` on both sides of
the functional equation and expand it by valuation.  If the transformed side
cannot be represented as the reflected cone plus the rank-one seam with the
correct measure weights, then the proposed product--ratio quarter-turn has no
authorized local source lift.
