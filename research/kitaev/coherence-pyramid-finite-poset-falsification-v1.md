# Falsification attempt on the finite certificate-poset conjecture

## Question

Does every legitimate transfer have a presentation-independent minimal antichain of failures in one finite certificate poset, with passage of all predicates sufficient for transfer?

## Claim boundary

This packet tests canonicity and falsifiability of the registry predicates. It does not deny that a fixed engineering checklist can be useful.

## Bold conjecture under test

For each typed transfer, a finite predicate poset is sufficient; failed transfers determine an audit-order- and presentation-independent minimal antichain; passage of all predicates excludes global failure.

## Falsification 1: predicate refinement changes the minimal antichain

Suppose a transfer fails the registry predicate `quotient_descended`. Replace that predicate by two predicates:

- invariance under the equivalence relation;
- existence of the induced target map.

These are jointly equivalent to descent, but a malformed fixture may fail both. The original registry reports the singleton antichain `{quotient_descended}`; the refined registry reports a two-element antichain. Conversely, adjoining the conjunction as one new predicate collapses any finite antichain to a singleton. Therefore the minimal antichain is not presentation-independent unless the programme supplies a canonical irreducible predicate basis and proves invariance under conservative refinements.

## Falsification 2: broad predicates make sufficiency tautological

The predicates `coherent_finite_composition`, `completed_or_unbounded`, and `source_typed_physical_readout` currently lack bounded acceptance schemas. Any discovered global obstruction can be reclassified as failure of one of them. Then the claim that no failure remains after all predicates pass is true by definition rather than risky. A finite list of names is not a finite certificate basis unless each predicate has an independently fixed constructor and hostile test.

## Global hostile fixture

Use the exponential covering map from the real line to the circle. On every proper arc of the circle there is a continuous logarithm. Local source typing, local comparison, quotient compatibility, and every finite composition wholly contained in one arc pass. Pairwise branch changes are integer translations. Yet no global continuous logarithm exists: a loop of winding number one returns with translation by one period.

This does not refute a predicate explicitly requiring global effective descent or loop coherence. It shows that finite local-square passage is insufficient and that the word `coherent` cannot stand in for the missing global acceptance test.

## Strongest residual

The conjecture is falsified as stated at presentation-independent uniqueness. Its sufficiency clause is currently non-falsifiable because broad predicates can absorb arbitrary residuals.

## Surviving conjecture

Fix a versioned predicate presentation with explicit constructors and acceptance tests. Relative to that presentation, each transfer has a reproducible set of failed predicates and a derived minimal antichain. Claims are invariant only under declared equivalences of predicate presentations. Global descent, loop coherence, completion, and readout each need bounded schemas; no claim of a canonical or complete finite basis is made.

## Disposition

Revise again. Replace `unique minimal antichain` by `minimal antichain relative to registry version`. Add predicate-presentation version, acceptance-test reference, and conservative-refinement map to every registry release. Add a global loop/descent hostile before admitting comparison systems assembled from local charts.
