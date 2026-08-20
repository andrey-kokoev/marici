---
authors:
  - marici.Nima
date: 2026-08-15
---
# Local Gysin Sufficiency No-Go and the Global Mapping-Fiber Definition Gate

## Record

Date: 2026-08-15

Status: proved scoped sufficiency no-go; global existence untyped.

This is a typing and provenance theorem. It corrects the claim that a new
local occurrence-Gysin axiom would by itself unlock the global construction.
It does not claim global nonexistence.

## The local Gysin package is already proved

The tempting claim is that \(\mathrm{GYS}_{\rm occ}\) is a new missing axiom.
That claim is false at its stated local scope. Entries 129--131 already
construct, locally, the labelled principal ideal and its dual evaluation, the
shifted Cartier \(\operatorname{Ext}^1\) class, the full Koszul--Cech lower
terms, both Tor grades, the graph Bockstein, the endpoint restrictions, and
scoped \(D03\) purity, together with its \(D_3\) rotations.

In particular, the proved local operation has the shifted form

\[
\operatorname{Tr}_i^!
=\operatorname{ev}_{I_i}\circ(g_i^!\otimes\mathrm{id}),
\qquad
g_i^!\in\operatorname{Ext}^1_R(R/I_i,I_i),
\]

and its edge realization is constrained by the Bockstein-compatible purity
maps \(\operatorname{pur}_i\). These are genuine local Cartier/purity data,
not placeholders for a further local axiom. Their proved scope is essential:
they are restrictions in local diagrams, not a normalization-provenanced
global sheet object or a global generic component.

The local Cartier class has cohomological degree \(+1\). In the required
global closed trace, that degree is absorbed by its coorientation shift
\([-1]\), so the primal mixed-variance trace has total degree zero. This
degree accounting does not construct either the global source or the trace.

## Established target data and source shadows

Entry 143 establishes the global target-side localization data

\[
F_B/F_V \longrightarrow E:=F_K/F_V \longrightarrow Q:=F_K/F_B,
\]

with its full Borel--Moore--Cech differential, fixed \(Q\)-generator types,
and nonzero generic class \(q_\Sigma\). The target and its quotient are not
missing objects.

There are also established source shadows:

- the normalization coefficient row;
- the formal branch mixed/multi-Rees totals; and
- the absolute mixed identity
  \[
  dH_\Sigma=q_\Sigma-\sum_i x_i\widetilde\xi_i.
  \]

The coefficient shadow is the established row

\[
0\longrightarrow B\longrightarrow B_+\oplus B_-
\longrightarrow C\longrightarrow0.
\]

These shadows record necessary coefficients, filtrations, and local
differentials. They do not yet form a normalization-provenanced global source
\(\mathcal S_{\rm sh}^{\rm norm,reg}\). In particular, no established source
object carries both the branch provenance and a branch-to-\(Q\) generic
component retaining the nonzero \(q_\Sigma\).

## Minimal ambient category

Let \(\mathsf{Diag}_{\rm est}\) be the minimal non-circular ambient category
of finite \(D_3\)-equivariant dg diagrams over the unlocalized occurrence
ring. Its objects contain only the following established data:

1. the normalization triangle;
2. the formal branch and independent multi-Rees diagrams;
3. the target localization triangle;
4. the local Cartier/purity diagrams; and
5. the endpoint subdiagrams and orientation lines.

Its morphisms preserve localization triangles, support and Rees filtrations,
and reciprocal-regular/Borel--Moore variance. Its homotopies are
\(D_3\)-equivariant and filtration-strict, vanish on the endpoints and based
\(\operatorname{gr}_Q\), and commute with the Bockstein and purity maps.

No relation in \(\mathsf{Diag}_{\rm est}\) adjoins the primal trace, its
conditional \(\alpha_{\rm sh}^{!,\check C}\) adjoint, \(\tau_Q\),
\(K_{\rm alt}\), a residue, or a parity value. Those symbols may occur as
future tests or names for missing data; they are not defining relations in
this category.

## The scoped sufficiency no-go

**Theorem.** Adding the proved local principal/Gysin arrows to
\(\mathsf{Diag}_{\rm est}\) does not instantiate

\[
R\!\operatorname{Hom}^{\rm fr}_{D_3}
\left(
  \mathcal S_{\rm sh}^{\rm norm,reg}\otimes^L E,
  \mathbf 1_{\chi_N}
\right)
\]

or its endpoint/\(Q\) homotopy fiber.

**Proof.** The displayed derived Hom requires an actual global source as its
first input. The normalization coefficient row and the formal branch/multi-Rees
totals supply shadows of such an input, but no object
\(\mathcal S_{\rm sh}^{\rm norm,reg}\) with normalization provenance is an
object of the established data. Therefore the tensor factor, and hence the
derived Hom, is not instantiated.

Even if one temporarily names a formal source, the required closed
degree-zero primal mixed-variance trace is absent. The local arrows prove the
Cartier restrictions but do not supply a trace/correspondence with the
required based generic \(Q\) comparison retaining \(q_\Sigma\ne0\). The two
endpoint connector cells are absent as well, so no endpoint/\(Q\) pointing
data are available from which a homotopy fiber could be formed.

Finally, every existing local endpoint-and-generic-relative gallery has
killed its \(q_i\). Such a gallery cannot determine a nonzero global
\(q_\Sigma\) component in \(Q\): the generic class that would have to be
tracked has already been quotiented away. Thus local principal/Gysin data are
necessary compatibility data, but are not sufficient source, generic, or
endpoint data. This proves non-instantiation in the stated ambient category;
it does not prove that a global construction cannot later exist. \(\square\)

## Earliest missing global construction

The earliest missing global construction has two ordered parts:

1. a normalization-provenanced source
   \(\mathcal S_{\rm sh}^{\rm norm,reg}\); and
2. a closed degree-zero primal mixed-variance trace
   \[
   \operatorname{Tr}^{\rm biv}_{\rm sh,\partial,Q}:
   \mathcal S_{\rm sh}^{\rm norm,reg}
   \mathbin\otimes^L
   \mathcal E_{\partial,Q}^{\rm BM,\check C}
   \longrightarrow
   \mathbf1_{\chi_N},
   \]
   together with two endpoint connector cells and a based nonzero \(Q\)
   comparison.

The endpoint connector cells have the required restriction form

\[
h_+,h_-:
\left.\operatorname{Tr}^{\rm biv}_{\rm sh,\partial,Q}\right|_{
\widetilde Z_\pm}
\Longrightarrow
\operatorname{ev}_{v_\pm}.
\]

The local \(\operatorname{Ext}^1\) degree \(+1\) of the Cartier operation is
absorbed by its coorientation \([-1]\) in this global degree-zero trace. Its
local restrictions must recover the proved \(g_i^!\) and
\(\operatorname{pur}_i\), including the \(D03\) scope and its \(D_3\)
rotations. The two endpoint connector cells compare the endpoint restrictions
of the trace with the established endpoint evaluations. The based generic
\(Q\) comparison must retain the fixed nonzero \(q_\Sigma\) class. These are
required compatibility conditions of the primal trace/correspondence, not
a freely assigned map.

Only after an independently proved supported closed-duality theorem for the
nonperfect extended-Cech target may one introduce
\(\alpha_{\rm sh}^{!,\check C}\) as the adjoint of this primal trace. Until
then, \(\alpha_{\rm sh}^{!,\check C}\) is conditional shorthand, not the
first constructed arrow or a presently typable morphism of triangles.

## Conditional definition of the mapping fiber

Only after the source, the primal trace restriction diagram, both endpoint
connector cells, and the based nonzero \(Q\) comparison exist may their
induced \((\tau_+,\tau_-,\tau_Q)\) point the definition

\[
\mathcal M_{\partial,Q}=
\operatorname{hofib}_{(\tau_+,\tau_-,\tau_Q)}
\left[
R\!\operatorname{Hom}^{\rm fr}_{D_3}
\left(
  \mathcal S_{\rm sh}^{\rm norm,reg}\otimes^L
  \mathcal E_{\partial,Q}^{\rm BM,\check C},
  \mathbf 1_{\chi_N}
\right)
\longrightarrow B_+\oplus B_-\oplus B_Q
\right].
\]

At present this mapping fiber is not instantiated. Parity remains undefined
now.

## Mandatory counterevidence and ablations

- The ordinary zero-section test gives \(0=\pm1\) on the conductor
  (entry 156).
- Relabeling a principal line alone leaves the nonzero operation in
  \(\operatorname{Ext}^1\), rather than producing an ordinary degree-zero
  global trace (entry 157).
- Every local endpoint-and-generic-relative gallery killed \(q_i\), so its
  relative quotient cannot determine the nonzero global \(q_\Sigma\) leg.
- A quotient that makes \(q_\Sigma\) bound does so by deleting the special
  galleries that would have carried the required comparison.
- Freely adjoining the primal trace, its conditional
  \(\alpha_{\rm sh}^{!,\check C}\) adjoint, or \(\tau_Q\) would encode the
  desired answer instead of testing whether the normalization geometry
  supplies it.

## Consequence and evidence

The correct status vocabulary is: **proved scoped sufficiency no-go; global
existence untyped**. This is a provenance boundary, not a claim of global
nonexistence. The next construction must produce the source and primal trace,
with the nonzero generic comparison and endpoint cells, together.

Evidence:

- entry 113: mixed boundary-crossing block and the nonzero \(q_\Sigma\) leg;
- entries 129--131: local principal-line, Koszul--Cech, Tor, Bockstein,
  endpoint, and scoped Cartier-purity package;
- entry 143: fixed endpoint/\(Q\) target and full BM--Cech realization;
- entry 154: global source and endpoint-cell typing gate;
- entries 156--157: zero-section and relabeling ablations.

## Outcome contract

~~~json
{
  "claim": "proved scoped sufficiency no-go; global existence untyped",
  "status": "proved",
  "assumptions": [
    "The occurrence ring remains unlocalized.",
    "Only established normalization, branch, target, local Cartier/purity, endpoint, and orientation data occur in the ambient category.",
    "Morphisms and homotopies preserve the stated localization, filtration, variance, Bockstein, purity, endpoint, and based gr_Q conditions.",
    "No primal trace, conditional alpha_sh adjoint, tau_Q, K_alt, residue, or parity relation is freely adjoined."
  ],
  "evidence_refs": [
    "src/ledger/20260814-113 Marked-Exit Tate Detector and the Mixed Boundary-Crossing Block.md",
    "src/ledger/20260814-129 Cox Principal-Line Trace and the Extraordinary Cousin Boundary.md",
    "src/ledger/20260814-130 Simultaneous D03 Endpoint Cousin Map and the PC Purity Boundary.md",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-154 Primal Bivariant Trace Retyping and the Double Object Gate.md",
    "src/ledger/20260815-156 Zero-Section Trace No-Go and the Principal-Dual-Line Gate.md",
    "src/ledger/20260815-157 Principal-Line Relabeling No-Go and the Ext-One Globalization Gate.md"
  ],
  "factorization_test": {
    "local_Gysin": "proved",
    "global_source": "unconstructed",
    "primal_trace": "unconstructed",
    "supported_duality": "unconstructed",
    "alpha_adjoint": "conditional shorthand",
    "based_Q_comparison": "unconstructed",
    "endpoint_connector_cells": "unconstructed",
    "mapping_fiber": "not_instantiated",
    "parity": "undefined"
  },
  "counterevidence": [
    "The ordinary zero-section specialization gives 0=+/-1 on the conductor.",
    "Principal-line relabeling leaves the nonzero operation in Ext1.",
    "Every local endpoint-and-generic-relative gallery killed q_i.",
    "A quotient making q_Sigma bound deletes the required special galleries.",
    "Freely adjoining the primal trace, alpha_sh adjoint, or tau_Q encodes the desired answer."
  ],
  "next_experiment": "Construct the normalization-provenanced source and closed degree-zero primal trace, including the endpoint connector cells and based nonzero Q comparison; then independently prove supported closed duality and test whether an adjoint alpha_sh exists before instantiating the mapping fiber."
}
~~~
