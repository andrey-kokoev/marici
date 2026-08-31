# The resolved four-matrix-unit test reduces to one mixed tail pairing

## Status

**Superseded calculation frontier.** The reduction of the positive resolved
Gram remains valid, but the formerly unevaluated mixed pairing has since been
proved real, explicit, and strictly positive:

\[
\beta_p=g_p
=2\bigl(C_{K_+*\rho}(\log p)-C_{K_+*\rho}(3\log p)\bigr)>0.
\]

It does not carry quarter-turn orientation; that belongs to the separately
typed boundary-Stokes/Wronskian linking polarization. See
`the-resolved-window-tail-is-a-difference-of-two-autocorrelation-values.md`,
`the-resolved-window-tail-is-strictly-positive-by-symmetric-unimodal-autocorrelation.md`,
and
`the-first-adams-normalization-frontier-is-a-typed-comparison-not-an-unknown-scalar.md`.

No G1.1/RH conclusion follows.

## Frozen resolved form

For the adjacent-window source vectors

\[
u=[W_L],\qquad v=[W_{2L}],\qquad L=\log p,
\]

use the selected resolved graph

\[
\mathcal Rf=(f,Bf,M_\Phi f),
\qquad
B=H_\Phi-M_\Phi I.
\]

Its polarized Green form is forced to be

\[
g_{\mathrm{res}}(f,h)
=(1+M_\Phi^2)\langle f,h\rangle
+\langle Bf,Bh\rangle.
\]

This formula is before the history codiagonal and therefore contains no wall--tail cross term.

## Four entries

The complete two-column target is

\[
G_p^{\mathrm{res}}=
\begin{pmatrix}
(1+M_\Phi^2)\langle u,u\rangle+\|Bu\|^2 &
(1+M_\Phi^2)\langle u,v\rangle+\langle Bu,Bv\rangle\\
(1+M_\Phi^2)\langle v,u\rangle+\langle Bv,Bu\rangle &
(1+M_\Phi^2)\langle v,v\rangle+\|Bv\|^2
\end{pmatrix}.
\]

Hence Hermitian symmetry gives

\[
G_{21}=\overline{G_{12}}.
\]

The diagonal history norms are controlled by the closed-history graph results.
The ordinary Hilbert pairings now have the closed formula

\[
\langle W_a,W_b\rangle
=2\bigl(R(a+b)-R(|a-b|)\bigr).
\]

The formerly new datum

\[
\beta_p:=\langle BW_L,BW_{2L}\rangle
\]

is also closed as the real positive scalar \(g_p\). Thus both off-diagonal
resolved matrix units follow:

\[
G_{12}=(1+M_\Phi^2)\langle W_L,W_{2L}\rangle+\beta_p,
\qquad
G_{21}=\overline{G_{12}}.
\]

Thus the four-unit test is not four independent analytic integrations.

## Expansion of the residual

Expanding \(B=H_\Phi-M_\Phi I\) gives

\[
\begin{aligned}
\beta_p
={}&\langle H_\Phi W_L,H_\Phi W_{2L}\rangle\\
&-M_\Phi\langle H_\Phi W_L,W_{2L}\rangle
-M_\Phi\langle W_L,H_\Phi W_{2L}\rangle\\
&+M_\Phi^2\langle W_L,W_{2L}\rangle.
\end{aligned}
\]

The final term is ordinary Hilbert data. The first three terms are the actual mixed history content. Translation covariance relates labels but does not erase the relative displacement \(L\) between \(W_L\) and \(W_{2L}\).

## Fourier-symbol form

On the bilateral translation-invariant realization, let \(h_\Phi(\xi)\) be the causal-history multiplier and

\[
b_\Phi(\xi)=h_\Phi(\xi)-M_\Phi.
\]

Then Plancherel reduces the residual to

\[
\beta_p
=
\int_{\mathbb R}|b_\Phi(\xi)|^2
\overline{\widehat W_L(\xi)}\widehat W_{2L}(\xi)\,d\xi,
\]

with the repository's Fourier normalization. For the real windows and real
causal-tail kernel, the spectral density is even and this pairing is real.
The positive resolved Gram therefore cannot supply the missing orientation.

## Source-side implication

The coefficient-side Green form is source-authorized only if its mixed value on

\[
|W_L\rangle\langle W_{2L}|
\]

is exactly the now-explicit analytic value \(g_p\). Defining the coefficient
form by pulling back that answer would still be circular; the source
constructor must independently produce the same value.

## Current earliest calculation

The mixed resolved-tail integration is closed. The remaining local tasks are:

1. derive the coefficient-side mixed Green entry independently;
2. construct the typed boundary-Stokes to theta/Wronskian comparison;
3. prove that its forced normalization is realized by the source constructor;
4. prove common-domain continuity, cutoff compatibility, and radical descent.

The positive resolved Gram and ordered linking polarization must remain
separately typed until that comparison theorem is established.
