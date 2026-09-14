# Smooth-branch normalization descent for the strict Q-targets

Date: 2026-09-08

## Presentation

The native node has the smooth normalization pieces

\[
B_+=A/I_E,\qquad B_-=A/I_O,
\]

both relative affine three-spaces over the spectator base, with common smooth conductor

\[
C=A/(I_E+I_O).
\]

These are not a smooth atlas of the node: the normalization map is finite rather than smooth at the conductor. They do, however, provide an exact normalization descent presentation.

Use the ordered Koszul resolutions `K_E`, `K_O`, and `K_6`. Its homological descent object is

\[
F=\operatorname{fib}igl(K_E\oplus K_O
\xrightarrow{(\iota_E,-\iota_O)}K_6\bigr).
\]

The already constructed maps from the 50-state node resolution are

\[
f_+(p_{U,V}),\qquad f_-(p_{U,V}),
\]

with coherence

\[
H(p_{U,V})=(-1)^{|U|}e_U\wedge e_V,
\qquad
dH+Hd=\iota_Ef_+-\iota_Of_-.
\]

Therefore

\[
P_B\longrightarrow F,
\qquad p\longmapsto(f_+(p),f_-(p),H(p))
\]

is a strict chain map. Its 130-state comparison cone contracts through 65 integral unit cancellations, proving it is a homotopy equivalence without localization or division.

## Dual and Q descent

Dualization does not split the conductor coupling. The conductor-to-sheet map retains the row `(1,-1)` after conductor base change, and the top connecting coefficient is `-1`. The descended conductor truncation is exactly

\[
q(p_{E,O}^{\vee})=-1,
\qquad q(\kappa)=1.
\]

Consequently the branchwise dual/formal Q-data descend to the strict singular `D35` and `D04` differentials rather than only to their cohomology groups.

The eight framed cycles descend because each has zero strict pullback defect and primitive coefficient one. Reflection exchanges the two marked branch presentations and their descended targets.

## Interpretation

This completes the viable replacement for a smooth native realization:

- smooth branchwise formal Q-presentations;
- explicit conductor gluing;
- chain-level coherence `H`;
- integral descent to the native singular target;
- compatibility with `q` and all eight spatial maps.

It remains incorrect to call the result one smooth Bruce Q-manifold. It is a singular formal Q-object presented by two smooth branches with derived normalization descent. Bruce's algebraic formulas and the GR distribution construction apply in the formal/IndCoh interpretation established separately.

## Verification

```sh
python research/voevodsky/check_marici_normalization_q_descent_20260908.py \
  --root . \
  --output research/voevodsky/marici_normalization_q_descent_certificate_20260908.json
```

The integration checker performs 28 new checks and consumes the independently verified 65-unit contraction of the complete comparison cone.
