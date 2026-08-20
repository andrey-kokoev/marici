# Loaded AW Collar Principal-Line Repair and the Spatial Connector Gate

Date: 2026-08-15  
Status: proved in two explicitly labelled finite coefficient models. The
ordinary unit-normalized loaded collar is falsified, while its principal-line
bivariant coefficient repair is proved. No spatial six-functor realization,
entry-143 identification, endpoint connector, graph admission, or physical
parity claim is made.

## Four-flip finite kernel holonomy

In the labelled \(D03\) double-Rees kernel square, orient the four edges as
the boundary of the product square. Each edge is the tensor of a primitive
occurrence relation with the full relative-normal Čech/Koszul interval. The
four orientation-normalized relative-normal caps are strict chain maps with
complementary residues \((+1,-1)\). Identity counits on the common labelled
spectator packets make all four shared-vertex Beck--Chevalley commutators
zero. Consequently the cyclic holonomy is

\[
\boxed{+\operatorname{id}}.
\]

The primitive product-Rees top has boundary

\[
(1,1,-1,-1),
\]

which supplies the four-edge coherence. Reflection reverses both the square
orientation and the normal cap, while the established road-orientation twist
restores covariance. Endpoint-exclusive normal grades and the four double
overlaps are integrated out. The common spectator packet retains one
\(\operatorname{Tor}_0\) and one \(\operatorname{Tor}_1\) grade, with no
higher Tor and no integer torsion.

This is a theorem in the finite labelled kernel category. It does not realize
the four kernels as normalization-provenanced spatial correspondences.

## Actual entry-136 collars and the ordinary negative control

The actual labelled barycentric boundary of \(K_6\) has 84 flags. For each
long road \(D\in\{14,03,25\}\), the entry-136 collar \(H_D\) has 16 flag
triangles: eight front and eight back. Every front flag has one collar
preimage, every back flag has one collar preimage, and each of the eight
middle flags has exactly two preimages, one in each half.

Under the entry-105 initial-face occurrence rule, deletion toward a front
flag is multiplication by the actual principal generator \(X_D\). Deletion
toward a back flag is a unit map. Hence in relative monomial degree zero the
front block has rank zero against a primitive right-hand side supported in
all 24 front coordinates. Therefore

\[
\boxed{\text{the simultaneously unit-normalized ordinary loaded collar is empty}.}
\]

This is a divisibility/grade obstruction, not integer torsion. It is retained
as the exact negative control and no inverse \(X_D^{-1}\) is introduced.

## Principal-line bivariant repair

Let \(J_D=(X_D)\) be the occurrence principal line and let
\(J_D^\vee\) be its dual. Assign exponent \(+1\) to the front
corestriction and to the corresponding labelled back section, and exponent
\(-1\) to the dual counit. The evaluation

\[
J_D^\vee\otimes J_D\longrightarrow R,
\qquad X_D^\vee(X_D)=1,
\]

has total line degree zero and primitive value one. On the actual flag set,
all 24 front evaluations and all 24 back labelled-section evaluations are
units. For every middle flag, the front-half and back-half routes evaluate to
the same unit, so all 24 middle coefficient squares commute.

Rotation \(v\mapsto v+2\pmod 6\) cycles

\[
D14\longmapsto D03\longmapsto D25\longmapsto D14,
\]

and reflection \(v\mapsto2-v\pmod6\) fixes \(D14\) and exchanges
\(D03,D25\). The principal-line assignment respects both actions. Its Cartier
codimension shift is one. The construction is integral and uses evaluation
of a line with its dual, not localization of the base ring.

Thus the precise scoped result is

\[
\boxed{
\text{ordinary unit lift: empty},\qquad
\text{principal-line bivariant coefficient repair: proved}.
}
\]

## Provenance boundary

The two certificates determine finite labels, signs, coefficient evaluations,
and coherence matrices only. They do not construct:

- a spatial extraordinary Gysin or Beck--Chevalley correspondence;
- an identification of the repaired flags with literal entry-143
  \([S,H]\) support states and stalk corestrictions;
- a normal--Čech enhancement beyond the spectator \(\operatorname{Tor}_0\)
  and \(\operatorname{Tor}_1\) grades recorded by the four-flip model;
- collar-to-Alexander--Whitney matrices in the physical mixed-variance
  category;
- either endpoint column or its connector two-cell;
- a normalization-provenanced generic \(Q\) source arrow.

Accordingly the actual endpoint-fixed mapping fiber is still uninstantiated.
The physical \(p_{\partial,Q}\), its mod-two class, and its Bockstein remain
undefined. The coefficient repair must not be renamed a spatial Gysin map or
identified with entry 143 by matching labels alone.

## Falsifiers

The four-flip theorem fails if a cap is not a chain map, a shared-vertex
commutator is nonzero, cyclic holonomy is not \(+\operatorname{id}\), the top
boundary is not primitive, reflection covariance fails, or the spectator Tor
ranks differ from \((1,1)\).

The actual-flag theorem fails if a collar does not split \(8+8\), a front or
back flag lacks its unique preimage, a middle flag does not have the two
opposite-half preimages, the initial front quotient is not \(X_D\), a line
evaluation has nonzero degree or value other than one, any of the 24 middle
squares fails, or the stated \(D_3\) actions do not preserve the construction.

A later spatial correspondence may realize the repair; that would not undo
the ordinary unit-lift negative control. Conversely, failure of spatial
descent would not invalidate the scoped coefficient theorem.

## Exact certificates

- `research/voevodsky/check_d03_four_flip_kernel_holonomy.rs`, SHA-256
  `3d713865162372e0d9d3b321bc24593371ef0757e4452f42e068d904cf346a4c`;
- `research/voevodsky/check_k6_loaded_aw_collar_actual_flags.rs`, SHA-256
  `fe02cf1f6940d00059b84fbe5790d622b8307b568904ba961936d2c1aaa19b38`.

Relevant inputs are entries 95, 105, 136, 143, 176, and 182.

## Next experiment

Construct the normal--Čech enhanced collar on the literal entry-143 stalk
diagram. Supply spatial maps realizing \(J_D^\vee\otimes J_D\to R\), write
the collar-to-Alexander--Whitney matrices and both endpoint columns, and test
the endpoint connector equation in one common six-functor category. Only
after those checks pass should one form the physical mapping fiber or ask for
its parity and Bockstein.

## Outcome contract

~~~json
{
  "claim": "The finite labelled four-flip double-Rees kernel has strict primitive caps, zero shared-vertex BC commutators, +id holonomy, primitive top boundary (1,1,-1,-1), and spectator Tor0/Tor1. On the actual 84 entry-136 flags the ordinary unit-normalized loaded collar is empty because every front corestriction carries X_D, while the scoped principal-line bivariant repair pairs J_D degree +1 with J_D^vee degree -1 to give primitive degree-zero units on all 24 front evaluations, all 24 back evaluations, and all 24 middle squares.",
  "status": "proved",
  "scope": "explicitly labelled finite four-flip kernel and actual-flag principal-line coefficient models only; the ordinary unit lift is falsified and no spatial or physical realization is inferred",
  "factorization": {
    "four_flip_caps": "strict primitive chain maps",
    "shared_vertex_BC": [0, 0, 0, 0],
    "cyclic_holonomy": "+id",
    "product_top_boundary": [1, 1, -1, -1],
    "reflection": "covariant after the established road-orientation twist",
    "spectator_Tor0_Tor1": [1, 1],
    "higher_Tor": 0,
    "barycentric_flags": 84,
    "collar_triangles_per_road": 16,
    "front_back_per_road": [8, 8],
    "ordinary_unit_solution": "EMPTY",
    "ordinary_obstruction": "24 front rows require the nonunit X_D",
    "principal_line": "J_D exponent +1",
    "principal_dual": "J_D^vee exponent -1",
    "front_evaluations": 24,
    "back_labelled_section_evaluations": 24,
    "middle_squares": "24 PASS",
    "D3_rotation": "PASS",
    "D3_reflection": "PASS",
    "cartier_codimension_shift": 1,
    "coefficient_inversion": false,
    "integer_torsion": "none",
    "spatial_six_functor_realization": "unconstructed",
    "literal_entry143_identification": "unconstructed",
    "normal_Cech_enhancement": "unconstructed beyond the recorded finite spectator grades",
    "endpoint_connectors": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_Bockstein": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_four_flip_kernel_holonomy.rs",
    "research/voevodsky/check_k6_loaded_aw_collar_actual_flags.rs",
    "src/ledger/20260814-95 Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary.md",
    "src/ledger/20260814-105 Absolute Support Complex, Shift-Corrected Purity, and the Marked-Correspondence Obstruction.md",
    "src/ledger/20260814-136 Canonical AW-Cap Roof and the Endpoint-Connector Gap.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-176 Central Exceptional Relative Cap and the Conditional Parity Test.md",
    "src/ledger/20260815-182 Loaded Fold-Kernel Generic Top and the Endpoint Connector Extension Gate.md"
  ],
  "checker_sha256": {
    "four_flip_kernel_holonomy": "3d713865162372e0d9d3b321bc24593371ef0757e4452f42e068d904cf346a4c",
    "loaded_aw_collar_actual_flags": "fe02cf1f6940d00059b84fbe5790d622b8307b568904ba961936d2c1aaa19b38"
  },
  "unconstructed": [
    "spatial extraordinary Gysin and Beck-Chevalley correspondence",
    "literal entry-143 support/stalk identification",
    "normal-Cech enhanced physical collar",
    "collar-to-AW matrices and both endpoint connectors",
    "normalization-provenanced generic Q arrow",
    "physical mapping fiber, p, and Bockstein"
  ],
  "counterevidence": [
    "The ordinary degree-zero front block has rank zero against 24 primitive required coordinates.",
    "Finite line evaluation does not itself provide a spatial extraordinary map.",
    "Finite identity counits do not instantiate physical endpoint columns."
  ],
  "next_experiment": "Construct the normal-Cech enhanced collar and spatial principal-line evaluation on literal entry-143 stalks, then write the collar-to-AW matrices and both endpoint connector cells before defining the physical mapping fiber."
}
~~~
