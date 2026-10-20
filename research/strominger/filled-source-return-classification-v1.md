# A fixed filled tetrahedron leaves one precisely classified return input

## Result

The actual retained tetrahedral interface does not automatically interpret all six original directed occurrences. With tetrahedral vertices ordered **A,D,B,C**, its edge slots bind as follows:

| Source occurrence | Filled-package path |
|---|---|
| AB | e02 |
| BC | e23 |
| CA | reverse e03 |
| AD | e01 |
| DB | e12 |
| BA | **Additional path B→A** |

The remaining tetrahedral slot e13 is **D→C**, compared with DB followed by BC by its existing face123. It is not BA. Counting six slots on each side would conceal this interface mismatch.

`agda/FilledSourceReturnClassification.agda` proves, for every type X and every fixed actual `RetainedTetrahedralPackage.Cells.Full X`:

    {six-arrow path assignments at the fixed vertex images,
     with all five specified edge-matching witnesses}
      ≃ (B ≡ A)
      ≃ (A ≡ A).

The second equivalence prepends the supplied AB path. The first includes the matching witnesses and their inverse homotopy; it does not merely count one unused field. All faces and the tetrahedral filler remain in the **fixed input parameter**. No recovery of that package from the unmarked output map, native producer reconstruction, or contraction of arbitrary retained histories is claimed.

Every BA choice gives an actual map from the existing six-arrow free realization into X, through the previously proved mapping equivalence. BA is recovered on its edge by reflexivity.

## Which cycles are filled?

The actual package supplies:

- face023: AB followed by BC equals the reversed interpretation of CA; the ABC cycle is null;
- face012: AD followed by DB equals AB; the forward discrepancy cycle is null;
- face123 and the remaining face/filler: the existing tetrahedral coherence, not another constraint on BA.

Consequently the **original directed ADB cycle** is sent to

    AD ; DB ; BA = AB ; BA.

That is the remaining based loop. A filled geometric ABD face uses reverse AB; replacing the separately retained BA occurrence by that reverse is an additional interpretation equation.

Two exact alternatives are now checked:

1. **No extra ADB filling requirement:** extensions form the target's based loop space. They need not be unique, but their ambiguity depends on X; not every target has nontrivial loops.
2. **Require the original directed ADB cycle to be null:** the BA choice together with its full null-homotopy forms a **contractible space**. The required equation is equivalent, at the witness-type level, to BA = reverse AB.

This is a conditional uniqueness theorem with an explicit decisive premise, not a reason to declare that premise already supplied. It does not say the filled package or the target X is itself a circle.

## Actual predecessor controls, not an invented replacement

- `research/nima/agda/SeedNativePromotionBindingGate.agda` already rejects a full package that preserves the unchanged free-source skeleton, even allowing propositional vertex identification. Its stronger theorem is imported in the fresh closure. The all-composite spine is inhabited but changes those independent source edges.
- `research/nima/agda/RetainedTetrahedralPackage.agda` already contains inhabited filled packages. The new counterexample uses its **same** `LossyDiagonal.ordinary` package over the universe of types, with all vertices Bool. BA may be the identity path or univalence of Boolean negation. Transport of false distinguishes these choices. The complete filled package is identical in both cases.
- The distinct BA assignments are proved distinct as assignments **at fixed vertex images**. No stronger unmarked-function comparison is asserted.
- The actual pointed `TypedFixture.result` used by the prior feedback example is separately instantiated with BA = reverse AB. Its return loop is null. The ambiguity theorem for the universe-valued fixture is **not** transferred to this pointed fixture.
- `research/nima/agda/TetrahedralComparisonFeedback.agda` and its note were inspected. Its feedback consumes an already filled marked payload and changes presentation histories, not the source's geometric AB/AD-DB paths. Its established existence is not reopened. It is hashed as inspected evidence, not reported freshly executed by this checker.

This respects the earlier correction in `research/nima/prior-feedback-recovery-after-free-seed-detour.md`: a free-source binding obstruction does not establish absence of native feedback or invalidate separately supplied filled packages.

## Verification

    python research/strominger/checkers/check_filled_source_return_classification.py

Fresh safe Cubical/guarded Agda closure passed with ignored interfaces, implicit libraries disabled, stable inputs and a conservative 2,294-file include-root/primitive manifest. Three compiler controls reject identifying the two actual BA choices, forcing arbitrary BA to be inverse AB, and silently binding the all-composite spine as the original free skeleton.

Cubical indexed-match warnings and the known `TypedGeneratorLayers` unused/unexported `isPropIsContr` import warning are explicitly recorded. No other-owner source was edited.

- Proof: `agda/FilledSourceReturnClassification.agda`
- Contract: `contracts/filled-source-return-classification.v1.json`
- Receipt: `results/filled-source-return-classification/verification.json`
- Dependency lock: `results/filled-source-return-classification/dependency-manifest.json`
- Connected net: `wg-source-determination-conjecture-net-v1.md`

## Closure and next effort

This bounded branch is now classified: free incidence gives three circles; the inspected filled target constrains two source cycles and leaves an exactly loop-valued return input; an additional ADB filling requirement uniquely determines that return together with its witness. None of these steps supplies a physical law or proves WG selects the corresponding task.

Do not keep extending this branch without new source relations or an independently specified observation task. The next implementation recommendation is the existing **canonical comparison synthesis** gate: turn the finite-reader classification into a native comparison-or-refusal procedure without accepting an arbitrary comparison as input. Broader continuation-policy classification remains open, but does not require repeating the completed topology tests.
