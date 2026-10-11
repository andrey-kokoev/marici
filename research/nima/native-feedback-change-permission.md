# Recover the actual change-permission rule: payload fixed, histories exchanged

## Correction to the recent instrument detour

The exhaustive Boolean instrument classification was correct for its stated
protection policies, but protecting EVERY source coordinate is not what the
existing native tetrahedral feedback does. Prior `agreement-payload-policy.md`
already establishes the relevant distinction:

- decoded tetrahedral payload is preserved;
- the ordered retained routes and their certificates are exchanged;
- equal route effects do not imply an unchanged comparison history.

This is an existing implemented operation, not a new proposed physical law.
We should not keep asking generic query recorders to select it.

## New direct native readout theorem

`agda/NativeFeedbackRouteReadout.agda` imports the ACTUAL
`TetrahedralComparisonFeedback.Fixture` and `AgreementPolicyBoundary`.
For a retained comparison c, observe

    R(c)=(steps(first(c)), steps(second(c))).

The source implementation itself proves definitionally

    R(exchange(c)) = swap(R(c)),
    decode(exchange(c)) = decode(c).

The existing fixture compares one identity-presentation step with two,
acting on the same filled typed-value tetrahedron. Its concrete readings are

    (1,2) -> (2,1).

The module proves these readings unequal, while the decoded payload stays
fixed. It also wraps the FULL comparison with the numeric reading and an
attachment proof; advancing this wrapper retains the changed source record
and preserves that proof. Counts are not substituted for the whole history.

Thus there is now a directly checked, nonconstant numeric history readout
of the actual native update. No arbitrary impulse, mass parameter, exchange
port or Boolean disturbance policy was supplied to obtain this swap.

## What this says about selection

The source operation does specify a concrete allowed change: exchange the
retained route roles, not the decoded object. This is more relevant to the
original retained-process question than freezing the entire current record.

The numeric swap has the same algebraic form as a two-port exchange, but
this does NOT identify route-step counts with oscillator amplitudes, particle
momenta or energies. The count reader is a deliberately chosen structural
observable. Other functions of the route lengths also intertwine with swapping;
this theorem does not select physical units or a mechanical readout.

Nor are the fixture's one/two identity-presentation routes the free seed's
AB versus AD,DB paths. The existing input is a filled tetrahedral package;
no missing free-seed face is manufactured by importing it.

## Relation to the initialization obstruction

`native-feedback-fixed-point-bridge.md` remains valid. A payload-only numerical
adapter pinned to its unperturbed fixed baseline cannot distinguish the
exchanged histories. The present observer instead reads retained route data.
It therefore detects source change without claiming that the fixed numerical
baseline was excited. To turn that history signal into a changing physical
field still requires an admitted coupling/readout map.

## Programme status

Resolved at the native structural level: which part of this actual comparison
may change, an implemented nontrivial update on it, a nonconstant readout,
and preservation of the decoded payload.

Still unresolved physically: map this history-bearing sector into the intended
carrier/record or interaction state while preserving the declared payload,
metric, units and relevant source compositions. The source law is no longer
an unspecified generic instrument; the remaining problem is its PHYSICAL
realization, not permission to swap the histories.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeFeedbackRouteReadout -Fresh

Fresh safe Cubical closure passes with ignored interfaces and stable inputs;
the pre-existing TypedGeneratorLayers import warning remains.
Receipt: `results/agda-NativeFeedbackRouteReadout.json`.
No physical charge, mass, time or energy theorem is claimed.
