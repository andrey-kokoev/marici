---
title: "The Physical Total-Energy Cusp Has an Integral Width-Two Defect"
date: 2026-08-20
entry: 1147
status: established-integral-nearby-lattice
sector: cosmology
---

# 1147 — The Physical Total-Energy Cusp Has an Integral Width-Two Defect

Sequence claim: `seqclaim-476eabfd05589065ba82427e`.

## Frozen physical cusp

The physical degeneration is

\[
E_T=0.
\]

Entries 148 and 317 establish that the Legendre semisimple sign is cancelled
by the \(B^{-1/2}\) Kummer twist. The resulting rank-two nearby object has
unipotent monodromy with rank-one nilpotent logarithm. Entry 369 fixes a
standard integral \(\Gamma(2)\) basis in which the cusp matrix is

\[
\boxed{
T=
\begin{pmatrix}
1&2\\
0&1
\end{pmatrix}.}
\]

This is also the integral realization of the already derived square-root
coarse-cusp relation

\[
q_{\rm mod}\sim E_T^2.
\]

## Smith calculation

The variation map is

\[
T-I=
\begin{pmatrix}
0&2\\
0&0
\end{pmatrix}.
\]

It has rank one, square zero, and sole nonzero Smith invariant \(2\).
Consequently

\[
\ker(T-I)\simeq\mathbb Z,
\]

while

\[
\boxed{
\operatorname{coker}(T-I)
\simeq
\mathbb Z\oplus\mathbb Z/2.}
\]

The free line is the ordinary Tate nearby grade. The \(\mathbb Z/2\) is the
integral width-two defect of the physical level-two cusp.

## Type verdict

This parity class is intrinsic to the sector-specific elliptic coefficient
lattice. It does not require an additional support divisor: the carrier is
still the existing total-energy normal, while the coefficient object
remembers that physical total energy is a square-root coordinate over the
coarse modular cusp.

Thus

\[
\boxed{
\text{linear resolved normal }E_T
+
\text{ width-two integral Legendre monodromy}
\Longrightarrow
\mathbb Z/2\text{ coefficient coinvariant}.}
\]

This is not yet a physical period or Cut class. Entry 317's simultaneous
Cut--nearby specialization of the positive Cayley--Menger/Leray chain at
\(E_T=y_{12}=0\) remains unconstructed.

## Next falsifier

Reduce the source-defined algebraic Cut map modulo two and test whether its
image lands in the torsion coinvariant or only in the free Tate line. The
calculation must retain the physical Leray tube, signed-minor boundary, and
occurrence labels at \(E_T=y_{12}=0\). A matrix-level projection without
that relative chain remains unauthorized.

Evidence:

- `research/benincasa/checkers/total_energy_legendre_integral_monodromy.py`;
- `research/benincasa/results/total-energy-legendre-integral-monodromy.json`;
- Entries 148, 161, 317, and 369.
