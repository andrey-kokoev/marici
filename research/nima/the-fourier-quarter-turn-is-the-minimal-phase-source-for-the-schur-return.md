# The Fourier quarter-turn is the minimal phase source for the Schur return

## Status

The direct endpoint Gram construction is rejected. The real windows \(W_L,W_{2L}\) generate only a real endpoint block \(A_p\). Any reciprocal odd coordinate must be induced by eliminating an independently typed oriented feature.

## Minimal reduced model

After radical reduction, suppose the tail–principal-value feature is one-dimensional with

\[
D_p=d_p>0,
\qquad
C_p=
\begin{pmatrix}
\alpha_p\\
i\beta_p
\end{pmatrix},
\qquad
\alpha_p,\beta_p\in\mathbb R.
\]

Then

\[
C_pD_p^{-1}C_p^*
=
\frac1{d_p}
\begin{pmatrix}
\alpha_p^2&-i\alpha_p\beta_p\\
i\alpha_p\beta_p&\beta_p^2
\end{pmatrix}.
\]

For

\[
G_p^{\mathrm{eff}}=A_p-C_pD_p^{-1}C_p^*,
\]

the induced endpoint orientation is therefore

\[
\operatorname{Im}(G_{p,12}^{\mathrm{eff}})
=
\frac{\alpha_p\beta_p}{d_p}.
\]

Reversing the oriented feature replaces \(i\) by \(-i\) and flips this sign while leaving the real endpoint data unchanged.

## Source of the phase

The required relative phase is not available from real multiplication histories. Its minimal source is the Fourier quarter-turn on the independently typed odd feature:

\[
\mathcal F K=V,
\qquad
\mathcal F V=-K.
\]

Thus the signed comoving face difference supplies the oriented magnitude carrier, the Fourier \(K\)-\(V\) rotation supplies the relative \(i\)-phase, and the tail/PV Green resolver supplies \(D_p^{-1}\). The Schur return is the compressed shadow of this three-stage interaction.

The source theorem must derive the three factors independently. Merely solving

\[
\frac{\alpha_p\beta_p}{d_p}=h_p
\]

is not constructor authority.

## Granularity-sensitive matching

For the strict grade-\(1,2\) cell, the matching target is

\[
h_p^{(1,2)}
=
(\log p)(p^{-1/2}+p^{-1}).
\]

For the completed all-grade packet, the target is

\[
h_p^{(\infty)}
=
\frac{(\log p)p^{-1/2}}{1-p^{-1/2}},
\]

and this equality is admissible only when the connected grade-\(\ge3\) tail is actually present in the auxiliary reservoir. The tail cannot be silently compressed into a two-grade endpoint label.

## General reduced-support statement

For a higher-dimensional auxiliary sector, use the reduced inverse or Moore–Penrose inverse only after proving

\[
\ker D_p\subseteq\ker C_p.
\]

Then the odd coordinate is

\[
h_p
=
-\operatorname{Im}
\left(C_pD_p^\dagger C_p^*\right)_{12},
\]

with the overall sign adjusted once to the frozen reciprocal convention.

If the full block is intended positive, its exact finite criterion is:

- \(D_p\ge0\);
- \(\ker D_p\subseteq\ker C_p\);
- \(A_p-C_pD_p^\dagger C_p^*\ge0\) on reduced endpoint support.

Boundedness at one prime is not completion control; the reduced resolvents and incidences require uniform estimates on compact off-seam regions.

## Falsifiers

1. **Fitted-factor hostile.** Rescale
   \[
   \alpha_p\mapsto r_p\alpha_p,
   \qquad
   \beta_p\mapsto r_p^{-1}\beta_p.
   \]
   The observed \(h_p\) is unchanged while one factor norm can diverge. Matching the Schur shadow does not control the constructor.

2. **Granularity hostile.** Fit the all-grade Euler odd current using only the grade-\(1,2\) endpoint cell. The scalar is correct but the missing connected tail has been smuggled into \(D_p\).

3. **Kernel hostile.** Let an auxiliary radical direction survive under \(C_p\). Different generalized inverses then give different returns.

4. **Phase hostile.** Replace the Fourier quarter-turn by a real propagation. The diagonal correction survives, but the imaginary endpoint entry vanishes.

## Next irreducible calculation

Construct, from source formulas:

\[
\text{signed face difference}
\longrightarrow
(K,V)\text{ Fourier feature}
\longrightarrow
D_p^\dagger\text{ tail/PV propagation}
\longrightarrow
\text{endpoint return}.
\]

Then verify that its Schur imaginary entry equals the correctly scoped Euler odd current with the frozen sign. This is now the earliest missing constructor for the first Adams edge.
