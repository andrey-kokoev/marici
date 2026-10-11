# Same interaction across retained presentations

## Prior clue implemented

The prior double-functor and attached-record analyses distinguish an
intervention from a presentation change. We now implement that distinction
for today's charge–mass–recoil packet. We do NOT relabel kick and drift as
commuting source axes or add a compensating face after their failure.

## Formal result on actual Tick histories

The new `Policy.Views` module in `agda/RetainedTickStateAction.agda` takes
a declared lossless view with encode/decode inverse laws. For the existing
actual Tick policy step, define

    view-step(t,v)=encode(step(t,decode(v))).

It proves the step square and the corresponding whole-history square:

    view-step(t,encode(x)) = encode(step(t,x)),
    view-act(h,encode(x)) = encode(act(h,x)).

It also proves identity and chronological composition on the view, and
compatibility with the ACTUAL square-clock cone encode/decode operation.
The policy is transported, rather than frozen while its state changes
presentation. No physical policy is selected by this theorem.

Fresh safe Cubical closure checking passes with ignored interfaces and
stable inputs; the existing TypedGeneratorLayers import warning remains.

## Physical comparison fixture

The new exact checker reuses the original comparison Packet, route validator
and three witness foci. Each view now retains an enlarged Whole:

    original witness packet,
    positions and momenta of both bodies,
    work-account balance,
    supplied drift duration,
    complete prior event records.

This explicitly extends the old Packet-only views. We do not pretend they
already contained a physical trajectory. Executing in a view means decode,
execute the same previously declared interaction, and re-encode.

All sixteen presentation-pair squares commute as equality of complete
records, including positions, momentum, work and route history. All 64
three-presentation transport compositions are checked, along with bounded
iteration composition and the original physical readouts.

This covariance follows by construction from losslessness. It is a verified
integration/typing result, NOT independent evidence for the physical law.
The Python mechanics have not been translated into an Agda instantiation;
the formal theorem and exact physical fixture have distinct verification
boundaries.

## Discriminating controls

- The same selected witness can accompany different initial momenta and
  produce different positions. Selected-focus-only views are not closed
  state descriptions for this interaction.
- Adding an identity operation to a valid comparison route leaves the
  physical response fixed but produces a distinct retained history.
- An adapter that changes the supplied duration keeps the triangle and
  momentum outputs unchanged but breaks position covariance. It is rejected.
- Presentation transport adds no event. The formal cone theorem separately
  covers actual native Tick histories; Python event counts are not equated
  with the source clock.

## What this repairs, and what it does not

The correct presentation/intervention squares now exist for a supplied
interaction law and lossless whole-state views. The earlier kick/drift
identification with the Bool square's axes REMAINS rejected. This construction
is not an unnoticed replacement proof of that failed internal identification.
The relationship between these presentation squares and all internal source
operations still requires its own interpretation.

The remaining physical-selection problem is narrower: supply the interaction
controls from the retained source instead of supplying charges, masses,
impulse kernel and duration externally. Prior reversible carrier/record
exchange is the strongest existing endogenous back-action candidate, per
`seed-seam-backaction-source-comparison.md`. Its carrier/feature/metric and
native-port adapters remain necessary; this note does not introduce a third
update law or assert that exchange is already a two-body mechanical impulse.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module RetainedTickStateAction -Fresh
    uv run --with sympy python research/nima/checkers/check_interaction_presentation_squares.py

139 new exact integration checks pass, alongside the rerun 99 physical
pipeline checks. Receipts: `results/agda-RetainedTickStateAction.json` and
`results/interaction-presentation-squares.json`.
