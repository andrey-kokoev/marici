# Forbidden-channel induction: extremal-selector tests

Recursive vertex deletion enlarges the problem from an original common-tree complex to a pure induced restriction obtained by forbidding channels. The shedding criterion is exact: a variable channel must be flippable in every surviving facet containing it.

## Tested selectors through n=8

1. **Minimal variable channel, fixed lex choice.** Fails recursively at n=5.
2. **First shedding channel among minimal variables.** Fails recursively at n=6.
3. **First shedding channel among maximal variables.** Fails recursively at n=6.
4. **First shedding channel among minimal or maximal variables.** Succeeds through n=7 but fails in five n=8 order orbits.
5. **First shedding variable channel with no extremality restriction.** Succeeds for every recursive state through n=8.

The corresponding executable certificates are:

- `check_minimal_variable_channel_vertex_decomposition.py`;
- `check_maximal_variable_channel_vertex_decomposition.py`;
- `check_extremal_variable_channel_vertex_decomposition.py`;
- `check_common_tree_lex_vertex_decomposition.py`.

## First genuinely interior obstruction

A seven-facet recursive state arising from the full eight-point associahedron has ten variable/forced channels in total and one forced channel. None of its inclusion-minimal or inclusion-maximal variable channels is shedding. Its shedding channels are

- `{1,2,3}`;
- `{1,2,8}`;
- `{1,7,8}`;
- `{6,7,8}`.

Each is strictly interior in the containment poset of variable canonical intervals: each contains a smaller variable interval and is contained in a larger variable interval.

Therefore no proof based solely on choosing a containment-extremal interval can establish hereditary vertex-decomposability.

## Revised combinatorial target

Let `A` be the allowed common channels after imposing an arbitrary forbidden set, and assume the induced noncrossing complex `K[A]` is pure. Prove:

> There exists `v in A` such that every maximal noncrossing set containing `v` admits the flip replacing `v` by another member of `A`.

This is a pure-restriction theorem for the noncrossing complex of the special channel set `D_alpha intersect D_beta`. The n=8 interior obstruction shows that its proof must use quadrilateral flip structure or interval overlap, not only the containment poset boundary.
