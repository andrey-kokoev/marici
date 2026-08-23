# The plain conductor kernel is rank six, not twenty-four

Date: 2026-08-23

For each maximal-cone sign vector \(\sigma\in\{\pm1\}^3\) and contracted
pair \(P=\{i,j\}\), the tensor cube of the primitive difference row retains
only

\[
(P,\sigma_k),
\qquad k\notin P,
\]

with coefficient \(\sigma_i\sigma_j\).  Hence its raw comparison matrix is

\[
6\times24
\]

and has exact rank six.  Its kernel has dimension eighteen.

This is a sufficiency no-go, not a rejection of the conductor kernel.  The
kernel supplies the correct mixed-variance operation, reflection character,
and primitive difference row.  It does not retain enough information to
identify Entry 260's 24 source relations with Entry 262's 24 literal rows.

Merely tensoring one or two unselected binary spectator factors repeats the
same six rows and leaves the rank equal to six.  Therefore the missing
Boolean-state and Tor labels must have source-derived **routing maps**.  They
cannot be appended as inert multiplicities after contraction.

The next exact construction must derive two routing bits from the full-log
exceptional and Cartier filtrations.  Only then can a genuine \(24\times24\)
comparison and the global six-short-facet boundary be tested.

Evidence:

- `research/nima/checkers/check_tate_plain_conductor_kernel_rank_gate.py`.
- Entries 251, 259--262, and 627.

