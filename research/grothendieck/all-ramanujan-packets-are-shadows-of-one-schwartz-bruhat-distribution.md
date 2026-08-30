# All Ramanujan Packets Are Shadows of One Schwartz--Bruhat Distribution

## The correct target space

Let \(\mathcal S(\mathbb A_f)\) be the finite-adelic
Schwartz--Bruhat space of locally constant compactly supported functions. The
multiplicative unit measure

\[
\nu_\times
=
\bigotimes_p\mu_p^\times
\]

is a finite Radon measure supported on
\(\widehat{\mathbb Z}^\times\subset\mathbb A_f\). Therefore it defines
a continuous distribution

\[
T_\times(\phi)
=
\int_{\widehat{\mathbb Z}^\times}\phi(x)\,d\nu_\times(x).
\]

Although \(T_\times\) has no density in additive
\(L^1(\widehat{\mathbb Z})\), it is an ordinary element of
\(\mathcal S'(\mathbb A_f)\).

## Finite sieve measures converge distributionally

Let

\[
d\nu_y=W_y\,d\mu_+
\]

be the finite prime-cutoff measure. Every test function restricted to
\(\widehat{\mathbb Z}\) factors through some finite quotient
\(\mathbb Z/M\mathbb Z\). Once the cutoff contains every prime dividing
\(M\), Chinese remainder factorization gives

\[
\int\phi\,d\nu_y
=
\int\phi\,d\nu_\times.
\]

Thus convergence is eventually exact on each Schwartz--Bruhat test:

\[
\nu_y\longrightarrow\nu_\times
\]

in the distributional weak topology.

The failure of additive \(L^1\) and \(L^2\) convergence is therefore not
failure of source completion. It is failure only of an incorrectly strong
target category.

## Fourier shadows

The additive character of conductor \(Q\) indexed by \(k/Q\) restricts on
\(\mathbb Z/Q\mathbb Z\) to

\[
\chi_{k/Q}(a)=e^{2\pi iak/Q}.
\]

Its pairing with the multiplicative unit distribution is

\[
\langle T_\times,\chi_{k/Q}\rangle
=
\frac1{\varphi(Q)}
\sum_{\substack{a\bmod Q\\(a,Q)=1}}
e^{2\pi iak/Q}
=
\frac{c_Q(k)}{\varphi(Q)}.
\]

Hence every normalized Ramanujan packet is a finite Fourier projection of the
single completed distribution \(T_\times\). Compatibility across moduli is
not an additional theorem; it follows from functorial restriction of one
measure.

## What happened to the half-density

The measures \(W_y\mu_+\) converge to \(T_\times\), while the square-root
vectors \(h_y=\sqrt{W_y}\) converge weakly to zero in additive \(L^2\).
Squaring and taking the conductor limit do not commute:

\[
h_y\rightharpoonup0,
\qquad
|h_y|^2\mu_+\longrightarrow\nu_\times.
\]

The completed state is therefore measure-valued or correspondence-valued,
not vector-valued in the additive representation. The separately
renormalized overlap belongs to its determinant line.

## Consequence for the RH programme

The finite residue/character side is now complete:

1. \(T_\times\) retains the multiplicative Haar state;
2. its Fourier transform retains every Ramanujan mode;
3. the square-current line retains the relative overlap anomaly.

No additional finite-conductor observer is missing. The unresolved theorem
is entirely in the coupling to the archimedean logarithmic boundary:

> The completed adelic correspondence must send the formal connected current
> into the half-normalized tempered distribution on the real logarithmic ray.

This coupling cannot be reduced to additive \(L^2\) convergence, but it can
be asked as continuity of a map between Schwartz--Bruhat test spaces and
their duals.

This statement concerns the angular unit-residue carrier. The radial
valuation tower producing prime powers is not contained in
\(T_\times\); it is the separate formal connected current constructed
earlier. The complete finite-adelic source retains both the radial Fock tower
and the angular Schwartz--Bruhat distribution before taking their
archimedean readout.

## Falsifier

A proposed finite completion fails if it:

- does not reproduce \(c_Q(k)/\varphi(Q)\) for every conductor;
- depends on a chosen cofinal sequence of moduli;
- requires an additive-Haar density for \(\nu_\times\);
- or treats the weak-zero half-density vector as the completed measure.
