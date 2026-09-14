# Dilation covariance makes the Fourier cutoff asymptotically identity on each recentered Hankel boundary fiber

## Local dilation covariance

Let `K` be a self-dual local field and let

\[
(D_a f)(x)
=|a|^{-1/2}f(a^{-1}x)
\]

be normalized dilation. Let

\[
P_R
=1_{\{|x|\le R\}},
\qquad
Q_R
=\mathcal F P_R\mathcal F^{-1}.
\]

The physical cutoffs satisfy

\[
D_aP_RD_a^{-1}
=P_{|a|R}.
\]

Self-dual Fourier transform reverses dilation:

\[
\mathcal F D_a
=D_{a^{-1}}\mathcal F
\]

up to the harmless source character convention. Consequently

\[
\boxed{
D_a^{-1}Q_RD_a
=Q_{|a|R}.
}
\]

## Recenter one moving module boundary

A boundary at radius `R_b` is recentered to unit radius by conjugating with `D_(a_b)`, where

\[
|a_b|=R_b.
\]

Under this recentering,

\[
\boxed{
D_{a_b}^{-1}Q_\Lambda D_{a_b}
=Q_{\Lambda R_b}.
}
\]

For the inner cutoff boundary `R_b=Lambda`, this becomes

\[
Q_{\Lambda^2}.
\]

For the outer annular boundary `R_b=R`, it becomes

\[
Q_{\Lambda R}.
\]

At reciprocal-oriented boundaries the corresponding conjugate orientation gives the same growing time--band product after inversion is included.

## Strong exhaustion

Since

\[
P_T\uparrow I
\qquad(T\to\infty),
\]

unitarity of Fourier transform gives

\[
Q_T\uparrow I
\]

strongly. Therefore

\[
Q_{\Lambda R_b}
\longrightarrow I
\]

strongly whenever

\[
\Lambda R_b\to\infty.
\]

This holds for `R_b=Lambda` and for every outer scale `R>Lambda`.

## Action on Hilbert--Schmidt boundary features

If `H` is Hilbert--Schmidt and `Q_T -> I` strongly with `||Q_T||<=1`, then

\[
\boxed{
\|(I-Q_T)H\|_{HS}
\longrightarrow0.
}
\]

To see this, approximate `H` in Hilbert--Schmidt norm by finite-rank operators; strong convergence is uniform on the finite-dimensional range, while the contraction bound controls the tail.

Apply this to the fixed recentered Hankel operators `H_k^plus/minus`. Then

\[
\boxed{
D_{a_b}^{-1}Q_\Lambda D_{a_b}
H_k^\pm
\longrightarrow
H_k^\pm
}
\]

in Hilbert--Schmidt norm.

Thus the Fourier cutoff does not alter the endpoint Hankel limit.

## Two-ended interval

For `P_L` in logarithmic notation, the two physical endpoints correspond multiplicatively to module radii `Lambda` and `Lambda^(-1)` only after choosing the symmetric module interval. Connes's displayed cutoff `|x|<=Lambda` has a singular end at zero rather than a second finite radial boundary.

The two-ended logarithmic model should therefore be interpreted through the module coordinate and its inversion compactification. At the zero end, apply module inversion first; Fourier covariance then again produces a cutoff parameter tending to infinity.

This is exactly where the primal/contragredient orientation must be retained. Treating both ends by one additive translation formula would suppress the modular factor.

## Annular channel

The annular physical channel has boundaries at `Lambda` and `R` in each retained orientation. After separately recentering each boundary, the Fourier cutoff parameters are at least

\[
\Lambda^2
\quad\text{or}\quad
\Lambda R.
\]

Both tend to infinity. Therefore every fixed recentered annular Hankel component is asymptotically unchanged by `Q_Lambda`.

## Semilocal dilation

On `A_S`, choose an idele `a_b` with total module

\[
|a_b|_S=R_b.
\]

The normalized semilocal scaling representation satisfies the same Fourier covariance, with the dual idele and source basic character. Since `O_S*` has total module one, the dilation descends to the conull class-group orbit.

Hence the recentered transported projection on `L2(C_S)` is unitarily equivalent to

\[
Q_{\Lambda R_b}
\]

possibly conjugated by a norm-one unitary. Such a unitary does not affect strong exhaustion or Hilbert--Schmidt convergence.

## Consequence for the boundary residual

Let

\[
\mathfrak h_S(g)
\]

denote the direct sum of recentered inner and annular Hankel boundary features, including norm-one fiber multiplicity. Then

\[
\boxed{
Q_\Lambda\mathfrak h_S(g)
-
\mathfrak h_S(g)
\longrightarrow0
}
\]

in the boundary Hilbert--Schmidt norm, after each moving boundary has been transported to its fixed reference fiber.

Thus the geometric boundary residual is governed by the physical cutoff commutator; the Fourier cutoff contributes no additional local endpoint operator in this recentered limit.

## Where prolate data remains

This does not make the global Halmos/prolate operator trivial. Prolate eigenvalues describe the interaction of the two cutoffs before endpoint recentering and control the transition between bulk and boundary modes.

The statement is narrower:

\[
\boxed{
\text{on each already isolated fixed endpoint Hankel fiber, }Q_\Lambda\to I.
}
\]

The Sonin sector and finite transition modes can remain in the global residual and must not be discarded.

## Remaining arithmetic identification

The boundary norm obtained geometrically is a weighted Hankel norm of the observer kernel. It remains to prove that, after:

- semilocal norm-one fiber integration;
- opposite-polarity sewing;
- Sonin conditioning;
- endpoint--gamma completion;

this norm equals

\[
W_{completed,S}(g*g^*).
\]

Dilation covariance removes the Fourier-cutoff endpoint ambiguity but does not prove this arithmetic identity.

## Cutoff-model limitation

The fixed Hankel fibers used here come from finite logarithmic interval/annulus regulators. Connes's actual physical cutoff is one-sided in module coordinates and becomes an infinite-multiplicative-volume window after the Radon--Nikodym transform. Therefore this endpoint calculation applies to the auxiliary two-sided regulated model; descent to the actual product cutoff remains open.

## Disposition

Within the auxiliary finite-window model, the transported Fourier cutoff has the endpoint limit:

\[
\boxed{
D_{a_b}^{-1}Q_\Lambda D_{a_b}
=Q_{\Lambda R_b}
\longrightarrow I.
}
\]

Therefore it preserves the recentered Hankel boundary feature asymptotically in Hilbert--Schmidt norm in that model. Before arithmetic identification, one must first compare the auxiliary lower-cutoff model with Connes's actual one-sided product cutoff.
