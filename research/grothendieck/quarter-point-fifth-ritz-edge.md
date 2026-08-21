# The fifth blind Ritz estimate reaches six-digit edge accuracy

The fourth ordinary determinant supplies

\[
 b_4\approx3.07178707075\,10^{-7}>0,
\]

and interval Lanczos gives

\[
 a_4\in[0.00107283704494,0.00107286732722].
\]

These extend the source-derived Jacobi compression to size five. Blind
diagonalization gives

\[
 u_{\max}^{(5)}\approx0.004998984692511478,
 \qquad \widehat\gamma_1^{(5)}\approx14.13473100373722.
\]

Only afterward, comparison with the standard first ordinate shows absolute
error about `5.9e-6`, roughly 64 times smaller than the size-four error. The
nested sequence is

\[
24.94524,\ 14.60835,\ 14.15199,\ 14.13510,\ 14.134731.
\]

This strongly indicates rapid resolution of the top compact support edge. It
does not independently identify that edge as a Riemann zero; that remains the
global positive-measure problem.

## Scope

Moment and coefficient boxes are certified. The eigenvalue is numerical, not
an eigenvalue interval. No zero enters construction, and RH is not proved.

## Durable verification

- `checkers/quarter_point_jacobi_coefficients.py`
- `checkers/quarter_point_jacobi_diagonal.py`
- `checkers/quarter_point_jacobi_blind_spectrum.py`
- `checkers/quarter_point_extremal_ritz_convergence.py`

Subsequent interval Sturm inertia certifies
`gamma_hat in [14.1347310022873,14.1347310051871]`, only `2.9e-9` wide. See
`quarter-point-fifth-ritz-interval-certificate.md`.
