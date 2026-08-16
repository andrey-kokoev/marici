# Projective Conductor Log-Torus Two-Top Source and the Spatial Can--Var Gate

Date: 2026-08-15  
Status: proved for the normalization-provenanced integral coefficient/log
two-top source. The spatial nearby-cycle can--var realization and literal
entry-143 rows remain unconstructed. No graph admission is claimed.

## Result

Let
\[
E=J_+/J_+^2=L_{14}\oplus L_{03}\oplus L_{25},
\qquad
\overline U=\mathbf P(E),
\]
and let \(D_{\rm SNC}\) be its three coordinate divisors. The canonical open
log stratum is
\[
U=\overline U\setminus D_{\rm SNC}\simeq(\mathbf G_m)^2.
\]

Its compactly supported integral cohomology has ranks
\[
\operatorname{rk}(H_c^2(U),H_c^3(U),H_c^4(U))=(1,2,1).
\]
The middle lattice is the \(A_2\) road lattice. In a simple-root basis,
rotation and reflection act by
\[
R=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
with
\[
R^3=S^2=1,\qquad SRS=R^{-1}.
\]
There are no nonzero integral \(R\)-fixed vectors in \(H_c^3\), while
\[
\operatorname{SNF}(R-I)=(1,3).
\]
Thus the middle weight retains, rather than rationally splits, the integral
three-primary Tate datum.

Both endpoint weights are primitive lines. The \(H_c^4\) line is
\(D_3\)-invariant. Rotation fixes \(H_c^2\), while reflection reverses its log
orientation. Tensoring with the independently fixed road-orientation line
contributes the second minus sign, so
\[
H_c^2(U)\otimes\operatorname{or}_{\rm road}
\]
is also \(D_3\)-invariant. Hence the canonical normalization-provenanced log
source contains two distinct invariant weight lines:
\[
\boxed{
H_c^4(U)\cong\mathbb Z,\qquad
H_c^2(U)\otimes\operatorname{or}_{\rm road}\cong\mathbb Z.
}
\]

After fixing the admitted positive log orientation, the primitive logarithmic
volume and Poincare duality give a unit comparison between the appropriately
shifted lines. Its matrix is \([1]\), with Smith form \([1]\). The direct
two-line lattice has Smith form \((1,1)\).

This identifies an intrinsic source for entry 204's required separation:

- the coherence weight can carry \(C_\Sigma\) and the discrepancy-two
  boundary multiplicity;
- the other weight can carry the primitively normalized physical
  \(H_\Sigma/q_\Sigma\) boundary;
- the \(A_2\) middle weight retains the order-three extension information.

The multiplicity-two and primitive-one target assignments are not asserted
here. They must be derived from a spatial can--var realization.

## Boundary

This theorem is not yet the requested full-log excess-Gysin correspondence.
The primitive log-volume comparison is a coefficient/log Gysin shape. It has
not been realized as a morphism of normalization/conductor nearby-cycle
objects, nor identified with the literal entry-143 support filtration.

The next required map is
\[
\operatorname{CanVar}^{!,\log}_\Sigma:
\left(H_c^2(U)\otimes\operatorname{or}_{\rm road}\right)[2]
\longrightarrow H_c^4(U)
\longrightarrow
\mathcal E_{\partial,Q}^{\rm BM,\check C},
\]
with associated grades satisfying all of the following:

1. the coherence grade maps with discrepancy multiplicity two to the
   primitive \(K_6\) top boundary;
2. the physical grade maps primitively to
   \(dH_\Sigma=q_\Sigma-\sum_Dx_D\widetilde\xi_D\);
3. the \(A_2\) middle lattice restricts to the three pair-overlap objects;
4. those restrictions derive the 24 literal \([S,H]\) rows;
5. endpoint framing and reflection commute with the comparison.

Until this map exists, the pairwise \(\Gamma_{ij}^{!,\log}\), endpoint/Q
mapping fiber, \(p_{\partial,Q}\), Bockstein, \(D_8\), and Jordan tests remain
open.

## Certificate

- \`research/voevodsky/check_p2_log_torus_two_top_can_var.rs\`
- SHA-256:
  \`985ae176f3ef88c4216891a01777c47902fe957572786a72ee31c27261b33c6e\`

Validation:

- \`rustfmt --edition 2021 --check\`: passed after formatting;
- \`rustc --edition=2021 -D warnings -O\`: passed;
- linked executable and all runtime assertions: passed;
- runtime JSON parsed and scoped status asserted: passed;
- temporary executable: removed.

The structured-command user-site binding currently admits only
\`node\`, \`pnpm\`, and \`npm\`; Rust validation therefore used the disclosed
native-shell exception after the sandbox helper failed to launch.

## Outcome contract

~~~json
{
  "claim": "The canonical open log stratum U=(G_m)^2 of the projective conductor supplies two distinct primitive D3-invariant top-weight lines after the established road-orientation twist. Its A2 middle lattice has coinvariant Smith form [1,3], and the positively oriented log-volume/Poincare bridge between the shifted endpoint lines is primitive of Smith form [1].",
  "status": "proved_scoped_normalization_provenanced_two_top_coefficient_log_source",
  "scope": "normalization-provenanced coefficient/log source only; spatial nearby-cycle can-var, discrepancy-two and qSigma target assignments, pair-overlap maps, literal entry143 rows, endpoint/Q mapping fiber, parity, D8, Jordan, and graph admission remain open",
  "evidence": {
    "open_log_stratum": "(G_m)^2",
    "compact_support_ranks_hc2_hc3_hc4": [1, 2, 1],
    "middle_rotation_fixed_rank": 0,
    "middle_coinvariant_smith": [1, 3],
    "loaded_d3_invariant_top_weight_lines": 2,
    "log_volume_bridge_smith": [1],
    "two_top_basis_smith": [1, 1],
    "spatial_can_var_comparison": "unconstructed",
    "literal_entry143_rows_constructed": 0,
    "physical_mapping_fiber": "unconstructed"
  },
  "checker_sha256": "985ae176f3ef88c4216891a01777c47902fe957572786a72ee31c27261b33c6e",
  "next_required_map": "Realize the primitive two-weight log bridge as a normalization/conductor nearby-cycle can-var map whose associated grades carry discrepancy-two coherence and primitive H_Sigma/q_Sigma, then derive the three pair-overlap restrictions and 24 literal rows."
}
~~~
