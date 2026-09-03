# K2 obstruction period normalization

## Question

What is the canonical mathematical period of `Xi_log`, and which orientation data does it require?

## Claim boundary

On the real torus defined by `|u|=|v|=1`, set `u=exp(i theta)` and `v=exp(i phi)` and orient it by `dtheta wedge dphi`. Then

`integral Xi_log = (2 pi i)^2 = -4 pi^2`,

so its normalized period is

`(2 pi i)^(-2) integral Xi_log = 1`.

This equals the primitive double residue and the oriented Parshin triangle coefficient. Reversing one circle or swapping `u` and `v` changes the sign; reversing both circles preserves it. The period is therefore canonical only relative to the ordered units `(u,v)` and the two chosen positive circle orientations.

This is a Betti-de Rham period of the algebraic torus. No source-derived map from the cosmological carrier, contour prescription, state/effect pairing, or physical record map to this cycle has been established. It is neither a horn filler nor yet a physical observable.

## Disposition

The K2 obstruction has primitive normalized mathematical period one. The next leaf audits whether any existing source geometry defines the required contour/readout interface; absent such a map, the period remains purely mathematical.

## Verification

- `research/voevodsky/check_cosmology_K2_obstruction_period_normalization.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
