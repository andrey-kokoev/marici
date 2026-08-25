# Muon–tau object-match gate (WP251)

## Frozen coherence test

Spend WP250's 48-event validation budget without changing its trigger family
or tau IDs. For one fired preregistered path, require last-filter-accepted
trigger objects of stored types 83 (muon) and 84 (tau). Match them within
`Delta R < 0.3` to a PF offline muon (`pt > 17 GeV`, `|eta| < 2.1`) and a
WP248-ID tau (`pt > 20 GeV`, `|eta| < 2.1`), with the offline pair separated by
`Delta R > 0.5`.

## Exact response

The coherent selection retains 389 of 14,688 signal events:

\[
A_{\mu\tau}^{\mathrm{coh}}=\frac{389}{14688}\approx0.02648.
\]

It removes 25 of WP250's 414 events, within the preregistered 48-event budget.
The exact minimum passing count remains 366, so 23 further events may be lost;
retaining 365 is the smallest hostile falsifier.

The oddball is exact: all 389 triggered events that reach both typed offline
objects also pass same-path trigger-object coherence. The 546 other triggered
events fail earlier because no tau satisfies the frozen offline requirements.
This is recorded, not interpreted as perfect detector matching.

## Claim boundary

WP251 is a signal-only 2015 **physical/readout pilot**, not a source identifier.
Background calibration, the 130/140/160 response family, common-era transfer,
and rank remain open. Run `uv run --with sympy python
research/flavor/checkers/wp251_mu_tau_object_match.py` for the exact result and
deliberate hostile residual.
