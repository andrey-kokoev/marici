# Muon–tau trigger pilot (WP250)

## Preregistered branch

After WP249 closed the double-hadronic-tau route, freeze the independently
motivated semileptonic decay branch `tau tau -> mu + tau_h`. Its source-local
instrument is the OR of the three recovered isolated-muon-plus-loose-tau20 HLT
paths, intersected with at least one tau passing WP248's frozen four-ID
conjunction. The trigger family and acceptance threshold were fixed before
counting.

## Exact pilot response

The trigger OR fires in 935 events; 5,619 events contain at least one frozen
offline-ID tau; their intersection is 414 of 14,688 events:

\[
A_{\mu\tau}=\frac{414}{14688}=\frac{69}{2448}\approx 0.02819.
\]

This exceeds WP246's weaker-pole one-event screen, approximately `0.02487`.
The exact minimum passing event count is 366, leaving a 48-event loss budget.
If trigger-object matching and offline-muon typing retain only 365 events, the
count gate fails. This is the smallest finite hostile falsifier.

## Claim boundary

WP250 is a source-local, named, event-level **physical/readout pilot**. It is
count-progressive, not yet a calibrated source identifier. It does not assert
that the trigger tau matches the selected offline tau, type an offline muon,
include backgrounds, transfer 2015 acceptance to 2016, interpolate the mass
grid, or establish rank. Those repairs must fit inside the exact 48-event loss
budget; the selection may not be loosened after seeing this count.

Run `uv run --with sympy python
research/flavor/checkers/wp250_mu_tau_trigger_pilot.py` to regenerate the JSON
and deliberate hostile residual.
