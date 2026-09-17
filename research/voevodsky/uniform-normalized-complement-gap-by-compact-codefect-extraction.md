# Uniform normalized complement gap by compact co-defect extraction

Fix a finite support window `I_L=[-L,L]`. Choose `beta_L` so that

\[
H_L=A_{\infty,L}+\beta_L I>0,
\]

where `A_{infty,L}` is the compressed archimedean-plus-endpoint operator, and
write

\[
A_L=H_L-D_L,
\qquad
C_L=H_L^{-1/2}D_LH_L^{-1/2}.
\]

Here `D_L` contains the compensating scalar shift and the finite signed
prime-power translations active on `I_L`.

The logarithmic archimedean operator on a bounded interval has compact
resolvent. Hence `H_L^{-1/2}` is compact. Since `D_L` is bounded for each fixed
`L` (a finite sum of compressed translations plus finite-rank terms), `C_L` is
compact and self-adjoint.

Fix once and for all `tau<1`, for example `tau=.9`, and let

\[
P_L=\mathbf1_{(\tau,\infty)}(C_L),
\qquad Q_L=I-P_L.
\]

Compactness implies `rank(P_L)<infinity` for every finite `L`. Use normalized coordinates `u=H_L^{1/2}f`. By spectral calculus,

\[
Q_L C_LQ_L\le \tau Q_L.
\]

Hence, whenever the normalized coordinate satisfies `u in ran(Q_L)`,

\[
A_L[f]
=\langle u,(I-C_L)u\rangle
\ge(1-\tau)\|u\|^2
=(1-\tau)H_L[f].
\]

The corresponding physical dangerous space is
`H_L^{-1/2} ran(P_L)`; the spectral projection is not asserted to commute
with `H_L`.

Thus the normalized complement gap `1-tau` is uniform in `L`; all possible
loss of positivity is confined to the finite-dimensional co-defect packet
`P_L`.

This theorem does **not** give a uniform bound on `rank(P_L)`. Such a bound is
not expected as `L` tends to infinity: the concentration count can grow with
the support length. What is uniform is the complement Loewner gap. A global
proof must therefore control a growing but finite packet, preferably through
an asymptotic edge model plus interval continuation, rather than assert one
fixed finite rank for all supports.
