# Crossing-Road Facewise Descent No-Go and the Derived Overlap Source Gate

Date: 2026-08-15  
Status: scoped falsification of crossing-road descent in the literal
entry-143 facewise/conewise refinement class. The enlarged extraordinary/cdh
category and its physical mapping fiber remain untyped. No graph admission is
claimed.

## The literal facewise category

Let \(\mathcal C_{\mathrm{face}}\) denote the finite class whose target
objects are the literal entry-143 face-indexed summands of
\(P=F_B/F_V\), together with their ordinary Cech localizations, and whose
maps preserve face labels and cone boundaries. It admits a simultaneous
\((u_a u_b)^{-1}\) target only when the two labelled rays lie in one
\(K_6\) face. It contains no extraordinary push-pull, cdh correspondence,
derived overlap source, or newly adjoined support grade.

For a cyclic adjacent pair in the dP6 hexagon, let \(r_a,r_b\) be the two
nonzero ray generators and let \(c_{ab}\) be the intervening cone generator,
with the declared cellular sign convention

\[
d c_{ab}=r_b-r_a.
\]

The two corresponding short diagonals cross. Therefore they have empty common
face support in \(K_6\), and \(P\) has no face grade for their pair. In
particular the formal double-Cech generator \(W_{ab}\) has no target object
in \(\mathcal C_{\mathrm{face}}\).

## Facewise descent no-go

There is no label-preserving cellular map in
\(\mathcal C_{\mathrm{face}}\) that sends both crossing ray generators
to their established nonzero target grades and extends across
\(c_{ab}\). Indeed, because no pair grade exists, any facewise candidate
must send \(c_{ab}\), equivalently \(W_{ab}\), to zero. But then

\[
d f(c_{ab})=0,\qquad
f(d c_{ab})=f(r_b)-f(r_a)\ne0,
\]

since the two ray images occupy distinct nonzero coordinates. Hence the chain
square fails. The exhaustive \(D_3\)/polarity-compatible dP6 ray census
shows this for both possible labelings and all six cyclic adjacent pairs.

This is an intrinsic no-go for \(\mathcal C_{\mathrm{face}}\), stronger
than saying that a map has not yet been constructed. It does **not** extend to
an extraordinary, logarithmic, cdh, or correspondence category. Such an
enlargement may contain a derived overlap carrier whose image is not required
to be a literal common face of \(P\).

The exact reused certificates are:

- `research/voevodsky/check_d03_dp6_common_refinement.rs`, SHA-256
  `c0838591bfb2e2f6ddf143951636e9d5346ab1cca6cfde43d50ab6f6123a9229`;
- `research/voevodsky/check_d03_weighted_adjacent_pair.rs`, SHA-256
  `5e6375625b0f51fbebcf7f46cf38c6b97b45f13f5a3c45da19a74bd117adf5c0`.

No new checker is introduced here.

## Completion and source dependency audit

Entry 113 supplies the semilinear mixed-block formula

\[
dH_\Sigma=q_\Sigma-
(x_1\widetilde\xi_1+x_3\widetilde\xi_3+x_5\widetilde\xi_5).
\]

It retains \(q_\Sigma\) as a generic chain generator. That fact alone
does not point its image in entry 143's quotient \(Q\). The naive positive
and reflected conductor pullbacks remain ordinary-contractible: after the
unimodular rebase of entries 133 and 162, they split into unit contractible
pairs. Before any manual basis identification they also lack the geometric
clutching that identifies the Morse occurrence packet with the dual-normal
packet. Thus neither copying the mixed block to both branches nor matching
their basis labels turns \(q_\Sigma\) into a based \(Q\) class.

This separates three statements:

1. the entry-113 differential is a valid source-side chain identity;
2. its absolute conductor pullback is contractible;
3. a nonzero relative class would require a geometrically typed enlargement
   in which the relevant contraction is inadmissible for independently stated
   support reasons.

The second statement does not prove a no-go for the third. Conversely, a
manual declaration that the two bases match is not the missing geometry.

## Exact missing enlarged structure

For each crossing pair \((a,b)\), the first new object must be a derived
overlap source \(W_{ab}\), with a support-typed extraordinary road map

\[
\alpha_{ab}^{!}:W_{ab}\longrightarrow i_{\mathrm{road}}^!E,
\]

whose two boundary restrictions recover the already fixed ray maps. This is
not a map to a nonexistent common face of \(P\). It must be accompanied by:

- attachment maps from both normalization branches and the conductor to
  \(W_{ab}\), including both Tor grades and the Morse/dual-normal clutching;
- a generic comparison retaining \(q_\Sigma\) and identifying it with a
  based nonzero class in the literal entry-143 \(Q\), rather than merely a
  source generator;
- the two endpoint connector cells comparing the branch counits with the
  road inclusion;
- pairwise crossing-road overlap homotopies, one triple/top filler, and the
  global reflection coherence.

These data define the candidate enlarged mapping diagram. They are not
implied by the scalar support lattice, by the abstract \(W_{ab}\) coefficient
closure, or by the local cap of entry 176.

## Why the local cap does not fix global parity

Entry 176 proves \(k=1\) and the primitive row \([2,1]\) inside its
explicitly labelled finite relative double-Rees square. Its local equation
has zero local parity and local Bockstein. But no constructed map identifies
that cap with the central correction of a global based endpoint/\(Q\)
mapping fiber. The missing crossing-road descent, endpoint connectors, and
triple/reflection coherences occur before that identification. Therefore

\[
p_{\partial,Q}\quad\text{and the global parity remain undefined}.
\]

Assigning them the local value zero would assume the very spatial comparison
whose construction is at issue.

## Falsifiers and anti-circularity

The \(\mathcal C_{\mathrm{face}}\) no-go is falsified by any literal
entry-143 support grade containing one of the certified crossing pairs, or by
a label-preserving cone image whose boundary equals the two nonzero ray
images. The completion audit is falsified by an already constructed,
provenance-carrying Morse/dual-normal clutching and branch/conductor map that
survives the required relative support restriction.

The following are not admissible repairs:

- zeroing a cone while retaining its two nonzero ray images;
- inserting a double-Cech target into \(P\) without changing the category;
- declaring \(q_\Sigma\) based merely because it is a source generator;
- deleting a contractible partner by hand;
- transporting entry 176's local \(k=1\) directly to global parity.

None of these controls rules out a genuinely constructed extraordinary/cdh
correspondence.

## Provenance

- entry 113: mixed source differential and retained generic generator;
- entries 133 and 162: absolute contraction and conductor-pullback no-go;
- entry 143: literal face-indexed endpoint/\(Q\) target;
- entry 165: exhaustive dP6 and weighted adjacent-pair support failures;
- entries 174 and 176: local two-edge coefficient trace and relative cap;
- entry 177: generic-incidence coefficient obstruction after the numbering
  hygiene repair.

## Next experiment

Construct one crossing-pair derived overlap object \(W_{03,25}\) from the
normalization/conductor correspondence, including its two branch attachment
maps and both Tor grades. Define
\(\alpha_{03,25}^{!}:W_{03,25}\to i_{\mathrm{road}}^!E\), verify
its two ray-boundary restrictions and its generic based-\(Q\) comparison,
then construct the shared endpoint cells. Only after this one overlap closes
should it be rotated and tested for triple and reflection coherence.

## Outcome contract

~~~json
{
  "claim": "In the literal entry-143 facewise/conewise refinement class C_face, every D3/polarity-compatible adjacent dP6 cone maps to a crossing pair of nonzero short-ray grades with no common K6 face. The double-Cech cone generator therefore has no target, while sending it to zero violates its two-ray boundary. Separately, the naive entry-113 branchwise conductor pullback is ordinary-contractible and does not supply Morse/dual-normal clutching or a based Q image of q_Sigma.",
  "status": "falsified",
  "scope": "scoped no-go for literal face-preserving crossing-road descent in C_face; enlarged extraordinary, logarithmic, cdh, and correspondence categories remain untyped and are not falsified",
  "assumptions": [
    "Entry-143 literal K6 face labels and its P/Q filtration are fixed.",
    "C_face permits only ordinary facewise/conewise maps and existing Cech grades.",
    "The two crossing ray images remain their established distinct nonzero coordinates.",
    "No derived overlap support object is silently adjoined."
  ],
  "factorization": {
    "equivariant_ray_labelings": 2,
    "crossing_adjacent_pairs": 6,
    "common_K6_face": "none for every crossing pair",
    "double_Cech_target_in_C_face": "absent",
    "zero_cone_chain_map": "fails because the two-ray boundary is nonzero",
    "extraordinary_or_cdh_no_go": "not claimed",
    "entry113_qSigma": "retained source chain generator only",
    "qSigma_based_in_literal_Q": "unconstructed",
    "naive_branch_conductor_pullback": "ordinary-contractible",
    "Morse_dual_normal_clutching": "absent before manual basis matching",
    "required_map": "W_ab -> i_road^! E",
    "branch_conductor_attachments": "unconstructed",
    "endpoint_connector_cells": "unconstructed",
    "triple_reflection_coherence": "unconstructed",
    "entry176_local_k": 1,
    "physical_p_partial_Q": "undefined",
    "global_parity": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_dp6_common_refinement.rs",
    "research/voevodsky/check_d03_weighted_adjacent_pair.rs",
    "src/ledger/20260814-113 Marked-Exit Tate Detector and the Mixed Boundary-Crossing Block.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-162 Cartier-Filtered Primal Bridge and the Absolute Contraction No-Go.md",
    "src/ledger/20260815-165 dP6 Common Refinement and the Log-Boundary Gysin Gate.md",
    "src/ledger/20260815-174 Two-Edge Bivariant Trace and the Unlocalized Two-Flip Alignment Gate.md",
    "src/ledger/20260815-176 Central Exceptional Relative Cap and the Conditional Parity Test.md",
    "src/ledger/20260815-177 Generic-Incidence Pairing No-Go and the Extraordinary Lower-Term Gate.md"
  ],
  "checker_sha256": {
    "dp6_common_refinement": "c0838591bfb2e2f6ddf143951636e9d5346ab1cca6cfde43d50ab6f6123a9229",
    "weighted_adjacent_pair": "5e6375625b0f51fbebcf7f46cf38c6b97b45f13f5a3c45da19a74bd117adf5c0"
  },
  "conditional_or_untyped": {
    "derived_overlap_source": "unconstructed",
    "extraordinary_road_map": "unconstructed",
    "generic_based_Q_comparison": "unconstructed",
    "global_mapping_fiber": "uninstantiated",
    "global_parity": "undefined"
  },
  "counterevidence": [
    "The abstract W_ab coefficient closure exists, but it has no ordinary facewise target in P.",
    "The full logarithmic boundary has a common dP6 refinement, so the facewise no-go cannot be promoted to a global geometric no-go.",
    "The source differential retains q_Sigma, but absolute contraction prevents treating that generator as a global trace class.",
    "Entry 176 proves only a local relative cap and does not supply crossing-road or endpoint coherence."
  ],
  "next_experiment": "Construct one derived crossing-pair overlap source W_03,25 with both branch/conductor attachments and Tor grades, map it extraordinarily to i_road^!E, verify both ray boundaries plus a based generic-Q comparison and endpoint cells, then rotate and test triple/reflection coherence."
}
~~~
