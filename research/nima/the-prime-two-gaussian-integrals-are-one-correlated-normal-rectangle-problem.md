# The prime-two Gaussian integrals are one correlated-normal rectangle problem

## Probabilistic representation

The density

\[
\rho(x)=e^{-\pi x^2}
\]

is a normalized Gaussian density with variance

\[
\operatorname{Var}(X)=\frac1{2\pi}.
\]

Let \(Q,X_1,X_2\) be independent with this density. Since

\[
-W_L(q)
=
\mathbb P(|X-q|\le L\mid Q=q),
\]

the endpoint Gram diagonal is

\[
a_L
=
\mathbb P(
|X_1-Q|\le L,
|X_2-Q|\le L
).
\]

Likewise the positive annular disagreement magnitude is

\[
|W_{2L}(q)-W_L(q)|
=
\mathbb P(
L<|X-q|\le2L
\mid Q=q
),
\]

so

\[
d_L^2
=
\mathbb P(
L<|X_1-Q|\le2L,
L<|X_2-Q|\le2L
).
\]

Thus both integrals are probabilities for the same bivariate Gaussian.

## Standardized pair

Define

\[
Z_j
=
\sqrt\pi(X_j-Q),
\qquad
j=1,2.
\]

Then

\[
\operatorname{Var}(Z_j)=1,
\]

and

\[
\operatorname{Cov}(Z_1,Z_2)
=
\pi\operatorname{Var}(Q)
=
\frac12.
\]

Therefore \((Z_1,Z_2)\) is a standard bivariate normal pair with correlation

\[
\rho_Z=\frac12.
\]

Writing

\[
u=\sqrt\pi L,
\]

one obtains the exact formulas

\[
a_L
=
\mathbb P(
|Z_1|\le u,
|Z_2|\le u
),
\]

and

\[
d_L^2
=
\mathbb P(
u<|Z_1|\le2u,
u<|Z_2|\le2u
).
\]

For the remaining prime,

\[
u_2=\sqrt\pi\log2.
\]

## One-dimensional conditional integrals

Let \(\varphi\) and \(\Phi_N\) be the standard normal density and
distribution function. Since

\[
Z_2\mid Z_1=x
\sim
N\!\left(
\frac x2,
\frac34
\right),
\]

the endpoint energy is

\[
a_L
=
\int_{-u}^{u}
\varphi(x)
\left[
\Phi_N\!\left(
\frac{u-x/2}{\sqrt3/2}
\right)
-
\Phi_N\!\left(
\frac{-u-x/2}{\sqrt3/2}
\right)
\right]dx.
\]

The disagreement probability is the sum of four analogous rectangle
integrals over

\[
[-2u,-u]\cup[u,2u].
\]

This is simpler to certify than the original nested window integrals: only
the standard normal CDF and one compact integration variable remain.

## Symmetry reduction

The joint density is invariant under simultaneous sign reversal and coordinate
exchange. Hence the annular square decomposes into:

- two equal same-sign rectangles;
- two equal opposite-sign rectangles.

Thus

\[
d_L^2
=
2P_{++}(u)+2P_{+-}(u),
\]

where

\[
P_{++}(u)
=
\mathbb P(
u<Z_1\le2u,
u<Z_2\le2u
)
\]

and

\[
P_{+-}(u)
=
\mathbb P(
u<Z_1\le2u,
-2u\le Z_2<-u
).
\]

Positive correlation makes the opposite-sign term substantially smaller,
explaining why the coarse one-variable tail envelope was wasteful.

## Certification target

At \(u=u_2\), it is enough to prove

\[
a_L>0.6
\]

and

\[
2P_{++}(u)+2P_{+-}(u)<0.1.
\]

These are compact bivariate-normal rectangle inequalities with a large
observed margin.

A rigorous checker can enclose \(\Phi_N\) using rational error-function
bounds and integrate by interval Simpson or Gauss--Legendre quadrature. The
Gaussian density supplies immediate derivative and tail bounds.

## Structural benefit

The same representation applies to every \(L\), not only \(\log2\).
It exposes monotonicity of \(a_L\) directly because the central rectangle
expands with \(u\).

The disagreement annulus is not set-monotone in \(L\), but its exact
probability now belongs to a fixed correlation model. No prime-specific
three-variable integration remains.

## Authority qualification

This probability calculation certifies only the Stieltjes norm inequality. It
remains downstream of:

- the source identification of the odd incidence with \(d_p\);
- the Wronskian rank-one character theorem;
- the completed theta shifted-history normalization.

## Verdict

The last numerical pilot is exactly a correlation-(1/2) Gaussian rectangle
problem. The desired rough inequalities can be certified using standard
one-dimensional normal-CDF integrals, without manipulating moving Stieltjes
windows directly.

This supplies a short proof route for the remaining \(p=2\) mass-bound
certificate.
