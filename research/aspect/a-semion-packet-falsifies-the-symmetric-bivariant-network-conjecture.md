# A semion packet falsifies the symmetric bivariant network conjecture

## Target

The conjecture claimed that every physical presentation is a diagram in a dagger symmetric monoidal double category.

The word “symmetric” is false.

## Exact hostile

Take the semion fusion packet with one nontrivial simple object \(s\), fusion \(s\otimes s=1\), and exchange scalar

\[
R_{ss}=i.
\]

The exchange is unitary, but its double braid is

\[
R_{ss}R_{ss}=i^2=-1.
\]

A symmetric monoidal category requires double exchange to equal the identity. The semion packet returns a measurable minus sign. Therefore a physically meaningful instrument–data network need not be symmetric monoidal.

The defect is not cured by calling the sign an extra scalar port. It is a relational comparison of two compositions, exactly the kind of lift cell isolated by Strominger.

## Strictification hostile

There is a second warning. On \(\mathbb Z_2\), define the normalized associator

\[
\omega(a,b,c)=(-1)^{abc}.
\]

It obeys the cocycle, hence pentagon, identity. It is not the coboundary of any normalized two-cochain: at \((1,1,1)\), every such coboundary equals one while \(\omega=-1\).

Thus the associator cannot be discarded as presentation noise. A grammar that treats all compositions as strictly equal erases physical coherence data even when its objects and arrows are correct.

## Disposition

The conjecture is falsified as stated. Its surviving core is bivariant diagrammatics, not symmetry or strict two-dimensional closure.

The repaired categorical carrier is:

> a dagger braided or ribbon higher equipment, with contravariant and covariant indexed faces, in which symmetry and categorical truncation depth are sector properties rather than universal axioms.

This carrier admits:

- symmetric sectors when double braiding is trivial;
- braided sectors when exchange order is retained;
- projective lift cells when compositions agree only after quotient;
- higher coherence cells when associators or anomalies are nontrivial.

The tower expressions remain meaningful, but they describe actual factorization in this higher equipment. They cannot be inferred from rank, port count, or a strict wiring diagram.

## New falsifier for the repair

For any proposed sector:

1. measure or compute double braiding;
2. test whether associators are cohomologically trivial;
3. test whether all comparison cells close at the declared categorical depth;
4. raise the carrier from symmetric to braided, or from 2-categorical to higher, whenever a residual survives.

The repaired conjecture fails if a physical packet has coherence of no finite or locally finite categorical presentation, or if two inequivalent higher diagrams remain indistinguishable under every admissible composition and comparison.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_bivariant_network_semion_falsifier.py
```
