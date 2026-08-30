# A closed Hall matching reserves the first even boundary rows

Before the first even extension, the old component has pole depths

\[
a=0,2,\ldots,q.
\]

The future semantic rows are

\[
-q-g-2,qquad -g-1.
\]

The first lies strictly left of the old component.  The following explicit
matching avoids the second as well.

For the two `a=0` columns, use

\[
(0,-)\mapsto1,
\qquad
(0,+)\mapsto q.
\]

For every `a>=2` minus column, use its left endpoint

\[
(a,-)\mapsto-a-g.
\]

For plus columns, generically use

\[
(a,+)\mapsto q-g-a.
\]

At odd grade there are two repairs:

\[
a=q+1-g,quad m=0:qquad(a,+)\mapsto0,
\]

using its nonzero `B1` coefficient proportional to `-g(g+3)`, and

\[
a=q-g-1,quad m=2:qquad(a,+)\mapsto2,
\]

avoiding collision with the `(0,-)` row.  Its `B1` coefficient has exactly one
admissible zero,

\[
(g,q)=(5,12).
\]

At that pair the zero is bypassed by the length-two alternating chain

\[
(4,+)\mapsto4,
\qquad
(6,+)\mapsto3.
\]

Both replacement weights are nonzero.  Thus this isolated failure is a local
chart obstruction, not a Hall deficiency.

All assigned rows are distinct.  Minus rows lie at or left of `-g-2`; generic
plus rows lie at or right of `-g`; parity separates their possible collisions.
The repaired rows fill the parity gaps zero and two, with the single longer
chain above when the row-two coefficient itself degenerates.

Therefore a complete nonzero Hall matching avoiding both future boundary rows
exists for every

\[
g\ge2,qquad q\ge2\text{ even}.
\]

This proves the support half of the reserved-row atlas theorem symbolically.
It does not by itself prove that the corresponding weighted maximal minor is
nonzero; that final initialization issue is an oriented-weight statement for
this explicit matching chart.

The checker audits the closed formulas through grade and even depth 100 and
retains the unrepaired odd-grade matching as a falsifier.
