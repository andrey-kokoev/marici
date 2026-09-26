# Comparisons between complete resolution histories

## Retained semantic records

`WholeHistoryComparisons.agda` fixes an interpretation algebra A. For two histories d,e with the same complete endpoint, their semantic comparison type is

Semantic(d,e) := evaluate(A,d) = evaluate(A,e).

A Compared record stores the endpoint, both complete histories, and the actual comparison witness. A Higher record stores two parallel witnesses and their equality. Reification stores the full records as next-level Complete values; history retention is independent of what the interpretation observes.

Identity, reversal, composition, associativity, right-unit and cancellation comparisons are provided using checked Cubical path operations. The higher reification explicitly includes both histories along with the witnesses and filler. The fixed interpretation is a parameter of the record types.

This construction concerns histories at a common complete endpoint. Comparisons across distinct endpoints require an additional endpoint equivalence/transport interface.

## Structural comparisons are distinct from supplied semantic paths

The Structural module takes a chosen law family and its interpretation. Generated comparisons have five constructors:

* reflexivity;
* inversion;
* composition;
* a selected law;
* rule congruence over the complete dependent premise family.

There is no arbitrary-semantic-witness import constructor. The sound function recursively interprets each generated comparison as a semantic path. Certified stores both histories, the generating derivation, its semantic witness and a path proving agreement with sound. That complete certificate is reifiable as a new Q.

The remaining witness-sensitive completeness type is now explicit:

For each semantic witness p between d and e, produce c:Generated(d,e)
and a higher witness sound(c)=p.

This is stronger than finding some comparison with the same endpoints. No inhabitant of this general completeness type is asserted.

## Concrete checked example and obstruction

`WholeHistoryComparisonInstance.agda` uses the earlier two histories from the same seed:

* direct identity-comparison rule;
* general comparison rule instantiated with identity equivalence.

Both yield the same complete endpoint. Their raw histories remain provably distinct.

An explicit endpoint-value interpretation reads the actual stored value of the endpoint. Under this observer, the two histories agree by a reflexive semantic path. The interpretation is a projection; the Compared/Certified records still retain both complete raw histories.

We then add one named law, identity-as-general, with that checked interpretation. It produces a structural comparison certificate, a next-Q retaining both histories, and a higher cancellation comparison. Recovery theorems check that both original histories remain in the reified certificate.

The empty-law basis is also examined. With only reflexivity, inversion, composition and congruence, every generated comparison induces an identity of raw histories. The previously checked history separation therefore proves:

* the available endpoint comparison has no derivation from that empty-law basis;
* the empty-law basis does not satisfy witness-sensitive semantic completeness.

Adding an appropriate cross-history law closes this concrete gap. This does not prove that this one law, or the current finite schemas, generate every semantic equivalence. It turns the completeness question into explicit law-basis obligations rather than admitting arbitrary witnesses under a different name.

## Verification

Fresh headless check:

```
agda --ignore-interfaces --transliterate -i research/nima/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/WholeHistoryComparisonInstance.agda
```

Exit 0 with Agda 2.8.0.1 / Cubical 0.9. This rechecked both new modules and their dependencies under `--safe --cubical --guardedness`, without new postulates or holes.

Files:

* `research/nima/agda/WholeHistoryComparisons.agda`
* `research/nima/agda/WholeHistoryComparisonInstance.agda`
