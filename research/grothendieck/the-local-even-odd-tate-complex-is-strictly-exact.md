# The Local Even--Odd Tate Complex Is Strictly Exact

## The two-term complex

Let \(\mathcal S_{\mathrm{ev}}(\mathbb R)\) and
\(\mathcal S_{\mathrm{odd}}(\mathbb R)\) be the even and odd Schwartz
subspaces. Differentiation defines

\[
d:\mathcal S_{\mathrm{ev}}(\mathbb R)
\longrightarrow
\mathcal S_{\mathrm{odd}}(\mathbb R)\,dx.
\]

It is injective: a constant Schwartz function is zero.

For an odd Schwartz function (g\), define

\[
(hg)(x)=\int_{-\infty}^{x}g(u)\,du.
\]

Oddness implies \(\int_{\mathbb R}g=0\), so (hg\) decays at both ends. It is
an even Schwartz function and

\[
d(hg)=g\,dx.
\]

Conversely, for even Schwartz (f\),

\[
h(f')=f.
\]

Thus

\[
d:\mathcal S_{\mathrm{ev}}
\xrightarrow{\sim}
\mathcal S_{\mathrm{odd}}dx
\]

is a continuous topological isomorphism with source-fixed inverse (h\).

## Interpretation

The even scalar vacuum and odd differential companion are not two freely
chosen channels. They are the two grades of a strictly exact local complex.
The endpoint integral is the contracting partner.

This supplies the incidence missing from the local parity-double picture: the
even source state maps under (d\) to its odd coefficient tensored with the
orientation line.

No nonzero local cohomology class can appear in this archimedean Schwartz
complex.

## Fourier covariance

Additive Fourier transform intertwines the differential with multiplication:

\[
\mathcal F_x(df)(\xi)
=2\pi i\xi\,\widehat f(\xi).
\]

The odd Fourier quarter-phase is therefore carried by the degree-one
companion generated from the even source. It is no longer an imported parity
channel, and its incidence is fixed before scalar projection.

## Global implication

Because the local complex is strictly exact, an unpaired state cannot be
created at the archimedean place alone. It can arise only when one of the
following fails:

1. restricted-product completion preserves the contraction;
2. primitive or square boundary currents lie in the completed domain;
3. finite and archimedean incidences commute with reciprocal sewing;
4. endpoint evaluation remains continuous in the completed topology.

This recovers the earlier completion-at-infinity frontier, now from a concrete
source-derived differential rather than a hypothetical Koszul complex.

## Scope boundary

The theorem is local. It does not identify zeros of \(\Xi\) with cohomology of
the completed adelic complex. The next hard gate is to construct the global
restricted-product differential and show that its determinant or boundary
section is the completed zeta readout without defining it backward from that
readout.
