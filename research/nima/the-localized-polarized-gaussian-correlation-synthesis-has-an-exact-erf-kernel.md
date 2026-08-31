# The localized polarized Gaussian correlation synthesis has an exact erf kernel

## Question

Can the missing first map on the ordered-pair arithmetic carrier be computed
for the actual labelled theta atoms?

## Claim boundary

Yes. For the Gaussian source atoms, every ordered-pair shell correlation has an
explicit error-function formula. This constructs the localized polarized
synthesis \(\widetilde B_{a,b}\) exactly and retains pair orientation. It does
not construct the final response current that must cancel the shell residual.

## Labelled atoms

Use the source-derived Gaussian family

\[
 \phi_n(x)=e^{-\pi n^2x^2},
 \qquad n\ge1.
\]

For an ordered pair \((n,m)\), define

\[
 \rho_{nm}^{[a,b]}(t)
 =\int_a^b\phi_n(x)\phi_m(x+t)\,dx,
 \qquad t\ge0.
\]

The localized polarized synthesis is

\[
 \widetilde B_{a,b}
 (e_n\otimes\overline{e_m})
 =\rho_{nm}^{[a,b]}.
\]

The atoms are real, but the ordered tensor notation is retained because
\((n,m)\) and \((m,n)\) carry opposite ratio orientation.

## Completing the square

Set

\[
 A_{nm}=n^2+m^2,
 \qquad
 c_{nm}(t)=\frac{m^2}{A_{nm}}t.
\]

Then

\[
 n^2x^2+m^2(x+t)^2
 =A_{nm}\left(x+c_{nm}(t)\right)^2
 +\frac{n^2m^2}{A_{nm}}t^2.
\]

Therefore

\[
 \rho_{nm}^{[a,b]}(t)
 =e^{-\pi\frac{n^2m^2}{A_{nm}}t^2}
 \int_a^b
 e^{-\pi A_{nm}(x+c_{nm}(t))^2}\,dx.
\]

## Exact kernel

Using the error function,

\[
 \rho_{nm}^{[a,b]}(t)
 =
 \frac{
 e^{-\pi\frac{n^2m^2}{A_{nm}}t^2}
 }{2\sqrt{A_{nm}}}
 \left[
 \operatorname{erf}\!\left(
 \sqrt{\pi A_{nm}}\left(b+c_{nm}(t)\right)
 \right)
 -
 \operatorname{erf}\!\left(
 \sqrt{\pi A_{nm}}\left(a+c_{nm}(t)\right)
 \right)
 \right].
\]

This formula is positive for \(a<b\) and \(t\ge0\).

## Ordered-pair orientation

Swapping \(n\) and \(m\) preserves

\[
 A_{nm}
 \quad\text{and}\quad
 \frac{n^2m^2}{A_{nm}},
\]

but changes the translation from

\[
 c_{nm}(t)=\frac{m^2}{A_{nm}}t
\]

to

\[
 c_{mn}(t)=\frac{n^2}{A_{nm}}t.
\]

Hence

\[
 \rho_{nm}^{[a,b]}(t) \neq \rho_{mn}^{[a,b]}(t)
\]

in general on a finite shell. Scalar symmetrization would erase precisely the
ratio orientation required by the polarized current.

## Full half-line limit

For \(a=0\) and \(b\to\infty\),

\[
 \rho_{nm}^{[0,\infty)}(t)
 =
 \frac{
 e^{-\pi\frac{n^2m^2}{A_{nm}}t^2}
 }{2\sqrt{A_{nm}}}
 \operatorname{erfc}\!\left(
 \sqrt\pi\frac{m^2}{\sqrt{A_{nm}}}t
 \right).
\]

The swapped ordered pair has the same Gaussian prefactor and the complementary
argument with \(m^2\) replaced by \(n^2\).

## Prime-shell specialization

For consecutive primes \(p<q\), set

\[
 a=\log p,
 \qquad
 b=\log q.
\]

Then every pair contribution to the ordinary shell density is explicit. If the
completed theta forcing has labelled coefficients \(c_n\),

\[
 \rho_{a,b}(t)
 =\sum_{n,m}c_n\overline{c_m}
 \rho_{nm}^{[a,b]}(t),
\]

with convergence controlled by Gaussian decay on the declared source core.

## Product and ratio variables

The symmetric factor

\[
 \frac{n^2m^2}{n^2+m^2}
\]

controls common decay. The asymmetric translation

\[
 \frac{m^2}{n^2+m^2}t
\]

retains ordered ratio information. Thus the exact kernel separates the product
shadow from the ratio-oriented boundary data without fitting a phase.

## Next source test

A proposed nonlocal response or linking current can now be tested on basis
pairs by applying it to the explicit kernel above. Candidate one requires that,
after endpoint-flux removal, its density equal the negative rank-one theta sum
for every consecutive-prime shell.

The two-label hostile can be evaluated with the same formula before any Xi
zero is used.

## Disposition

The first missing arrow

\[
 e_n\otimes\overline{e_m}
 \longmapsto\rho_{nm}^{[a,b]}
\]

is now explicit. The remaining missing arrow is the source-derived response
current from these kernels to the reciprocal/linking shell contribution. No RH
conclusion is authorized.
