# Projective Conductor SNC Augmentation and the Literal Pair-Vertex Gate

Date: 2026-08-15  
Status: proved in the canonical integral coefficient/log model of the
projectivized positive conductor normal cone. Literal entry-143 pair-vertex
corestrictions and the acyclic-complement contraction are not constructed.
The endpoint/\(Q\) mapping fiber and its physical parity remain undefined.
No graph admission is claimed.

## Canonical projective normal cone

On the positive normalization sheet, entry 93 gives
\[
J_+=(x_1,x_3,x_5),\qquad
E=J_+/J_+^2=L_{14}\oplus L_{03}\oplus L_{25}.
\]
Thus \(q:\mathbf P(E)\to Z\) is canonical. Its three coordinate
hyperplanes form an SNC divisor with three pairwise intersections and no
triple intersection.

After torus-orientation integration, its moment-corner complex is
\[
\mathbb Z\langle H\rangle\xrightarrow{N}
\mathbb Z^3\xrightarrow{R-I}\mathbb Z^3,
\quad N=(1,1,1)^T,
\quad R=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]
The exact identity \((R-I)N=0\) proves \(d^2=0\).

If \(S\) fixes road \(14\) and exchanges \(03,25\), reflection acts by
\(-1\) on the top, \(-S\) on oriented facets, and \(SR^{-1}\) on pairwise
intersections. Therefore
\[
(R-I)(-S)=(SR^{-1})(R-I),\qquad (-S)N=-N.
\]
This is the signed integral \(D_3\) covariance.

## Primitive Gysin, lines, and augmentation

For \(\xi=c_1(\mathcal O_{\mathbf P(E)}(1))\), projective-bundle integration
is primitively normalized:
\[
\boxed{q_*(\xi^2)=1.}
\]
No integer or occurrence parameter is inverted.

The divisor \(D_D\) is cut by a section of
\(\mathcal O(1)\otimes q^*L_D^\vee\). Its residue retains \(L_D\), and
entry 184's principal-dual evaluation has degree \((+1)+(-1)=0\) and value
one. The pairwise intersections remain as the SNC Cech overlap row; deleting
them would destroy the square-zero identity.

Let \(q_\Sigma=q_{14}+q_{03}+q_{25}\) be entry 113's road norm and let
\(s_D\) be the three oriented special residues. Projective trace followed by
the integral road transfer gives
\[
\boxed{dH_{\mathbf P^2}=q_\Sigma-s_{14}-s_{03}-s_{25}.}
\]
The row \([1,-1,-1,-1]\) has Smith form \([1]\). It is primitive and
torsion-free. It retains the three-primary Tate augmentation:
\[
\epsilon(q_\Sigma)=3=1+1+1=\sum_D\epsilon(s_D).
\]
This is the coefficient/log shadow of entry 113's mixed block, not yet its
literal spatial realization.

## Literal pair-vertex gate

A physical map to \(\mathcal E_{\partial,Q}^{\rm BM,\check C}\) must send
the top to \(H_\Sigma\), the augmentation to the based \(q_\Sigma\), each
facet to the rotated entry-112/131 Cartier gallery, and each pairwise
intersection to the common literal entry-143 short-boundary stalk reached by
the two adjacent restrictions.

The first three assignments have canonical coefficient formulas. The last
assignment is absent. On the actual AW collar it expands to 24 pair-vertex
rows. Entry 184 proves equality of their coefficient evaluations, but no
six-functor map identifies them with literal \([S,H]\) corestrictions.

Entry 179 gives a scoped no-go for doing this facewise: each of the six
cyclic adjacent dP6 pairs labels crossing short diagonals, with no common
\(K_6\) face. A zero overlap image violates
\[
df(c_{ab})=f(r_b)-f(r_a)\ne0.
\]
This does not rule out an extraordinary/logarithmic/cdh overlap object.
Exact reused certificates are:

- `research/voevodsky/check_d03_dp6_common_refinement.rs`, SHA-256
  `c0838591bfb2e2f6ddf143951636e9d5346ab1cca6cfde43d50ab6f6123a9229`;
- `research/voevodsky/check_d03_weighted_adjacent_pair.rs`, SHA-256
  `5e6375625b0f51fbebcf7f46cf38c6b97b45f13f5a3c45da19a74bd117adf5c0`.

Entry 119 supplies a second exact boundary warning. The endpoint-relative
gallery has eight edges, six internal vertices, boundary rank six, and a unit
\(6\times6\) minor. Its two route classes form a saturated \(\mathbb Z^2\),
and the positive mark selects one primitive line, but this does not construct
the spatial contraction. Its checker is

- `research/voevodsky/check_d03_q0_endpoint_relative_tor_lift.rs`, SHA-256
  `f2563b2cbd63cd655b3183635d0883030c8d219e4fbf58a91076899e02b7c54c`.

Entry 136's full-cone lift also retains an affine rank-nine family. The
projective top and facets fix the homology-bearing roof but do not select its
acyclic-complement contraction. Endpoint columns cannot remove this
ambiguity until the 24 spatial pair-vertex homotopies exist in the same
category.

## Certificate and validation

- `research/voevodsky/check_p2_conductor_snc_augmentation.rs`
- SHA-256
  `9940cc06895fc15cc1ae697de8d9f59919ed5c73268fb0eef0c39ff0c67164f0`.

MCP worker validation:

- `rustfmt --edition 2021 --check`: passed;
- `rustc --edition=2021 -D warnings --emit=metadata`: passed with empty
  stdout and stderr;
- the temporary metadata artifact was removed and confirmed absent;
- linked execution was unavailable because MSVC `link.exe` is missing, so
  runtime assertions and JSON output were not executed.

The checker explicitly records 24 required literal vertex rows, zero
constructed rows, and `rank9_contraction_constructed=false`.

## Consequence

The projective conductor normal cone supplies the integral SNC source,
primitive Gysin augmentation, line factors, overlap census, and coefficient
\(D_3\) signs. The earliest remaining arrow is a derived overlap
correspondence from every pairwise SNC stratum to the literal road costalk,
with its two boundary restrictions fixed by the adjacent facet maps.

Until those 24 rows and the induced contraction exist, the endpoint/\(Q\)
mapping fiber is uninstantiated. Thus \(p_{\partial,Q}\), its polarity
Bockstein, and \(\omega_{\rm load}\) remain undefined.

## Outcome contract

~~~json
{
  "claim": "The canonical P2 conductor SNC coefficient/log complex has top boundary N=(1,1,1), pair boundary R-I, square-zero differential, primitive projective Gysin, primitive augmented row [1,-1,-1,-1], degree-zero line evaluation, and signed D3 covariance while preserving the integral factor-three Tate augmentation.",
  "status": "proved_scoped_coefficient_log_augmentation__literal_pair_vertex_realization_open",
  "scope": "canonical integral P2 coefficient/log model only; no literal entry143 pair-vertex maps, extraordinary overlap, acyclic contraction, physical mapping fiber, parity, or graph admission",
  "factorization": {
    "top_to_facets": [1, 1, 1],
    "facets_to_pairs": "R-I",
    "d_squared": 0,
    "projective_gysin": 1,
    "augmented_row": [1, -1, -1, -1],
    "augmented_smith": [1],
    "endpoint_augmentation": "3=1+1+1",
    "line_exponents": [1, -1],
    "line_evaluation": 1,
    "facets": 3,
    "pairwise_intersections": 3,
    "triple_intersections": 0,
    "literal_entry143_vertex_rows_required": 24,
    "literal_entry143_vertex_rows_constructed": 0,
    "crossing_adjacent_pairs": 6,
    "rank6_gallery_boundary": "proved with unit minor",
    "rank9_contraction_constructed": false,
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_Bockstein": "undefined"
  },
  "checker_sha256": {
    "p2_snc": "9940cc06895fc15cc1ae697de8d9f59919ed5c73268fb0eef0c39ff0c67164f0",
    "dp6_common_refinement": "c0838591bfb2e2f6ddf143951636e9d5346ab1cca6cfde43d50ab6f6123a9229",
    "weighted_adjacent_pair": "5e6375625b0f51fbebcf7f46cf38c6b97b45f13f5a3c45da19a74bd117adf5c0",
    "endpoint_relative_rank6": "f2563b2cbd63cd655b3183635d0883030c8d219e4fbf58a91076899e02b7c54c"
  },
  "counterevidence": [
    "The 24 coefficient middle equalities are not literal stalk corestriction maps.",
    "The six adjacent dP6 pairs are crossing diagonals without common literal faces.",
    "The rank-six gallery boundary and primitive mark do not construct the spatial contraction.",
    "The AW roof retains a rank-nine acyclic-complement ambiguity."
  ],
  "minimal_repair": "Construct three derived pair-overlap maps and their 24 literal entry143 corestrictions, then solve the contraction and endpoint connector equations without changing the fixed top, facet, or qSigma rows."
}
~~~
