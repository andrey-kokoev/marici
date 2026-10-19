# Graded paths with occupied-support rewrites

## Objects

A reader object records:

```
(reader ID, species role, body site, realization origin, orientation)
```

A body may carry several reader objects. Particle counting is by occupied body
site and species, not by number of reader objects. Full marked charts remain
attached witness data; the small executable algebra uses their saved IDs.

## Arrows

An arrow is a witnessed path, annotated by:

```
(source reader, target reader, realization grade, full coefficient map,
 required occupied support, reference support, ordered native word)
```

Reference support contains occupied support. In the current executable test,
these support sets track carrier body sites, not all external chart-alias
vertices; full coordinate/alias validity is checked by the separate Python
witness checker before the algebra tests run.

Two paths with identical endpoints and maps need not be the same arrow. Their
words, support requirements and reference data can differ.

## Composition and identities

For composable paths a then b:

- endpoint readers must agree exactly;
- grades add;
- full five-coordinate maps compose;
- occupied supports and reference supports each take their union;
- words concatenate.

The identity at a reader has zero grade, identity coefficient map, empty word
and support consisting of that reader's occupied body site. These definitions
satisfy associativity and identity laws. The implementation checks them on the
saved N-15 and Ne-22 operation graphs.

## Reversal

R exchanges reader P/E roles, preserves N, toggles orientation, reverses path
order and inverts coefficient maps. Body-site support sets remain unchanged.

With grades measured in one fixed original coordinate:

```
grade(R(a)) = -grade(a)
R(a then b) = R(b) then R(a)
R(R(a)) = a
```

This is an involutive, composition-reversing map with an object involution.
It is not assumed to be an ordinary dagger fixing every object. Reflecting
coordinate labels as K-origin would express grades in a different coordinate;
that separate convention is not silently mixed into this algebra.

The previous context-aware M/C frame reversal supplies the chart-level layer.
This path model does not derive or replace that layer.

## The experimental rewrite

Within an actual selected configuration, consider the native pair:

```
P --PN--> N --NE--> E
```

The contraction guard requires:

- both factors are the specified, previously validated native operations;
- both have zero grade;
- P, N and E lie on three distinct body sites;
- P/E share exactly their C1/M1 edge;
- N is unoccupied in the selected configuration;
- the selected P reader has no onward selected native transfer;
- E is terminal.

The rewrite creates a PE arrow with:

```
same source and target
same zero grade
same full composed coefficient map
same reference support {P,N,E}
occupied support {P,E}
```

The uncontracted and contracted arrows are distinct. Forgetting the occupancy
requirement makes their endpoint/grade/map descriptions agree. That is the
precise meaning of retaining the transfer while removing occupied N support.

Terminality and vacancy refer to a selected configuration, so this is a
**context-conditioned graph rewrite**, not an unconditional equality in the
free path category. The containing assembly must still pass its global checks.

Its reverse rule is defined by conjugation with R. A forward terminal boundary
becomes a reversed entry boundary. It would be incorrect to demand the same
forward-terminal predicate after reversing the diagram.

## Executable checks

A separate Python witness audit runs as a prerequisite and its source hashes
are checked for freshness. The algebra checker reports:

| Property | Checks |
|---|---:|
| Left/right identities | 316 |
| Associativity | 350 |
| Reversal of composition | 229 |
| Double reversal | 158 |
| Successful experimental contractions | 6 |
| Invalid-contraction controls rejected | 24 |

The six contractions belong to the four previously passing N-14/Ne-21
configurations; two configurations use two contractions each. Invalid controls
occupy the reference neutron, violate proton-reader terminality, violate
electron terminality or remove the shared edge.

No additional isotope witness was searched. Category laws organize the rule;
they do not derive its occupancy permission. No confluence theorem, arbitrary
rewrite equivalence, full monoidal structure or knot invariant is asserted.
Production and viewer remain unchanged.

## Reproduction

```sh
python research/strominger/checkers/check_terminal_pe_independent.py
python research/strominger/checkers/check_graded_path_rules.py
```

Evidence: `results/graded-path-rules/verification.json`.
