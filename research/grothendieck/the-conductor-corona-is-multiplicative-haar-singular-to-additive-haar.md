# The Conductor Corona Is Multiplicative Haar Singular to Additive Haar

## Prime-filtration martingale

Let \(\mu_+\) be normalized additive Haar measure on
\(\widehat{\mathbb Z}=\prod_p\mathbb Z_p\). For each prime define

\[
Y_p(x)
=
\frac{\mathbf 1_{x_p\in\mathbb Z_p^\times}}{1-p^{-1}}.
\]

The prime coordinates are independent under \(\mu_+\), and

\[
\mathbb E_{\mu_+}Y_p=1.
\]

For the primorial cutoff \(Q_y=\prod_{p\le y}p\), set

\[
W_y=\prod_{p\le y}Y_p.
\]

Then

\[
W_y
=
\frac{Q_y}{\varphi(Q_y)}
\mathbf 1_{(x,Q_y)=1},
\]

the mean-one Ramanujan survivor state from the preceding results. Relative to
the increasing prime-coordinate filtration, \((W_y)\) is a positive
mean-one martingale.

## Almost-sure collapse

Let

\[
A_y=\{x:x_p\in\mathbb Z_p^\times,\ \forall p\le y\}.
\]

These events decrease and

\[
\mu_+(A_y)
=
\prod_{p\le y}(1-p^{-1})
\longrightarrow0.
\]

Their intersection is \(\widehat{\mathbb Z}^\times\), which therefore has
additive Haar measure zero. For \(\mu_+\)-almost every \(x\), some prime
coordinate is divisible by that prime, and from that cutoff onward
\(W_y(x)=0\). Hence

\[
W_y\longrightarrow0
\]

almost surely.

But \(\mathbb E W_y=1\) for every cutoff. The martingale is not uniformly
integrable. Its missing mean is exactly the conductor-corona mass detected by
the weak-escape theorem.

## The limiting measure

Define

\[
d\nu_y=W_y\,d\mu_+.
\]

For every finite collection of prime coordinates, \(\nu_y\) eventually
gives each coordinate the normalized additive Haar measure conditioned on
\(\mathbb Z_p^\times\). These finite marginals are compatible. Their
projective limit is

\[
\nu_\times
=
\bigotimes_p\mu_p^\times,
\]

where \(\mu_p^\times\) is normalized Haar measure on
\(\mathbb Z_p^\times\).

Thus \(\nu_\times\) is multiplicative Haar measure on the compact finite
idele-unit group

\[
\widehat{\mathbb Z}^\times
=
\prod_p\mathbb Z_p^\times.
\]

It is supported on a set of \(\mu_+\)-measure zero. Therefore

\[
\nu_\times\perp\mu_+.
\]

The conductor corona is not an unknown extra state. It is the multiplicative
Haar boundary, singular with respect to the additive Haar carrier.

## Local density and global failure

At every finite set of places the change of measure is ordinary:

\[
\frac{d\mu_p^\times}{d\mu_p^+}
=
\frac{\mathbf 1_{\mathbb Z_p^\times}}{1-p^{-1}}.
\]

The finite product is exactly \(W_y\). Globally, the Radon--Nikodym density
collapses almost surely and its second moment diverges. Hence the additive and
multiplicative presentations are locally absolutely continuous but globally
singular.

This is a precise measure-theoretic realization of the programme's recurring
rule:

> Every finite comparison is invertible, while completion changes the
> admissible measure class.

## Relation to the half-density seam

The finite-place singularity is paired with the archimedean change from
additive measure \(dx\) to multiplicative measure \(d^\times x=dx/|x|\).
The half-density twist is the symmetric normalization of this modular change.
Its spectral unitary axis is the critical seam.

The complete RH carrier should therefore be a correspondence between:

1. additive adelic Haar, carrying theta and Poisson sewing;
2. multiplicative idelic Haar, carrying the connected Euler current;
3. the modular half-density line comparing their measure classes.

No bounded density map exists globally between the first two.

## Consequence

The missing connected-realization theorem must be formulated before additive
Hilbert completion, as a boundary-bearing correspondence or relative
measure-class construction. Attempting to represent multiplicative Haar as an
ordinary vector in additive \(L^2\) necessarily produces the martingale
collapse, square-norm divergence, and conductor escape already observed.

This identifies the carrier but does not prove RH. The remaining theorem is
that the complete additive--multiplicative correspondence, including its
archimedean half-density, sends the connected prime discrepancy to a tempered
relative boundary state.

## Falsifier

A proposed construction fails if it:

- claims \(W_y\) is uniformly integrable;
- gives \(\nu_\times\) an \(L^1(\mu_+)\) density;
- discards the mean lost in the almost-sure limit;
- treats finite local absolute continuity as global equivalence;
- or completes in additive \(L^2\) before retaining the multiplicative
  measure-class boundary.
