# On a Rank-One Tail Module Linear Boundary Rows Are Syzygies or New Boundary Conditions

After diagonal control sewing, every constructible terminal state is

\[
(G(0),c)=(F(s)c,c).
\]

Every linear terminal port restricts to multiplication by
`alpha(s)F(s)+beta(s)`. This yields a complete classification:

- a row valid for every constructible state is a syzygy of the terminal graph;
- a row with `beta=0` is Evans-derived and adds no force at a zero;
- a row with nonzero `beta` excludes a nonzero zero-state only by imposing a
  genuinely new boundary condition.

Therefore adding further linear primitive, square, seam, or archimedean ports
cannot solve the remaining problem unless their vanishing on zero-states is
independently derived. The surviving mechanism must be nonlinear in the state:
a bilinear Green, Wronskian, or Clifford conservation identity coupling the
off-seam coordinate to a faithful full-state energy, together with a
source-authorized endpoint-flux cancellation.

Research packet:
`research/grothendieck/on-a-rank-one-tail-module-linear-boundary-rows-are-syzygies-or-new-boundary-conditions.md`

Exact checker:
`research/grothendieck/checkers/check_rank_one_terminal_row_classification.py`

The checker passes 8/8 exact tests.
