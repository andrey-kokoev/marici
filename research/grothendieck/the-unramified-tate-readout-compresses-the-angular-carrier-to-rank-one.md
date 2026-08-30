# The Unramified Tate Readout Compresses the Angular Carrier to Rank One

## Local radial--angular decomposition

Every nonzero \(p\)-adic number has a unique decomposition

\[
x=p^ku,
\qquad
k\in\mathbb Z,
\quad
u\in\mathbb Z_p^\times.
\]

Normalize multiplicative Haar measure so that
\(\mathbb Z_p^\times\) has mass one. For the unramified source vector
\(\phi_p=\mathbf 1_{\mathbb Z_p}\) and a multiplicative character
\(\chi\), the local Tate integral is

\[
Z_p(\phi_p,\chi,s)
=
\sum_{k\ge0}
\chi(p)^k p^{-ks}
\int_{\mathbb Z_p^\times}\chi(u)\,d^\times u.
\]

If \(\chi\) is nontrivial on \(\mathbb Z_p^\times\), character
orthogonality gives

\[
\int_{\mathbb Z_p^\times}\chi(u)\,d^\times u=0.
\]

For the trivial angular character, the integral is one and

\[
Z_p(\mathbf 1_{\mathbb Z_p},1,s)
=
\sum_{k\ge0}p^{-ks}
=
\frac1{1-p^{-s}}.
\]

Thus the ordinary Riemann local factor retains the full radial valuation tower
but compresses the multiplicative angular carrier to its one-dimensional
trivial-character quotient.

## Relation to Ramanujan packets

The Ramanujan coefficients

\[
\frac{c_Q(k)}{\varphi(Q)}
\]

are additive Fourier shadows of multiplicative unit Haar. They are essential
for proving that additive Poisson transport and residue incidence are
faithfully represented.

They are not multiplicative angular characters in the local Tate integral.
The scalar Riemann readout does not query those additive modes; it pairs the
unit group only with the constant multiplicative character. Consequently all
angular information is compressed to total mass one before the Euler factor
is formed.

## Exact rank statement

Let \(L_p\) be the local scalar Tate observer on angular functions:

\[
L_p(f)
=
\int_{\mathbb Z_p^\times}f(u)\,d^\times u.
\]

Its image is one-dimensional, and its kernel contains every nontrivial
multiplicative character. The completed scalar zeta section factors through

The completed scalar zeta section factors through the angular carrier, then
\(\mathbb C\), then the radial Euler tower.
The first arrow is rank one.

## Consequence

Recovering the angular Schwartz--Bruhat distribution repairs provenance and
completion faithfulness, but it does not by itself change the scalar divisor.
After rank-one angular compression, the same radial Euler factor remains.

Therefore the Ramanujan carrier cannot orient Riemann zeros unless the source
provides an additional operation coupling an additive angular Fourier mode to
the radial Mellin flow before the rank-one quotient.

Such an operation would have to be independently derived from Poisson--Tate
sewing. Adding arbitrary angular probes after observing the scalar zero would
only enlarge the readout and would not transport scalar nullity into those
ports.

## Revised architecture

The finite adelic source has:

1. a radial valuation/Fock tower;
2. an angular Schwartz--Bruhat distribution;
3. additive Fourier coherence between angular shadows;
4. a rank-one unramified Tate observer.

The RH-bearing object, if it exists, must be a pre-observer cross-term between
the radial and angular components. The standard scalar local zeta integral
contains no such nontrivial angular channel.

## Fourier closure strengthens the no-go

Let a unit \(a\in\mathbb Z_p^\times\) act by

\[
(\rho(a)f)(x)=f(a^{-1}x).
\]

With self-dual additive Haar normalization, local Fourier transform satisfies

\[
\mathcal F_p\rho(a)=\rho(a^{-1})\mathcal F_p.
\]

Hence the unit-invariant subspace is preserved by local Fourier transform.
The unramified vector \(\mathbf 1_{\mathbb Z_p}\) lies in that subspace and,
for the standard self-dual character, is Fourier fixed:

\[
\mathcal F_p\mathbf 1_{\mathbb Z_p}
=
\mathbf 1_{\mathbb Z_p}.
\]

Therefore the whole unramified local Fourier--Tate pipeline remains spherical.
It cannot generate a nontrivial finite-place angular mode and later feed that
mode back into the radial Mellin tower. This closes the proposed local
angular--radial cross-operation for the ordinary Riemann source.

To obtain such a cross-operation one must either change the local source to a
ramified representation, retain a genuinely global incidence operation not
factored place by place, or use an archimedean--finite comparison before the
unramified scalar quotient. The first option changes the \(L\)-function; the
other two require new source constructors.

## Falsifier

A proposed angular mechanism fails if it:

- inserts a nontrivial unit character into the Riemann section without
  changing the source to a twisted \(L\)-function;
- treats additive Ramanujan modes as multiplicative Tate characters;
- acts only after the rank-one angular average;
- claims local Fourier transport creates a nonspherical mode from the
  unramified vector;
- or assumes that faithful angular provenance makes the scalar compression
  faithful.
