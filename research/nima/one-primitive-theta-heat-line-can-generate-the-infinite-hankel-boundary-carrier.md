# One primitive theta heat line can generate the infinite Hankel boundary carrier

The continuum rank of the Euler singular kernel does not contradict the
source theorem that scale-derivative closure has exactly one primitive heat
channel.

These are different ranks:

- source-generator rank: one independent primitive line \(H_1\);
- orbit rank: the closed span of all its Mellin/scale translates.

A single cyclic vector for a continuous semigroup can generate an
infinite-dimensional Hilbert space. Here the Euler singular features are

\[
a\longmapsto e^{-au},
\]

whose closed span in \(L^2(\mathbb R_+,du)\) is infinite-dimensional even
though they are the orbit of one Laplace vacuum under multiplication by
\(e^{-au}\).

The theta source has the analogous form. The raw heat line is

\[
H_1(t)=\sum_{n\ge1}n^2e^{-\pi t n^2},
\]

and the completed seam tower is generated from \(H_1\) together with
\(M_0,M_1,\ldots\) under the scale derivative. The source theorem says no
second independent raw heat generator appears. It does not say that the
scale orbit of \(H_1\) has finite dimension.

Thus the matching problem can now be typed correctly. Let
\(\mathcal H_{\mathrm{heat}}\) be the cyclic closure of the source heat line
under the admitted scale semigroup. Seek an interface

\[
U:
L^2(\mathbb R_+,du)
\longrightarrow
\mathcal H_{\mathrm{heat}}
\]

such that the Euler Laplace features \(e^{-au}\) map to the corresponding
theta heat histories and

\[
\langle Ue^{-au},Ue^{-bu}\rangle
=
\frac{4}{\zeta(3/2)^2}\frac1{a+b}
+
G_{\mathrm{regular}}(a,b).
\]

The singular coefficient fixes the asymptotic spectral density of the cyclic
heat representation. In spectral language, if the heat-line orbit has measure
\(d\nu(u)\), the interface requires

\[
d\nu(u)
\sim
\frac{4}{\zeta(3/2)^2}\,du
\]

in the boundary regime responsible for \(a,b\downarrow0\). The precise end
of the spectral variable must be derived from the frozen scale convention.

This gives a source-native next theorem:

> Compute the spectral measure of the cyclic theta heat line under logarithmic
> scale transport and compare its boundary density with the Cauchy
> max-kernel residue.

If the densities match, one primitive source channel is sufficient to carry
the whole infinite-rank Euler pole. If they differ by a bounded positive
weight, a bi-bounded comparison may still exist. If the density vanishes,
blows up at a different rate, or has the wrong multiplicity, theta heat cannot
supply the required Schur channel.

The finite five-cell remains necessary for endpoint incidence and
orientation, but it should not be charged with continuum rank. Its role is to
attach the cyclic heat carrier to the completed boundary form.

The minimal hostile has exactly one primitive heat generator and the correct
diagonal pole, but spectral multiplicity two. Another has multiplicity one
with density \(u^\alpha du\), producing \((a+b)^{-1-\alpha}\) rather than the
required Cauchy kernel.
