# A four-object plane-bearing infinity-category

## Question

Extend the plane-bearing triangular seed to four objects with direct, partially mediated, and fully mediated routes.

## Simplicial category

Let the objects be

\[
1,2,3,4.
\]

For \(i\leq j\), let \(P(i,j)\) be the set of strictly increasing directed paths from \(i\) to \(j\), including the identity path when \(i=j\).

Define a groupoid \(G(i,j)\):

- its objects are the paths in \(P(i,j)\);
- between every ordered pair of paths are two planes labelled by \(C_2\);
- plane composition adds labels modulo two.

The mapping space from \(i\) to \(j\) is the nerve of \(G(i,j)\). For \(i>j\), it is empty.

Composition concatenates path objects and adds plane labels modulo two. Path concatenation and label addition are associative and have identity paths and zero labels as units. This defines a simplicial category \(\mathcal P_4\).

## Route content

There are four routes from \(1\) to \(4\):

\[
(1,4),
\qquad
(1,2,4),
\qquad
(1,3,4),
\qquad
(1,2,3,4).
\]

There are two planes between every ordered pair of these routes. In particular, the direct route and full route remain distinct and admit two comparisons.

## Infinity-category

Define

\[
X=N_{\mathrm{hc}}(\mathcal P_4).
\]

Every mapping space is empty or the nerve of a groupoid, hence Kan. The homotopy-coherent nerve of a simplicial category with Kan mapping spaces is a quasicategory. Therefore \(X\) is an infinity-category.

This construction includes nontrivial plane multiplicity rather than reducing every comparison to strict equality.

## Mechanical audit

The exact checker verifies:

- the path counts between all ordered object pairs;
- four routes from \(1\) to \(4\);
- path-composition associativity;
- plane-label composition associativity;
- left and right identity paths;
- two planes from the direct route to the full route.

## Claim boundary

This is a constructed four-object plane-bearing infinity-category. Its choice of two planes between every route pair is freely specified, not derived from the coherence pyramid's source geometry. The object labels \(1,2,3,4\) are categorical objects here; this construction does not identify them with arity-grade types.

## Verification

```text
python research/voevodsky/checkers/check_four_object_plane_bearing_coherent_nerve.py
```

Artifacts:

- `research/voevodsky/checkers/check_four_object_plane_bearing_coherent_nerve.py`
- `research/voevodsky/results/four_object_plane_bearing_coherent_nerve.json`
