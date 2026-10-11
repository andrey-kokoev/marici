# Whole-Tick return realization

Implementation: `agda/TickWholeReturnRealization.agda`.

## Standard-complex extension now proved

`spectral-whole-return-proof.md` constructs unitary return paths on the metric interval [0,2] using the same source-derived spectral local-core witness. It proves endpoints, seam continuity, piecewise local generator laws, whole-record coherence and fixed-source faithfulness. This closes the clarified external-path existence claim in standard C4; it does not complete the operational backend described below.

## Earlier operational construction

At fixed source `s`, extract the two ordered schedule tags. For each tag, reverse the operation order and traverse the existing glued completion charts from `run leftFirst s` back to `s`. The result is a pair of whole path objects.

Agda proves:

- `return-start` and `return-finish`: exact target/source endpoints;
- `return-continuous`: coordinatewise continuity for the existing final topology on glued completion charts;
- `reconstruction-coherence`: rebuilding the entire Tick from its tags preserves the realization;
- `same-tags-coherence`: equal tags give equal realizations;
- `schedule-swap`: exchanging the retained schedules exchanges the two paths.

## Correction to the earlier contract

`TickRetainedStructure.observation-factors` already proves that every whole-Tick observation factors through the two schedule tags. Its `canonical-return-section` identifies each section with the canonical one. Requiring independently observable section-interior data was therefore the wrong target. Whole-record reconstruction coherence is the appropriate law here.

**No pointwise selector:** the construction returns functions on external glued completion charts, not C4 states indexed by Cubical `I`.

## Completion phase implementation

`agda/TickCompletionPhase.agda` constructs `phase p t = exp(0,-p*t)` using the operational complex completion exponential. Fresh Agda closure proves its start value is one, identifies its cosine/sine components, and reduces its finish to `(cos(-p),sin(-p))`. Receipt: `results/agda-TickCompletionPhase.json`.

The full phase test remains `+-`: a completion-valued pi with half-turn laws, unit norm, and metric continuity are still needed. The all-degree Taylor proof of `cos(x)^2 + sin(x)^2 = 1` and an explicit uniform finite-sum norm-defect bound are recorded in `phase-pythagorean-series.md`, with 305 exact controls. Next: transfer that bound through the operational completion schedules to obtain the Agda identity.

## Remaining analytic bridge

The existing completion legs are affine interpolations. Their glued parameter is two whole completion charts with final topology, not a proved metric interval. The midpoint test rejects these affine legs as unitary: every basis state has squared norm `1/2` there. The replacement `U(t)=(I-Q)+exp(-i*pi*t)Q`, `Q=(I-P)/2`, passes the exact matrix test and all-time projector proof; see `return-leg-unitarity.md`. The remaining bridge is implementing this complex phase in the completion, with parameter domain, continuity, and generator compatibility proved. This implementation closes whole-record reconstruction and schedule coherence, not that analytic bridge.
