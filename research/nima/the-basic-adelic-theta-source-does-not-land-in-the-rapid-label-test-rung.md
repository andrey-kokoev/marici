# The basic adelic theta source does not land in the rapid-label test rung

## Test of the proposed realization

The proposed map

\[
\iota:\mathcal S(\mathbb A)
\longrightarrow
\mathcal S_{\mathrm{lab}}
\widehat\otimes_\pi\mathscr G
\]

is too strong for the canonical unramified source.

Take the basic finite component

\[
\phi_f=\mathbf 1_{\widehat{\mathbb Z}}.
\]

Its rational sampling produces the ordinary positive-integer theta labels.
In the normalized logarithmic-translation chart, those labels have a common
radial atom up to the declared Euler half-density factors. The label
coefficients are therefore constant or of fixed finite exponential order;
they are not rapidly decreasing in every positive label weight.

For example, the primitive half-density scale has magnitude `n^{-1/2}`. Its
rapid-label seminorm would contain

\[
\sum_{n\ge1}n^{2a}n^{-1}
\]

and diverges for every `a>0`. The constant occupancy row fails even more
strongly. Restriction to primes does not repair the divergence.

Hence the basic adelic theta source cannot map into

\[
\mathcal S_{\mathrm{lab}}
=
\bigcap_{a>0}\ell^2(n^{2a})
\]

under the normalized translated-atom realization used by the ordered graph.

## Correct rigged type

The rapid-label space remains the valid test rung on which primitive, square,
and Mellin rows act continuously. The adelic theta synthesis belongs instead
to an intermediate graph/distributional domain

\[
\mathcal S_{\mathrm{lab}}
\subset D_{\theta}
\subset
\mathcal S_{\mathrm{lab}}'.
\]

The source-retaining realization must therefore have type

\[
\iota_{\theta}:
\mathcal S(\mathbb A)
\longrightarrow
D_{\theta}
\widehat\otimes\mathfrak B_S,
\]

or be represented directly as a continuous kernel from label tests into the
ordered radial graph. It cannot be a state-valued map into the top test rung.

## Consequence for bilinear currents

Dual membership alone is not enough to define the ordered Green pairing of
two theta distributions. A common graph domain must additionally specify how
one factor is regularized or smoothed so that

\[
\langle F,S H\rangle
\]

is a closed dual pairing rather than a product of distributions. Finite Euler
cutoffs define such pairings temporarily, but cutoff independence on test
vectors does not prove convergence on the theta source.

This is precisely why the source-retaining span must keep the adelic source
coordinate and why the completed Green current cannot be obtained by a Riesz
identification.

## Revised obstruction

The missing adelic theorem is not a map into the rapid test carrier. It is the
construction of `D_theta` together with:

1. continuous adelic theta synthesis into that domain;
2. Fourier and reciprocal invariance;
3. closed extension of the ordered Green pairing;
4. continuity of primitive, square, endpoint, and archimedean traces;
5. cutoff-independent convergence of the polarized current.

The rapid carrier proves continuity of the observers. It does not assert that
the observed theta source is itself a rapid test vector.
