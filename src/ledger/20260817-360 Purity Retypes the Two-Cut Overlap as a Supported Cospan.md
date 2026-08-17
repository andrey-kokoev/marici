---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Purity Retypes the Two-Cut Overlap as a Supported Cospan

## Question

Entry 359 found a canonical locally closed common overlap. Its initial
formulation suggested that ordinary restriction followed by extension by
zero might already give a transition between the two rank-twelve sector
objects. The hard-to-vary claim tested here is

\[
\boxed{
p_{23!}p_{12}^*
\text{ canonically defines a degree-zero cross-sector coefficient arrow.}
}
\]

This is a type test before any cyclic basis identification or fitted
projector.

## Purity degree

The common open curve (C^\circ) has complex codimension one in each sector
surface open. For

\[
p_{ij}:C^\circ\longrightarrow U_{ij},
\]

absolute purity gives

\[
\boxed{
p_{ij}^!\mathcal L_{ij}
\simeq p_{ij}^*\mathcal L_{ij}[-2](-1).
}
\]

The source-derived identity of the two ordinary Cayley--Menger/Kummer
restrictions has bidegree ((0,0)). A cohomological correspondence feeding
the target counit requires the extraordinary restriction of bidegree
((-2,-1)). Therefore the ordinary identity cannot silently be used as the
required correspondence class.

The proposed degree-zero transition is falsified.

## Corrected object

The frozen normal equations and their Koszul orientation identify the two
extraordinary restrictions on the common curve:

\[
\mathcal K_{12,23}
\simeq p_{12}^!\mathcal L_{12}
\simeq p_{23}^!\mathcal L_{23}.
\]

Localization provides canonical counits

\[
p_{12!}\mathcal K_{12,23}\longrightarrow\mathcal L_{12},
\qquad
p_{23!}\mathcal K_{12,23}\longrightarrow\mathcal L_{23}.
\]

These arrows have the common supported object as source. They form a cospan
inside the two different sector categories after the appropriate direct
images. They do not compose into a transition between the full sector
objects because no canonical retraction

\[
\mathcal L_{12}\longrightarrow p_{12!}\mathcal K_{12,23}
\]

or its cyclic analogue is supplied by the localization triangle.

## Consequence for the rank-twelve comparison

The obstruction occurs before the explicit (9+3) filtration is reached.
Consequently no rank-twelve connection matrix should be compared across the
overlap until a source-defined specialization/retraction is found. Cyclic
relabeling remains an isomorphism between whole source sectors, but it is not
an overlap restriction.

The surviving statement is

\[
\boxed{
\text{the frozen two-Cut geometry canonically defines a common supported
coefficient object with maps into both sectors, not a descent transition.}
}
\]

## Classification

| Datum | Classification |
|---|---|
| (C^\circ) | existing carrier intersection |
| ([-2](-1)) | codimension-one purity |
| Koszul sign | frozen normal orientation |
| (mathcal K_{12,23}) | shared supported coefficient object |
| two counits | shared support-sensitive calculus |
| full-sector retraction | absent |
| degree-zero transition | falsified |
| new carrier datum | none |

## Correction to Entry 359

Entry 359 has been amended: its initially displayed
(p_{23!}p_{12}^*) transition was not type-correct as a degree-zero
cohomological correspondence. The valid conclusion of that entry is the
locally closed extraordinary cospan described above.

## Evidence

- `research/benincasa/marici-gm/src/bin/overlap_coefficient_type_gate.rs`;
- `research/benincasa/overlap-coefficient-type-gate-certificate.json`;
- Entries 357 and 359.

## Next falsifier

Search the frozen deformation-to-the-normal-cone/nearby-cycle geometry of
the pair (q_{\mathcal G_{12}}=q_{\mathcal G_{23}}=0) for a canonical
specialization

\[
\mathcal L_{12}\longrightarrow p_{12!}\mathcal K_{12,23}
\]

or the corresponding map from sector 23. Freeze the normal coordinates,
positive sheet, occurrence boundaries, and support before calculation.

If nearby cycles or a source-defined boundary map provides the retraction
with the required purity shift, composing it with the opposite counit gives
the first genuine cross-sector coefficient arrow. If not, the common object
is only supported incidence data and the global sector assembly remains a
cyclic equivariant sum rather than descent.
