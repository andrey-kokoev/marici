# Muon–tau background pilots (WP252)

## Frozen background grammar

Before inspecting yields, freeze the minimum simulated family as
`DYJetsToLL_M-50`, `TT`, and `WJetsToLNu`, plus a separate data-driven QCD
fake-control gate. For each simulated process, choose the smallest online file
from its official 2015 MiniAODv2 CMS record. The files are streamed through
their official XRootD URIs; TLS verification was not bypassed when HTTPS failed.

## Pilot response

Apply WP251 without changing its paths, IDs, thresholds, or matching:

- DY: 1 of 899 selected; 149 negative-weight events;
- top: 38 of 9,600 selected;
- W+jets: 0 of 809 selected; 132 negative-weight events.

Signed generator-weight normalization gives nonzero DY and top selected support.
Composed with the official pilot cross sections, their estimated selected rate
exceeds the weaker unit-mixing signal rate by roughly five orders of magnitude.
This is a pilot obstruction, not a precision background prediction.

## Disposition

WP252 falsifies **rate-only source identification** for the WP251 record. The
zero W count is censored by the finite pilot and is not promoted to zero
support. QCD is not represented by simulation here and still requires an
independently typed fake-rate control experiment. A successor needs full
weighted mass/readout shapes, uncertainties, and a rank/power test; count
acceptance alone has no selection authority.

Run `uv run --with sympy python
research/flavor/checkers/wp252_mu_tau_background_pilots.py` for the exact
composition and deliberate zero-background failure.
