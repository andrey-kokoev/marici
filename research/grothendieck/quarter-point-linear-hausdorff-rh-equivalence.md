# RH as linear complete monotonicity of the quarter-point jet

Rescale the compact coordinate by `x=u/4` and moments by

\[
 m_k=4^{-k}A_k.
\]

Hausdorff's moment theorem states that an infinite real sequence is represented
by a positive measure on `[0,1]` exactly when it is completely monotone:

\[
 \boxed{C_{k,j}:=(-1)^j\Delta^jm_k
 =\sum_{r=0}^j(-1)^r{j\choose r}m_{k+r}\ge0}
 \qquad(k,j\ge0).
\]

Indeed, under a representing measure,

\[
 C_{k,j}=\int_0^1x^k(1-x)^j\,d\nu(x).
\]

Conversely, complete monotonicity constructs the unique Hausdorff measure.
Combined with the completed-source analytic identification already proved in
the quarter-point equivalence packet, this gives another RH-equivalent target:
every source-linear binomial combination `C_(k,j)` is nonnegative.

This is a major simplification of proof search. Hankel/localizer determinants
are excellent finite operator certificates, but the infinite existence theorem
can be attacked through linear inequalities rather than nonlinear minors. The
two descriptions encode the same compact measure from different directions.

All 55 available inequalities with `k+j<=9` are now interval-certified
strictly positive. This finite triangular region does not imply the infinite
condition or even replace the precise truncated extension criteria; its value
is to validate the new source-linear attack surface.

## New source question

Seek a direct completed-prime/gamma representation

\[
 C_{k,j}=\text{positive source quantity}

\]

uniformly in both indices. Such a representation would prove the entire
Hausdorff hierarchy at once and hence construct the unique Jacobi/Weyl limit.
This is now a cleaner universal-positivity target than guessing determinant
factorizations order by order.

## Scope

Fifty-five certified inequalities do not prove RH. The equivalence also
depends on the previously stated analytic identification of the completed
source resolvent.

## Durable verification

- Checker: `checkers/quarter_point_complete_monotonicity.py`
- Result: `results/quarter-point-complete-monotonicity.json`

All inequalities assemble into one bivariate source generator expressed by
two fractionally related evaluations of `S`. See
`hausdorff-bivariate-source-generator-theorem.md`.
