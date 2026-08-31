# The canonical even-odd theta compression gives an explicit tau candidate

## Normalized reciprocal columns

On the relative wall-history carrier, let

\[
T=\frac{H-H^*}{2}
\]

be the reciprocal-odd Volterra history operator.  The canonical even and odd
theta source vectors are

\[
e=\frac{\Phi}{\|\Phi\|_2},
\qquad
o=\frac{\Phi'}{\|\Phi'\|_2}.
\]

They are orthonormal by parity.  Define the two-column incidence candidate

\[
V_\theta:\mathbb C^2\to\mathcal H_{\rm rel},
\qquad
V_\theta(1,0)=e,
\quad
V_\theta(0,1)=o.
\]

This is the most direct normalized reciprocal theta plane.  Whether it is
exactly the ledger's coefficient incidence \(V\) remains a source-typing
question.

## Exact odd matrix coefficient

The established relative identity is

\[
\langle\Phi',T\Phi\rangle=-\|\Phi\|_2^2.
\]

Since \(T^*=-T\),

\[
\langle\Phi,T\Phi'\rangle
=-\langle T\Phi,\Phi'\rangle
=\|\Phi\|_2^2.
\]

Therefore

\[
\langle e,To\rangle
=\frac{\|\Phi\|_2}{\|\Phi'\|_2}
=:r_\Phi>0.
\]

Parity kills the diagonal coefficients, so

\[
V_\theta^*iTV_\theta
=
\begin{pmatrix}
0&i r_\Phi\\
-i r_\Phi&0
\end{pmatrix}.
\]

With the ledger convention

\[
V^*iTV
=i\tau
\begin{pmatrix}
0&-1\\1&0
\end{pmatrix},
\]

the canonical theta-plane compression gives

\[
{
\tau_\theta
=-\frac{\|\Phi\|_2}{\|\Phi'\|_2}.
}
\]

Its sign is fixed and agrees with the previously established negative odd
incidence orientation.

## Positivity criterion

For this normalized compression,

\[
|\tau_\theta|<1
\iff
\|\Phi\|_2<\|\Phi'\|_2.
\]

The full retained-history theorem already proves positivity through the
stronger uniform bounds for \(I\pm iH\). Thus this scalar inequality is not
needed to establish the operator gate. It is instead a consistency check on
the proposed finite compression.

The non-proof scout
`checkers/check_rh_theta_tau_compression_numeric.py` evaluates the exact theta
series and reports

\[
\|\Phi\|_2^2\approx0.319751812,
\qquad
\|\Phi'\|_2^2\approx3.263887326,
\]

hence

\[
\tau_\theta\approx-0.312996101.
\]

Doubling the Simpson resolution changes both squared norms by less than
\(7\times10^{-15}\) relatively. This is numerical evidence only, not an
interval-certified norm inequality or a ledger-column identification.

## What is and is not identified

This calculation proves:

- the odd compression on the normalized \((\Phi,\Phi')\) plane is explicit;
- no free scalar remains once that plane and normalization are chosen;
- the compressed sign is source-fixed;
- the magnitude is one Sobolev norm ratio.

It does **not** prove that \(V_\theta\) is the ledger incidence \(V\).  The
coefficient wall module may carry Euler, Wronskian, half-density, or
prime-dependent normalizations before entering the history carrier.  If its
columns are

\[
V(e_1)=\alpha e,
\qquad
V(e_2)=\beta o,
\]

then

\[
\tau=-\alpha\beta
\frac{\|\Phi\|_2}{\|\Phi'\|_2}
\]

for real orientation-preserving scales.  Those scales cannot be guessed from
the normalized theta plane.

## Revised incidence-compression gate

The remaining G1.1 theorem is now sharply normalized:

> Prove that the source incidence columns entering the causal-history block are
> exactly the normalized theta columns \((e,o)\), or derive their source scales
> \((\alpha,\beta)\); then compare the resulting
> \(\tau=-\alpha\beta\|\Phi\|_2/\|\Phi'\|_2\) with the frozen Euler/Wronskian
> odd coefficient.

Thus the analytic compression formula is closed.  The unresolved content is
the typed incidence normalization and arithmetic identification, not the
Volterra matrix element itself.  No RH conclusion is authorized.
