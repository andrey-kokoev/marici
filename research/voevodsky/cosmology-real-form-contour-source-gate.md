# Real-form contour source gate

## Question

Do the actual source coordinates select the compact unit-torus period contour?

## Claim boundary

No. The exceptional complement is the split rational torus with coordinates `(u,v)`. Its inherited real structure is ordinary conjugation, whose fixed locus is `(R*)^2`. The period contour `|u|=|v|=1` is instead fixed by the compact involutions

`u -> 1/conjugate(u)` and `v -> 1/conjugate(v)`.

In each factor the split and compact fixed loci intersect only at `+1` and `-1`; the split real locus cannot sweep the compact two-cycle. A Cayley transform between presentations requires a choice of square root of `-1`, a boundary-point normalization, and orientations. None is supplied by the rational DNC, rank-26 relations, exceptional triangle, or Parshin flags.

The DNC parameter and exceptional coordinate ratios also carry no physical-time meaning. No map to a physical-time, boundary-condition, detector, or record object has been declared.

## Disposition

The unit torus is a valid chosen Betti generator in the complexification, not a contour selected by the available split source geometry. The next leaf tests whether any sourced boundary condition or canonical Cayley transform supplies the compact real-form twist and orientations.

## Verification

- `research/voevodsky/check_cosmology_real_form_contour_source_gate.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
