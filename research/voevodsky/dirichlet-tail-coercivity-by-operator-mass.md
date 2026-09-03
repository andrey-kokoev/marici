# Dirichlet-tail coercivity from the finite operator mass

## Question

Can the infinite tail gate be closed without incorrectly diagonalizing interval translations?

## Claim boundary

This packet proves existence of a finite tail cutoff and gives conservative block bounds. It does not certify the finite low-block eigenvalue or exploit cancellation among prime translations.

## Translation bound

For \(0\le a<2L\), zero-extension translation on \((-L,L)\),

\[
(T_af)(x)=\mathbf 1_{(-L,L-a)}(x)f(x+a),
\]

is a contraction on \(L^2(-L,L)\). If the prime operator is the finite sum

\[
P_L=\sum_{a\in A_L}w_aT_a
\]

with the source prefactor and adjoint terms included in the declared weights, then

\[
\lVert P_L\rVert\le A_L:=\sum_{a\in A_L}|w_a|.
\]

Consequently, for the Dirichlet projections \(E_N\) and \(Q_N\),

\[
\lVert Q_NP_LQ_N\rVert\le A_L,
\qquad
\lVert E_NP_LQ_N\rVert\le A_L.
\]

These are operator bounds and do not use a scalar frequency symbol.

## Tail reserve

Let the positive diagonal part be

\[
D_L=\log(1+\sqrt{-\Delta_D}).
\]

On the tail,

\[
Q_ND_LQ_N
\ge
\log\left(1+\frac{(N+1)\pi}{2L}\right)Q_N.
\]

If the remaining bounded localization contribution has norm at most \(C_{\rm loc}\), then the tail block has lower bound

\[
\delta_N=
\log\left(1+\frac{(N+1)\pi}{2L}\right)-A_L-C_{\rm loc}.
\]

Thus \(\delta_N>0\) whenever

\[
N+1>
\frac{2L}{\pi}
\left(e^{A_L+C_{\rm loc}}-1\right).
\]

The cutoff may be enormous, but it is finite and source-derived once \(A_L\) and \(C_{\rm loc}\) are fixed.

## Low-tail coupling

The same mass estimate gives the conservative Schur coupling bound

\[
\lVert E_NP_LQ_N\rVert^2/\delta_N
\le A_L^2/\delta_N.
\]

A positive full form follows if the certified ground eigenvalue \(\mu_N\) of the finite low block satisfies

\[
\mu_N>A_L^2/\delta_N.
\]

Sharper shifted-sine overlap matrices can reduce the coupling bound, but they are not required to prove that the infinite tail is a finite-cutoff problem.

## Disposition

The infinite tail and coupling gates reduce to finite data without scalar-symbol transport. The remaining decisive gate is a directed finite low-block enclosure, potentially with a sharper finite coupling matrix if the mass bound is too costly.

## Verification

- `research/voevodsky/checkers/check_dirichlet_tail_operator_mass.py`
- `research/voevodsky/results/dirichlet_tail_operator_mass.json`
- `research/grothendieck/dirichlet-tail-not-scalar-frequency-is-the-source-derived-resonance-object.md`
