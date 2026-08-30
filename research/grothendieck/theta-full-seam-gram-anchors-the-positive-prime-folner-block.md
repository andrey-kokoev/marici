# Theta full seam Gram anchors the positive prime Følner block

## Bounded question

Packet 221 proves that finite seam traces vanish on normalized long
prime-power blocks. Does the independent seam state itself vanish there?

## Seam-history atoms

For \(q>0\), retain the reflected seam history

\[
h_q(t)={\bf1}_{0\le t\le q}\Phi(q-t).
\]

Its norm is

\[
\|h_q\|^2
=\int_0^q\Phi(r)^2\,dr.
\]

Therefore

\[
\|h_q\|^2\longrightarrow
\|\Phi\|_{L^2(0,\infty)}^2
\]

as \(q\to\infty\). The seam component retains asymptotically full source
energy even though its endpoint trace \(h_q(0)=\Phi(q)\) decays.

## Positive prime-orbit block

Fix \(L=\log p\) and use the normalized coefficient block

\[
v_N=\frac1{\sqrt N}\sum_{k=1}^{N}e_{p^k}.
\]

Its synthesized seam state is

\[
H_pv_N=\frac1{\sqrt N}\sum_{k=1}^{N}h_{kL}.
\]

The theta source is nonnegative, so every Gram entry satisfies

\[
\langle h_{jL},h_{kL}\rangle\ge0.
\]

Consequently the diagonal contribution alone gives

\[
\|H_pv_N\|^2
\ge
\frac1N\sum_{k=1}^{N}\|h_{kL}\|^2.
\]

Taking the lower limit yields

\[
\liminf_{N\to\infty}\|H_pv_N\|^2
\ge
\|\Phi\|_{L^2(0,\infty)}^2>0.
\]

Thus Nima's positive Følner packet defeats every finite boundary readout but
does not escape through the full seam Gram.

## Readout versus state

This sharply separates two objects that must not be conflated:

- the seam trace is a scalar boundary port with summable orbit coefficients;
- the seam history is an infinite-rank translated state retaining bulk energy.

The trace vanishes as boundary divided by volume. The full state does not,
because its translated mass moves outward rather than disappearing.

This is the same quotient phenomenon found earlier for a single far label,
now upgraded to a long prime-power block: the visible boundary coordinate
tends to zero while the retained seam fiber remains nonzero.

## Uniform-frame gate

The positive block is not the general coefficient hostile. Complex phases can
cancel cross terms. For arbitrary coefficients, the translate Gram is governed
by its Toeplitz symbol, formally

\[
W_p(\theta)
=\frac1L\sum_{m\in\mathbb Z}
\left|\widehat\Phi
\left(\frac{\theta+2\pi m}{L}\right)\right|^2.
\]

A uniform lower frame bound is equivalent to

\[
\inf_{\theta}W_p(\theta)>0.
\]

The positive Følner calculation proves survival at the zero-frequency mode.
It does not prove the full lower frame bound. The sharp hostile is a modulated
long block concentrating near a zero of \(W_p\).

## Conservation gate

Even a positive seam Gram is not yet RH force. It must enter the doubled Green
identity with a source-fixed sign and must be tied to the scalar-zero endpoint
condition. Otherwise it is merely a faithful retained state whose scalar trace
can vanish.

The next two exact questions are therefore:

1. Does \(W_p\) have a positive lower bound for each prime orbit, and can that
   bound survive the all-prime completion?
2. Does the full seam Gram occur in the typed mixed residual with the sign
   required by the seam-selective oscillator law?

## Scope

This packet proves that the full seam Gram anchors the positive normalized
prime-power Følner blocks that defeat all finite boundary ports. It does not
prove a uniform translate-frame bound, control modulated packets, establish
the sign of the seam term in the global Green identity, or prove RH.
