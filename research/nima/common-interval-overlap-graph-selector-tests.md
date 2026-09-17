# Selector tests on common-interval overlap graphs

The identity

\[
K(\alpha,\beta)=\operatorname{Ind}(O(\alpha,\beta))
\]

allows standard graph-theoretic shedding criteria to be tested directly.

## Neighborhood domination

A familiar sufficient condition for a shedding vertex in an independence complex uses nested neighborhoods: select `v` when a neighboring vertex `u` has a closed neighborhood contained in that of `v`. This gives recursive decompositions for many graph classes.

`check_dominated_or_c5_vertex_decomposition.py` tests this selector, first with a 5-cycle exception and then with full type-A associahedral overlap graphs admitted as atomic base cases.

The rule fails:

- with only domination and `C5`, failures begin at six points;
- admitting every full type-A associahedral state as an atom still leaves a nine-facet, eight-vertex recursive obstruction immediately after decomposition of the six-point atom;
- the obstruction has overlap-graph degree sequence `(2,2,3,3,3,3,4,4)` and no usable domination selector.

Thus these common-interval overlap graphs are not recursively codismantlable by neighborhood inclusion, even after ordinary associahedra are treated as known vertex-decomposable atoms.

## Consequence

The required shedding phenomenon is genuinely exchange-theoretic. It is not explained by:

- containment-minimal intervals;
- containment-maximal intervals;
- either containment extreme;
- closed-neighborhood domination;
- domination plus cycle or associahedral atoms.

A successful proof must use the full quadrilateral replacement relation among maximal nonoverlapping interval families. The promising object is therefore not merely the overlap graph, but the pair consisting of that graph and its maximal-independent-set exchange structure.
