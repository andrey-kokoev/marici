# A finite seam Schur complement cannot control the global Laguerre form

## Bounded question

Can the augmented seam packet `(Theta,H_1,M_0,...)` be truncated at finite
order and Schur-complemented to obtain the first generalized Laguerre form of
`Xi` for every real spectral parameter?

## Hostile finite-jet deformation

Write the completed even Fourier source as `Phi(u)>0`.  Fix any finite jet
order `N` and define

\[
 g_N(u)=u^{2N+2}e^{-u^2},
 \qquad
 \Phi_\varepsilon(u)=\Phi(u)(1+\varepsilon g_N(u)).
\]

The multiplier is even and bounded.  For sufficiently small real
`epsilon`, it is strictly positive.  Therefore `Phi_epsilon` retains:

1. positivity of the completed source;
2. reciprocal reflection `u -> -u`;
3. every derivative at the self-dual seam through order `2N+1`.

But its Fourier transform changes by

\[
 X_\varepsilon(x)-X(x)
 =\varepsilon\int_{\mathbb R}
 \Phi(u)g_N(u)e^{ixu}\,du,
\]

which is not identically zero because `Phi g_N` is a nonzero integrable
function and Fourier transformation is injective.

Thus no construction depending only on the finite seam jet can reconstruct
the global transform `X(x)`, its derivatives, or its Laguerre form for all
`x`.

## No-go theorem

\[
 \boxed{
 \text{finite seam data}
 \not\Longrightarrow
 \text{global Fourier--Laguerre orientation}.}
\]

In particular, a finite matrix built only from seam values of
`Theta,H_1,M_0,...,M_N` cannot have a Schur complement identically equal to
the first Laguerre form throughout the real spectral axis unless additional
global transport data are supplied.

This is an information-theoretic obstruction, not a counterexample to the
specific theta function.  The deformation need not lift to the full adelic
labelled source.  Its role is to prove that the finite seam packet alone is
insufficient authority.

## What survives from packet 116

The modular derivative identity remains valuable: it proves that the
primitive channel is not an adjustable local counterterm and closes the
bilateral derivative presentation.  What fails is the inference that local
closure supplies global oscillatory control.

The corrected architecture is

\[
 \boxed{
 \text{closed seam packet}
 +\text{source-labelled transport over all }u
 \longrightarrow
 \text{candidate Laguerre form}.}
\]

## Exact global object

For

\[
 X(x)=\int_{\mathbb R}\Phi(u)e^{ixu}\,du,
\]

the first Laguerre form is

\[
 \mathcal L_1[X](x)=(X'(x))^2-X(x)X''(x).
\]

It has the two-copy representation

\[
 \boxed{
 \mathcal L_1[X](x)
 =\frac12\iint_{\mathbb R^2}
 (u-v)^2\Phi(u)\Phi(v)e^{ix(u+v)}\,du\,dv.}
\]

The squared separation is positive, but the sum-coordinate phase is global
and oscillatory.  Seam jets control local moments of this object; they do not
orient its Fourier transform.

## Next gate

The next admissible object is therefore the full transported two-copy source,
with variables

\[
 S=u+v,
 \qquad D=u-v.
\]

One must derive, from the integral winding labels and modular reflection, a
canonical conditional transport in `D` at fixed `S` whose pushforward has a
nonnegative cosine transform.  This returns to the adjacent-band programme,
but now with the all-order integral sign-regularity theorem as source input.

The falsifier is local: one source-authorized adjacent `S`-band pair for which
the transported negative cosine contribution exceeds its positive partner.
No amount of additional seam derivatives can repair such a failure.
