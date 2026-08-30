# Theta tail and seam share the complete oriented source jet

## Question

Does the opposed inward derivative of the theta tail and seam atoms create a
genuine second-order seam defect, or does orientation convert it into smooth
global matching?

## The two source restrictions

For a positive label (r), Grothendieck's source atoms are

\[
g_r(t)=\Phi(r+t),
\qquad t\ge0,
\]

and

\[
h_r(t)=\Phi(r-t),
\qquad 0\le t\le r.
\]

Use one global oriented coordinate (x), with the tail on (x>0) and the
reflected seam component on (x<0):

\[
G_r(x)=
\begin{cases}
g_r(x),&x>0,\\
h_r(-x),&-r<x<0.
\end{cases}
\]

But on both sides,

\[
G_r(x)=\Phi(r+x).
\]

The two components are restrictions of one translated source germ.

## Complete jet matching

The inward half-line jets are

\[
g_r^{(k)}(0)=\Phi^{(k)}(r),
\qquad
h_r^{(k)}(0)=(-1)^k\Phi^{(k)}(r).
\]

Reflection of the negative half contributes another factor ((-1)^k).
Therefore the global left jet is

\[
\partial_x^k h_r(-x)\big|_{x=0^-}
=\Phi^{(k)}(r),
\]

which equals the global right jet for every (k\ge0).

The apparent opposite first derivatives are the correct inward-normal
description of one smooth oriented germ.

## Distributional consequence

For a general piecewise (H^2) function,

\[
\partial_x^2G
=G''_{\mathrm{reg}}+[G']_0\delta_0+[G]_0\delta_0'.
\]

Here

\[
[G]_0=0,
\qquad
[G']_0=g_r'(0)+h_r'(0)=0.
\]

Thus neither a delta-prime nor a delta occurs at second order. More
generally, complete oriented jet matching removes every seam-supported
distribution produced solely by differentiating the sewn source germ.

This statement holds label by label and therefore for every finite labelled
linear packet.

## Where a genuine seam current can still arise

A nonzero seam term may still be produced by:

1. a discontinuous or sign-changing operator coefficient;
2. integration by parts on a deliberately cut domain;
3. the endpoint of the finite crossing interval at (x=-r);
4. a Clark fold or spectral derivative that acts differently on the charts;
5. arithmetic aggregation that does not preserve the source jet;
6. a completion in which the common jet trace is not continuous.

Such a term belongs to the operator, cutoff, or coefficient lens. It is not a
failure of the underlying source germ to sew.

## Correction to defect language

The pair

\[
\bigl(\Phi(r),2\Phi'(r)\bigr)
\]

records a common value and an inward-normal comparison. The second coordinate
must not be called a global derivative jump without applying the reflection
orientation. Its global jump is zero.

This distinction matters because an inward boundary form may legitimately
use the sum or difference of normal currents, while a distributional seam
singularity is governed by global oriented jumps.

## Consequence for the programme

The source-level seam is smoother than the scalar common-trace theorem alone
reveals. The missing Green or arithmetic defect cannot be justified merely by
pointing to opposite inward derivatives. Its producing operator must be
written explicitly.

The highest-information next test is therefore to type every claimed seam
term by origin:

- source-germ jump;
- operator-coefficient jump;
- cut-boundary current;
- arithmetic aggregation residual;
- completion trace failure.

The first class is zero for the canonical theta atoms.

## Falsifier certificate

    {
      "code": "theta_source_seam_jet_mistyped",
      "right_germ": "Phi(r+x)",
      "left_reflected_germ": "Phi(r+x)",
      "all_oriented_jet_jumps": 0,
      "claimed_source_delta": "nonzero",
      "required_alternative_origin": true
    }

## Disposition

The theta tail and seam atoms share the entire oriented source jet. No
seam-supported distribution arises from differentiating their canonical
gluing. Surviving seam currents require an independently displayed operator,
cutoff, coefficient, or completion mechanism.

## Claim boundary

This is a local seam-germ theorem on the interval where both restrictions are
defined. It does not eliminate the remote endpoint at (x=-r), Green
boundary forms created by cutting the domain, Clark-sheet operator defects,
or discontinuities introduced by arithmetic completion.
