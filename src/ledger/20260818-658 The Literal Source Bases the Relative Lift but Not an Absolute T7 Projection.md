---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 658 — The Literal Source Bases the Relative Lift but Not an Absolute \(T_7\) Projection

## Hard-to-vary claim

The complete post-\(q_{\mathcal G_{12}}\)-residue source form already gives
a distinguished lift of the physical wall cocycle in the open/relative
coefficient object. No IBP primitive is needed to choose that relative
class. What remains unconstructed is a projection of the relative source
class onto the absolute algebraic kernel \(\mathcal T_7\).

## Complete localization fiber

Let \(C_{\rm phys}\) be the complete post-residue complex retaining all five
source poles, and let \(C_W\) be its shared-three-wall localization target
with the two occurrence walls retained as coefficient divisors. Denote the
canonical boundary morphism by

\[
\partial_W:C_{\rm phys}\longrightarrow C_W.
\]

Entry 657 identifies the complete five-pole residue quotient as rank twenty
inside the deletion--restriction sequence

\[
0\longrightarrow M_4\longrightarrow M_5
\xrightarrow{\operatorname{Res}_{G_{12}}}M_{4|G_{12}}
\longrightarrow0,
\qquad 15+20=35.
\]

Entry 650's rank sequence \(9\to15\to6\) instead concerns its shared-wall
presentation and must not be substituted for the complete five-pole ranks.

Entries 647--648 freeze the literal unsplit source form

\[
\Omega_{\rm phys}
=
\frac{da\wedge db}
{\sqrt{K_E}\,q_{g1}q_{g2}q_{g3}}
\left(
\frac1{q_{g23}}+\frac1{q_{g31}}
\right)
\]

and compute its closed wall cocycle:

\[
\partial_W[\Omega_{\rm phys}]=[\rho_{\rm phys}].
\]

Therefore

\[
\boxed{
[\Omega_{\rm phys}]
\in
\partial_W^{-1}([\rho_{\rm phys}])
}
\]

is a source-defined basepoint of the complete localization fiber. The
physical source supplies one of its points without any choice of IBP
primitive.

This statement uses the complete post-residue five-pole source and is
unaffected by Entry 656's correction of the three-pole pre-residue
subpacket.

## What IBP can and cannot change

Changing the generating basis of the IBP/syzygy row space changes reduction
representatives, not the quotient class of the fixed source form:

\[
[\Omega_{\rm phys}]
\in H^2(S_E\setminus W_{123})
\]

is basis-independent by construction. Entry 655 explains why exact IBP
corrections also leave its wall cohomology class unchanged.

Thus the question “does IBP choose a lift of \(\rho_{\rm phys}\)?” has
already been answered by the source form itself. The remaining question has
a different type:

\[
\boxed{
\text{is there a source-defined retraction or splitting that assigns
absolute nine-master coordinates to the relative class?}
}
\]

## Why \(T_7\) is still not selected

Entry 150 provides

\[
0\longrightarrow\mathcal T_7
\longrightarrow\mathcal M_q^{(9)}
\longrightarrow\mathbb V_{\rm ell}(-1)
\longrightarrow0
\]

inside the absolute nine-master object. But
\([\Omega_{\rm phys}]\) belongs to the complete open/relative object and
has nonzero wall boundary. It is not thereby an element of the absolute
nine-master object, so it has no intrinsic \(\mathcal T_7\) coordinate.

Producing one requires a section or retraction of the localization sequence,
or equivalently a normalized decomposition

\[
[\Omega_{\rm phys}]
=
s([\rho_{\rm phys}])+j(m),
\qquad m\in\mathcal M_q^{(9)}.
\]

Different choices of \(s\) shift \(m\) by an absolute class.
Neither logarithmic tangency nor ordinary IBP quotient reduction specifies
\(s\).

## Classification

- existing carrier: the frozen Cayley--Menger surface and marked walls;
- canonical coefficient datum: the literal relative/open source class;
- missing secondary datum: a source-defined localization splitting;
- new carrier datum: none.

## Consequence for the coefficient architecture

The natural physical object at this stage is the relative Gauss--Manin
class itself, not a fitted absolute \(T_7\) projection. This favors the
architecture

\[
\boxed{
\text{shared carrier and localization calculus}
+
\text{sector-specific relative coefficient object}.
}
\]

## Next falsifier

Construct the retained rank-thirty-five presentations required by Entry 656
and verify that their prescribed unsplit source sum maps under Poincaré
residue and localization to Entry 648's \(\rho_{\rm phys}\). This tests the
complete pre-residue-to-relative-source chain without asking for an
unmotivated absolute splitting.

Only after that chain is constructed should one test whether a
source-normalized finite-part or physical-chain pairing canonically supplies
a section \(s\).

## Evidence

- Entries 150, 647--650, and 655--656;
- research artifact research/benincasa/source-bases-localization-fiber.json.
- epistemic event `ev-000000000260-99fdebec-97c8-4fe0-b6aa-500f4ef20aca`.

## Outcome contract

~~~json
{
  "claim": "A separate IBP primitive is required to choose a relative lift of the physical wall cocycle.",
  "status": "falsified",
  "source_defined_relative_lift": true,
  "source_lift": "[Omega_phys]",
  "boundary": "[rho_phys] in the complete five-pole localization complex",
  "complete_residue_quotient_rank": 20,
  "canonical_absolute_T7_projection": false,
  "missing_datum": "localization splitting or retraction",
  "next_experiment": "Construct the complete rank-35 pre-residue source map to the post-residue physical relative class."
}
~~~
