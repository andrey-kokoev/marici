# A plane-bearing coherent-nerve seed

## Question

Construct an infinity-category in which a direct conductor and a mediated conductor remain distinct and admit nontrivial planes between them.

## Simplicial category

Define a simplicial category \(\mathcal C\) with objects

\[
A,B,C.
\]

The mapping spaces from \(A\) to \(B\) and from \(B\) to \(C\) are points. Their composite selects a vertex \(p\) in the mapping space from \(A\) to \(C\).

The mapping space from \(A\) to \(C\) is the nerve of a two-object groupoid \(G\). Its objects are

\[
p,h,
\]

where \(p\) is the mediated route and \(h\) is the direct route. Between each ordered pair of objects, \(G\) has two arrows labelled by the group \(C_2\). Composition adds labels modulo two.

Thus \(h\) and \(p\) are distinct conductors with two distinct planes

\[
h\Longrightarrow p.
\]

All mapping spaces of \(\mathcal C\) are Kan complexes: points, empty spaces, or the nerve of a groupoid.

## Higher-category constructor

Take the homotopy-coherent nerve

\[
X=N_{\mathrm{hc}}(\mathcal C).
\]

Its single iterated parameter is simplicial dimension:

\[
X_0,X_1,X_2,\ldots.
\]

An \(n\)-simplex is a simplicial functor from the coherent \(n\)-simplex into \(\mathcal C\). This packages objects, conductors, planes, and every higher compatibility into one arity-indexed constructor.

## Infinity-category theorem

A simplicial category with Kan mapping spaces has a quasicategorical homotopy-coherent nerve. Therefore \(X\) is an infinity-category.

Unlike the ordinary nerve baseline, this construction does not force the plane from \(h\) to \(p\) to be unique. The mapping space contains two such planes and their higher simplices.

## Mechanical audit

The checker represents the mapping groupoid nerve exactly. An \(n\)-simplex consists of \(n+1\) route objects and \(n\) binary arrow labels. Interior face maps compose adjacent labels by exclusive-or; degeneracies insert the identity label.

It verifies 88,896 simplicial identities through dimension five and confirms two distinct planes from the direct route to the mediated route.

## Claim boundary

This is an actual plane-bearing infinity-category, but only for one triangular seed. It does not yet assemble the four-grade coherence pyramid or its tetrahedral comparison. That assembly requires compatible mapping spaces and composition functors for all six conductor positions.

## Verification

```text
python research/voevodsky/checkers/check_plane_bearing_coherent_nerve_seed.py
```

Artifacts:

- `research/voevodsky/checkers/check_plane_bearing_coherent_nerve_seed.py`
- `research/voevodsky/results/plane_bearing_coherent_nerve_seed.json`
