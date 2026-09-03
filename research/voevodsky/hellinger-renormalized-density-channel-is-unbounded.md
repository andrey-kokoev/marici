# Hellinger-renormalized density channel is unbounded

## Question

Can inverse-Hellinger normalization preserve a nonzero bulk--corona overlap while keeping the finite density comparison bounded?

## Claim boundary

No. The scalar normalization that restores constant overlap makes the canonical density multiplication operator diverge as \(Q/\varphi(Q)\). A local multiplication commutator is zero and cannot absorb the divergence. This does not exclude a nonlocal source-derived channel.

## Finite channel

For squarefree \(Q\), set

\[
w_Q
=
\frac{Q}{\varphi(Q)}
\mathbf 1_{U_Q},
\qquad
T_Q=M_{\sqrt{w_Q}}
\]

on additive \(L^2\). Its operator norm is

\[
\lVert T_Q\rVert
=
\sqrt{\frac{Q}{\varphi(Q)}}.
\]

The Hellinger affinity is

\[
\mathcal A_Q
=
\sqrt{\frac{\varphi(Q)}Q}.
\]

The unique scalar normalization restoring unit overlap is

\[
\widetilde T_Q
=
\mathcal A_Q^{-1}T_Q.
\]

Consequently,

\[
\lVert\widetilde T_Q\rVert
=
\frac{Q}{\varphi(Q)}
=
\prod_{p\mid Q}
\left(1-\frac1p\right)^{-1}.
\]

Along conductors exhausting the primes this tends to infinity. Thus \(\widetilde T_Q\) has no bounded operator limit.

## Commutator test

Both \(T_Q\) and any local prime-label multiplication generator are multiplication operators. Hence

\[
[T_Q,M_g]=0.
\]

A local order generator therefore supplies no counterterm for the divergent scalar normalization. Any useful order--Mellin commutator must contain a genuinely nonlocal operation.

## Refinement residual

Even if one chooses scalar factors \(a_Q\), a bounded coherent family would require

\[
R_{Q',Q}
=
a_{Q'}T_{Q'}J^+_{Q',Q}
-
J^\times_{Q',Q}a_QT_Q
\]

to vanish or converge to zero on a common dense domain. The inverse-Hellinger choice already fails the uniform boundedness prerequisite, so it cannot define such a family in the ambient \(L^2\) topology.

## Disposition

The scalar-renormalized local-density branch is closed. The first open constructor remains a source formula for a nonlocal finite channel \(C_Q\). Before discussing its higher residual, that formula must specify source and target spaces, conductor refinement maps, normalization, and Mellin action.

## Verification

- `research/voevodsky/checkers/check_hellinger_renormalized_density_channel.py`
- `research/voevodsky/results/hellinger_renormalized_density_channel.json`
