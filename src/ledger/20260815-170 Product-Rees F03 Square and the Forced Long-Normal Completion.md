# Product-Rees F03 Square and the Forced Long-Normal Completion

## Record

Date: 2026-08-15

Status: two scoped theorems proved. The full product-Rees occurrence square
constructs the primitive \(p_{03}\) and its strict peripheral boundary, and
its tensor with the complete line-valued long-normal factor constructs the
unique facewise local enhancement. Spatial distribution of the entry-100
Tor packet, extraordinary endpoint/flip counits, three-road normalization
gluing, and parity remain unconstructed. No graph admission is claimed.

## The full product-Rees occurrence square

Work over the unlocalized polynomial occurrence ring \(A\). Put

\[
I=(x_0,x_1),
\qquad
J=(x_3,x_4).
\]

The two ordered pairs are disjoint regular sequences. Let

\[
\pi:Y_{03}longrightarrow\operatorname{Spec}A
\]

be the product of the two Rees blowups, and use the convention-free
tautological ideal line

\[
\mathcal O_{Y_{03}}(-E_I-E_J).
\]

Its derived pushforward is the product ideal

\[
R\pi_*\mathcal O_{Y_{03}}(-E_I-E_J)=IJ
\]

with no higher contribution in this regular disjoint-pair case. Tensoring
the two primitive length-one ideal resolutions gives the exact complex

\[
\boxed{
0\longrightarrow A
\xrightarrow{d_2}A^4
\xrightarrow{d_1}A^4
\longrightarrow IJ
\longrightarrow0.
}
\]

Its chain ranks are

\[
1\longrightarrow4\longrightarrow4.
\]

Choose the four vertex generators in the order

\[
v_{03}=x_0x_3,
\quad
v_{04}=x_0x_4,
\quad
v_{13}=x_1x_3,
\quad
v_{14}=x_1x_4.
\]

The four middle generators are the oriented sides of the weighted product
square \((x_0,x_1)\boxtimes(x_3,x_4)\), and the top generator is
\(p_{03}\). The differentials are the tensor-product Koszul boundaries;
with one global product orientation,

\[
d_1d_2=0
\]

symbolically over \(A\).

## Exactness, saturation, and primitive top

Each factor resolution has primitive relation, and the two variable pairs
are disjoint. Hence

\[
\operatorname{Tor}^{A}_{k>0}(I,J)=0,
\qquad
I\otimes_AJ\xrightarrow{\sim}IJ.
\]

Both intermediate homology groups vanish. A unit maximal minor of the
edge-to-vertex incidence shows that its rank-three boundary lattice is
saturated; the top column is primitive as well. Thus the resolution has no
integer torsion and

\[
H_0\simeq IJ.
\]

Relative to the short-boundary support \(F_B\), all four edges lie in
\(F_B\), while the long-facet top survives. Therefore

\[
\boxed{
[p_{03}]\ne0,
\qquad
d p_{03}=\partial F_{03}\subset F_B,
}
\]

and \([p_{03}]\) is the primitive relative \(F03\) class. The product Rees
space constructs not just the relative class but its complete strict
four-edge peripheral lift.

## Exact entry-143 short-H-empty collar

The product-square resolution is exactly the \(H=\varnothing\) short collar
of the fixed entry-143 target \(E=F_K/F_V\) over the long facet \(F03\).
The label-preserving identification is

\[
p_{03}\longleftrightarrow[\{D03\},\varnothing],
\]

\[
e_a\longleftrightarrow[\{D03,x_a\},\varnothing],
\qquad
a\in\{0,1,3,4\},
\]

and

\[
v_{ab}\longleftrightarrow
[\{D03,x_a,x_b\},\varnothing],
\qquad
a\in\{0,1\},\quad b\in\{3,4\}.
\]

These are actual noncrossing faces. The entry-143 radial occurrence
differential on this collar is the weighted product-square differential, so
the identification is strict before quotienting by \(F_B\). The phrase
“short-\(H\)-empty” is essential: this theorem does not identify the other
circle grades or freely add denominators.

After quotienting the four edges and vertices by \(F_B\), only the primitive
\(p_{03}\) remains in the local long-facet quotient.

## The line-valued long three-state factor

Let \(D=D03\). The long-normal factor is

\[
C_D:
\mathbb Z\langle t_D,n_D\rangle
\xrightarrow{[y_D,1]}
\mathbb Z\langle p_D\rangle,
\]

where

\[
y_D=X_D\otimes u_D^\vee.
\]

This is a line-valued section, not the base-ring fraction \(X_D/u_D\).
The reciprocal dual \(u_D^\vee\) is evaluated only in the bivariant normal
pairing. No global inversion of \(u_D\) occurs.

Tensor the entire occurrence square \(P_{03}\) of ranks \((1,4,4)\) with
\(C_D\), using

\[
d=d_{P_{03}}+(-1)^{\deg P_{03}}d_{C_D}.
\]

The total ranks are

\[
\boxed{2\longrightarrow9\longrightarrow12\longrightarrow4.}
\]

Every peripheral edge and every vertex occurs in both long states. These
lower copies are forced by the tensor differential; they are not optional
decorations. Direct calculation gives

\[
d^2=0
\]

on every basis generator.

## Why a top-only attachment fails

Suppose one attaches only \(t_D\) or \(n_D\) to the nonclosed top
\(p_{03}\), omitting the corresponding peripheral copies. Then

\[
d^2(t_D\otimes p_{03})
=y_D\,d_{P_{03}}p_{03}\ne0,
\]

and

\[
d^2(n_D\otimes p_{03})
=d_{P_{03}}p_{03}\ne0.
\]

Both failures have four nonzero peripheral components. Therefore the naive
top-only attachment is not a chain complex. The full facewise tensor is the
minimal strict completion: its signed cross terms cancel precisely because
all lower copies are present.

## Local Q row after the full completion

Only after constructing the complete tensor may one quotient every
peripheral \(P_1/P_0\) copy. The remaining local long-facet row is

\[
\boxed{
[,y_D\mid1,]
=
\left[\frac{X_D}{u_D}\ \middle|\ 1\right]
}
\]

in the legal target Cech realization. The displayed fraction is the image of
the line-valued section in the summand where \(D\in S\setminus H\); it is not
a base localization. This is the entry-143 local \(Q\) radial/normal row.

Thus the quotient matrix is a consequence of the full collar complex. It
cannot be used to define a top-only antecedent, because that antecedent has
nonzero \(d^2\) before quotienting.

## Entry-100 excess packet: algebraic preservation and spatial gate

The entry-100 reciprocal/BM excess packet is an external tensor factor. Its
repeated-\(u_3\) grades

\[
\operatorname{Tor}_0,
\qquad
\operatorname{Tor}_1
\]

are algebraically preserved by tensoring with the complete local enhancement;
no naive contraction or integer torsion appears.

This algebraic preservation is not yet a spatial distribution theorem. In
entry 143, Cech states are indexed by varying circle sets \(H\subseteq S\).
The two Tor grades and their lower terms must be placed across those actual
face/circle summands with the reciprocal source/original-BM target variance.
The current checkers do not construct:

- the extraordinary endpoint counits on the two marked half-corridors;
- the first- and second-flip spatial incidence maps;
- the distribution of the repeated-\(u_3\) excess through all lower
  \(H\subseteq S\) terms; or
- the comparison identifying the resulting overlap class with the literal
  entry-143 states.

Consequently the local tensor proves coefficient compatibility and forces
the correct lower ranks, but it does not complete the entry-100 spatial
mixed-variance attachment.

## Global gluing boundary

The theorem is confined to one \(F03\) branch. It does not identify the
three branchwise generic tops with one global top, construct their
\(D_3\)-compatible overlaps, or build the normalization-sheet source map.
In particular, it does not construct

\[
dH=q_J-x_3\widetilde\xi_{03}
\]

as a comparison into the fixed endpoint/\(Q\) target. The peripheral collar
lies in \(F_B\); its strict existence does not supply the retained nonzero
\(q_J\) leg.

The outstanding global data are:

1. extraordinary endpoint/flip counits distributing the Tor grades;
2. a support-typed source-normalization to local-\(Q\) specialization;
3. three-road \(D_3\)-equivariant generic-top gluing;
4. the entry-160 logarithmic Beck--Chevalley cells; and
5. both endpoint comparison cells.

Until these exist, the endpoint-fixed mapping fiber is uninstantiated and
reflection parity is undefined.

## Anti-circularity controls

- Do not retain \(p_{03}\) while discarding its strict four-edge boundary
  before forming the chain complex.
- Do not attach only the long top states; the resulting differential does
  not square to zero.
- Do not interpret \(y_D=X_D\otimes u_D^\vee\) as global inversion of
  \(u_D\).
- Do not infer the full varying-\(H\) Cech distribution from the
  \(H=\varnothing\) collar.
- Do not identify algebraically preserved Tor grades with spatially attached
  endpoint residues.
- Do not infer three-road gluing, source normalization, a generic \(Q\) leg,
  Beck--Chevalley, parity, or graph admission from the local tensor theorem.

## Falsifiers and scope

The product-Rees theorem would be falsified by nonzero intermediate homology,
torsion or nonsaturation, failure of \(d_1d_2=0\), a nonprimitive top, or a
peripheral edge outside \(F_B\).

The local enhancement theorem would be falsified by failure of its rank
census, nonzero \(d^2\) in the full tensor, a lower copy not forced by the
Leibniz differential, or failure of the peripheral quotient to give
\([y_D,1]\). Conversely, a top-only complex with \(d^2=0\) would falsify its
scoped negative control.

The spatial boundary would be crossed by explicit extraordinary counits and
a face/circle-indexed distribution of both entry-100 Tor grades, followed by
source normalization and three-road gluing retaining \(q_J\). No global
nonexistence theorem is asserted.

## Provenance and exact certificates

The exact checkers are

- `research/voevodsky/check_d03_product_rees_occurrence_square.rs`; and
- `research/voevodsky/check_d03_local_long_normal_enhancement.rs`.

Their SHA-256 hashes are, respectively,

- `616d86db3c4398cb2bc3701447e2ba830df1e6e150f56a4c4e9d0f7e4fe46e9d`;
  and
- `520060a6873ad59fde16c300d29d6943fda6555208033c0411edd66495c0bd62`.

The first verifies the exact saturated \(1\to4\to4\) resolution, primitive
top, strict peripheral boundary, vanishing positive Tor, and absence of
torsion. The second verifies the \(2\to9\to12\to4\) rank census, signed
total differential, forced lower copies, local \([y_D,1]\) quotient, and
both top-only \(d^2\) failures.

The collar identification also uses entry 143's fixed face/circle labels;
the entry-100 Tor statement uses its independently proved reciprocal/BM
coefficient packet. Neither checker claims the missing global spatial
attachment.

## Next experiment

Construct the extraordinary endpoint/flip counits on the complete
\(2\to9\to12\to4\) local complex and distribute the entry-100
\(\operatorname{Tor}_0/\operatorname{Tor}_1\) packet across every required
entry-143 state \([S,H]\). Verify all lower Cech squares before quotienting.
Then rotate the construction to \(F14\) and \(F25\), glue the three generic
tops through a normalization-provenanced source retaining \(q_J\), and test
the logarithmic Beck--Chevalley and endpoint cells. Only afterward instantiate
the framed mapping fiber or compute parity.

## Outcome contract

~~~json
{
  "claim": "The full F03 product-Rees occurrence square is an exact saturated 1-to-4-to-4 resolution with primitive p03 and strict four-edge boundary in F_B; tensoring the entire square with the line-valued long three-state factor gives the canonical 2-to-9-to-12-to-4 local enhancement with d squared zero, forced lower copies, and local Q row [X_D/u_D|1], while every top-only attachment fails d squared.",
  "status": "proved",
  "scope": "one F03 product-Rees occurrence square, its complete line-valued long-normal tensor, and relative local-Q quotient only; no graph admission, global three-road gluing, source normalization, or parity",
  "assumptions": [
    "A is the unlocalized polynomial occurrence ring and (x0,x1),(x3,x4) are disjoint regular pairs.",
    "One global product orientation fixes the occurrence-square signs.",
    "y_D means X_D tensor u_D^vee before its legal target-Cech realization.",
    "Entry-143 face/circle labels and entry-100 reciprocal/BM Tor packet remain fixed."
  ],
  "factorization": {
    "product_Rees_ideals": ["I=(x0,x1)", "J=(x3,x4)"],
    "occurrence_resolution_ranks": [1, 4, 4],
    "occurrence_d_squared": "zero",
    "occurrence_intermediate_homology": [0, 0],
    "occurrence_saturation": "unit maximal minor",
    "occurrence_positive_Tor": "zero",
    "relative_top": "primitive p03",
    "peripheral_boundary": "all four edges in F_B",
    "entry143_short_H_empty_collar": "p03, four D03-short edges, and four D03-short-short vertices identified strictly",
    "long_factor": "[t_D,n_D] -> p_D with row [y_D,1]",
    "long_line_typing": "y_D=X_D tensor u_D^vee",
    "enhanced_total_ranks": [2, 9, 12, 4],
    "enhanced_d_squared": "zero",
    "forced_lower_copies": "all four edges and four vertices in both long states",
    "naive_t_top_only": "falsified: d2=y_D*d(p03) is nonzero",
    "naive_n_top_only": "falsified: d2=d(p03) is nonzero",
    "local_Q_row": ["X_D/u_D", "1"],
    "entry100_Tor0_Tor1": "algebraically preserved",
    "varying_H_spatial_distribution": "unconstructed",
    "extraordinary_endpoint_flip_counits": "unconstructed",
    "three_road_source_normalization_gluing": "unconstructed",
    "mapping_fiber": "uninstantiated",
    "parity": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_product_rees_occurrence_square.rs",
    "research/voevodsky/check_d03_local_long_normal_enhancement.rs",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-160 Primal Localization-Triangle Obstruction and the One-Road Beck-Chevalley Cell.md",
    "src/ledger/20260815-166 Two-Support MV Excess and the Missing D03 Chart-Generic Leg.md",
    "src/ledger/20260815-168 Full Rees First-Flip Occurrence Kernel and the External Normal Gate.md"
  ],
  "checker_sha256": {
    "product_rees_occurrence_square": "616d86db3c4398cb2bc3701447e2ba830df1e6e150f56a4c4e9d0f7e4fe46e9d",
    "local_long_normal_enhancement": "520060a6873ad59fde16c300d29d6943fda6555208033c0411edd66495c0bd62"
  },
  "counterevidence": [
    "A top-only long attachment has nonzero second differential on all four peripheral components.",
    "The H-empty collar does not determine the varying-H Cech distribution of the entry-100 Tor packet.",
    "The strict peripheral lift lies in F_B and does not itself supply the retained generic q_J leg.",
    "No extraordinary endpoint/flip counits or three-road normalization gluing have been constructed."
  ],
  "next_experiment": "Construct extraordinary endpoint/flip counits on the full 2-to-9-to-12-to-4 complex, distribute both entry-100 Tor grades over every required [S,H] state, then rotate and glue the three roads through a normalization-provenanced source retaining q_J before testing Beck-Chevalley, the framed mapping fiber, or parity."
}
~~~
