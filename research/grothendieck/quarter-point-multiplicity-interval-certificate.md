# The blind residue-one prediction is interval-certified

For monic orthogonal polynomials `p_k` with norms `h_k`, the Gaussian weight is

\[
 w(u)=\left(\sum_{k=0}^{4}\frac{p_k(u)^2}{h_k}\right)^{-1}.
\]

Outward evaluation at the certified top node gives

\[
 w_{\max}\in[0.00499903811082216,\ 0.00499903815612013].
\]

Since multiplicity `m` contributes quarter-point mass `m u`, division yields

\[
 \boxed{\widehat m_1\in
[1.000010685627119,\ 1.000010695098347]}.
\]

The slight excess above one naturally comes from finite quadrature assigning
unresolved tail mass to the top node; it is not evidence for nonintegral true
multiplicity.

## Scope

This certifies a finite residue estimator. It does not prove limiting ratio
one, first-zero simplicity, or eigenspace dimension. No zero enters construction.

## Durable verification

- Checker: `checkers/quarter_point_multiplicity_interval.py`
- Result: `results/quarter-point-multiplicity-interval.json`
- Polynomial data: `results/quarter-point-jacobi-diagonal.json`
