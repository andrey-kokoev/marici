# Central Exceptional Relative Cap and the Conditional Parity Test

Date: 2026-08-15  
Status: proved only in the explicitly labelled finite double-Rees product
model. The physical endpoint/\(Q\) mapping fiber and its global parity remain
undefined. No graph admission is claimed.

## The labelled product theorem

In the finite central double-Rees model, the two labelled blowup projections
canonically distinguish the occurrence and normal factors. The double
exceptional fibre is

\[
E_{\mathrm{occ,norm}}
=\mathbb P(I_{\mathrm{occ}}/I_{\mathrm{occ}}^2)
\times
\mathbb P(I_{\mathrm{norm}}/I_{\mathrm{norm}}^2)
\cong \mathbb P^1_{\mathrm{occ}}\times\mathbb P^1_{\mathrm{norm}}.
\]

Its tautological ruling lines are canonically

\[
\operatorname{pr}_{\mathrm{occ}}^*\mathcal O(-1)=\mathcal O(-1,0),
\qquad
\operatorname{pr}_{\mathrm{norm}}^*\mathcal O(-1)=\mathcal O(0,-1).
\]

Thus the graph-Tor determinant is
\(L^{-1}=\mathcal O(-1,-1)\), not a constant anti-sheet object. This
factorization is a theorem of the explicitly labelled product model; it is
not inferred merely from entry 173's base component ideals.

Let \(I_{\mathrm{occ}}\) and \(I_{\mathrm{norm}}\) be the two
oriented cellular intervals. Treat the normal factor as the framed pair
\((I_{\mathrm{norm}},\partial I_{\mathrm{norm}})\). There is a unique
primitive positive degree-\(-1\) cap

\[
\mathrm{cap}_{\mathrm{norm}}:
C_\bullet(I_{\mathrm{occ}}\times I_{\mathrm{norm}},
 I_{\mathrm{occ}}\times\partial I_{\mathrm{norm}})
\longrightarrow C_{\bullet-1}(I_{\mathrm{occ}}).
\]

It sends the oriented face to the physical occurrence edge, the vertical
edges to the aligned endpoints with shifted-chain signs, and the horizontal
edges to zero. All face, edge, and corner equations pass; crossed corners are
killed by normal degree. Since

\[
H^1(I_{\mathrm{norm}},\partial I_{\mathrm{norm}};\mathbb Z)
\cong\mathbb Z
\]

without torsion, positive endpoint normalization uniquely fixes
\(k=+1\). The output is the legal central edge
\(e_r=\{D_{03},x_3\}\). The \(D_{03}\) and repeated-\(u_3\)
factors are spectators, and their mixed squares commute with the tensor
signs.

## Virtual Cartier cancellation

The derived double-zero graph fibre supplies
\(L^{-1}[1]\). The hypersurface extraordinary pullback supplies the
virtual Cartier factor \(i^!L=L[-1]\). Therefore

\[
L^{-1}[1]\otimes L[-1]\simeq\mathcal O.
\]

Both the ruling bidegree and cohomological shift cancel. Relative
Borel--Moore normal integration consequently has rank-one primitive
coefficient \(+1\). Ordinary derived pushforward of
\(\mathcal O(-1,-1)\) is not the functor used here.

Reflection reverses the occurrence and normal orientations. Their product
makes the face even, while normal integration has the odd target character;
the fixed polarity/road-orientation twist makes this local comparison
equivariant. This local sign check does not construct the global \(D_3\)
reflection square.

## Negative controls

For the absolute normal interval,

\[
\delta:C^0(I_{\mathrm{norm}})=\mathbb Z^2
\longrightarrow C^1(I_{\mathrm{norm}})=\mathbb Z,
\qquad \delta=(-1,1),
\]

is surjective. Hence \(H^1(I_{\mathrm{norm}})=0\), and the absolute cap
is exact and nullhomotopic. Independently, the constant anti-sheet
\(\operatorname{Ext}^1\) candidate is zero. The relative boundary and the
line-valued exceptional determinant are essential; deleting either does not
produce an alternative global class.

## Local parity and the global boundary

The finite relative cap gives the primitive framed row

\[
[2,k]=[2,1].
\]

It is surjective. In this labelled local model the equation

\[
2p_{\mathrm{loc}}+k=1
\]

therefore gives

\[
p_{\mathrm{loc}}=0,\qquad
p_{\mathrm{loc}}\bmod2=0,\qquad
\beta_{\mathrm{loc}}=0.
\]

These are local coefficient conclusions only. They do **not** instantiate or
evaluate the physical/global \(p_{\partial,Q}\). Still unconstructed are:

- pairwise crossing-road support descent in the literal \(K_6\) support;
- the two endpoint connector cells and the three-road butterfly;
- the global \(D_3\) reflection square;
- the \(D_8\)/polarity and Jordan coherences;
- the retained generic-to-special \(Q\) leg and the based physical mapping
  fiber.

Accordingly the global parity is undefined. Substituting the local value into
\(p_{\partial,Q}\) before constructing those maps would be circular.

## Falsifiers

The scoped theorem fails if the labelled double-Rees fibre is not the stated
product with its two canonical projections; if either tautological line has
the wrong bidegree; if the extraordinary factor is not \(L[-1]\); if a
crossed corner survives normal degree; if any cellular chain square fails; if
positive endpoint normalization does not select \(k=1\); or if the fixed
local reflection character is inconsistent. A later failure of road descent,
endpoint gluing, or global symmetry coherence would falsify only the physical
application, not this finite relative-cap theorem.

## Provenance

- `research/voevodsky/check_d03_central_exceptional_trace.rs`, SHA-256
  `d7f4c0338512fc859734132e65d5e1fdc8b95e9905d6ae18756e2beea21e52d9`;
- `research/voevodsky/check_d03_central_relative_cap_parity.rs`, SHA-256
  `2022562e1789d10d63767e6727ad5db0ccf1ad3f0e75f43d94e561528802c6c7`;
- ledger entries 93, 100, 113, 143, 160, 173, 174, and 175.

## Next experiment

Construct the support-typed exceptional correspondence into the literal
entry-143 central edge and full local-\(Q\) collar while retaining the generic
\(q_\Sigma\) leg and both Tor grades. Rotate it through all three roads,
construct each pairwise lower-overlap homotopy and the triple/top filler, then
construct both endpoint connector cells and verify the global \(D_3\)
reflection square before testing \(D_8\)/Jordan compatibility. Only after
that acceptance test defines the based mapping fiber may
\(p_{\partial,Q}\) be evaluated.

## Outcome contract

~~~json
{
  "claim": "Inside the explicitly labelled finite central double-Rees product model, the double exceptional fibre canonically factors as P1_occ x P1_norm with tautological rulings O(-1,0) and O(0,-1); the framed normal-relative cap is unique, primitive, and normalized by k=1; L^-1[1] tensor i^!L=L[-1] cancels to O; and the local framed row [2,1] has zero local parity and local Bockstein.",
  "status": "proved",
  "scope": "explicitly labelled finite double-Rees product, relative normal cap, normal-Gysin bigrading, local reflection character, and local coefficient parity only; no graph admission and no physical/global endpoint-Q value",
  "assumptions": [
    "The Rees-enlarged conductor uses the exact labelled product model and its two canonical ruling projections.",
    "The normal interval is retained relative to both boundary points.",
    "The fixed polarity/road-orientation convention supplies the local target character.",
    "No local coefficient is identified with the physical mapping-fiber obstruction before global descent."
  ],
  "factorization": {
    "double_exceptional_fibre": "P(I_occ/I_occ^2) x P(I_norm/I_norm^2)",
    "occurrence_ruling": "O(-1,0)",
    "normal_ruling": "O(0,-1)",
    "graph_Tor": "L^-1[1]=O(-1,-1)[1]",
    "extraordinary_Cartier": "i^!L=L[-1]",
    "virtual_cancellation": "L^-1[1] tensor L[-1]=O",
    "relative_normal_H1": "Z, torsion free",
    "normalized_cap_coefficient": 1,
    "cellular_chain_squares": "pass",
    "crossed_corners": "killed by normal degree",
    "target_edge": "e_r={D03,x3}",
    "local_reflection": "occurrence -1 times normal -1 gives even face; oriented Gysin matches odd target",
    "absolute_normal_H1": 0,
    "absolute_cap": "exact/nullhomotopic",
    "constant_anti_sheet_Ext1": "zero",
    "framed_row": [2, 1],
    "local_p": 0,
    "local_parity_mod2": 0,
    "local_Bockstein": 0,
    "physical_p_partial_Q": "undefined",
    "global_parity": "undefined"
  },
  "unconstructed": [
    "pairwise crossing-road support descent",
    "two endpoint connector cells and three-road butterfly",
    "global D3 reflection square",
    "D8/polarity and Jordan coherences",
    "generic-to-special Q leg and based physical mapping fiber"
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_central_exceptional_trace.rs",
    "research/voevodsky/check_d03_central_relative_cap_parity.rs",
    "src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260814-113 Marked-Exit Tate Detector and the Mixed Boundary-Crossing Block.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-160 Primal Localization-Triangle Obstruction and the One-Road Beck-Chevalley Cell.md",
    "src/ledger/20260815-173 Component-Supported Semistable Node and the vplus Coefficient Counit.md",
    "src/ledger/20260815-174 Two-Edge Bivariant Trace and the Unlocalized Two-Flip Alignment Gate.md"
  ],
  "checker_sha256": {
    "central_exceptional_trace": "d7f4c0338512fc859734132e65d5e1fdc8b95e9905d6ae18756e2beea21e52d9",
    "central_relative_cap_parity": "2022562e1789d10d63767e6727ad5db0ccf1ad3f0e75f43d94e561528802c6c7"
  },
  "counterevidence": [
    "The absolute cap is nullhomotopic.",
    "The constant anti-sheet Ext-one candidate is zero.",
    "The global crossing-road, endpoint, D3-reflection, D8, and Jordan coherences are absent.",
    "The physical p_partial_Q and global parity remain undefined."
  ],
  "next_experiment": "Build the support-typed exceptional-to-Q correspondence, rotate it through the three roads, verify pairwise overlap and triple/top descent, attach both endpoint connectors, and close the global D3 reflection square before testing D8/Jordan and evaluating p_partial_Q."
}
~~~
