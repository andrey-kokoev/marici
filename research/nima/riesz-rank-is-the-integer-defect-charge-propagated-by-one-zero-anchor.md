# Riesz rank is the integer defect charge propagated by one zero anchor

## Defect projection

On a stabilized reduced carrier, let \(K_X(s)\) be the cutoff
Birman--Schwinger family. Fix a contour \(\Gamma\) around the generalized
eigenvalue one, lying in the resolvent set.

Define

\[
P_X(s)
=
\frac{1}{2\pi i}
\int_\Gamma
(z-K_X(s))^{-1}\,dz.
\]

For compact \(K_X(s)\), the projection has finite rank. Define the defect
charge

\[
q_X(s)=\operatorname{rank}P_X(s).
\]

It counts algebraic eigenvalue multiplicity inside \(\Gamma\).

## Local constancy

Suppose \(K_X(s)\) varies norm-resolvent continuously while \(\Gamma\) stays in
the resolvent set. Then \(P_X(s)\) varies continuously in operator norm.

If two projections satisfy

\[
\lVert P-Q\rVert<1,
\]

their ranges are isomorphic and

\[
\operatorname{rank}P=\operatorname{rank}Q.
\]

Therefore \(q_X(s)\) is locally constant.

Since it is integer-valued, it is constant on every connected parameter
component on which the contour-resolvent hypotheses remain valid.

## One-anchor propagation

Let \(C_0\) be a connected compact parameter component. Suppose there is one
source-authorized anchor \(s_0\in C_0\) such that

\[
P_X(s_0)=0.
\]

If \(\Gamma\) remains in the resolvent set for every \(s\in C_0\), then

\[
q_X(s)=q_X(s_0)=0
\]

throughout \(C_0\). Hence

\[
P_X(s)=0
\]

for every \(s\in C_0\).

Thus one zero-defect anchor plus a no-contour-crossing theorem excludes the
entire connected component at that cutoff.

The anchor must be source-derived. Choosing a point because a scalar numerical
scan found no zero does not establish categorical authority.

## Cutoff propagation

Let cutoff comparison maps transport the reduced carriers and contour
resolvents. If

\[
\lVert P_Y(s)-J_{XY}P_X(s)J_{XY}^{-1}\rVert<1
\]

on the identified defect subspaces, then the ranks agree:

\[
q_Y(s)=q_X(s).
\]

Under norm-resolvent convergence, this holds eventually. Hence a zero charge at
one sufficiently large cutoff propagates through all later cutoffs.

Earlier cutoffs remain a finite audit. A new defect charge can appear only
where the comparison or contour-resolvent cell fails.

## Parameter--cutoff charge graph

Form a graph whose vertices are admissible pairs \((X,s)\). Join vertices when
there is:

- a parameter path segment on which \(\Gamma\) stays in the resolvent; or
- a cutoff comparison with norm-continuous Riesz transport.

The charge \(q_X(s)\) is constant on every connected component of this graph.

An RH completion certificate can therefore consist of:

1. one zero-charge anchor per graph component;
2. verified contour-resolvent edges connecting the component;
3. reciprocal identification of paired components.

This is a finite combinatorial shadow of the spectral completion theorem.

## First crossing witness

A change in \(q_X(s)\) requires at least one typed failure:

1. \(\Gamma\) meets \(\sigma(K_X(s))\);
2. the reduced carrier ceases to be stable;
3. the contour resolvent loses boundedness;
4. cutoff comparison ceases to be norm-continuous;
5. reciprocal transport fails to preserve the pencil.

The sharp machine witness is the first parameter or cutoff where

\[
\inf_{z\in\Gamma}
\sigma_{\min}(z-K_X(s))
=
0
\]

in finite dimension, or where the corresponding resolvent norm diverges.

Record:

- the crossing parameter and cutoff;
- the crossing spectral point \(z\in\Gamma\);
- the incoming and outgoing Riesz ranks;
- the emerging generalized eigenspace;
- its reciprocal image;
- the first failed carrier or resolvent cell.

This witness localizes defect creation.

## Reciprocal charge

If a source reciprocal map \(J_X\) intertwines the pencils, then it transports
the Riesz projections:

\[
P_{-,X}(1-s)
=
J_XP_{+,X}(s)J_X^{-1}
\]

in the declared frame. Therefore

\[
q_{-,X}(1-s)=q_{+,X}(s).
\]

A defect token appears with its reciprocal partner unless the crossing occurs
on a fixed seam locus. Failure of rank equality falsifies the reciprocal
operator comparison even when scalar determinants satisfy a functional
equation.

## Relation to determinant winding

For determinant-class families, the rank \(q_X(s)\) equals the algebraic count
of characteristic-determinant zeros in the eigenvalue disk bounded by
\(\Gamma\).

It can be computed by an argument-principle integral. This is a topological
count, not the magnitude or phase normalization of the completed determinant
line.

A nonzero determinant multiplier can change magnitude and phase without
changing \(q_X\). Conversely, a contour crossing changes \(q_X\) even if a
separate scalar normalization obscures the event.

## Holomorphic families

If \(K_X(s)\) is holomorphic in \(s\), then \(P_X(s)\) is holomorphic while
\(\Gamma\) stays in the resolvent.

A holomorphic finite-rank projection has locally constant rank. The defect
bundle

\[
\operatorname{ran}P_X(s)
\]

is therefore a holomorphic vector bundle of constant rank on each admissible
component.

The zero-charge case is the zero bundle. A contour crossing is the only place
where a nontrivial defect bundle can be born or die.

## Why an anchor is not RH by itself

An anchor proves zero charge at one point. The no-crossing theorem carries the
RH content across the parameter component.

If the contour can cross spectrum, the anchor has no global force. If the
common carrier rotates or collapses, charge comparison is undefined. If the
limit gap is unknown, no common contour exists.

Thus anchor, transport, and contour separation are three distinct cells.

## Interaction with the seam

The open half-planes are separate parameter components after removing the seam.
A right-sector anchor propagates only through the right component.

Reciprocal congruence transfers it to the left component. The contour may fail
at the seam where the Green form degenerates; this is compatible with allowed
critical-line zeros.

No theorem should demand one contour through the seam.

## Hostile tests

1. A zero anchor without no-crossing control does not propagate.
2. Pointwise zero charge on disconnected samples does not cover a component.
3. Rank comparison on unstable carriers is undefined.
4. Scalar determinant reciprocity does not imply reciprocal charge equality.
5. Near-crossings with large resolvent norm must not be treated as safe.
6. Determinant magnitude control does not determine Riesz rank.
7. A moving contour can hide crossings unless its motion is source-governed.

## Consequence for categorical RH

The spectral defect is now an integer-valued charge. Once the common reduced
carrier and contour are established, a single source-authorized zero anchor
per open-sector component propagates by local constancy, provided a
no-contour-crossing theorem holds.

This changes the final spectral task from checking every parameter separately
to constructing:

- one anchor;
- one connected transport domain;
- one uniform resolvent contour;
- reciprocal charge transport.

## Verdict

Riesz rank is the categorical defect charge near generalized eigenvalue one.
It is locally constant under admissible parameter and cutoff transport. A
defect can appear only at a typed contour-crossing or carrier failure. One
zero-charge anchor therefore excludes an entire connected open-sector
component once no-crossing and reciprocal transport are proved.
