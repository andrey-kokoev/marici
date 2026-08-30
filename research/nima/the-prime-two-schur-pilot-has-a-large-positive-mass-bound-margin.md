# The prime-two Schur pilot has a large positive mass-bound margin

## Numerical pilot

For

\[
L=\log2,
\]

evaluate

\[
a_2
=
\int_{\mathbb R}
|W_L(q)|^2e^{-\pi q^2}\,dq
\]

and

\[
d_2^2
=
\int_{\mathbb R}
|W_{2L}(q)-W_L(q)|^2e^{-\pi q^2}\,dq.
\]

A high-resolution symmetric Simpson pilot on \([-4,4]\), using the
error-function representation of the Gaussian windows, gives

\[
a_2\approx0.637405004,
\]

\[
d_2^2\approx0.0613563031.
\]

With

\[
M_\Phi
=
\xi\!\left(\frac12\right)
\approx0.497120778,
\]

the sufficient right-hand side is

\[
8(1-M_\Phi)^2a_2
\approx1.289534124.
\]

Hence the observed ratio is

\[
\frac{d_2^2}
{8(1-M_\Phi)^2a_2}
\approx0.0475802.
\]

The pilot margin is approximately

\[
1.22818.
\]

## Interpretation

The coarse monotone envelope could not decide \(p=2\), but the actual
Gaussian disagreement is far smaller than that envelope. The theta-mass
Schur certificate appears to pass by more than a factor twenty.

Since every \(p\ge3\) already passes through the monotone analytic
envelope, the numerical evidence supports a prime-uniform local
Schur-survival margin.

## Not yet a proof

The pilot used ordinary floating-point quadrature and a standard numerical
error-function evaluation. It is evidence, not a certified inequality.

The proof packet still requires outward enclosures for:

\[
a_2>0.6374-\epsilon_a,
\]

\[
d_2^2<0.06136+\epsilon_d,
\]

and

\[
M_\Phi<0.497121+\epsilon_M,
\]

with errors small enough that the intervals remain disjoint after forming

\[
d_2^2
<
8(1-M_\Phi)^2a_2.
\]

Because the observed margin is large, very coarse rigorous enclosures will
suffice.

## Easy certification budget

It is enough, for example, to prove bounds of the rough form

\[
a_2>0.6,
\qquad
d_2^2<0.1,
\qquad
M_\Phi<0.5.
\]

These imply

\[
8(1-M_\Phi)^2a_2
>
8\left(\frac12\right)^2(0.6)
=
1.2
>
0.1.
\]

Thus no high-precision theorem is needed. The next analytic task is to derive
these three rational inequalities directly from Gaussian and theta integral
bounds.

## Consequence if certified

Once these rough bounds are proved, the mass estimate yields

\[
q_{p,\pm}<16a_p
\]

for every prime and both reciprocal sheets, conditional on:

- constructor identification \(J_{\mathrm{src}}=J_{\mathrm{top}}\);
- exact normalized shifted-history square;
- reciprocal-odd Wronskian factorization.

The local Schur-loading margin would then be closed analytically, leaving
source functoriality rather than coercivity as the first Adams obstruction.

## Reproducibility note

The pilot computation used:

- the exact formula
  \[
  W_t(q)
  =
  -\frac12
  \left[
  \operatorname{erf}(\sqrt\pi(q+t))
  -
  \operatorname{erf}(\sqrt\pi(q-t))
  \right];
  \]
- symmetry about \(q=0\);
- Simpson integration on \([0,4]\) with \(200000\) panels;
- a negligible Gaussian tail beyond \(4\) at displayed precision.

A final checker should replace the approximate error function and tail claim
by interval-certified implementations.

## Verdict

The sole small-prime pilot passes decisively. The remaining proof does not
require delicate numerical analysis: rational bounds
\(a_2>0.6\), \(d_2^2<0.1\), and \(M_\Phi<0.5\) already provide an
order-of-magnitude safety margin.

This converts the pending finite computation into three elementary
inequalities suitable for a short certified checker or direct analytic proof.
