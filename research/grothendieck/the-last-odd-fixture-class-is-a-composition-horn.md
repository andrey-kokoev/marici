# The last odd fixture class is a composition horn

## Exact fill

The remaining reciprocal-odd cycle in Voevodsky's finite fixture is the boundary of

\[
\tau=-[w,-w,-a]+[-w,w,a].
\]

Each summand is an ordinary composition triangle. The first compares the two-step route `w -> -w -> -a` with the direct edge `w -> -a`; the second compares `-w -> w -> a` with `-w -> a`. Reciprocal reflection exchanges the two triangles, so their signed difference is odd.

## Conditional categorical closure

If the fixture 1-skeleton is the nerve of a category in which the displayed direct edges are the composites of the corresponding edge pairs, both inner horns have canonical fillers. Then `tau` is source-authorized by composition, the residual odd class vanishes, and the relative selector torsor is trivial on this fixture.

If the edges encode physical or analytic correspondences whose composites are not declared, the common endpoints do not create a 2-simplex. In that typing, adjoining `tau` remains unauthorized.

## New first missing datum

The missing datum is no longer an unspecified contraction. It is the composition readback for two exact pairs:

\[
(w\to -w)\circ(-w\to -a)=w\to -a,
\]

\[
(-w\to w)\circ(w\to a)=-w\to a,
\]

with the repository's actual composition convention. One must verify that these edges are morphisms in one category, that the direct edges are their composites rather than merely endpoint-matched alternatives, and that reciprocal reflection preserves the composition cells.

## Falsifier

The conditional fill fails if either pair is noncomposable, if its declared composite differs from the direct edge, or if reflection maps the composition witness to a distinct unfilled horn. Endpoint equality alone is insufficient.

## Disposition

Do not call `tau` canonical from graph combinatorics. Ask whether the source fixture is a category nerve and inspect its composition law. Under a positive readback the finite odd obstruction closes; under a negative readback it remains a genuine one-dimensional class.
