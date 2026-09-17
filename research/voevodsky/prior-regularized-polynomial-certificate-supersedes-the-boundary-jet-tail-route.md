# The prior regularized-polynomial certificate supersedes the boundary-jet tail route

A prior continuum certificate already implements the correct a posteriori
Schur mechanism for a closely related compact-window Weil form:

\[
F-BC^{-1}B^*=J-R^*C^{-1}R,
\qquad R=B^*-CY,
\]

and replaces the exact tail inverse by a proved floor `C>=alpha Q`, yielding

\[
F-BC^{-1}B^*\ge J-\alpha^{-1}R^*R.
\]

The pipeline in
`run_regularized_polynomial_certificate_pipeline.py` includes concentration
trace control, a finite tail-map candidate, exact-span orthogonalization,
residual Gram assembly, analytic Legendre-tail allowance, and final Arb
`LDL*`. This is stronger and better conditioned than certifying individual
dangerous eigenvectors and all of their boundary jets.

For the present `L=0.55` two-prime form, the reusable components are:

1. the gamma-floor tail `q(250)(I-K_250)` already certified here;
2. the complete rank-670 directed two-prime and endpoint matrices;
3. the trace-derived floor and range-compatible residual identity;
4. exact polynomial residual coefficients and an analytic coefficient tail;
5. final finite residual-Gram `LDL*`.

The source-specific changes are only the support radius, addition of the
`log 3` translation, rank 670 instead of 160, and the new directed gamma-floor
matrix. The old first-prime positivity result itself cannot be imported, but
its certificate architecture can.

Disposition: stop developing the nine-level boundary-jet certificate unless
the regularized residual Gram fails. The next executable task is to generalize
the existing pipeline inputs to the two-prime rank-670 artifacts.
