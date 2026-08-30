# Theta direct and dual tail systems carry opposite incidence arrows

## Direct tail generator

In the integrating-factor frame, the finite source tail obeys

\[
 Y'(q)=-u_s(q)c,
 \qquad
 c'(q)=0,
\]

where

\[
 u_s(q)=f(q)e^{sq}.
\]

On the split state (Y\oplus F), with one-dimensional forcing coordinate
(F=\mathbb Cc), the generator is

\[
 A_s(q)=
 \begin{pmatrix}
 0&p_s(q)\\
 0&0
 \end{pmatrix},
 \qquad
 p_s(q)=-u_s(q).
\]

Thus the source equation supplies forcing-to-endpoint incidence

\[
 p_s:F\longrightarrow Y,
\]

while its endpoint-to-forcing block is exactly zero.

## What Clark observation supplies

The Clark endpoint rows have the form

\[
 O_j=\begin{pmatrix}1&\mathcal C_a^jF(s)\end{pmatrix}.
\]

Their first coefficient is a direct endpoint sensor. In Kitaev's static
incidence theorem, this is the nonzero endpoint coefficient that repairs
observability. It is not a dynamical map from endpoint displacement into the
forcing state.

Therefore Clark observation does not manufacture the missing reverse generator
block. Its job is different: it makes endpoint and forcing coordinates jointly
visible, including at scalar zeros.

## Directional capability split

The direct tail system has:

- source-derived actuation of endpoint displacement through (p_s);
- source-derived endpoint observation through the coefficient one in every
  Clark row; and
- no endpoint-to-forcing feedback block.

Consequently its finite realization may be reachable and observable without
being dynamically bidirectional. Minimality does not imply a closed
circulation or a conservative boundary law.

## Dual system

Taking the adjoint reverses the triangular incidence:

\[
 A_s(q)^*
 =\begin{pmatrix}
 0&0\\
 \overline{p_s(q)}&0
 \end{pmatrix}.
\]

The dual carrier therefore contains the opposite arrow

\[
 q_s:Y\longrightarrow F.
\]

Fourier--Tate duality is the source-authorized operation relating the direct
and dual valuation sectors. However, an arrow living in the dual sector does
not automatically become an endomorphism of the direct sector. Authority
cannot be transported across that distinction without an explicit sewing map.

## Two-sector consequence

Bidirectional incidence is distributed across the two reciprocal sectors:

\[
 F_+\longrightarrow Y_+,
 \qquad
 Y_-\longrightarrow F_-.
\]

To obtain one closed boundary-current system, reciprocal sewing must identify
or pair these arrows on a common completed carrier. The critical seam is the
known locus where local Tate sewing is unitary, but unitarity alone does not
prove that the resulting positive supply or zero orientation closes.

This is a precise version of the two-sector intuition: each half-plane shadow
carries one direction of an incidence that only the completed relational
object can make bidirectional.

## Completion hostile

Because theta tails decay, the pointwise incidence magnitude

\[
 |p_s(q)|=|f(q)e^{sq}|
\]

tends to zero along the far tail for fixed (s). The dual incidence does the
same in its corresponding chart. Hence no cutoff-uniform theorem may use a
pointwise lower bound on either arrow. Only an accumulated path Gramian or a
source-derived sewing estimate can remain viable.

## Revised boundary-current target

The next finite compiler must contain four separately typed items:

1. direct actuation (p_s);
2. Clark endpoint observation;
3. dual incidence (q_s); and
4. Fourier--Tate sewing between their carriers.

It must then compute the mixed boundary-supply residual. A cancellation that
uses (q_s) as though it already lived in the direct carrier is unauthorized.

## Falsifier

The directional typing fails if the direct tail equation contains a nonzero
endpoint-to-forcing block, or if Clark differentiation acts on the state
generator rather than the output family. A sewn bidirectional theorem fails
if its comparison map is absent, unbounded in the completed topology, or valid
only after identifying the two sectors by hand.

## Scope

This derives the direct incidence arrow, proves the reverse arrow is absent
there, and locates it in the dual tail system. It does not construct the full
Fourier--Tate sewing map, close the mixed supply residual, orient zeros, or
prove RH.
