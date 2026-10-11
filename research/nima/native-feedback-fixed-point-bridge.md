# Testing the actual payload identification: the unperturbed image is fixed

## Fresh inputs

Read `TetrahedralHierarchyAtVertex.agda` and the actual source specialization in `AgreementPolicyBoundary.agda`. The native view retains the full typed tetrahedral package and its marked value. Its decoder recovers that payload; exchanging the comparison routes changes their history but not the decoded payload.

Compare this with the existing twelve-triangle geometry's actual phase-aligned assembled mode, rather than the deliberately perturbed preparations used in the barycenter tests. These remain two distinct source sectors; the purpose is to test the proposed identification, not assume it has already been constructed.

## The geometric baseline is not the contrast preparation

Reconstruct every local complex mode and transport it back using its stored source rotation. All twelve become the same v0. Their coefficients relative to v0 are exactly

    u=(1,1,...,1).

With empty memory, the conservative projector lift obeys

    U(u,0)=(u,0).

Thus the specific existing baseline has no stored or active contrast to exchange. The earlier u+d preparation is a different state, not an automatically produced output of the native history exchange.

## Formal intertwining obstruction

Let c be the actual native comparison from the existing typed tetrahedral fixture, and sigma its exchange. The source already proves sigma(c) differs from c.

Suppose a proposed numerical adapter Phi satisfies

    Phi(sigma(c))=U(Phi(c)),
    Phi(c)=(u,0).

Since this numerical state is fixed, necessarily

    Phi(sigma(c))=Phi(c).

The new safe Cubical module `NativeFeedbackFixedPointBridge.agda` proves this implication for any fixed target state and any proposed intertwiner, using the actual source comparison and its existing nontriviality theorem. Such an adapter cannot be injective on this source pair.

The module also proves that any observation depending only on the source's decoded payload is invariant under its exchange. This does not require the numerical model: the payload is unchanged definitionally while the history changes.

This is not a prohibition on coarse observers. A complete retained package may preserve the distinct native history separately while showing the same numerical active value. But such an observer cannot explain a changing numerical barycenter on this two-record orbit.

## Nontrivial orbit images are possible, but require different data

For the existing interface contrast d and any chosen beta, the pair

    Phi_beta(c)=(u+beta*d,0),
    Phi_beta(sigma(c))=(u,beta*d)

intertwines this two-point exchange with the conservative swap. Both decode to u+beta*d. Exact controls use beta=0,1/2,1,2.

- beta=0 matches the unperturbed geometric payload, but the two numerical images coincide.
- Every tested nonzero beta distinguishes the histories, but changes the decoded payload away from the existing baseline.

These are orbit-level algebraic candidates, not a constructed map on all native comparisons. They demonstrate precisely where the previous preparation entered. Merely exhibiting a commuting two-cycle does not select its contrast amplitude or identify its physical origin.

## Consequence for the source-informed phase selection

The previous packet conditionally selected the return phase by preserving a fixed linear reconstructed payload. That remains valid. It does not supply the missing initial excitation or identify the coefficient field with the native tetrahedral object.

To obtain nontrivial center dynamics while retaining the geometric baseline, a further source mechanism must prepare a nonempty bank, change the numerical encoding, or couple a specified history observable into the active field. Which of those is physically justified is not settled by the source exchange's existence. We do not insert a contrast merely to make that exchange visible.

The current branch therefore distinguishes two questions that should no longer be conflated:

1. Given a phase-bearing preparation, can conservative memory return a first-moment signal? **Yes, conditionally, already checked.**
2. Does the inspected unperturbed source create that preparation through its existing native history exchange and proposed fixed numerical initialization? **No nontrivial intertwining image is possible under those conditions.**

This is a bounded initialization/adapter obstruction, not a theorem excluding all WG-to-physics realizations. No electron creation, charge, mass or recoil is derived.

## Verification

- `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeFeedbackFixedPointBridge -Fresh` passed with ignored interfaces and stable inputs. The existing `TypedGeneratorLayers` unused-import warning remains; no new source-owner modification was made.
- Receipt: `results/agda-NativeFeedbackFixedPointBridge.json`.
- `python research/nima/checkers/check_native_feedback_fixed_point_bridge.py` passed exact phase alignment, fixed-point and orbit-adapter controls and verified the formal source digest.
- Results: `results/native-feedback-fixed-point-bridge.json`.

No prior law, native fixture or geometric baseline was changed. No ledger entry, commit or physical publication is claimed.
