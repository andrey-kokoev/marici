# Entry 2352: Cosmology capability matrices form equivariant descent data, not yet a sheaf

The sheaf conjecture was tested on the independent cosmological occurrence
charts `G12`, `G23`, and `G31`.  Their rank-26 quotient transitions are
invertible, the rank-seven annihilator planes are carried contragrediently to
the independently constructed target planes, and the cyclic transition
product is exactly

\[
T_{31,12}T_{23,31}T_{12,23}=I_{26}.
\]

Thus the coefficient matrices are local presentations of one descent object.
However, the source has no `G12`--`G23` double-pole overlap.  The charts are
related by source relabelling, not by restriction along ordinary open-set
intersections.  The correct object is therefore an equivariant vector bundle
or representation on the cyclic action groupoid, not a Čech sheaf on the
physical base.

Nor is it yet an operational capability bundle: the seven-plane consists of
coefficient annihilator classes, not source-admissible successor operations.
The next lift must attach operations, composition, and diagnostic selection
to these local fibers while preserving the same transitions.

The strongest current statement is:

\[
\text{local coefficient matrices}
+\text{source transitions}
+\text{cocycle}
=\text{equivariant descent datum}.
\]

Evidence:

- `research/nima/capability-matrices-form-equivariant-descent-not-yet-a-sheaf.md`
- `research/nima/checkers/check_capability_matrix_equivariant_descent.py`
- `research/nima/results/capability_matrix_equivariant_descent.json`
- sequence claim `seqclaim-1a58ee21f2ad1ef62aab49d5`
