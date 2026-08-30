# The observer seam defect has a continuum logarithmic-scale profile

## Normalized scale measure

For

\[
\sigma=\frac12+\varepsilon,
\]

the observer dual-energy mass is asymptotically modeled by

\[
d\mu_\varepsilon(u)
=
\frac{e^{-2\varepsilon u}}{u\,Z_\varepsilon}\,du,
\qquad
u=\log n,
\qquad
Z_\varepsilon\sim\log\frac1\varepsilon.
\]

This is the continuous scale model of the normalized coefficient weights

\[
\frac{n^{-1-2\varepsilon}}{\log n}.
\]

Introduce the logarithmic scale exponent

\[
y
=
\frac{\log u}{\log(1/\varepsilon)}.
\]

For \(0<y<1\),

\[
u=\varepsilon^{-y},
\qquad
\frac{du}{u}
=
\log\frac1\varepsilon\,dy,
\]

and

\[
e^{-2\varepsilon u}
=
e^{-2\varepsilon^{1-y}}
\longrightarrow1.
\]

Therefore the normalized defect measure converges, in the integral model, to Lebesgue measure on the full interval

\[
0\le y\le1.
\]

## Meaning

The seam defect is not concentrated at one terminal scale. Its energy is asymptotically spread uniformly over logarithmic scale exponents from fixed scales to the cutoff scale \(u\sim\varepsilon^{-1}\).

This sharpens the earlier escape statement:

\[
\text{observer seam defect}
\neq
\text{one rank-one wall residue}.
\]

The natural compactification is a scale corona with a continuum coordinate \(y\), not automatically a single constant or delta wall direction.

## Boundary-port implication

A finite-dimensional external controller can still observe this continuum if its incidence integrates the scale profile faithfully. But that requires an explicit source map

\[
\mathcal C_{\mathrm{scale}}
\longrightarrow
B_{\mathrm{ext}},
\]

where \(\mathcal C_{\mathrm{scale}}\) carries the limiting defect measure and

\[
B_{\mathrm{ext}}
=
\langle1,\delta_0,K,V\rangle.
\]

Dimension counting alone does not forbid such an integral observer, but joint faithfulness is nontrivial. A single scalar port may retain total mass while losing profile-dependent cancellation.

## Test-function formulation

For a bounded continuous test function \(\varphi\) on \([0,1]\), the desired asymptotic is

\[
\frac{
\sum_{n\ge2}
\frac{n^{-1-2\varepsilon}}{\log n}
\,
\varphi\!\left(
\frac{\log\log n}{\log(1/\varepsilon)}
\right)
}{
\sum_{n\ge2}
\frac{n^{-1-2\varepsilon}}{\log n}
}
\longrightarrow
\int_0^1\varphi(y)\,dy.
\]

A rigorous discrete theorem needs sum-integral control uniform over the declared test class.

## New hostile

Two normalized seam sequences have the same total logarithmic divergence and identical constant-wall scalar, but different distributions in \(y\). If the completed Green flux distinguishes them while the external controller does not, the controller is not faithful on the seam defect space.

## Revised completion theorem

The observer completion should provide:

1. a compactified logarithmic-scale defect space;
2. weak convergence of normalized Riesz mass into that space;
3. a source-derived incidence into the external five-cell controller;
4. a lower frame bound on the subset relevant to zero states;
5. compatibility with reciprocal/Fourier sewing.

Only after this theorem may the logarithmic observer boundary value be treated as fully captured by the finite external ports.
