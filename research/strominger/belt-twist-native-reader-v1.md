# Belt-chart twist versus native neutron reader advance

## Exact geometric match

The belt-reader interface's proper-permutation loop has order two. Its expression
depends on the explicit marking of the reference pair's common edge and outer
vertices. Of the four possible such markings, exactly two give

```
b <-> v,  u <-> c
```

with `b=M0`, `u=C1`, `v=M1`, `c=C2`. This is the actual marked four-vertex
permutation of the native same-body N reader advance.

This constrains the previously arbitrary marking; it does not declare every
marking equivalent while keeping the C/M labels fixed.

## Native availability and the facet metric

Replayed the native generator for all 24 saved hydrogen seed markings.

- Eight admit a same-body N reader advance. All eight have exactly the
  geometric permutation above, and increase origin by one.
- The same eight, and no others in this sample, preserve the N-facet edge
  metric under that permutation.
- Two admitted advances restore the four-vertex chart geometry while
  increasing absolute origin by two.

Thus the previously found chart twist has a native marked-geometric realization
on precisely the metric-compatible subset of this local sample. The other 16
cases are not made admissible by changing or forgetting the metric.

## Interpretation and remaining interface

The two-face reader can switch to its complementary two-face presentation
inside the same tetrahedron, keeping its graded history. The belt's local
chart construction can be marked so its loop has that same endpoint action.
This is a concrete connection between belt charts and realization geometry,
stronger than merely sharing an order-two symmetry.

It does not yet identify execution of a belt-chart loop with a native reader
advance. Equality of marked endpoint permutations cannot supply the loop's
origin increment, its five-coefficient action, or an induced transformation on
the 36 field components. The latter operator and its P/N compatibility remain
the next field-sewing obligations. No global tessellation or admission rule is
changed.

```sh
node research/strominger/checkers/check_belt_twist_native_reader.mjs
```

Evidence: `results/belt-twist-native-reader/verification.json`.
