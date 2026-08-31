# The Gaussian-pair endpoint transform is an explicit entire erfc section

## Question

Can the forcing term in the Gaussian-pair spectral Ward identity be evaluated
without numerical quadrature?

## Claim boundary

Yes. Each endpoint-product transform has a closed complementary-error-function
formula and is entire in the Evans parameter. Consequently the pairwise Ward
identity and every parameter jet are explicit. This does not prove that the G4
linking port realizes the formula.

## Endpoint product

For an ordered pair \((n,m)\) and endpoint \(x\ge0\), define

\[
 g_{nm}(x,t)
 =e^{-\pi n^2x^2}e^{-\pi m^2(x+t)^2}.
\]

Its analytic-transpose Laplace readout is

\[
 G_{nm,x}(z)
 =\int_0^\infty e^{-zt}g_{nm}(x,t)\,dt.
\]

Expanding the exponent gives

\[
 G_{nm,x}(z)
 =e^{-\pi(n^2+m^2)x^2}
 \int_0^\infty
 e^{-\pi m^2t^2-(z+2\pi m^2x)t}\,dt.
\]

## Exact formula

Gaussian completion yields

\[
 G_{nm,x}(z)
 =\frac{1}{2m}
 \exp\!\left(
 -\pi n^2x^2+zx+\frac{z^2}{4\pi m^2}
 \right)
 \operatorname{erfc}\!\left(
 \sqrt\pi mx+\frac{z}{2\sqrt\pi m}
 \right).
\]

Although displayed as an exponential times \(\operatorname{erfc}\), this is
entire in \(z\), as is immediate from its Gaussian integral representation.

For a shell \([a,b]\),

\[
 F_{nm}^{[a,b]}(z)
 =G_{nm,b}(z)-G_{nm,a}(z).
\]

## Initial value

The source initial value is

\[
 \rho_{nm}^{[a,b]}(0)
 =\int_a^b e^{-\pi(n^2+m^2)x^2}\,dx
\]

and therefore

\[
 \rho_{nm}^{[a,b]}(0)
 =\frac{1}{2\sqrt{n^2+m^2}}
 \left[
 \operatorname{erf}\!\left(
 \sqrt{\pi(n^2+m^2)}b
 \right)
 -
 \operatorname{erf}\!\left(
 \sqrt{\pi(n^2+m^2)}a
 \right)
 \right].
\]

## Fully explicit Ward identity

Let

\[
 \kappa_{nm}=\frac{n^2m^2}{n^2+m^2},
 \qquad
 \alpha_{nm}=\frac{m^2}{n^2+m^2}.
\]

Then the pairwise ordinary shell satisfies

\[
 2\pi\kappa_{nm}\partial_z I_{nm}^{(0),[a,b]}(z)
 -zI_{nm}^{(0),[a,b]}(z)
 =\rho_{nm}^{[a,b]}(0)
 +\alpha_{nm}
 \left[G_{nm,b}(z)-G_{nm,a}(z)\right].
\]

Every term on the right is now a closed source formula.

## Ordered orientation

The endpoint transform is asymmetric in the ordered pair. Swapping \(n,m\)
changes both the Gaussian scale in the complementary-error-function argument
and the forcing coefficient \(\alpha_{nm}\). The symmetric decay coefficient
\(\kappa_{nm}\) does not erase this orientation.

## Exact hostile test

For any proposed linking response \(L_{nm}^{[a,b]}(z)\), form

\[
 \mathcal R_{nm}^{[a,b]}(z)
 =L_{nm}^{[a,b]}(z)
 -\rho_{nm}^{[a,b]}(0)
 -\alpha_{nm}
 \left[G_{nm,b}(z)-G_{nm,a}(z)\right].
\]

If the proposed response claims to implement the Ward forcing, this entire
residual must vanish identically. Evaluation at one generic rational or
algebraic parameter already supplies a counterexample when nonzero; agreement
at Xi zeros alone is not admissible.

## Jet access

Parameter derivatives follow either by differentiating the explicit entire
formula or by differentiating under the Gaussian integral. This provides every
order required by multiplicity tests, including the top derivative appearing
in the Ward recurrence.

## Disposition

The Gaussian-pair spectral forcing is now completely explicit in endpoint and
initial-value data. Candidate one has a closed basis-pair falsifier; the
remaining task is to extract the actual G4 reciprocal/linking shell formula and
compare it with this section. No RH conclusion is authorized.
