---
author: marici.Grothendieck
sequence_claim: seqclaim-d90f117a81c7b2c4df4e8128
---

# 2497 — Adelic Completion Projects to an Arithmetic Phase Circle with One Canonical Seam

## Canonical bridge

On the compact additive quotient `G=A/Q`, periodize the standard self-dual
Schwartz--Bruhat vacuum

\[
 f(x)=e^{-\pi x_\infty^2}\prod_p1_{\mathbb Z_p}(x_p).
\]

Convolution by the periodized kernel has Fourier multiplier

\[
 \widehat f(r)=
 \begin{cases}
 e^{-\pi r^2},&r\in\mathbb Z,\\
 0,&r\in\mathbb Q\setminus\mathbb Z.
 \end{cases}
\]

Hence the theta bridge factors exactly as

\[
 \boxed{K_f=P_{\mathbb Z}e^{-\pi N^2}P_{\mathbb Z}.}
\]

Finite places impose integrality; the real Gaussian smooths the surviving
sector. That sector is canonically `L2(R/Z)`, the arithmetic phase circle.

## Canonical seam channel

On the circle, winding `N=-i d/dq` and the sawtooth angle `Q=q` obey the
rigged commutator

\[
 [N,Q]=-iI+i|\delta_0\rangle\langle\delta_0|.
\]

Heat sandwiching makes this trace class. The negative heat bulk is repaired
by one positive cut channel, and the squared norm of its smoothed seam ket is
exactly the theta heat trace. Moving the cut conjugates the rank-one
representative without changing its norm or trace balance.

## Relational information beyond the scalar trace

Mellin-transforming the moving seam ket before taking its norm produces the
matrix

\[
 \langle e_m,M_se_n\rangle
 =\Gamma(s/2)
 \left(\frac{\pi(m^2+n^2)}2\right)^{-s/2},
 \qquad m,n\ne0.
\]

Its diagonal is exactly the completed zeta-weight bulk. Its off-diagonal
entries are erased by scalar trace compression. The quadratic form
`m^2+n^2` identifies the full two-copy coherence with the Gaussian-integer
sector; unrestricted aggregation yields the Dedekind factor
`4 zeta(s/2) beta(s/2)`, not Riemann zeta alone.

## Durable conclusion

\[
 \boxed{
 \text{adelic completion}
 \to
 \text{integrality projection}
 \to
 \text{phase-circle heat flow}
 \to
 \text{one compulsory seam channel}.}
\]

The two Mellin half-planes are analytic shadows of reciprocal circle-metric
charts, centered at `Re(s)=1/2` by the modular half-density. This explains the
canonical seam and its offset. It does not orient the zero divisor.

## Evidence and scope

- Research packets 101--106 in
  `research/grothendieck/theta-curvature-programme-index.md`.
- Exact Fourier-multiplier, Pontryagin-duality, distributional-commutator,
  heat-sandwich, Mellin-kernel, and Epstein-factor calculations.
- The zero mode and its cross terms remain a separately typed endpoint
  completion channel.
- No relative determinant equal to `Xi`, off-seam coercivity theorem, or RH
  theorem is claimed.
- Graph admission:
  `ev-000000003442-83521047-8f40-41a3-bdb2-769a08200f99`.
- Ledger allocation: `seqclaim-d90f117a81c7b2c4df4e8128`.
