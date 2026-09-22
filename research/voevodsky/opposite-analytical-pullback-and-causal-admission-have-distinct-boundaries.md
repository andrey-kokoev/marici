# Opposite analytical pullback and causal admission have distinct boundaries

## Constructed analytical recipes

The actual aggregate recipes use two ordered windows, fixed component scales S[j], positive denominators, and response W equal to R or N. Under complement reversal on the six-event packet, define

    Wop(a,b) = W(63-b,63-a).

Reverse the window sequence as well as each window's endpoints. Keep the component index, its coefficient and S[j]. Transform every denominator term by the same rule. Evaluation through Wop recovers exactly the original scalar product and denominator. This supplies an explicit coordinate-pullback recipe backed by the original response evaluations.

The checker verifies all 2,925 aggregate row terms and every denominator. It also checks 41,664 endpoint additivity identities. Original positivity transfers because every opposite response evaluation is the same positive original evaluation. The test relies on the owning response semantics and positivity certificates; it does not redo their analytic integration proofs.

The base observer's rho/sigma coefficients were already carried unchanged in the formal opposite packet. The new construction makes the aggregate window transport explicit. It is a companion recipe construction; the earlier formal packet retains original window labels as coefficient provenance.

This closes coordinate-level analytical transport. A detector operating directly on reversed physical windows would require a separate acquisition constructor. Coordinate pullback makes no such physical claim.

## Fresh proof-frame replay

The actual signed transport checker freshly rebuilt both frames and rejected changed calibration binding, status claim, cost, positive row and missing positive row. The deadline checker then freshly replayed both worlds: fast delivery certifies at A at time five, delayed delivery leaves A's coarse transcripts identical with opposite definite outcomes.

These replayable frames provide an explicit forward dependency constructor from retained raw rows and signed calibration to a locally verified certificate.

## Causal test: distinguish logical duality from time reversal

An additional adversarial interpretation reverses the schedule t'=K-t while retaining the original event constructors: B issues and A receives/replays that issued frame. In every tested fast/delayed world, the transformed receive event precedes its required issuance event. Thus this fixed-constructor time-reversal interpretation fails admission.

This is a test of a stronger interpretation, not a refutation of logical history/possibility duality. Logical reversal of a dependency diagram gives an opposite diagram. It does not automatically turn receiving or validating a certificate into a constructor that issues that certificate. A candidate opposite causal protocol must declare its input evidence, issuance rule, delivery dependencies and local replay rule.

The current forward source-authorized artifacts provide no such opposite issuance constructor. One could add evidence or constructors, but those additions would change the contract and need independent justification.

## Disposition

- Actual algebraic opposite rows/actions: verified in the preceding transport checker.
- Explicit analytical coordinate pullback: verified here.
- Existing forward proof-carrying availability: freshly replayed.
- Time reversal preserving issue/receive constructors: obstructed.
- Separately admitted opposite causal protocol: open.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/certify_signed_task_transport.py
    uv run --with python-flint python research/voevodsky/checkers/check_signed_certificate_deadline.py
    python research/voevodsky/checkers/check_opposite_recipe_and_causal_admission.py

Artifact: `results/opposite-recipe-and-causal-admission.json`.
