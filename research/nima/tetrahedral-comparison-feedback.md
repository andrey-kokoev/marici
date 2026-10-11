# Resume the prior native feedback with a marked tetrahedral payload

## Reused mechanism

`agda/TriangleComparisonFeedbackRegression.agda` already implements feedback on an entire retained comparison: exchange its two routes, certificates and witness orientation, exchange again, compare with identity, then promote that new comparison for the next iteration. The chosen exchange law is an existing input, not a law inferred from endpoint incidence.

The new `agda/TetrahedralComparisonFeedback.agda` supplies an adapter to this mechanism. It does not replace it with another guessed update and does not require the obstructed free seed paths to become equal.

## Adapter and checked computations

1. Begin with a filled `RetainedTetrahedralPackage.Cells.Full` and a chosen mark.
2. Use the lossless `TetrahedralHierarchyAtVertex` view, retaining both marked value and full package.
3. Regard that view as an atomic payload in the existing compiler. Compare one identity presentation step with two identity steps. These are new presentation histories, NOT the seed's AB and AD DB paths.
4. Feed the resulting entire comparison into the prior `Feedback.run`.
5. Pass its exact promoted payload to the next prior feedback instance.

The first exchange is provably nontrivial: the first retained route changes length from one to two. The complete comparison records differ. Decoding after the two feedback iterations recovers the original comparison, marked view and full tetrahedron. The generic complete-package recovery theorem covers vertices, edges, faces and filler together. The resulting map is injective.

A concrete instance uses the already inhabited `RetainedTetrahedralPackage.TypedFixture.result`, not hypothetical inhabitants of the obstructed `SeedTetrahedronBridge.WithFaces`. Its output, recovery and nontrivial exchange are checked as well.

## Exact scope

This closes a TYPE/RETENTION adapter to the existing comparison-level feedback. It is more than attaching metadata to an unchanged comparison: the retained comparison fields are acted on, and the generated record is genuinely fed into the next constructor.

However, the tetrahedral package is treated as an atomic payload. The chosen exchange does not inspect or change its geometric fields. The decoded marked value and full tetrahedron are preserved. Thus this is not yet a field-sensitive tetrahedral back-reaction law, nor an implementation of the numerical four-packet carrier-record exchange. The adapter also does not derive a physical choice of feedback law, scalar gain, mass scale or G.

The important correction to the earlier detour remains: native feedback already existed. The free-seed face obstruction does not prevent applying it to existing filled packages. Future physical work should target the explicit binding between retained tetrahedral data and an active response, not rediscover generic feedback or erase source histories.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module TetrahedralComparisonFeedback -Fresh

Fresh safe Cubical/guardedness closure passed with ignored interfaces and stable inputs, including the existing native feedback dependencies. Receipt: `results/agda-TetrahedralComparisonFeedback.json`. Finished 2026-10-05T22:06:56.7981706Z. Source SHA-256: `6bdedcd198a6d84bf7a00431c4fbab7c80b2a627fc8f9575a8e525437be2260d`.

During development, explicit presentation indices resolved route inference metas; the fixture's mark was qualified through its defining module. The final full check passed. No postulates or unresolved holes were added. No ledger entry, commit or publication is claimed.
