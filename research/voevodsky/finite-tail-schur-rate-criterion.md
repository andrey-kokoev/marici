# Finite-tail Schur rate criterion

## Question

When does decaying Galerkin coupling compensate for a finite-block pivot that also approaches zero?

## Claim boundary

This packet derives an asymptotic rate criterion for the finite/tail Schur budget. It does not establish the relevant source exponents for the Weil operator.

## Rate model

Let the cutoff be \(M\). Assume:

\[
m_M\ge c_mM^{-p},
\qquad
b_M\le c_bM^{-q},
\qquad
a_M\ge c_a\log M-C_a,
\]

where \(m_M\) is finite-block coercivity, \(b_M\) is finite/tail coupling, and \(a_M\) is signed tail reserve. The Schur condition is

\[
b_M^2\le m_Ma_M.
\]

The ratio obeys

\[
\frac{b_M^2}{m_Ma_M}
\lesssim
\frac{M^{p-2q}}{\log M}.
\]

Therefore:

- if \(2q>p\), the ratio tends to zero;
- if \(2q=p\), the logarithm still drives it to zero;
- if \(2q<p\), the power loss dominates and the criterion can fail.

Thus the sharp asymptotic rate gate in this model is \(2q\ge p\), together with positive source constants and a valid tail lower bound.

## Exact fixtures

For \(M=2^k\), the admitted fixture uses

\[
m_M=M^{-1},\qquad b_M=M^{-1},\qquad a_M=\log M.
\]

Its Schur residual is \(M^{-1}\log M-M^{-2}>0\) for every checked \(M\ge2\).

The hostile fixture uses \(m_M=M^{-3}\) with the same coupling and tail. Its residual \(M^{-3}\log M-M^{-2}\) is negative on every checked cutoff.

## Relation to Sobolev control

The Sobolev factorization supplies a candidate coupling rate through the embedding tail. It does not supply the finite-block pivot exponent \(p\). Since compact operators have eigenvalues accumulating at zero, that pivot rate must be measured or bounded independently.

## Disposition

The off-diagonal gate is reduced to comparing two source rates: coupling decay \(q\) and finite-pivot decay \(p\). A tail theorem alone cannot decide positivity. The next executable source test should estimate these rates from interval Galerkin matrices and certified tail bounds.

## Verification

- `research/voevodsky/checkers/check_finite_tail_schur_rate_criterion.py`
- `research/voevodsky/results/finite_tail_schur_rate_criterion.json`
