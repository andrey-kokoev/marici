# The Incidence Kernel Coefficients Are Not an Equivariant Charge Character

WP847 tests whether WP820's integer incidence complex derives the full
character used by WP846. It does not. Although

\[
Bq=0,
\qquad q=(1,2,3)^T,
\]

interpreting the entries of (q) as weights of
(Q=\operatorname{diag}(1,2,3)) would require a target generator (A) with
(AB=BQ). The necessary kernel condition fails:

\[
BQq=(-2,-6)^T\ne0.
\]

Consequently the kernel line is not (Q)-stable and no target generator
intertwines the proposed action. The complex has rank two, kernel dimension
one, zero cokernel, and ordinary Euler index one. It does not produce the
three-term character (z+z^2+z^3).

WP846 remains a valid conditional threshold repair when the labelled charge
character is independently admitted. A new (U(1))-equivariant complex with
an oriented representation-valued index must be constructed before the
character remainder and holonomy probes acquire source authority.

Verification: 12 of 12 exact checks pass in
`research/flavor/checkers/wp847_incidence_kernel_not_equivariant_charge_index.py`.

Graph admission: `ev-000000007936-1b0faecb-fe6f-4278-9cc6-c0f081374498`.
