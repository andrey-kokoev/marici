---
authors:
  - marici.Nima
---
# Primal Bivariant Trace Retyping and the Double Object Gate

## Record

Date: 2026-08-15

Status: scoped typing correction and simplified formula objective. No
normalization-sheet kernel, endpoint connector, or parity value is claimed.

Entries 143--146 and 153 describe the remaining datum as an arrow

\[
\mathcal S_{\rm sh}^{\rm norm,reg}
\longrightarrow
\mathbb D_{\rm supp}
(\mathcal E_{\partial,Q}^{\rm BM,\check C})\otimes\chi_N.
\]

The notation conceals two independent construction gaps. The target-side
Borel--Moore Cech complex is constructed, but neither its supported Verdier
dual nor the reciprocal-regular normalization-sheet source is presently an
instantiated global chain object. The next experiment should therefore be
formulated using the constructed primal target.

## What is constructed

Entry 93 proves the finite normalization--conductor square

\[
0\longrightarrow B
\longrightarrow B_+\oplus B_-
\xrightarrow{\varepsilon_+-\varepsilon_-}C
\longrightarrow0
\]

and its polarity-odd first conormal symbol. It explicitly does not supply a
filtered scalar differential or a chain map realizing that symbol.
Consequently
\(\mathcal S_{\rm sh}^{\rm norm,reg}\) is currently a formula objective:
its closed-fibre, associated-grade, and coefficient shadows exist, but the
full reciprocal-regular source complex does not.

Entry 143 and its exact checker construct the primal target

\[
\mathcal E_{\partial,Q}^{\rm BM,\check C}
=
\bigoplus_{(S,H)\notin F_V}
R[X][u_a^{-1}:a\in S\setminus H]\,[S,H]
\]

with differential

\[
d[S,H]
=
\sum_{a\ {\rm addable}}
\epsilon(S,a){X_a\over u_a}[S+a,H]
+(-1)^{3-|S|}
\sum_{h\in H}(-1)^{{\rm pos}(h)}[S,H-h].
\]

Its endpoint filtration and seven-generator nonzero \(Q\) quotient are
strict and \(D_3\)-equivariant. What is not constructed is a point-set
supported dual of this nonperfect extended-Cech object. The canonical finite
semilinear dual of \(F_K/F_V\) does not provide that object: it reverses the
road arrow and omits the extended-Cech support terms.

## Corrected formula objective

The missing kernel should first be constructed as a primal bivariant trace:

\[
\boxed{
\operatorname{Tr}^{\rm biv}_{\rm sh,\partial,Q}:
\mathcal S_{\rm sh}^{\rm norm,reg}
\mathbin\otimes^L
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\longrightarrow
\mathbf1_{\chi_N}.
}
\]

This formulation uses the target that actually exists. An adjoint arrow into
\(\mathbb D_{\rm supp}(\mathcal E)\) may be recovered only after the relevant
supported closed structure or duality theorem has independently been built.
It must not be used to define that structure.

The trace is not sufficient by itself. It must come with two endpoint
comparison cells

\[
h_+, h_-:
\operatorname{Tr}^{\rm biv}_{\rm sh,\partial,Q}\big|_{\widetilde Z_\pm}
\Longrightarrow
\operatorname{ev}_{v_\pm},
\]

compatible with the closed-sheet label maps, the road inclusion, and the
based generic \(Q\) quotient. Their sheet difference defines the future
endpoint restriction

\[
r_{\partial,Q}(\beta_+,-\beta_-),
\]

and only its physical-reflection value may be reduced modulo two to obtain
\(p_{\partial,Q}(f_3)\).

## Earliest construction gate

Construct a single \(D_3\)-equivariant ringed support/nearby-cycle diagram
whose data include:

1. the two normalization branches and doubled conductor fibre;
2. the independent occurrence and multi-Rees filtrations;
3. reciprocal-regular branch packets and the original/Borel--Moore target;
4. the mixed block
   \(dH_\Sigma=q_\Sigma-\sum_i x_i\widetilde\xi_i\), retaining its nonzero
   generic \(Q\) leg;
5. both repeated-normal Tor grades;
6. the two endpoint restrictions and their comparison cells;
7. the separate polarity, determinant, and physical-normal lines.

The source complex, trace, and endpoint cells must be derived together from
this diagram. Tensoring the coefficient pullback with the local Tor packet is
not a substitute: after forgetting the framed support data, entry 133 proves
that the resulting ordinary common-ring Hom complex is contractible.

## Mandatory ablations

Before reading any physical shadow, the candidate must satisfy:

\[
\operatorname{Forget}_{Q,{\rm supp}}
(\operatorname{Tr}^{\rm biv}_{\rm sh,\partial,Q})\simeq0,
\]

and

\[
\operatorname{Forget}_{\rm Tate\ window}
(\operatorname{Tr}^{\rm biv}_{\rm sh,\partial,Q})\simeq0.
\]

It must also remain a chain map with all lower Cech terms retained. Only
after these tests pass may one evaluate, in order,

\[
p_{\partial,Q}(f_3),
\qquad
\partial_{\rm pol}(p_{\partial,Q}),
\qquad
K_{\rm alt},\ q_\Sigma,\ \eta_{3,{\rm mix}},\ [dX_{03}].
\]

## Falsification boundary

The local synthesis is falsified in this model if:

- no ringed support diagram simultaneously realizes the source and primal
  trace;
- the trace differential cannot retain the nonzero \(Q\) leg;
- the two endpoint cells are incompatible;
- the framed mapping fibre is zero;
- its intrinsic parity is odd;
- or a proposed class survives either mandatory forgetting ablation.

A rank-one result obtained after replacing the primal Cech target by its
finite dual, globally localizing the source, or imposing the desired residue
is inadmissible.

## Consequence for the active conjecture

The value

\[
p_{\partial,Q}\in H^1(D_3;\mathbb Z_{\rm or})
\]

remains undefined. The closed-conductor carrier has an even reflection
shadow, but it lies in \(F_B\) and therefore kills the distinguished \(Q\)
leg. It cannot decide the conjecture in entry 153.

The immediate objective is now smaller and better typed: construct the
primal trace and its endpoint cells without presupposing either a global
supported dual or a completed scalar source.

## Evidence

- entry 93: exact normalization--conductor square and associated-grade symbol;
- entry 113: canonical mixed boundary-crossing block with nonzero \(Q\) leg;
- entry 133: ordinary-derived contraction and mandatory framing ablation;
- entry 143: constructed endpoint/\(Q\) BM--Cech target and finite-dual
  limitation;
- entries 141, 144, and 153: polarity-first obstruction theory.

No new Rust checker is warranted for this typing correction. The proposed
trace and source do not yet define a finite matrix, and encoding their desired
components would manufacture the missing datum.

## Outcome contract

~~~json
{
  "claim": "The remaining normalization-sheet kernel must first be formulated as a primal bivariant trace S_sh^{norm,reg} tensor E_endpoint,Q^{BM,Cech} -> 1_chiN with two endpoint comparison cells. Neither S_sh^{norm,reg} nor D_supp(E_endpoint,Q^{BM,Cech}) is currently constructed as a global chain object, so the adjoint-arrow formula conceals two construction gaps and p_partial,Q remains undefined.",
  "status": "conditional",
  "assumptions": [
    "The exact scopes of entries 93, 113, 133, 141, 143, 144, and 153 are retained.",
    "The constructed primal BM-Cech target and its endpoint/Q filtration are held fixed.",
    "No supported-duality equivalence is assumed for the nonperfect extended-Cech object."
  ],
  "evidence_refs": [
    "src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md",
    "src/ledger/20260814-113 Marked-Exit Tate Detector and the Mixed Boundary-Crossing Block.md",
    "src/ledger/20260814-133 Ordinary-Derived Ablation and the Framed Off-Diagonal Objective.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-153 Polarity-First Correction to the Deutsch-Popperian Butterfly Conjecture.md"
  ],
  "factorization_test": {
    "primal_target": "constructed",
    "global_reciprocal_sheet_source": "unconstructed",
    "global_supported_dual_of_extended_Cech_target": "unconstructed",
    "primal_bivariant_trace": "formula objective",
    "endpoint_comparison_cells": "unconstructed",
    "closed_carrier_reflection_shadow": "even but Q-invisible",
    "endpoint_Q_parity": "undefined"
  },
  "counterevidence": [
    "Entry 93 supplies an associated-grade conormal symbol, not a filtered scalar chain complex.",
    "The finite semilinear dual reverses the road arrow and omits extended-Cech support data.",
    "The ordinary common-ring Hom shortcut is contractible.",
    "The closed-conductor carrier lies entirely in F_B and cannot retain q_Sigma."
  ],
  "next_experiment": "Construct one ringed D3-equivariant normalization-sheet/endpoint-Q correspondence and its primal trace, including both endpoint cells, the based Q leg, independent multi-Rees support, and both Tor grades; run the two forgetting ablations before computing reflection parity."
}
~~~
