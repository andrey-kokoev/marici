# Operational unit-circle flow: proved

`agda/TickConstructedUnitCircleFlow.agda` constructs `operational-unit-circle-flow : OperationalUnitCircleFlow`.

The record carries unit norm and full metric regularity for the **same fixed** `TickCompletionPhase.phase`, at every completion-valued scale and time. Regularity includes metric continuity and the exact all-increment derivative `(-i*p)*phase p`. There is no existential choice of a different curve, rational-input restriction, standard-real interpretation assumption, or new postulate.

Direct record field types caused cached elaboration timeouts while traversing the operational schedules. Opaque `UnitNormLaw` and `RegularityLaw` presentations avoid that expansion. Public `unit-norm-law-definition` and `regularity-law-definition` paths expose their exact theorem types; the obligations are unchanged. Cached assembly then passed in 6.989 seconds. Cached success was not admitted as proof evidence.

Fresh safe `--ignore-interfaces` closure passed in **1886.962 seconds**, rechecking the full norm and derivative dependency closure. Receipt: `results/constructed-unit-circle-flow-fresh.json`.

The net records `completion-unit-circle-flow` as **++**. The full half-turn remains at its historical +- outcome until its separate assembled certificate is freshly checked. The whole-return target remains open.

Next recommendation: **prove/operational-unitary-half-turn**, combining this flow with the already checked Machin endpoints and the explicitly accepted mixed-level standard-pi identification. The identification must not be relabeled kernel-proved.

```text
python research/nima/checkers/check_constructed_unit_circle_flow.py --timeout 2400
python research/nima/checkers/test_completion_refinement_net.py
python research/nima/checkers/test_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_net.py
```
