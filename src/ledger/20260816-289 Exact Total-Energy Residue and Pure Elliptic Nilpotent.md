---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Exact Total-Energy Residue and Pure Elliptic Nilpotent

## Result

The total-energy residue of the frozen absolute nine-master
\(q_{\mathcal G_{12}}\)-sector is now explicit.

Use the source slice

\[
X_1=\rho\lambda,
\qquad
X_2=\lambda,
\qquad
X_3=1,
\]

so that

\[
E=(\rho+1)\lambda+1.
\]

In the equation-(58) basis \((e_1,\ldots,e_9)\), the residue of the exact
connection at

\[
\lambda=-\frac1{\rho+1}
\]

has only two nonzero blocks:

\[
\boxed{
R_E
=
(1)_{e_1}
\oplus
0_{e_2,\ldots,e_6}
\oplus
B_\rho,
}
\]

where

\[
\boxed{
B_\rho=
\begin{pmatrix}
-\frac12&
\frac{\rho+1}{2}&
\frac{\rho+1}{2\rho}
\\[2mm]
-\frac1{4(\rho+1)}&
\frac14&
\frac1{4\rho}
\\[2mm]
-\frac{\rho}{4(\rho+1)}&
\frac\rho4&
\frac14
\end{pmatrix}.
}
\]

Direct exact multiplication gives

\[
\operatorname{rank}B_\rho=1,
\qquad
\operatorname{tr}B_\rho=0,
\qquad
\boxed{B_\rho^2=0}.
\]

The residue \(1\) on \(e_1\) is integral and therefore has trivial local
monodromy. After this apparent integral gauge is removed, the complete
absolute monodromy is unipotent with

\[
\boxed{
\operatorname{rank}N_E=1,
\qquad
N_E^2=0.
}
\]

The nilpotent is purely elliptic. The algebraic rank-seven kernel has
identity monodromy at generic nonsoft \(E=0\).

## Frozen computation

No compactification, projector, or residue ansatz was introduced. The input
is the exact source-normalized connection already recorded in
`research/benincasa/nine_master_connection_results.json`.

For every matrix entry, take the ordinary logarithmic residue

\[
\operatorname{Res}_{E=0}(A\,d\lambda)
=
\operatorname{Res}_{\lambda=-1/(\rho+1)}(A\,d\lambda).
\]

The resulting symbolic matrix is displayed above.

As an independent exact audit, every one of the \(81\) entries was
recomputed after specializing

\[
\rho=2,3,\ldots,65.
\]

This gives

\[
64\cdot81=5184
\]

exact BigInt comparisons and zero mismatches.

## Gysin-kernel test

At \(E=0\), the entry-150 algebraic vector in the last-three space is
proportional to

\[
v_{\rm alg}
=
\left(
\frac{\rho-1}{\rho+1},
2,
-2
\right)
\]

in the ordered basis \((e_7,e_8,e_9)\). Exact multiplication gives

\[
\boxed{
v_{\rm alg}B_\rho=0.
}
\]

Also \(e_6\) has zero residue. Therefore the complete final-block
algebraic plane

\[
\langle e_6,v_{\rm alg}\rangle
\]

is killed by the nilpotent, while the induced operator on the rank-two
Gysin quotient has rank one.

Hence

\[
\boxed{
N_E=N_{\rm ell}
}
\]

on the absolute nine-master system: there is no additional
total-energy nilpotent in \(\mathcal T_7\).

## Compatibility with the Legendre description

The pure elliptic object is

\[
\mathcal K_{B^{-1/2}}
\otimes
m^*\mathbb H_{\rm Leg}.
\]

At \(E=0\), both the Legendre degeneration at its coarse cusp and the
Kummer factor contribute order-two semisimple characters. Their product is
trivial in the source-normalized block, while the nodal unipotent survives.
The exact residue therefore refines the earlier standard-degeneration
inference:

\[
T_s=I,
\qquad
T_u=\exp N_E,
\qquad
\operatorname{rank}N_E=1,
\qquad
N_E^2=0.
\]

This monodromy statement is directly computed from the source connection,
not merely inferred from the nodal curve.

## Consequence for the total-energy split model

Entry 286 finds two \(\mathbb P^2\) sheets glued along a conic. The present
connection calculation shows that its generic absolute nearby-cycle
extension contains only:

1. the rank-seven algebraic Tate system with trivial local monodromy;
2. the rank-two elliptic/Tate limit with one rank-one nilpotent.

Thus the four enhanced points do not create an additional absolute
nilpotent block. Their higher-Rees effects belong to marked
Cut--nearby/excess data, as found in entries 319--320, rather than to a new
absolute Gauss--Manin summand.

## Classification

| Structure | Geometric home |
|---|---|
| integer residue on \(e_1\) | apparent algebraic gauge |
| zero residue on \(\mathcal T_7\) | algebraic Tate coefficient system |
| \(B_\rho\) | nodal elliptic nearby cycles |
| rank-one \(N_E\) | Legendre/Gauss--Manin coefficient data |
| enhanced-point higher grades | marked higher-Rees/excess data |
| new carrier datum | none |

## Deutsch--Popperian update M2.32

The hard-to-vary claim

\[
\text{the total-energy split surface may add a nontrivial algebraic
nilpotent to the absolute nine-master system}
\]

is falsified.

The narrower surviving theorem is

\[
\boxed{
\text{the generic nonsoft absolute }E=0\text{ nilpotent is exactly the
rank-one elliptic nodal nilpotent.}
}
\]

This is strong evidence for H2: the global split and enhanced-point
geometry change the coefficient filtration but do not force a new carrier
or an extra absolute monodromy sector.

## Scope boundary

This entry computes the absolute rank-nine residue only. It does not yet
determine the off-diagonal residue of the canonical marked extension

\[
0\to H^2(S_E)
\to H^2(S_E\setminus W)
\to H^1(W)(-1)
\to0.
\]

In particular, it does not identify the total-energy specialization of the
invariant top conductor lift with the entry-319 exceptional interval merely
because both occur at the physical enhanced point.

## Next hostile test

Compute the marked quotient monodromy at \(E=0\) directly from the frozen
six-edge conductor graph and the exact wall roots. Then determine the
off-diagonal top column by comparing its disappearing cycle with the
source-selected exceptional boundary

\[
(-1,1)
\in
H_1(\mathbb P^1,\{p_0,p_-,p_+\}).
\]

The finite falsifier is either:

1. a nonzero mixed-column residue despite the two conductor roots remaining
   distinct; or
2. a top-column class not generated by the physical enhanced-point
   log blowup and its existing algebraic functional.

Only the second outcome can challenge the shared-carrier hypothesis.
