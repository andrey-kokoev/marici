# Relative Translation Is Conserved and the Comb Defect Is the Primitive Current

## Opposite norm characters

Let

\[
(T_uf)(q)=f(q+u)
\]

on the two sector spaces

\[
\mathcal H_{\pm,\varepsilon}
=
H^1\left(
\mathbb R,
e^{\pm(1+\varepsilon)q}\,dq
\right).
\]

A change of variables gives

\[
\lVert T_uf\rVert_{+,\varepsilon}
=
e^{-(1+\varepsilon)u/2}
\lVert f\rVert_{+,\varepsilon},
\]

and

\[
\lVert T_ug\rVert_{-,\varepsilon}
=
e^{(1+\varepsilon)u/2}
\lVert g\rVert_{-,\varepsilon}.
\]

The two norms acquire opposite dilation characters.

## Conserved relative interface

For the relative pairing

\[
\langle f,g\rangle_{\mathrm{rel}}
=
\int_{\mathbb R}f(q)\overline{g(q)}\,dq,
\]

common translation is exactly conserved:

\[
\langle T_uf,T_ug\rangle_{\mathrm{rel}}
=
\langle f,g\rangle_{\mathrm{rel}}.
\]

Thus the two sector weights are presentation coordinates around one conserved
relative interaction.

## Arithmetic covariance defect

The direct comb trace is

\[
B_+f
=
\sum_{n\geq1}n^{-1/2}f(\log n).
\]

For a positive integer \(m\),

\[
B_+T_{\log m}f
=
\sum_{n\geq1}
n^{-1/2}f(\log(mn)).
\]

Writing \(k=mn\) gives

\[
m^{-1/2}B_+T_{\log m}f
=
\sum_{m\mid k}
k^{-1/2}f(\log k).
\]

Therefore

\[
B_+f
-
m^{-1/2}B_+T_{\log m}f
=
\sum_{m\nmid k}
k^{-1/2}f(\log k).
\]

The failure of the integer comb to transform as one continuous dilation
character is exactly the current carried by labels not divisible by \(m\).

For a prime \(p\), this is the primitive \(p\)-free channel.

## Reciprocal sector

The reciprocal trace satisfies the reflected identity

\[
B_-g
-
m^{-1/2}B_-T_{-\log m}g
=
\sum_{m\nmid k}
k^{-1/2}g(-\log k).
\]

Hence the primitive defect occurs on both sector charts with opposite scale
orientation.

## Structural consequence

The relative carrier transport is exactly conserved. Arithmetic enters only
through the comb's covariance defect:

- continuous translation belongs to the carrier;
- divisibility incidence belongs to the observation boundary;
- the primitive current is their commutator residual.

This derives the prime-scale repair current inside the completed two-sector
rigging rather than adding it afterward.

## Next gate

Iterating the identity along powers of \(p\) produces the valuation filtration.
The next exact audit is whether the \(p\)-adic defect tower and its reciprocal
reflection assemble into a trace-class relative boundary operator after the
primitive and square channels are retained explicitly.

## Falsifier

The theorem fails if common translation does not conserve the relative pairing
or if the comb residual contains any label divisible by \(m\). Both claims
follow by change of variables and reindexing.
