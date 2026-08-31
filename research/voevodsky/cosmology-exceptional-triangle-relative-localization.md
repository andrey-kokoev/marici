# Relative localization on the exceptional triangle

## Result

The three strict-transform lines on `E=P^2` have dual graph a triangle. Its oriented edge-boundary matrix has rank two and a primitive one-dimensional cycle. In the programme's pair-face convention this cycle has residue vector `(1,-1,1)`, exactly the residue vector of `Xi_log`. The oriented exceptional face has the opposite vector `(-1,1,-1)`.

Therefore relative localization gives a source-geometric explanation of the closed pair

`Xi_log + minus_sigma123`.

It also separates this class from the exceptional hyperplane class: `H` restricts to zero on the triangle complement, while `Xi_log` is the boundary/dual-graph weight class.

## Claim boundary

Relative localization identifies the target class and proves its cancellation with the exceptional face. It does not supply an incoming degree-one chain whose differential is that pair. Promoting the primitive dual-graph cycle itself to such a chain would repeat the abstract `tau_p` insertion.

## Disposition

The relative-localization leaf is completed. The next leaf is the total-lift existence gate: inspect the resolved blow-up carrier for a cone cell over the primitive triangle cycle. Its differential must be `Xi_log+minus_sigma123` with unit coefficient. If no such geometric cell exists, the relative class remains a genuine obstruction rather than a Bockstein source.

## Verification

- `research/voevodsky/check_cosmology_exceptional_triangle_relative_localization.py`
- `research/voevodsky/results/cosmology_exceptional_triangle_relative_localization.json`
