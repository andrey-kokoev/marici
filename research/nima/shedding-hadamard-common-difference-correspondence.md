# Shedding as a finite common/difference decomposition

Fix a pure facet state `K` and a shedding channel `v`. Partition its facets into

\[
\mathcal F_v=\{T:v\in T\},\qquad
\mathcal F_{\bar v}=\{T:v\notin T\}.
\]

For every `T in F_v`, shedding gives the unique ridge flip

\[
\phi_v(T)=(T\setminus\{v\})\cup\{v'_T\}\in\mathcal F_{\bar v}.
\]

The map `phi_v` is injective: if two facets had the same image, the shared ridge's unique completion by `v` would recover the same source facet. Hence the facet module splits into disjoint two-dimensional blocks

\[
\operatorname{span}\{e_T,e_{\phi_v(T)}\}
\]

plus unmatched avoiding facets.

On every paired block apply the Hadamard rotation

\[
c_T=\frac{e_T+e_{\phi_v(T)}}{\sqrt2},\qquad
d_T=\frac{e_T-e_{\phi_v(T)}}{\sqrt2}.
\]

The common vector `c_T` retains the shared ridge context `T\setminus{v}`. The difference vector `d_T` records the alternative channel completion `v-v'_T`. Thus shedding canonically constructs equal-rank common and difference sectors. Maximum overlap selects a channel for which this decomposition exists while its incompatibility incidence is maximal.

`check_shedding_hadamard_pairing.py` verifies this decomposition along maximum-degree shedding recursions through every order pair at `n<=8`:

- 2,491 distinct recursive states;
- 4,339 disjoint paired blocks;
- common rank 4,339;
- difference rank 4,339;
- 3,023 unmatched avoiding facets;
- no nonunique or noninjective flip pairing.

This is the finite combinatorial counterpart of the analytical Hadamard splitting

\[
C=\frac12(F_T+F_0),\qquad D=\frac12(F_T-F_0).
\]

An actual identification with the Voevodsky relative row requires a realization functor sending paired facet generators to the two analytical legs and intertwining these Hadamard rotations. The combinatorial source decomposition is now explicit; constructing that functor is the remaining comparison map.
