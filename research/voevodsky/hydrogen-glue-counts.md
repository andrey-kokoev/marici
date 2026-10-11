# Testing two placements of neutron-as-glue

## Frozen assumptions

The operator asks to test both a nuclear glue placement and a proton–electron interface glue placement, counting the same kind of primitive arrows used in the 1836 construction: nonzero exact coefficient transfers between distinct typed stage ports.

This test supplies the simplest explicit glue contract: an identity factorization through a new typed interface. That contract is a hypothesis. Neither an electron's potential tetrahedral complex nor an independent neutron carrier is constructed. The electron interior remains an unknown common cost E; it is not silently replaced by a scalar point or one arrow.

The tested electron boundary has 36 separately typed channels, matching the retained core's 36 visible coordinates. One identity wire per coordinate in each direction is supplied. This is a declared boundary contract, not a result forced by electric charge, the six-belt or the full inward-fold structure. A full electron implementation may require a different contract and cost.

Two protocol observables are kept separate: the core's complete return operator N, and the attachment protocol's identity return I_36. We do not count arbitrary recurrent walks through the combined graph as the chosen observable.

## Actual constructed counts

| Conditional candidate | Core protocol arrows | Boundary attachment arrows | Known total, excluding E |
| --- | ---: | ---: | ---: |
| H-1-labelled boundary prototype | 1836 | 72 | 1908 |
| H-2-labelled nuclear glue | 1872 | 72 | 1944 |
| H-2-labelled interface glue | 1836 | 108 | 1944 |

### Baseline attachment

For each visible coordinate i, add raw_i -> electron_i -> raw_i, with unit weights. This is 36+36=72 arrows. The electron port is a typed interface endpoint, not a proof that the associated electron interior exists.

### Nuclear placement

Factor the retained G stage as I_36 G. Each existing local-to-aligned coefficient is redirected to a new nuclear-glue stage; 36 unit arrows take that stage to aligned. The original L and dense feedback N remain. The core count is 108+432+36+1296=1872, with the same complete core return N.

This preserves G's coefficients and composite map but changes the endpoints of its 432 active arrows. It is a new factorization, not an assertion that 36 arrows were simply appended to an entirely untouched graph. The original package remains retained as source/provenance, while the reported cost counts each active candidate protocol's arrows, not all historical records in the Merkle store.

### Interface placement

Leave the original core unchanged. Replace each outgoing raw_i -> electron_i wire by raw_i -> interface-glue_i -> electron_i, retaining electron_i -> raw_i. This gives 36+36+36=108 attachment arrows and the same attachment return I_36.

## What the equality of counts means

Both full-width placements add 36 active arrows, but they are different typed networks. Their coincidence is not a neutron prediction: it follows because both chosen interfaces have width 36.

For an attachment interface restricted to m selected visible channels, the same explicit rules give:

| Width m | Baseline + E | Nuclear placement + E | Interface placement + E |
| --- | ---: | ---: | ---: |
| 1 | 1838 | 1874 | 1839 |
| 6 | 1848 | 1884 | 1854 |
| 12 | 1860 | 1896 | 1872 |
| 36 | 1908 | 1944 | 1944 |

The formulas are 1836+2m, 1872+2m and 1836+3m respectively. These controls vary the declared boundary observable; they do not establish that a narrower interface retains everything an actual electron realization needs.

## Pruning and semantic test

Every active core arrow lies on a positive closed protocol traversal. Their weights sum to one. Every attachment arrow lies on a positive identity-return traversal; their weights sum to 36. The two covers jointly contain every active arrow of the full-width candidate.

Deleting any active arrow with the remaining coefficients and stage protocols fixed destroys at least one of the two return observables. Thus each candidate is pruning-minimal for the declared pair of protocols, in the same deletion-only sense used for the original network. This does not prohibit contracting an identity stage or refactoring the graph.

That distinction is decisive here: both glue stages can be contracted without changing the observed pair (N,I_36). **Neither identity-glue placement establishes a distinguishable isotope at this interface.** More structure would have to make the glue a noncontractible, observable part of the retained realization rather than a redundant factorization.

## Verification and artifacts

All 12 tests passed: exact counts, full matrix compositions, positive protocol coverage, distinct typed graphs, width dependence, missing-arrow and protocol-substitution controls, and serialized replay. A passing suite certifies these conditional constructions and their failure to distinguish isotopes; it does not identify the candidates with physical H-1 or H-2.

```text
python research/voevodsky/checkers/check_hydrogen_glue_counts.py
```

- `research/voevodsky/results/hydrogen_glue_counts.json`: counts, tests and assumptions.
- `research/voevodsky/results/hydrogen_glue_store.json`: source package, all three typed networks and their protocol declarations.
- `research/voevodsky/checkers/check_hydrogen_glue_counts.py`: constructor and exact verifier.

No atomic masses, neutron energy or electron interior cost are inferred. The next discriminating requirement is a specified glue invariant or retained witness obligation that differs between the two candidates and cannot be removed by identity-stage contraction.
