# Elementary enclosure of the gamma tail

## Question

Can the received gamma-tail formula be reduced to an elementary monotone bound suitable for allocating the rank-two interval budget?

## Claim boundary

The erfc reduction and monotonicity are exact. The received integral-tail formula has not been independently derived from the source integrand, and the numerical design point is high-precision rather than directed-rounding interval output.

## Received bound

For truncation point \(R\), the reported gamma tail is

\[
B(t,R)
=
\frac{
 e^{-R}
 +2\sqrt{\pi t}\,e^{t/4}
 \operatorname{erfc}
 \left(\frac{R+2t}{4\sqrt t}\right)
}{1-e^{-R}}.
\]

Use the standard inequality

\[
\operatorname{erfc}(u)
\leq
\frac{e^{-u^2}}{\sqrt\pi\,u},
\qquad u>0.
\]

With

\[
u=rac{R+2t}{4\sqrt t},
\]

this gives

\[
B(t,R)
\leq
\frac{
 e^{-R}
 +\dfrac{8t}{R+2t}
  \exp\left(\frac t4-\frac{(R+2t)^2}{16t}\right)
}{1-e^{-R}}.
\]

## Exponent cancellation

The second exponent simplifies exactly:

\[
\frac t4-rac{(R+2t)^2}{16t}
=
-\frac R4-rac{R^2}{16t}.
\]

Thus the elementary bound is

\[
B(t,R)
\leq
\frac{
 e^{-R}
 +\dfrac{8t}{R+2t}
 e^{-R/4-R^2/(16t)}
}{1-e^{-R}}.
\]

The Gaussian correction is much smaller than \(e^{-R}\) in the current small-\(t\) region.

## Uniformity in the sampled argument

For fixed \(R>0\), let

\[
g_R(t)
=
\frac{8t}{R+2t}
 e^{-R/4-R^2/(16t)}.
\]

Its logarithmic derivative is

\[
\frac{d}{dt}\log g_R(t)
=
\frac1t-rac2{R+2t}+rac{R^2}{16t^2}.
\]

The first two terms combine to

\[
\frac{R}{t(R+2t)}>0,
\]

so \(g_R(t)\) is strictly increasing. A uniform bound on \(0<t\leq t_{\max}\) is obtained by evaluating only at \(t_{\max}\).

## Design point

At

\[
R=40,
\qquad
t_{\max}=0.08,
\]

high-precision evaluation of the elementary upper expression gives approximately

\[
4.248354255291589\times10^{-18}.
\]

This value is not yet a certified interval because the exponential evaluations were not directed-rounded. It nevertheless fixes the scale: a directed enclosure below \(4.249\times10^{-18}\) should be straightforward.

For a difference sample, two tails contribute, so the corresponding moment-tail budget remains below roughly \(8.5\times10^{-18}\). This is negligible relative to the observed \(7.553\times10^{-8}\) determinant margin after ordinary sensitivity factors.

## Remaining computation

The main certification cost is now the finite gamma integral on

\[
[0,40].
\]

A valid implementation must provide:

- the exact source integrand and normalization;
- outward-rounded range enclosures on every quadrature cell;
- a proved quadrature remainder;
- directed rounding for the elementary tail;
- four sample intervals propagated through the determinant error budget.

The tail no longer motivates an asymptotic-series implementation unless finite-interval quadrature proves unstable.

## Disposition

The gamma tail is not the current numerical obstruction. The first missing typed object is a certified finite-interval quadrature of the exact gamma integrand. Once produced, the existing error budget decides the rank-two sign.

## Verification

- `research/voevodsky/gamma-tail-elementary-enclosure-v1.json`
- `research/voevodsky/checkers/check_gamma_tail_elementary_enclosure.py`
- `research/voevodsky/results/gamma_tail_elementary_enclosure.json`
