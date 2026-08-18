---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 655 — Exact IBP Primitives Cannot Change the Wall Cohomology Class

## Type correction

Entry 652 proposed computing a cohomological boundary-residue map from the
three minimal logarithmic IBP generators to the shared-wall cocycle module.
For exact IBP corrections, that map is identically zero.

Let \(W\) be one component of the frozen logarithmic wall divisor and let
\(\nabla=d+d\log(u)\wedge\) be the twisted differential. For every logarithmic
primitive \(\alpha\), the residue morphism is a chain map up to the standard
degree sign:

\[
\boxed{
\operatorname{Res}_W(\nabla\alpha)
=
(-1)^\sigma\nabla_W\operatorname{Res}_W(\alpha).
}
\]

Consequently

\[
\bigl[\operatorname{Res}_W(\nabla\alpha)\bigr]=0
\qquad\text{in}\qquad
H^\bullet(W,\nabla_W).
\]

The same statement holds for the total residue morphism of the three-wall
Čech/localization complex: an exact correction in the ambient logarithmic
complex maps to a total coboundary on the wall complex.

## Consequence for Entries 650--652

The three degree-seven vector fields of Entry 652 can have nonzero
form-level residues. They supply distinct legal IBP representatives and may
matter to a chain homotopy. But their exact differentials cannot alter the
cohomology class

\[
[\rho_{\rm phys}]\in H^1(W_{123})(-1).
\]

Therefore the proposed cohomological rank is forced:

\[
\boxed{
\operatorname{rank}
\left(
\nabla\operatorname{Der}^{(7)}(-\log D)
\longrightarrow H^1(W_{123})(-1)
\right)=0.
}
\]

This is not evidence that the three primitives are equivalent. It says
that ordinary cohomology forgets precisely the homotopy data that could
distinguish them.

## What can base the lift torsor

Entry 650's lift problem is a splitting problem for the localization
triangle, not a search for an exact form with nonzero residue cohomology.
The required datum has type

\[
h:\ C_W\longrightarrow C_{\rm open}[-1]
\]

together with a declared identity such as

\[
\partial_W h+h\partial_W
=
\operatorname{id}-s\pi,
\]

or an equivalent source-normalized contracting homotopy/finite-part
splitting. Only such secondary data can choose an origin among the absolute
lifts while remaining invisible after passage to ordinary cohomology.

The source syzygy condition

\[
V(K_E)\in(K_E),
\qquad
V(q_i)\in(q_i)
\]

guarantees admissibility of candidate homotopies. It does not supply the
normalization, side condition, or projection needed to define \(h\).

## Classification

- existing carrier: the frozen Cayley--Menger and five-wall divisor;
- shared calculus: residue as a morphism of logarithmic/twisted complexes;
- missing datum: source-normalized secondary chain homotopy or localization
  splitting;
- new carrier datum: none.

## Next falsifier

Freeze the literal physical proper-top generator from Entry 653 and run the
source IBP reduction with two independently chosen bases of the
three-dimensional degree-seven syzygy space. Compare the resulting absolute
nine-master lifts.

If their difference is zero in \(\mathcal T_7\), the reduction defines a
candidate basis-independent splitting. If it is nonzero, ordinary source
IBP reduction does not canonically base the lift torsor; an additional
physical-chain or finite-part normalization is required.

## Evidence

- the standard residue-chain-map identity for logarithmic de Rham
  complexes;
- research artifact `research/benincasa/ibp-residue-chain-map-type-gate.json`;
- epistemic event `ev-000000000255-16b62d4d-6dd5-47e5-b156-14bd0e348e69`;
- numbering-correction event `ev-000000000256-f7a301b7-8eca-4e7f-9f6b-ba1755b0b48a`;
- Entries 326, 648, 650--653.

## Outcome contract

~~~json
{
  "claim": "Exact logarithmic IBP corrections can have nonzero image in shared-wall cohomology.",
  "status": "falsified",
  "cohomological_residue_rank": 0,
  "form_level_residue_may_be_nonzero": true,
  "canonical_T7_lift": "not established",
  "required_object": "source-normalized chain homotopy or localization splitting",
  "next_experiment": "Test nine-master lift independence under two bases of the complete degree-seven syzygy space."
}
~~~
