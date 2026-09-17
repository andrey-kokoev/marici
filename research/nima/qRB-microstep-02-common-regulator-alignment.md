# qRB microstep 02: common-regulator alignment

The next requirement is not a uniform bound. It is that the Tate and reference presentations use the same common weighted bulk before subtraction.

For aligned finite regulators,

$$
G_T=K+D_T,
\qquad G_0=K+D_0,
$$

so the common bulk cancels in the relative comparison:

$$
G_T-G_0=D_T-D_0.
$$

The exact rational fixture `check_positive_regulator_alignment_fixture.py` passes all checks at exact arithmetic, including positivity of both finite Gram forms and failure under mismatched placement.

This establishes the correct local `R` rule: align the regulator first, then take the signed relative readout. Independent sharp windows are not interchangeable.

Still open: extending this identity from the finite fixture to the analytic semilocal regulator family and proving convergence of the cross-readout.
