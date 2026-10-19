# Weighted A3 net: uncaptured prior research — 2026-10-13

## Review scope

Compared the 11-node `research/conjecture_net/contracts/weighted-a3-descent-work-net.v1.json` and its handoff against relevant existing Nima notes and source constructors. This is a bounded evidence-discovery review, not a scientific replay or an update to the Nima-owned contract. Scripts were read, not executed. Missing receipts do not count as fresh verified completions.

The net correctly leaves weighted canonical descent open. Several useful predecessor constructions and controls are absent from its explicit artifact/evidence list. These can narrow the next tasks without claiming their canonical-form acceptance gates are satisfied.

## 1. Untransported generalized-R evaluation already exists

**Relevant node:** `untransported-simple-forms`.

Unlisted predecessors:

- `research/nima/nnmhv_coherence_paths.py`
- `research/nima/check_nnmhv_boundary_transport.py`
- `research/nima/dual_r_invariant.py`
- `research/nima/check_nnmhv_kernel_wall_tail_boundary.py`

The history compiler records the upper replacement exactly when b2=b1. For supported simple roots, terminal xi follows (n,b1,2), the lower endpoint is external label 2, and the updated upper follows (n,2,b1).

The wall/tail checker already constructs BOTH scalar inputs to the desired difference: it calls the same generalized-R evaluator with transported upper endpoint and with `upper0=lam[b2].T*eps`. Thus removal of the upper update is not an unspecified numerical operation. The evaluator returns a sparse degree-four eta polynomial as well as its prefactor and eta coefficient row, so the untransported *superfunction candidate* can be retained before component extraction.

**What belongs in the net:** a sourced endpoint-switch/superfunction precursor, referenced by the open simple-form node; distinguish this from a completed canonical representative.

**Still missing:** proof/admission that the untransported product is an appropriate canonical-form object, its positroid/positive-chart realization, orientation and localization. Removing a mandated boundary replacement from a sourced history is an auxiliary candidate operation, not automatically a term of the sourced BCFW chain. Do not promote a sparse superfunction to a positive-cell canonical form without those checks.

**Useful next conjecture:** the three explicit untransported products admit canonical representatives compatible with the transported charts. Test that proposition on the existing source-defined products, rather than inventing products from K0 values.

## 2. Component selector and normalization are partially specified already

**Relevant nodes:** `composite-normalization-definition`, `untransported-simple-forms`, `negative-simple-difference-forms`.

Unlisted predecessors:

- `research/nima/nnmhv-component-23-support-theorem.md`
- `research/nima/check_nnmhv_kernel_wall_tail_boundary.py`
- `research/nima/check_eight_point_history_positroid_matching.py`
- `research/nima/dual_r_invariant.py`

The support theorem specifies extraction of product_A eta_2^A eta_3^A and the normalized history contribution

    prefactor_outer * prefactor_inner
      * (q_outer[2]*q_inner[3]-q_outer[3]*q_inner[2])^4 / <23>^4.

Only left-nested histories with a1=2,a2=3 survive generically. The matcher compares all 70 one-SU(4) degree-four coefficients and bosonic prefactors for transported histories; its code checks projective full-form ratio 1 at its declared exact kinematic fixture, with a shift parameter for additional controls.

**What belongs in the net:** the existing selector, normalization and full-superfunction matching protocol as typed precursor evidence. The component specification need not start from an empty interface.

**Still missing:** source-normalized extraction/pushforward on differential forms and seven-form residues, and its compatibility with the 20 physical divisor sectors. Fixture coefficient matching is not a universal symbolic equality or a residue-map theorem.

## 3. Scalar nine-facet augmentation is a distinct completed precursor

**Relevant node:** `nine-facet-typing-audit`; contextual prerequisite to final assembly.

Unlisted predecessor: `research/nima/checkers/check_n8_physical_facet_cochain.py`.

The existing code assigns positive-root facets K0 and negative-simple facets B_ii=K_ii-K0_ii, computes top-boundary incidence signs, and checks that the oriented cochain evaluated on the top boundary equals the selected physical scalar. It also checks K=K0+B.

**What belongs in the net:** explicit scalar-augmentation evidence, separate from the absent form map. This is the algebraic target the new form construction should reproduce.

**Still missing:** restriction/residue maps; scalar augmentation cannot resolve normalized nine-facet form preimages or weighted cancellation. The receipt `n8-physical-facet-cochain.json` is absent here; the checker is available but was not rerun.

## 4. Full A3 combinatorial stratum index is available

**Relevant node:** `weighted-codimension-two-cancellation`.

Unlisted predecessors:

- `research/nima/arbitrary-m-codimension-two-counting-theorem.md`
- `research/nima/checkers/check_arbitrary_m_codim2_facet_incidence.py`
- `research/nima/checkers/check_arbitrary_n_boundary_cluster_completion.py`

The A3 auxiliary suite contains 21 compatible pairs: PP=10, PN=8, NN=3; parent types are 12 pentagon-square and 9 pentagon-pentagon. The checker enumerates the pairs and states a per-stratum contract: parent identifiers, source preimages, two oriented residues, common representative or nonincidence proof, transition/Jacobian, and coefficientwise disposition.

The history compiler also supplies the root labels and identifies upper updates exactly with simple roots; the all-n boundary-completion checker tests that labeling through n=30. This is a labeling/support result, not arbitrary-n form descent.

**What belongs in the net:** the explicit auxiliary indexing/coverage specification. Use it to track which combinatorial pairs acquire a physical lift, which do not, and which remain undefined.

**Still missing:** actual physical shared-stratum incidence after the normalized map. The 21 auxiliary pairs must not be substituted for physical incidence, especially given the net's rejected selected-incidence inference. Counts do not prove physical coverage.

## 5. Selected seven-pair orientation control is uncaptured

**Relevant nodes:** `selected-chart-census`, `common-oriented-simple-charts`, `weighted-codimension-two-cancellation`.

Unlisted predecessor: `research/nima/checkers/check_n8_shared_boundary_orientation_cancellation.py`.

The existing code reads our census and checks two incidences and opposite deletion-parity signs for each of seven shared selected boundary keys. It explicitly retains the common-normalization/transition gate and notes that unmatched selected boundaries may meet the other fourteen histories or the exterior.

**What belongs in the net:** an intermediate selected-incidence orientation control, not new full-chain cancellation or a weighted theorem. It can supply regression expectations for future chart comparisons.

**Still missing:** common-chart Jacobians and coefficient normalization for these paired selected residues and for transported/untransported pairs. Its receipt is absent here.

## 6. Boundary-update interference is an exact scalar hostile candidate

**Relevant nodes:** simple-form/difference construction and normalization controls.

Unlisted predecessors:

- `research/nima/check_nnmhv_boundary_update_interference_minor.py`
- `research/nima/check_nnmhv_simple_root_interference_control.py`

At the declared rational n=8 fixture, the code tests that the upper update flips a particular 2x2 kernel minor from positive to negative. Its eight update-toggle configurations isolate alpha_2 as the control for the unique negative minor.

**What belongs in the net:** a proposed source-switch regression/hostile. It can detect accidentally using transported K in place of K0 or erasing the subtraction distinction.

**Still missing:** fresh receipts and canonical-form interpretation. Neither total positivity nor its failure is a proof/refutation of canonical residue cancellation. This control should not gate descent as a positive geometric assumption.

## 7. Flat cluster weights are not the form comparison

**Relevant node:** `composite-normalization-definition`, as an excluded shortcut.

Unlisted predecessors:

- `research/nima/a3-physical-weight-resolution-gate.md`
- `research/nima/checkers/check_n8_boundary_completed_cluster_transport.py`
- `research/nima/checkers/check_a3_weighted_local_system_code.py`
- `research/nima/coherent-resolution-20-turn-completion.md`

The rational vertex-product transport is a diagonal gauge twist with telescoping square/pentagon holonomy and zero augmented homology. IMPORTANT: the completed cluster-transport code uses transported K for its positive coordinates, whereas the physical facet cochain uses K0. These are different constructions even though both use B for negative-simple completion.

**What belongs in the net:** a named rejected shortcut: flat mutation transport does not supply the K0/B canonical comparison or determine residue coefficients. Preserve the K-versus-K0 distinction in any imported conventions.

The cosmological example `research/nima/residue-incidence-normalization-dpc.md` independently illustrates a rescaling ambiguity of incidence-only normalization. It is an analogy/control rationale, not a prerequisite or proof about this A3 source.

## Availability and stale scope warnings

During this review, the following additional cited receipts were absent:

- `research/nima/results/nnmhv-kernel-wall-tail-boundary.json`
- `research/nima/results/nnmhv-simple-root-interference-control.json`
- `research/nima/results/nnmhv-component-23-support-theorem.json`
- `research/nima/results/nnmhv-boundary-transport.json`
- `research/nima/results/n8-physical-facet-cochain.json`
- `research/nima/results/n8-shared-boundary-orientation-cancellation.json`
- `research/nima/results/arbitrary-m-codim2-facet-incidence.json`
- `research/nima/results/arbitrary-n-boundary-cluster-completion.json`

This extends the handoff's seven-file operational inventory; it does not negate the historical results or license replacement data. Source code and notes can support specification now; coefficient replay needs recovered/verified inputs. No source-owner producer was executed here.

`coherent-construction-law.md` contains a useful conditional pushforward/residue assembly law and selected-component projection, but its broad historical seven-point certification statement must not be imported without the later `nnmhv-selector-transfer-typing-audit.md` and `seven-point-positroid-compiler-has-three-collapsed-image-cells.md` corrections. That seven-point branch is not needed to close this fixed-n=8 net.

## Recommended integration

Keep the existing scientific frontier open. Add the above sources as precursor artifacts and explicit controls, not seven new blockers or unrelated research tasks.

Priority:

1. Attach the endpoint-switch evaluator and explicit component selector to the two ready frontier nodes.
2. Add scalar augmentation as the target regression and preserve K versus K0.
3. Attach the auxiliary 21-stratum index with physical-nonincidence/undefined dispositions.
4. Include selected orientation and update-toggle controls in successor comparison receipts.
5. Extend the operational recovery inventory and pin source snapshots before replay.

The most consequential discovery is that the source-level untransported *superfunction construction* and scalar selector already exist. The genuinely absent step is their admitted canonical-form/chart realization and normalized boundary comparison—not definition of an endpoint switch from scratch.
