# Actual Tick-history action, and the failed kick/drift face attachment

## Structural attachment now proved

`agda/RetainedTickStateAction.agda` imports the ACTUAL
`RetainedSquareConeClock.Bridge.AtSource` Tick and History types. For an
attached state type and supplied policy `step : Tick -> State -> State`,
it constructs chronological execution and proves:

- empty history acts as identity;
- `act(h++k,x)=act(k,act(h,x))`;
- executing the encoded cone history after decoding equals original execution;
- execution retains the full original Tick history, not just its final state;
- extension retains a certified source-to-final-state attachment.

Thus a completed square can return its base source while its attached
state evolves. No fabricated Tick token or interaction-event count is used
in these formal theorems. The action is generic at a FIXED source; it is not
yet a dependent action across changing sources.

The step policy is an explicit parameter. A stationary policy also satisfies
all these laws, and its history action is proved stationary. Consequently
these structural obligations alone do not force excitation, impulse or time.
The Python physical model has not been translated into Agda by this theorem.

## Test the internal face, not just the list action

A tempting stronger attachment identifies the left square axis with the
physical impulse and the right axis with free drift. The existing source
square certifies equality of the two schedules. Does that face survive?

Use the preceding interaction harness without changing its laws:

    kick:  (x,p) -> (x,p+J)
    drift: (x,p) -> (x+tau M^-1 p,p).

Kick then drift gives `x+tau M^-1(p+J)`; drift then kick gives
`x+tau M^-1 p`. Their position difference is exactly

    tau M^-1 J.

For positive duration and masses this vanishes only for zero impulse.
Momentum and work-account outputs agree, but observable positions do not.

In the original charge–mass–recoil fixture, starting at rest with duration 1,
the position residuals are

    body 1: (-1,-2,1)
    body 2: (2/3,4/3,-2/3).

The exact checker retains this failure. Therefore the natural kick/drift
axis assignment is NOT an interpretation preserving the source's equal-target
square face on this physical state space. A momentum-only observer could hide
the residual, but that would abandon the intended position readout. The
failure already occurs at the face, before higher coherence is considered.

This does not prohibit assigning a whole completed Tick an external
kick–drift update. The formal list action permits that. But such assignment
would not, by itself, interpret the Tick's INTERNAL operations and witness.
Confusing these two claims would falsely close the end-to-end construction.

## Remaining precise task

Find a source-supported physical interpretation whose internal comparison
maps preserve the retained face, with position retained; alternatively justify
a different target comparison structure rather than asserting equality of
these unequal states. Then specify the whole-history controls, duration and
energy source. No universal obstruction to other interpretations is claimed.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module RetainedTickStateAction -Fresh
    uv run --with sympy python research/nima/checkers/check_tick_interaction_attachment.py

Fresh safe Cubical headless checking passes with ignored interfaces; only
the existing `TypedGeneratorLayers` import warning remains. The exact checker
checks the formal receipt/source hash, reruns the preceding 99 integration
checks, and verifies both the concrete and symbolic nonzero face residual.

Receipts: `results/agda-RetainedTickStateAction.json` and
`results/tick-interaction-attachment.json`.
