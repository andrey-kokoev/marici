# Arbitrary-n planar biadjoint tree amplitude

## Theorem

Let `P_n` be a convex polygon with cyclically labelled vertices `1,...,n`, and let
`D_n` be its diagonals. Attach a commuting variable `X_d` to every `d in D_n`.
For `n >= 3`, define

\[
m_n=\sum_{T\in\operatorname{Tri}(P_n)}\prod_{d\in T}\frac1{X_d}.
\]

Then, for every `n >= 3`:

1. `m_n` has one unit-coefficient term for every planar cubic tree, equivalently every triangulation of `P_n`.
2. It has `C_{n-2}` terms, where `C_r=(1/(r+1)) binom(2r,r)`.
3. It is invariant under the dihedral action on polygon labels.
4. Its only poles are the planar channels `X_d=0`, all are simple, and

   \[
   \operatorname*{Res}_{X_d=0}m_n=m_{P_L(d)}m_{P_R(d)},
   \]

   where cutting along `d` produces the two polygons `P_L(d)` and `P_R(d)`.

This is the stripped planar tree-level biadjoint amplitude appearing in the ABHY construction.

## Proof

### Cubic trees and triangulations

The planar dual of a triangulation has one vertex for each triangle and one internal edge for each polygon diagonal. Every internal dual vertex is trivalent after external polygon edges are restored as leaves, so the dual is a planar cubic tree. Conversely, embedding a planar cubic tree in the disk and taking its planar dual gives a unique polygon triangulation. Under this bijection, internal tree propagators are exactly triangulation diagonals. Thus the displayed sum is precisely the unit-numerator planar cubic-tree expansion.

### Catalan count

Fix the boundary edge `(1,n)`. In every triangulation it belongs to a unique triangle `(1,k,n)`, with `2 <= k <= n-1`. Removing that triangle leaves independently triangulated polygons on the vertex intervals `1,...,k` and `k,...,n`. Hence, writing `t_n=|Tri(P_n)|` and setting `t_2=t_3=1` for the empty/triangle factors,

\[
t_n=\sum_{k=2}^{n-1}t_k t_{n-k+1}.
\]

This is the Catalan recurrence with `t_n=C_{n-2}`. It proves the count for every `n`, not only enumerated values.

### Dihedral invariance

Every dihedral permutation `g` of polygon vertices preserves boundary edges, diagonals, crossing, and maximal noncrossing sets. Therefore `T -> gT` is a bijection of triangulations. Relabelling `X_d -> X_{gd}` permutes the summands of `m_n`, proving invariance.

### Pole set and simplicity

Each triangulation is a set, so every variable `X_d` occurs with exponent either zero or minus one in each summand. Consequently all poles are simple and lie among planar diagonal variables. Every diagonal extends to a triangulation, so every planar channel actually occurs.

### Factorization

Fix a diagonal `d`. Multiplying by `X_d` and setting `X_d=0` retains exactly the triangulations containing `d`, with that factor removed. Cutting along `d` gives a map

\[
\{T\in\operatorname{Tri}(P_n):d\in T\}
\longrightarrow
\operatorname{Tri}(P_L(d))\times\operatorname{Tri}(P_R(d)),
\qquad
T\longmapsto(T\cap P_L,T\cap P_R).
\]

It is bijective: restriction gives the forward map, while the union of two side triangulations with `d` gives its inverse. Propagator monomials split multiplicatively under this bijection. Therefore

\[
\begin{aligned}
\operatorname*{Res}_{X_d=0}m_n
&=\sum_{T\ni d}\prod_{e\in T\setminus\{d\}}X_e^{-1}\\
&=\left(\sum_{T_L}\prod_{e\in T_L}X_e^{-1}\right)
  \left(\sum_{T_R}\prod_{e\in T_R}X_e^{-1}\right)\\
&=m_{P_L(d)}m_{P_R(d)}.
\end{aligned}
\]

This proves all four claims for arbitrary multiplicity. No finite enumeration is used in the proof.

## Constructive finite enumeration

The proof is constructive and uses a finite enumeration for each fixed `n`. Enumerate triangulations by choosing the unique triangle `(1,k,n)` incident to `(1,n)`, recursively enumerating the two smaller polygons, and taking every Cartesian-product pair. Each recursive call strictly reduces the vertex count, so the enumeration terminates. The branches are disjoint because `k` is uniquely determined. Thus the finite output is complete and duplicate-free for every supplied finite `n`.

The executable checker `check_arbitrary_n_planar_biadjoint_finite_enumeration.py` performs this exhaustive recursion for every `3 <= n <= 14`, enumerating 290,511 triangulations in total and checking every factorization channel. The arbitrary-`n` conclusion still comes from the termination, disjointness, and induction argument above; no single bounded run can logically establish a universal statement by itself.

## Relation to executable evidence

The finite checker instantiates the same recursive enumeration and cut bijection used in the proof. It is therefore an executable finite certificate for each tested multiplicity and a regression test for the arbitrary-input construction.

## Boundary

This theorem proves the planar biadjoint tree expansion and its combinatorial factorization. It does not by itself prove the full arbitrary-`n` ABHY canonical-form pullback, projectivity of the scattering form, nonplanar double-partial amplitudes, or any loop statement.
