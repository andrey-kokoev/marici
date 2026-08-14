# Simultaneous D03 Endpoint Cousin Map and the PC Purity Boundary

## Record

Date: 2026-08-14

Status: proved exact simultaneous endpoint identities in the frozen
coefficient/Cousin model; actual ringed PC extraordinary-costalk promotion is
untyped, not falsified. The accompanying Rust certificate has been statically
audited but has not yet completed formatter/compiler/runtime verification.

Scope: the \(x_3\) road edge of the fixed \(D=03\) road square, tensoring the
occurrence Koszul--Cech map of entry 129 with the reciprocal-standard/original-
Borel--Moore normal packet of entries 97 and 100. No scalar-source
specialization or nonzero generic \(Q\)-leg is constructed here.

## The two endpoint quotients

Write the road square as

\[
R\langle F\rangle\longrightarrow
R\langle a,b,c,d\rangle\longrightarrow
R\langle v_{00},v_{10},v_{01},v_{11}\rangle
\]

with

\[
dF=x_3a-x_4b-x_0c+x_1d.
\]

There are two closed opposite-path quotients on the \(x_3\) edge.

At \(v_{00}\), quotienting by
\(\langle b,d,v_{10},v_{01},v_{11}\rangle\) gives

\[
F\xrightarrow{(x_3,-x_0)^T}(a,c)
\xrightarrow{(-x_0,-x_3)}v_{00}.
\]

After the forced top and edge orientations, this is the standard ordered
Koszul diamond for \((x_0,x_3)\).

At \(v_{10}\), quotienting by
\(\langle b,c,v_{00},v_{01},v_{11}\rangle\) gives the entry-121 diamond

\[
F\xrightarrow{(x_3,-x_1)^T}(a,-d)
\xrightarrow{(x_1,x_3)}v_{10}.
\]

Both quotient maps and their finite-free dual extension-by-zero maps commute
with the road differential. Their incidence matrices are saturated and use
no rational splitting.

## Simultaneous occurrence Gysin

For \(i=0,1\), let \(g_i^{!,\mathrm{occ}}\) be entry 129's full
Koszul--Cech map from the \(x_3\) edge to the \((x_i,x_3)\) corner. In the
ordered target Cech complex,

\[
g_i^0(r)=(r/x_i,0),
\qquad
g_i^1(t)=t/x_i.
\]

The degree-zero term is essential:

\[
d_{\rm Cech}g_i^0=g_i^1d_{\rm Cech}.
\]

Thus the top occurrence values are

\[
\frac1{x_0x_3},
\qquad
\frac1{x_1x_3}.
\]

The cellular edge incidence is negative at \(v_{00}\) and positive at
\(v_{10}\); the retained endpoint coorientation cancels the first sign.
Consequently both oriented endpoint classes are positive. This is one
product-Cartier edge class with two restrictions, not two independently fitted
fractions.

## Frozen normal packet

Retain the two support variances:

\[
\text{reciprocal regular source}
\quad\text{versus}\quad
\text{original locally-finite/Borel--Moore target}.
\]

For the repeated normal,

\[
D_3=K(u_3^\vee)\otimes K(u_3),
\qquad
u_3^\vee=-q_3^{-1}u_3,
\]

entry 100 gives

\[
0\longrightarrow K(u_3^\vee)[1]
\xrightarrow{\iota}D_3
\xrightarrow{\pi}K(u_3^\vee)
\longrightarrow0
\]

with

\[
\eta_{3,\mathrm{mix}}=(-q_3,-1),
\qquad
\operatorname{tr}^{\rm ex}(\eta_{3,\mathrm{mix}})=1.
\]

The quotient \(\pi\) retains \(\operatorname{Tor}_0\); the primitive excess
retraction retains \(\operatorname{Tor}_1\). On the graph
\(q_3-1=t_3x_3\), the filtered square is

\[
\operatorname{tr}^{\rm ex}\iota([t_3])
=[t_3]\,\pi(\mathrm{section}).
\]

The remaining ordered normals are

\[
Q_{03}=(u_0,u_1,u_3,u_5),
\]

and the complete normal Koszul--Cech map sends the primitive excess class to

\[
\left[\frac1{u_0u_1u_3u_5}\right].
\]

All negative powers occur only in the target Cech localization summands.

## Theorem: the coefficient/Cousin endpoint map closes

In the frozen coefficient/Cousin category define

\[
\Gamma_i^{(0)}
=
g_i^{!,\mathrm{occ}}\widehat\otimes
(\kappa_{Q_{03}}\circ\pi),
\]

\[
\Gamma_i^{(1)}
=
g_i^{!,\mathrm{occ}}\widehat\otimes
(\kappa_{Q_{03}}\circ\operatorname{tr}^{\rm ex}),
\qquad i=0,1.
\]

The occurrence, normal, and mixed differential squares commute. The mixed
square is exactly the graph-Cartier identity above; the total mixed terms
cancel by the Koszul sign. Both Tor grades and every lower Cech term are
retained.

After applying the independent physical orientation line
\([dX_{03}]=+1\), the two residues are

\[
\boxed{
\Gamma_0(\eta_{3,\mathrm{mix}})
=
+\left[
\frac1{x_0x_3u_0u_1u_3u_5}
\right]\otimes[dX_{03}],
}
\]

\[
\boxed{
\Gamma_1(\eta_{3,\mathrm{mix}})
=
+\left[
\frac1{x_1x_3u_0u_1u_3u_5}
\right]\otimes[dX_{03}].
}
\]

The second equality reproduces entry 121. The first is its simultaneously
oriented \(v_{00}\) companion. No occurrence variable, support normal, or
integer is inverted in the source; no coefficient, sign, or splitting is
fitted.

## Sharp blocker: one purity map is still absent

The theorem lands in the coefficient object

\[
C_{(x_i,x_3)}^{\mathrm{occ}}
\widehat\otimes C_{Q_{03}}^{\mathrm{norm}}
\otimes[dX_{03}].
\]

It does not construct the ringed extraordinary-costalk comparison

\[
\boxed{
\operatorname{pur}_{i,3}^{\mathrm{PC}}:
\mathbb D(Q/B_{\mathrm{opp},i})
\widehat\otimes
\mathcal C_{Q_{03}}^{\mathrm{norm}}
\longrightarrow
i_{v_i}^{!}\mathcal Q_{03,\partial,\mathrm{lf}}^{\mathrm{PC}}.
}
\]

Entry 121 explicitly leaves this comparison unconstructed even at \(v_{10}\).
Entry 97's complete road trace cannot replace it: the corner class is
supported and dies after full occurrence localization, whereas the complete
road trace retains its generic augmentation. Ordinary coherent restriction
cannot replace it either, because the Cousin boundary of a regular unit is
zero.

Therefore the graph conjecture that
\(g_3^{!,\mathrm{occ}}\) promotes to \(g_3^{!,\mathrm{PC}}\) is neither
proved nor falsified. Its coefficient, sign, twist, Tor, and lower-Cech
shadows all pass. The first unconstructed datum is a single product-Cartier
purity/costalk natural transformation along the \(x_3\) edge; its two endpoint
maps should be restrictions of that one arrow.

The scalar-source problem is separate. Nothing here constructs
\(d_{\mathrm{sp,sc}}\), \(G_{03}^{\mathrm{Cousin}}\), or the required nonzero
generic \(Q\)-leg.

## Evidence

Static exact certificate:

- research/voevodsky/check_d03_x3_loaded_pc_endpoint_boundary.rs
- SHA-256
  8232278ae1344c212ca9baf5eab35d015396fee540be52004d9016f4258c834f

The file encodes both road quotients and dual maps, every occurrence
Koszul--Cech degree, the reciprocal/BM \(q_3\)-unit pairing, the Tor quotient
and primitive excess, all sixteen normal Koszul--Cech degrees, the filtered
Bockstein square, both loaded residues, and the target-typing negative control.

Runtime verification is pending: the available shell sandbox failed before
launching the formatter, and this continuation is MCP-only. No formatter,
compiler, or executable-pass claim is made in this entry.

## Next experiment

Construct one edge-level purity map
\(\operatorname{pur}_{x_3}^{\mathrm{PC}}\) whose restrictions are
\(\operatorname{pur}_{0,3}^{\mathrm{PC}}\) and
\(\operatorname{pur}_{1,3}^{\mathrm{PC}}\). Require it to commute with

\[
\pi,\qquad
\operatorname{tr}^{\rm ex},\qquad
\beta_{x_3},\qquad
\kappa_{Q_{03}},
\]

and with every lower occurrence-Cech term. A support change, deletion of
either Tor grade, or chosen Laurent splitting falsifies the promotion.

## Outcome contract

~~~json
{
  "claim": "The frozen D03 coefficient/Cousin data admit one simultaneous filtered x3 endpoint map whose v00 and v10 residues have the required twist, Tor, lower-Cech, and physical-orientation factors.",
  "status": "proved_in_fixed_coefficient_model__full_pc_promotion_untyped",
  "assumptions": [
    "Entries 97, 100, 121, and 129 are frozen inputs.",
    "The coefficient corner objects are not silently identified with ringed PC extraordinary costalks.",
    "Inverses occur only in target Cech localization summands.",
    "The physical line [dX03] is retained and evaluated separately."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_x3_loaded_pc_endpoint_boundary.rs sha256:8232278ae1344c212ca9baf5eab35d015396fee540be52004d9016f4258c834f",
    "ledger entries 97, 100, 121, and 129"
  ],
  "factorization_test": {
    "v00_coefficient_square": "passed by exact static derivation",
    "v10_coefficient_square": "passed by exact static derivation",
    "Tor0_and_Tor1": "both retained",
    "lower_Cech_terms": "all retained",
    "loaded_v00_residue": "+1/(x0*x3*u0*u1*u3*u5) times [dX03]",
    "loaded_v10_residue": "+1/(x1*x3*u0*u1*u3*u5) times [dX03]",
    "actual_ringed_PC_promotion": "untyped",
    "certificate_runtime": "not run"
  },
  "counterevidence": [
    "Entry 121 leaves the ringed PC extraordinary-costalk purity unconstructed at v10.",
    "The full road trace has different support and cannot substitute for the corner purity map.",
    "Ordinary coherent Cousin restriction of a regular unit is zero."
  ],
  "next_experiment": "Construct one product-Cartier edge purity map pur_x3^PC and derive both endpoint comparisons from it."
}
~~~
