# The window-to-theta connection square has an exact curvature term

## Purpose

The moving-center ray split and half-density transport construct the carrier
comparison between the adjacent Gaussian-window history and the theta
completion domain. The remaining question was whether the comoving
connection intertwines strictly with the theta completion operator.

It does not. The defect is nevertheless explicit and source-derived.

## Operators on one ray

Let

\[
A=x\partial_x,
\qquad
P=A(A+1).
\]

Under half-density transport, the theta completion operator
\(\partial_u^2-\frac14\) corresponds to \(P\). The nontrivial part of the
comoving window connection is the ray derivative \(\partial_x\), with the
sign selected by the two moving fronts.

The elementary identities

\[
\partial_x A=(A+1)\partial_x,
\qquad
\partial_x(A+1)=(A+2)\partial_x
\]

give

\[
\partial_xP=(A+1)(A+2)\partial_x.
\]

Therefore

\[
[P,\partial_x]
=
-2(A+1)\partial_x.
\]

Equivalently,

\[
P\partial_x
=
\partial_xP-2(A+1)\partial_x.
\]

## Consequence for the comparison square

The window-to-theta square is not a strict commuting square. Its canonical
comparison 2-cell is the first-order curvature operator

\[
\Omega=-2(A+1)\partial_x.
\]

For the two reciprocal front channels, the opposite comoving signs produce
opposite curvature signs. Hence reflection exchanges the two curvature
components rather than erasing them.

This is the missing grade-sensitive information. Since \(A+1\) raises the
effective Jordan complexity of a differentiated Gaussian, the comparison
cannot land in one scalar theta-history line. It naturally lands in the
cyclic dilation module already required by the three-grade completion packet.

## Integrated identity

On any common rapid core on which the integrations are justified,

\[
P\int_L^{2L}\partial_x f_t\,dt
=
\int_L^{2L}\partial_x(Pf_t)\,dt
-
2\int_L^{2L}(A+1)\partial_x f_t\,dt.
\]

Thus an endpoint-only comparison omits the second integral. That omitted term
is not an arbitrary correction: it is the exact curvature of the source
connection against theta completion.

The relative Green/Stokes mixed form must therefore contain two typed pieces:

1. the transported endpoint boundary;
2. the integrated curvature return.

Only their sum can define the source-authorized polarized comparison.

## Radical and orientation gates

A candidate mixed form obtained from this identity must still prove:

- the curvature integral is continuous on the rapid twisted core;
- it extends to the completed theta cyclic domain;
- moving-cut traces at \(x=0\) cancel between the two ray branches;
- the endpoint and curvature pieces jointly annihilate both Green radicals;
- reciprocal reflection sends the odd part to its adjoint-negative channel;
- the prime-labelled assembly preserves the exact diagonal decomposition.

The first Adams edge therefore remains unconstructed, but its missing
comparison is no longer an unspecified polarization.

## Hostiles

### Strict-square hostile

Discard \(\Omega\) and identify \(P\partial_x\) with
\(\partial_xP\). The endpoint scalar can remain correct while the
three-grade theta packet is wrong.

### Scalar-line hostile

Project \((A+1)\partial_x f\) back onto one scalar history line. This can
match one observed coefficient but loses the cyclic higher-grade leakage.

### Unpaired-cut hostile

Keep the curvature on each ray but omit the interface trace at \(x=0\).
Pointwise Gaussian symmetry does not by itself prove Green-domain
cancellation.

## Frontier

The earliest unresolved constructor has contracted to a curvature-completed
Green identity:

\[
\text{endpoint transport}
+
\text{integrated }[-2(A+1)\partial_x]
\longrightarrow
\text{polarized theta boundary form}.
\]

This rules out both the naive strict intertwiner and the identification of the
Adams edge with the theta Jordan operator. The Adams edge, if it exists, is
the defect-space correspondence induced after this curvature-completed
comparison descends through the source Green quotients.
