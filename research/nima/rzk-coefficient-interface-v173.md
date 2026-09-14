# v173: explicit L2-to-log rank detector

The rank-one quotient selector is now explicit. Let `rho0` extract the u0
coefficient of `a^3 b^0`.

Every A-image column has u0 a-order at least four. The apparent `a^3` term from
`(3/2)d_a k` is always multiplied by an L2 base factor of positive a-order.
Therefore `rho0` annihilates A in all degrees. Exact expansion through D28
cross-checks all 6,960 labelled columns.

On the distinguished transition `3a^3+3a^3b`, `rho0` has value 3. Thus
`rho=rho0/3` selects the log primitive with unit pairing over `Z[1/3]`.
There is no integral unit pairing for this transition; the D12/D16/D20 left-
annihilator computations found the same detector ideal `(3)`.

This corrects the quotient language of module 199: `rho` acts on the Bockstein
image modulo the A-image, not on the cokernel after adjoining the full
Bockstein image.

Evidence is `results/L2-explicit-transition-detector.json` from
`checkers/check_L2_explicit_transition_detector.py`.
`rzk/201-l2-explicit-transition-detector.rzk.md` passes all eight declarations
without assumptions.
