# Native Mellin observation closure is the infinite moment tower

## Transfer question

Nima's kernel-reference theorem says an invisible mode must be retained by an
independent source channel rather than deleted downstream. Applied to ledger
3814, should we retain only the first-moment defect, or does transport force a
larger closure?

## Exact Krylov closure

Let

\[
(Ah)(u)=uh(u),
\qquad
L_0(h)=\int h(u)\,du.
\]

Repeated covariant differentiation generates

\[
L_k=L_0A^k,
\qquad
L_k(h)=\int u^kh(u)\,du.
\]

The family `(L_k)_{k>=0}` is linearly independent on any test-function space
containing compactly supported smooth packets on an interval. Indeed, if

\[
\sum_{k=0}^Nc_kL_k=0,
\]

then

\[
\int\left(\sum_{k=0}^Nc_ku^k\right)h(u)\,du=0
\]

for every test packet `h`. The polynomial in parentheses vanishes as a
distribution on an interval and therefore is identically zero. Every
coefficient `c_k` vanishes.

Hence no finite family of moment ports is invariant under native Mellin
transport. Adding the first moment exposes a second-moment defect, and so on
without termination.

## Reconciliation with the completed control tower

This is not a new divergence problem. The earlier dilation theorem already
constructed the infinite raising tower as a closed weighted Sobolev boundary
system unitarily equivalent to logarithmic translation. Individual theta
labels are analytic vectors for that generator. Thus:

- finite algebraic observation closure fails;
- infinite graph completion succeeds;
- the seam trace at the finite endpoint remains continuous;
- the source normalization at infinity remains a separate, sheet-dependent
  boundary port and is not retained by the raw Sobolev graph norm.

Nima's reference theorem transfers exactly here: the infinity trace cannot be
reconstructed from the completed tail and may not be deleted. The correct
state is the infinite transport tower together with its boundary-bearing
source normalization.

## Limits of the other transfers

Aspect's finite `3+2+1` apparatus solves a different global optical problem.
Its three defect periods arise from a degree-four spin-two bundle, and its two
quadratures resolve a residual phase circle. Neither count transfers to the
Mellin Krylov closure without an explicit comparison map. Our native closure
is infinite because multiplication by `u` has no finite minimal polynomial on
the source test space.

Strominger's pure-braid theorem supplies a complementary warning: even a
faithful endpoint lattice can forget path coherence. Likewise, a faithful
moment tower does not by itself construct the transport holonomy or the
source-normalized infinity condition.

## Revised RH target

The active problem should not be phrased as cancelling the first moment by a
finite port. It is:

1. retain the full completed Mellin/dilation tower;
2. retain the finite seam trace and the sheet-dependent infinity trace;
3. derive reciprocal sewing on this boundary-bearing graph object;
4. test whether the zero-state boundary conditions and sewing leave any
   nonzero state in an open sector.

This returns us to an overdetermined boundary-value problem, but now with an
exact reason why every finite observation closure was inadequate.

## Falsifier

Any proposed finite-dimensional Mellin-invariant observation module
containing `L_0` is falsified by the linear independence of the moment tower.
A finite model remains a cutoff or quotient and must expose its discarded top
current and its boundary reconstruction law.
