# Alternating error-function series give rational certificates for the five normal bounds

## Series certificate

For \(xge0\),

\[
\operatorname{erf}(x)
=
\frac2{\sqrt\pi}
\sum_{n=0}^{\infty}
\frac{(-1)^nx^{2n+1}}
{n!(2n+1)}.
\]

At every argument needed for the prime-two audit, the absolute terms decrease
from the first term onward. Therefore even and odd partial sums give outward
bounds, and the first omitted term bounds the remainder.

Since

\[
\Phi(z)
=
\frac12
\left[
1+
\operatorname{erf}
\left(
\frac z{\sqrt2}
\right)
\right],
\]

all five normal inequalities have elementary alternating-series
certificates.

## Rational input enclosure

Use the conservative rational bounds

\[
3.14159<\pi<3.14160,
\]

\[
0.693147<\log2<0.693148,
\]

\[
1.73205<\sqrt3<1.73206.
\]

They imply an outward interval for

\[
u=\sqrt\pi\log2
\]

contained in

\[
1.22856<u<1.22859.
\]

Monotonicity of \(\Phi\) and \(Q\) determines which endpoint must be
inserted in each inequality.

## Required arguments

The four distinct normal arguments are

\[
u,
\qquad
\frac32u,
\qquad
\frac{u}{2\sqrt3},
\qquad
\sqrt3u.
\]

The corresponding error-function arguments are obtained by division by
\(\sqrt2\). All lie below \(1.51\).

For \(0\le x\le1.51\), the ratio of consecutive absolute series terms is

\[
\frac{x^2(2n+1)}
{(n+1)(2n+3)}
<1
\]

for every \(n\ge0\). Hence the alternating enclosure is valid uniformly
over all required intervals.

## Coarse certified targets

Ten alternating terms are far more than necessary to obtain outward
enclosures of the form

\[
0.8903<\Phi(u)<0.8905,
\]

\[
0.9672<\Phi(3u/2)<0.9675,
\]

\[
0.3613<
Q\!\left(
\frac{u}{2\sqrt3}
\right)
<0.3616,
\]

\[
0.0165<Q(\sqrt3u)<0.0169.
\]

These intervals imply the five bounds used in the Schur proof:

\[
\Phi(u)>0.89,
\]

\[
0.967<\Phi(3u/2)<0.968,
\]

\[
Q\!\left(
\frac{u}{2\sqrt3}
\right)<0.362,
\]

\[
Q(\sqrt3u)<0.017.
\]

The displayed decimal endpoints are terminating rationals; no floating-point
semantics is required.

## Proof-producing checker design

A checker needs only exact rational arithmetic:

1. represent the input intervals as fractions;
2. bound square roots by squaring rational endpoints;
3. propagate the four argument intervals monotonically;
4. evaluate even and odd partial sums as fractions;
5. multiply by rational enclosures for \(2/\sqrt\pi\);
6. assert that the resulting intervals lie inside the coarse targets.

The largest factorial is only \(10!\), so integer growth is negligible.

## Remaining theta scalar

This closes the Gaussian-window side of the prime-two certificate. One
separate scalar inequality remains:

\[
M_\Phi
=
\xi\!\left(\frac12\right)
<\frac12.
\]

That inequality should be proved from the source theta or completed-xi
representation. It must not be inferred from the decimal approximation
\(0.497120778\).

## Consequence

Once \(M_\Phi<1/2\) is source-certified, the rational chain is complete:

\[
a_2>0.6,
\qquad
d_2^2<0.1,
\]

and

\[
8(1-M_\Phi)^2a_2>1.2>d_2^2.
\]

Together with the monotone envelope for \(p\ge3\), this proves the
prime-uniform theta-mass Schur-loading inequality.

## Verdict

No numerical quadrature is needed for the remaining Stieltjes bounds.
Alternating error-function series with ten rational terms certify all five
normal-CDF inequalities.

The sole scalar analytic residue is now the source inequality
\(\xi(1/2)<1/2\).
