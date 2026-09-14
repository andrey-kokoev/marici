# v171: L2-to-log primitive rank reduction

The local logarithmic packet has one primitive orientation line, whereas the
true L2 Bockstein rational ranks at D12--D28 are `8,14,18,22,26`. Therefore
no physical comparison to that primitive line can retain all Bockstein
directions injectively.

Any such map has kernel rank at least `7,13,17,21,25` at the five cutoffs. This
is not an obstruction to a physical comparison; it determines its form. The
physical nearby-cycle realization must factor through a selected scalar
quotient/readout of the Bockstein cokernel.

Accordingly the next datum is a functional rho on the relation-derived
Bockstein quotient, together with proof that the actual physical Cech residual
lies in the rho-detected direction. Mapping every synthetic relation cell
faithfully into the rank-one log primitive is too strong and unnecessary.

Evidence is `results/L2-to-log-primitive-rank-reduction.json` from
`checkers/check_L2_to_log_primitive_rank_reduction.py`.
`rzk/199-l2-to-log-primitive-rank-reduction.rzk.md` passes all eight declarations
without assumptions.
