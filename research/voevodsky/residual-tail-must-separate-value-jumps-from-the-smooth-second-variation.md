# Residual tails must separate value jumps from smooth second variation

Applying the first-variation Gram to the entire residual is far too crude. At
`L=.6495` it produces a tail-Gram norm `6.38` and destroys positivity, despite
the directly computed mode blocks showing a critical correction around
`10^-14`.

The reason is structural. The `1/n` Legendre coefficient term comes only from
interior **value jumps**. After those finitely many jump atoms are extracted
explicitly, the remaining residual is continuous and piecewise smooth.
Integrating the Legendre identity a second time gives

\[
\|r_n^{\rm smooth}\|\le \frac{C_L}{n^2}
 \mathcal V^{(2)}(g),
\]

where the second variation contains the weighted absolutely continuous second
derivative and the finitely many first-derivative jumps. Consequently

\[
\sum_{n=N}^\infty
 (r_n^{\rm smooth})^*r_n^{\rm smooth}
\preceq
\frac{C_L^2}{3(N-1)^3}G^{(2)}.
\]

The complete tail must therefore be bounded as

\[
R_{\ge N}^*R_{\ge N}
\preceq
2G_{\rm jump}(N)+2G_{\rm smooth}^{(2)}(N),
\]

or, more sharply, by retaining their cross Gram. The directed jump calculation
already preserves positivity. Charging the smooth derivative density to the
same first-variation Cauchy bound incorrectly promotes a rapidly decaying
component to a `1/n` tail and loses several powers of `N`.

Next implementation: subtract the four explicit prime-translation value jumps,
assemble the matrix-valued second-variation Gram of the continuous remainder,
and apply the `N^-3` tail factor at `N=4000`.
