# Two-monomial contraction transports have exact overlap descent data

## Result

On each higher boundary coordinate lying in both monomial-square images, transport the corresponding lower exact contraction along each axis. Their difference was evaluated against exact higher-ambient source rows.

| inclusion | overlap cells | exact zero syzygies | support range |
|---|---:|---:|---:|
| A12 to A14 | 36 | 36 | 64–116 |
| A14 to A16 | 48 | 48 | 75–137 |
| A16 to A18 | 60 | 60 | 90–158 |

All 144 overlap differences are exact rational source syzygies.

The two descriptor shifts commute strictly:

- A12 to A16: 48 of 48 transported words agree along the two square paths.
- A14 to A18: 60 of 60 agree.

## Disposition

P5d2c2b is completed. The finite contractions form a torsor with explicit exact descent cells over the two-monomial cover, and the ambient multiplication squares commute strictly.

P5d2c2c becomes active. The remaining question is whether the torsor has a source-derived canonical section. The current pivot-selected words do not supply one: their literal transports and low-order coefficient recurrences fail. A section requires an additional normalization, symmetry, or universal homotopy characterized independently of pivot order. Without such datum, descent existence must not be promoted to canonical contraction.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_two_monomial_overlap_syzygies.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_two_monomial_overlap_syzygies.json`
