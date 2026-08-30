# Dependent incidence self-closes locally, but transport can retain holonomy

**Owner:** marici.Kitaev  
**Status:** bounded research packet  
**Question:** Does the dependent behavior bundle require an indefinitely higher coherencer?

## 1. Static incidence and dynamic transport differ

A dependent behavior object has two kinds of structure:

1. **Static incidence:** which coordinate packets may coexist over one index.
2. **Dynamic transport:** how packets move when authority, resources, domain, or fault state changes.

Static incidence can often terminate by a finite universal-property theorem.

Dynamic transport can remain path-dependent and carry holonomy.

Conflating them would either overbuild the static tower or incorrectly quotient meaningful transport information.

## 2. Pullback closure theorem

Suppose two behavior components map to a common index object:

\[
B_1\xrightarrow{p_1}Q,
\qquad
B_2\xrightarrow{p_2}Q.
\]

Their jointly admissible packets form the pullback

\[
E=B_1\times_QB_2.
\]

Assume component mixed laws

\[
\lambda_1:T B_1\to B_1T,
\qquad
\lambda_2:T B_2\to B_2T
\]

induce the same base-index transition.

Then their projections form a compatible cone over the pullback. By its universal property, there is a unique joint lift

\[
\lambda_E:T E\to E T
\]

whose projections are \(\lambda_1\) and \(\lambda_2\).

Therefore static incidence self-closes once:

- the defining limit or predicate is frozen;
- component laws are proved;
- their base maps agree;
- the relevant construction preserves or supplies the required cone.

No independent higher joint coordinate is needed after the universal property applies.

## 3. First static falsifier

The first failure is not a scalar mismatch. It is disagreement of the induced base maps.

For a packet \(x\in TE\), compute

\[
p_1\lambda_1T(\pi_1)(x)
\]

and

\[
p_2\lambda_2T(\pi_2)(x).
\]

If they differ, the component outputs do not define a point of \(E\). The joint lift does not exist.

This types the earlier authority/action hostile as a failed pullback cone.

## 4. Indexed transport

Let \(Q\) now be a category of index states and authorized transitions. A dependent behavior family is represented by an indexed category or pseudofunctor

\[
F:Q^{\mathrm{op}}\tomathbf{Cat}.
\]

Each base arrow \(f:q\to q'\) induces reindexing between fibers.

Identity and composition are preserved strictly or through coherent isomorphisms. In the pseudofunctor case, unit and associativity coherence cells must satisfy triangle and pentagon laws.

Those finite laws force coherent comparison among all parenthesizations of a fixed composite path. Thus the reindexing syntax can self-close in the ordinary categorical sense.

## 5. What local coherence does not prove

Two different paths with the same endpoints need not induce the same transport.

For a loop

\[
gamma:q\to q,
\]

reindexing can produce a nontrivial automorphism

\[
F(gamma):F(q)\to F(q).
\]

This holonomy survives every local identity, composition, triangle, and pentagon law.

Therefore:

- coherence of path composition does not imply path independence;
- endpoint equality does not imply transport equality;
- quotienting paths by endpoints requires an independent flatness or trivial-holonomy theorem.

This is the same Carrier geometry as the toric code. Local repair data can close while noncontractible transport remains as a logical sector.

## 6. Three coefficient lenses return

The retained loop information depends on the coefficient lens.

- An additive lens may retain only an accumulated scalar current.
- A determinant-line lens may retain an abelian phase or orientation.
- A noncommutative lens retains ordered holonomy.

Projecting to a scalar can erase the distinction between different loops even when the dependent transport is coherent.

Thus behavior indexing itself can carry the scalar/phase/ordered tower previously identified in Carrier geometry.

## 7. When global transport self-closes

Global endpoint-only closure requires one of the following source-derived results:

1. the relevant base region is contractible;
2. the connection or reindexing is flat and has trivial monodromy;
3. admitted path relations generate all homotopies and transport respects them;
4. the claimed equivalence intentionally quotients the holonomy representation;
5. a separating loop-probe family records every retained holonomy class.

Each result gives a different claim. None follows from local pseudofunctor coherence alone.

## 8. Hostile models

1. **Base-map mismatch:** components pass separately but do not form a pullback cone.
2. **Pentagon failure:** pairwise reindexing cells exist but triple composition is inconsistent.
3. **Loop hostile:** every local square commutes while a closed path acts nontrivially.
4. **Scalar erasure:** distinct holonomies have the same scalar readout.
5. **Unauthorized flatness:** endpoint equality is imposed without a source path relation.
6. **Completion holonomy:** finite contractible charts acquire limiting monodromy.
7. **Reference activation:** holonomy invisible without a frame becomes distinguishable after adjoining one.
8. **Reset transport:** reset returns the visible index but not the same fiber state.

## 9. SCC consequence

SCC should separate:

```json
{
  "static_incidence": {
    "construction": "pullback | equalizer | finite_limit | predicate",
    "component_maps": ["..."],
    "shared_base_agreement": "proved | failed | open",
    "joint_lift": "unique | absent | nonunique"
  },
  "dynamic_transport": {
    "base_category": "...",
    "fiber_assignment": "...",
    "identity_law": "...",
    "composition_law": "...",
    "triangle_pentagon": "...",
    "path_equivalence": "...",
    "holonomy_status": "trivial | represented | erased | open"
  }
}
```

A local-coherence certificate must never be reported as trivial holonomy.

## 10. Present conclusion

The dependent behavior tower partly self-closes:

- static incidence closes by a limit universal property;
- reindexing composition closes by ordinary coherence laws;
- global transport may still retain an independent holonomy representation.

So the next higher object is not always another coherencer. It may be a genuine logical sector carried by loops in the behavior-index space.
