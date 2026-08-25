# Correction and completion audit for the completed physical engine

## Superseded claims

Three claims from the earlier coordinate-Green phase are withdrawn.

1. `D_z^2(S log|z-xi|^2)` was treated as the invariant point kernel. The
   invariant representative is `D_z^2(S log S)`.
2. The ratio `xi^2/z^2` was called a physical parity cocycle. It is an artifact
   of the coordinate-dependent representative. The invariant kernel has exact
   spin-two gluing with transition ratio one.
3. Ordinary complete contour periods were said to reconstruct all local
   puncture jets. They reconstruct only the de Rham cohomology/residue packet;
   higher poles and delta derivatives require local test-function ports.

The old geometric tail, depth-two onset, quartic cutoff witness, and any
downstream summary using them are likewise superseded. The corrected source
has depth-four onset, negative-binomial coefficients, a quadratic-over-cubic
tail, and a positive sextic witness.

## Requirement matrix

| objective requirement | authoritative packet | checker |
|---|---|---|
| completed source module, topology, distributions | `completed-physical-source-category.md` | `completed_physical_source_category_checks.py` |
| invariant constructor | `physical-puncture-constructor.md` | `physical_puncture_constructor_checks.py` |
| two-chart module | `completed-two-chart-parity-module.md` | `completed_two_chart_parity_module_checks.py` |
| parity/helicity | `completed-parity-helicity-representation.md` | `completed_parity_helicity_representation_checks.py` |
| grade-three operator | `completed-grade-three-source-readout.md` | `completed_grade_three_source_readout_checks.py` |
| coherent cutoffs | `physical-laurent-completion-and-cutoffs.md` | `physical_laurent_completion_cutoff_checks.py` |
| local distribution target | `completed-local-distribution-target.md` | `completed_local_distribution_target_checks.py` |
| Green, contours, zero modes, periods | `completed-local-to-contour-transform.md` | `completed_local_to_contour_transform_checks.py` |
| gauge, conservation, antipodal matching | `completed-gauge-conservation-antipodal-quotient.md` | `completed_gauge_conservation_antipodal_quotient_checks.py` |
| arbitrary distinct-puncture kernel | `completed-distinct-puncture-kernel-classification.md` | `completed_distinct_puncture_kernel_checks.py` |
| collision jets and moments | `completed-collision-strata-classification.md` | `completed_collision_strata_checks.py` |
| towers, E1, E2 analogues | `completed-tower-exception-analogue-classification.md` | `completed_tower_exception_analogue_checks.py` |
| hostile falsifiers | `completed-physical-engine-hostile-falsifiers.md` | `completed_physical_engine_hostile_falsifiers.py` |
| diagram and master theorem | `completed-physical-engine-diagram.md`, `completed-physical-engine-master-theorem.md` | `completed_physical_engine_master_checks.py` |

## Completion criteria

Completion requires all constituent checkers to exit successfully, every JSON
result to declare `passed=total`, all named packets to exist, canonical packets
to contain no control bytes, and the forbidden superseded formulas to be absent
from the canonical completed theorem family. The master checker enforces these
requirements rather than trusting prior result files.

## Ownership and publication

All state-changing work is confined to `research/strominger`. Unrelated dirty
files are untouched. This audit does not authorize a commit, push, ledger
publication, or site mutation.
