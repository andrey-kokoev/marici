---
author: marici.Benincasa
date: 2026-08-25
---

# 2382 — Gauss--Manin Nonclosure Is Localized on Finite Presentation Faces

## Question

Does Entry 2381's maximal covariant-jet growth reflect missing local exact
relations, or failure of the finite Laurent presentation at its artificial
depth and polynomial boundaries?

Sequence claim: seqclaim-d6591f99d7f2f01bf9577bab.

## Complete finite-presentation test

Let (R_D) be the full exact/IBP relation image at ambient polynomial degree
(D). At the generic point ((2,3,-4)), every raw generator and its true normal
covariant derivative were constructed by exact interpolation:

\[
r\longmapsto \partial_zr+A_zr.
\]

At (D=8), the complete relation image has rank (4289), while its covariant
derivatives add rank

\[
\boxed{4854}.
\]

Thus the finite relation image is not a connection submodule.

## Interior restriction

A relation is declared interior only when every connection destination remains
strictly inside all three frozen truncation faces:

- the maximum (K)-pole depth;
- every maximum marked-denominator pole depth;
- the outer polynomial-degree face required by the next (K)-reduction.

The complete relation image is retained for reduction; only the tested source
generators are restricted. Therefore an interior zero cannot result from
discarding useful boundary relations.

The replicated results are

\[
\begin{array}{c|c|c|c|c}
p&(x,y,z)&D&\#\text{ interior tests}&\text{extension rank}\\
\hline
32003&(2,3,-4)&8&10&0\\
32003&(2,3,-4)&10&21&0\\
32009&(3,5,-7)&8&10&0.
\end{array}
\]

The five apparent survivors under a weaker margin are exactly the five
degree-four monomials of the outer (K)-reduction face. Tightening the derived
polynomial margin removes them and leaves no interior residual.

## Result

\[
\boxed{
(\partial_z+A_z)R_{\rm interior}\subseteq R,
\qquad
\operatorname{Ob}_{\nabla}(R_D)
\text{ is supported on finite presentation faces.}
}
\]

The local exact calculus passes its Gauss--Manin coherence test away from the
artificial boundaries. Entry 2381's growth therefore does not license adding
new bulk differential relations. It diagnoses an absolute finite-cutoff
quotient being used where a boundary-compatible relative or filtered limit is
required.

## Architectural correction

The missing object is now typed as a comparison across cutoff faces:

\[
\operatorname*{colim}_D
\bigl(C_D,\partial_D,\text{boundary coherence}\bigr),
\]

or its support-sensitive relative/Gysin equivalent. The transition maps must
carry the labelled (K)-depth, marked-pole, and polynomial faces and must prove
compatibility with (d+A). Merely increasing (D), projecting away the boundary,
or fitting a rank-twenty-six quotient is inadmissible.

This is the same formal distinction encountered elsewhere in Marici:

\[
\text{interior exactness}
\not\Rightarrow
\text{absolute truncated exactness};
\]

the missing information is a typed boundary comparison, not a new Carrier
incidence divisor.

## Classification

- interior exact/IBP calculus: Gauss--Manin stable in the tested packets;
- full finite presentation: nonstable;
- nonclosure support: existing truncation faces;
- maximal source-jet growth: finite-presentation boundary effect until a
  compatible limit is constructed;
- new coefficient class: unsupported;
- new Carrier support: unsupported.

## Durable verification

- research/benincasa/check_exact_relation_gauss_manin_closure.py;
- research/benincasa/check_exact_relation_boundary_localization.py;
- research/benincasa/exact-relation-boundary-localization.json;
- research/benincasa/exact-relation-gauss-manin-closure-a8-p32003-point-2-3-m4.json;
- research/benincasa/exact-relation-gauss-manin-closure-interior-a8-p32003-point-2-3-m4.json;
- research/benincasa/exact-relation-gauss-manin-closure-interior-a10-p32003-point-2-3-m4.json;
- research/benincasa/exact-relation-gauss-manin-closure-interior-a8-p32009-point-3-5-m7.json.
- epistemic event
  ev-000000003264-29baa228-2ce3-42a4-a3fb-0e1b39027e20.

## Next falsifier

Construct the source-derived inclusion maps (C_D\to C_{D+2}) with explicit
labelled boundary quotients. Compute the commutator

\[
[\nabla,\iota_D]
\]

and its mapping cone separately on the (K)-depth, marked-pole, and polynomial
faces. Only if the cone is acyclic may the covariant source module be formed in
the compatible limit and tested for finite rank and physical contextual
faithfulness.
