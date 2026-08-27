# RH det3 composition forces a mixed boundary coherencer

## Result

An order-three regularized determinant is not ordinarily multiplicative under successive transformations on one carrier.

For commuting scalar increments (a) and (b), composition gives

\[
1+c=(1+a)(1+b),
\qquad
c=a+b+ab.
\]

The regularized bulk factor has logarithmic anomaly

\[
\mathfrak a_3(a,b)
=
ab\left(a+b+\frac{ab}{2}\right).
\]

For (a=1/2) and (b=1/3), this is (11/72).

The removed linear and quadratic boundary counterterm has exactly the opposite anomaly. Consequently the full finite determinant is multiplicative, while the regularized bulk and boundary packet are multiplicative only together.

## Typing consequence

The primitive and square currents cannot be represented as two independent additive ledgers once prime additions interact on a common carrier. Their boundary object needs a mixed comparison cell whose value cancels the regularized determinant anomaly.

There are two structurally different cases.

### Orthogonal prime blocks

If labelled prime additions enter as a direct sum of independent blocks, the regularized determinant factorizes without a mixed anomaly. Primewise current composition is admissible.

### Successive transformations on one carrier

If additions act through

\[
(I+A)(I+B),
\]

the mixed anomaly is generally nonzero. The source must derive its boundary comparison cell from the same composition. Declaring primewise additivity would erase real interaction data.

This supplies a finite typing test for the proposed adelic colligation: determine whether distinct primes are orthogonal objects, commuting endomorphisms of one object, or only partially composable correspondences. Those choices have different determinant coherence laws.

## Categorical formulation

The order-three determinant is not a strict monoidal functor on the full operator category. It becomes coherent only after adjoining the low-order anomaly object. The combined assignment

\[
K
\longmapsto
\bigl(\det_3(I+K),\ J_1(K),\ J_2(K)\bigr)
\]

must carry a comparison cell for composition. The cell is trivial on direct sums and nontrivial on overlapping transformations.

Thus the primitive and square currents are not merely values accompanying the bulk. They are the data that repair the monoidality lost by regularization.

## DPC

Candidate: multiply primewise regularized determinants and add primitive and square currents independently.

Verdict: valid only after proving orthogonal block incidence.

Candidate: assume commuting prime transformations have no anomaly.

Verdict: rejected by the exact scalar hostile (11/72).

Surviving candidate: construct the joint two-prime source block, classify its incidence, and derive the mixed boundary comparison before scalar projection.

## Immediate finite test

For two labelled prime additions (p) and (q):

1. construct the joint carrier and both incidence maps;
2. decide whether their images are orthogonal, overlapping, or sequential;
3. compute direct and staged order-three determinants;
4. compute the mixed primitive-square boundary term;
5. verify exact cancellation of the multiplicative anomaly.

If the anomaly is nonzero and no source-derived boundary cell supplies it, the determinant comparison route fails before completion.
