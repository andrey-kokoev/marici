# Polarity flip transport is unspecified in the audited source

Recorded: 2026-10-22 by `marici.Strominger` from the operator-supplied Shoshin audit. Audited revision: `cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c`. This note preserves that bounded source inspection; it does not claim an independent rerun of the pinned revision or an exhaustive audit of later revisions.

## Question and claim boundary

Does the source define polarity-fiber transport across quadrangulation flips whose double-cover class can be compared with the orientation cover of the quadrangulation surface? A marked two-point torsor, polygon-symmetry covariance, and an independently constructed orientation cocycle do not by themselves supply that transport.

SCC obligation: upstream source realization of a two-point transport, before readout descent or cover-class comparison. The missing operation stops this branch; no corrective cocycle or new attachment is inferred.

## Inspected candidates

All links below are pinned to the audited revision.

| Source | Actual operation | Why it does not establish polarity flip transport |
| --- | --- | --- |
| [`orientation_local_system_audit()`](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/nima/check_surface_rees_carrier.py#L498-L553) | Constructs cellular cocycles and selects one outside the coboundary span. | It selects the nonzero orientation class; its docstring excludes proving that QTDS polarity realizes it. |
| [`edge_transport()`](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/nima/check_scalar_edge_transport.py#L694-L759) | Additive rational chain indexed by diagonal marks, connecting matched minus/plus occurrences. | It is not a permutation of the polarity fiber across a flip. |
| [`orientation_voltage()`](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/nima/check_scalar_edge_transport.py#L860-L907) | Independently selects a nonzero cellular cocycle. | Selecting the desired class does not identify a source polarity operation. |
| [Ledger 87 covariance audit](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/nima/check_eight_point_pc_homotopy.rs#L1978-L2037) | `swaps_sheet = (amount % 2 == 1) ^ reflect`. | Inputs are polygon rotations/reflections, not quadrangulation flips. |
| [`primitive_quotient_voltage()`](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/nima/check_global_halfline_atlas.rs#L867-L899) | Normal-sign voltage from contraction positions in ordered normal pairs. | No polarity state is transported. Its interpretation as coefficient transition units requires a common primitive quotient. |

The last candidate computes, for the shared diagonal \(D=Q\cap Q'\),

\[
v(Q,Q')=\operatorname{pos}_{Q}(D)+\operatorname{pos}_{Q'}(D)\pmod2.
\]

Its scope is stated in [Ledger 88's conditional theorem](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/src/ledger/20260814-88%20Primitive%20Half-Line%20Cospans%20and%20the%20Crosscap-Counit%20Gap.md#L539-L581). [Ledger 406](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/src/ledger/20260817-406%20The%20Primitive%20Cousin%20Normalization%20Selects%20the%20Nonzero%20Mobius%20Atlas%20Class.md) selects an additive Mobius class but does not construct transition automorphisms or multiplicative holonomy. Neither result supplies the missing polarity bijections.

## Disposition and reopening condition

No source-defined table \(\epsilon_{\mathrm{pol}}(e)\) was extracted. Its eight triangle-boundary parities, four square-boundary parities, octagonal-boundary parity and five-flip crosscap parity are **undefined**, not zero and not failed tests. Successful checks for orientation or normal-sign cocycles cannot be transferred to polarity without an identification of their operations.

Reopen only when the source supplies, for every flip \(e:Q\to Q'\),

\[
T_e:\mathrm{Pol}(Q)\longrightarrow\mathrm{Pol}(Q'),\qquad
T_e\tau=\tau T_e,\qquad T_{\bar e}=T_e^{-1},
\]

or an explicit theorem identifying such transport with an existing candidate. Then local labels express \(T_e(\sigma)=\sigma+\epsilon_{\mathrm{pol}}(e)\). Relabeling by \(g(Q)\) changes edge bits by

\[
\epsilon'_{\mathrm{pol}}(e)=\epsilon_{\mathrm{pol}}(e)+g(Q)+g(Q'),
\]

so closed-loop parity is unchanged. The missing datum is transport, not a label choice.

The acceptance test is to verify even parity around every face, then evaluate the five-flip crosscap loop specified in Ledger 22. Once the face equations hold, crosscap parity one identifies the orientation cover; parity zero gives the trivial cover. Nonzero face parity prevents extension of the proposed graph cover over the surface. No full coefficient/residue realization is required merely to define and test these bijections.

## Relation to the recorded seam theorem

The [shared-seam observability theorem](shared-seam-observability.md), summarized in ledger entry 4330, concerns a specified local linear operator pair and an explicit reference involution. It does not depend on this global cover identification and is unchanged. This audit records provenance for an already acknowledged gap, not a new negative theorem; no additional public ledger entry is allocated.
