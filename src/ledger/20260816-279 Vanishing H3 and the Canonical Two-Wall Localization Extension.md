---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Vanishing \(H^3\) and the Canonical Two-Wall Localization Extension

## Result

Entries 342--343 left open the localization boundary

\[
H^1(W_1\cup W_2)(-1)\longrightarrow H^3(S_E).
\]

On the generic smooth de Rham locus its target vanishes:

\[
\boxed{H^3(S_E)=0.}
\]

Moreover, the union of the two frozen denominator walls is principal on
the affine residue surface. Its degree-zero Gysin class therefore vanishes.
Consequently the marked \(q_{\mathcal G_{12}}\)-residue sector fits into
the canonical short exact sequence

\[
\boxed{
0\longrightarrow H^2(S_E)
\xrightarrow{j^*}
H^2\!\left(S_E\setminus(W_1\cup W_2)\right)
\xrightarrow{\operatorname{Res}_W}
H^1(W_1\cup W_2)(-1)
\longrightarrow0.
}
\]

Its generic ranks are

\[
\boxed{0\longrightarrow 9\longrightarrow12\longrightarrow3
\longrightarrow0.}
\]

This sequence is canonical. A splitting is not.

## Frozen compactification

Retain entry 150's compactification

\[
S_E=\overline S_E\setminus D_\infty,
\]

where \(\overline S_E\) is a generic smooth degree-two del Pezzo surface
and \(D_\infty\) is its connected smooth anticanonical elliptic curve.
Thus

\[
H^1(\overline S_E)=H^3(\overline S_E)=0,
\qquad
\operatorname{rank}H^2(\overline S_E)=8.
\]

No new compactification, boundary component, or coefficient summand is
introduced.

## The top Gysin map

The localization sequence for
\(D_\infty\hookrightarrow\overline S_E\) contains

\[
0=H^3(\overline S_E)
\longrightarrow H^3(S_E)
\longrightarrow H^2(D_\infty)(-1)
\xrightarrow{i_*}H^4(\overline S_E).
\]

Both groups at the right have rank one. The Gysin map is nonzero: for the
normalized top class \(\eta\) of the connected curve,

\[
\int_{\overline S_E}i_*\eta=\int_{D_\infty}\eta=1.
\]

Hence \(i_*\) is an isomorphism over the generic de Rham field, and

\[
\boxed{H^3(S_E)=0.}
\]

Equivalently, the localization boundary of every finite-wall conductor
class vanishes before any choice of master basis or physical cycle.
Because the statement holds for the full cohomology of the double-cover
surface, it also holds in each deck-character summand used to realize the
source Kummer coefficient.

## Independent rank-nine audit

The preceding part of the same compactification sequence is

\[
H^0(D_\infty)(-1)
\xrightarrow{i_*}H^2(\overline S_E)
\longrightarrow H^2(S_E)
\longrightarrow H^1(D_\infty)(-1)
\longrightarrow0.
\]

The first map sends \(1\) to \([D_\infty]\), which is nonzero; indeed

\[
D_\infty^2=(-K_{\overline S_E})^2=2.
\]

Therefore

\[
\operatorname{rank}H^2(S_E)
=(8-1)+2=9.
\]

This recovers geometrically the rank-seven algebraic kernel plus rank-two
elliptic quotient of entry 150:

\[
0\longrightarrow\mathcal T_7
\longrightarrow H^2(S_E)
\longrightarrow H^1(D_\infty)(-1)
\longrightarrow0.
\]

It supplies no canonical splitting of that sequence.

## The finite-wall Gysin is zero

On \(S_E\), the two source walls are cut by the actual lower
denominators

\[
W_1=\{q_{\mathfrak g_1}=0\},
\qquad
W_2=\{q_{\mathfrak g_2}=0\}.
\]

Their reduced union is the principal Cartier divisor

\[
W=W_1\cup W_2
=\{q_{\mathfrak g_1}q_{\mathfrak g_2}=0\}.
\]

It is connected because the two wall curves meet at the same-sheet points
\(P_\pm\) of entries 266, 341--343. Hence \(H^0(W)\) has rank one. The
degree-zero Gysin in the wall localization sequence sends its generator to
the divisor class \([W]\), but

\[
[W]=c_1\!\left(\mathcal O_{S_E}(\operatorname{div}
(q_{\mathfrak g_1}q_{\mathfrak g_2}))\right)=0.
\]

Thus the exact localization segment

\[
H^0(W)(-1)\longrightarrow H^2(S_E)
\longrightarrow H^2(S_E\setminus W)
\longrightarrow H^1(W)(-1)
\longrightarrow H^3(S_E)
\]

reduces to the displayed short exact sequence.

Entry 343 gives

\[
\operatorname{rank}H^1(W)=3
\]

with the saturated conductor filtration

\[
0\to H^1(W_1)\oplus H^1(W_2)
\to H^1(W)
\to \mathbb Q_{\rm top}
\to0.
\]

Therefore the mixed grades \(101,110\) and top grade \(111\) are the
three-dimensional quotient of one canonical marked relative extension.

## Deutsch--Popperian verdict

The hard-to-vary conjecture was

\[
\boxed{
\text{a nonzero }H^3(S_E)\text{ obstruction may prevent the frozen
two-wall conductor lattice from lifting to marked relative cohomology.}
}
\]

It is falsified on the generic smooth locus. The target is zero and the
wall divisor is principal. Every conductor class lifts to
\(H^2(S_E\setminus W)\), although no canonical lift is selected.

The narrower surviving statement is

\[
\boxed{
\text{the unresolved datum is the extension class and its physical
relative-chain realization, not existence of a lift.}
}
\]

## Classification

\[
\boxed{
\begin{array}{c|c}
\text{structure} & \text{geometric home}\\
\hline
\mathcal T_7 & \text{algebraic part of }H^2(S_E)\\
\mathbb V_{\rm ell}(-1) & H^1(D_\infty)(-1)\\
g_{101},g_{110},g_{111} & H^1(W_1\cup W_2)(-1)\\
\text{mixed/top gluing} & \text{localization extension in }H^2(S_E\setminus W)\\
\text{localization obstruction} & 0\\
\text{new carrier datum} & \text{none}
\end{array}
}
\]

The coefficient system is filtered, not canonically decomposed:

\[
0\to H^2(S_E)\to H^2(S_E\setminus W)
\to H^1(W)(-1)\to0.
\]

## Limits

This entry is restricted to the generic smooth de Rham locus. It does not:

- extend the sequence across the elliptic, conductor, signed-energy, or
  soft discriminants;
- compute the Gauss--Manin extension matrix;
- select a splitting or coordinates for conductor classes in the absolute
  nine-master basis;
- construct the physical relative integration chain;
- prove integral lattice normalization;
- identify the source quartic \(\mathcal Q\) with this extension class.

In particular,

\[
H^3(S_E)=0
\not\Rightarrow
\text{the marked relative extension splits as a variation}.
\]

## Next hostile falsifier

Compute the Gauss--Manin connection of the canonical rank-twelve marked
residue extension in a cover adapted simultaneously to
\(D_\infty\), \(W_1\), and \(W_2\). Determine its off-diagonal
extension block without choosing a section after seeing the answer.

Then test whether every non-elliptic pole of that block is generated by the
already frozen energy, conductor, soft, and \(\mathcal Q\) supports.

The finite falsifier is:

\[
\boxed{
\text{the extension connection has a residual pole whose divisor cannot
be derived from the frozen compactification and marked walls.}
}
\]

Only such a residual divisor can reopen the new-carrier question.

## Outcome contract

~~~json
{
  "claim": "A nonzero H3(S_E) obstruction may prevent the frozen two-wall conductor lattice from lifting to marked relative cohomology.",
  "status": "falsified_on_generic_smooth_de_Rham_locus",
  "compact_surface": "generic degree-two del Pezzo",
  "boundary": "connected smooth anticanonical elliptic curve",
  "H3_compact": 0,
  "top_boundary_gysin_rank": 1,
  "H3_affine": 0,
  "H2_affine_rank": 9,
  "wall_union": "principal connected divisor div(q_g1*q_g2)",
  "wall_H1_rank": 3,
  "marked_H2_rank": 12,
  "canonical_sequence": "0 -> H2(S_E) -> H2(S_E minus W) -> H1(W)(-1) -> 0",
  "canonical_splitting": false,
  "new_carrier_datum": false,
  "remaining_problem": "Gauss-Manin extension class, discriminant extension, and physical relative-chain realization"
}
~~~
