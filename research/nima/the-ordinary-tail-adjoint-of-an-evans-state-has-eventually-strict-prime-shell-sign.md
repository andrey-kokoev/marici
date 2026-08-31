# The ordinary tail adjoint of an Evans state has eventually strict prime-shell sign

## Positive theta tail

On the positive folded chart, the completed theta profile is real, positive,
strictly decreasing, and superexponentially decaying. Define its logarithmic
decay rate

\[
\lambda(q)
=
-\frac{\Phi'(q)}{\Phi(q)}.
\]

The explicit Gaussian theta series gives

\[
\lambda(q)\to+\infty,
\qquad
\frac{\lambda'(q)}{\lambda(q)^2}\to0.
\]

For the leading \(n=1\) Gaussian term,
\(\lambda(q)\sim2\pi e^{2q}\).

## Right Evans history

For fixed complex \(z\), the positive-end history is

\[
u_+(q;z)
=
-
\int_q^\infty e^{z(q-r)}\Phi(r)\,dr.
\]

Endpoint Laplace asymptotics gives

\[
u_+(q;z)
=
-\frac{\Phi(q)}{\lambda(q)+z}
\bigl(1+o(1)\bigr)
\]

as \(q\to+\infty\), locally uniformly for \(z\) in compact sets.
Consequently

\[
\operatorname{Re}
\bigl(
\Phi(q)\overline{u_+(q;z)}
\bigr)
=
-
\frac{\Phi(q)^2(\lambda(q)+\operatorname{Re}z)}
{|\lambda(q)+z|^2}
\bigl(1+o(1)\bigr)
<0
\]

for all sufficiently large \(q\).

## Nested prime moments

The ordinary zeroth-order part of the centered primitive column is

\[
b_p^{(0)}(q)
=
p^{-1/2}\Phi(q)\mathbf1_{[0,\log p]}(q).
\]

If its adjoint moments vanished for every prime,

\[
\langle b_p^{(0)},u_+(z)\rangle_{L^2}=0,
\]

then subtraction for consecutive primes \(p_n<p_{n+1}\) would give

\[
\int_{\log p_n}^{\log p_{n+1}}
\Phi(q)\overline{u_+(q;z)}\,dq
=0.
\]

For sufficiently large \(n\), the real part of the integrand is strictly
negative throughout this interval. The integral cannot vanish. Therefore the
ordinary-tail adjoint sequence is nonzero for every fixed \(z\):

\[
(B_\Sigma^{(0)})^\dagger u_+(z)\ne0.
\]

This conclusion applies in particular at every Xi zero.

## Meaning for the full Green adjoint

The completed Green incidence may contain derivative, wall, reciprocal, and
polarization ports in addition to the ordinary \(L^2\) tail port. The theorem
above does not forbid cancellation after those components are summed into one
source adjoint coordinate.

It does prove that any identity

\[
B_\Sigma^\dagger u_z=0
\]

must use an explicit nontrivial cancellation against the eventually
sign-definite ordinary tail moment. It cannot follow from the Evans seam
mismatch alone or from decay at infinity.

If the retained output keeps the ordinary tail port as a separate faithful
coordinate rather than summing it with the other Green ports, then the
unchanged Evans promotion is impossible outright.

## Uniformity qualification

The onset of strict sign depends on \(z\). The asymptotic is uniform only on
compact parameter sets; no uniform threshold over the unbounded critical seam
is asserted.

## Disposition

The ordinary theta-tail component of the arithmetic adjoint residual never
vanishes on an Evans state. A viable conservative chain map must therefore
exhibit a source-authorized derivative/wall/reciprocal cancellation or modify
the history. No such cancellation identity is currently proved. No RH
conclusion is authorized.
