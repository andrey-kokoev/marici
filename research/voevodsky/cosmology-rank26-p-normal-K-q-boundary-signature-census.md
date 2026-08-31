# Cutoff-boundary q-lift signature census

## Test

All 60 boundary residuals at monomial degrees 8–10 were solved independently with q-only provenance. Each coefficient list was normalized by subtracting the target monomial exponent from every q-row exponent, then grouped by K pole and total degree.

## Result

Every identity reconstructs exactly modulo `T + S_K`, but pole and total degree do not determine one common template.

| pole | degree | rows | normalized signatures |
|---:|---:|---:|---:|
| 0 | 8 | 9 | 9 |
| 0 | 9 | 10 | 5 |
| 0 | 10 | 11 | 11 |
| 1 | 8 | 9 | 9 |
| 1 | 9 | 10 | 5 |
| 1 | 10 | 11 | 11 |

The proposed six-template compression is therefore falsified. Direction within the monomial boundary matters to the pivot-normalized q correction.

## Disposition

N3b3d1 is falsified as a pole/degree-only template claim. The 60 exact lifts remain valid finite certificates.

The boundary signatures exhibit repeated patterns across adjacent exponents and degrees, so N3b3d is not exhausted. The next child N3b3d2 should classify signatures by coordinate distance from the cutoff faces, rather than total degree alone. Because provenance is pivot-order-dependent, any resulting compression remains a presentation template unless reconstructed as a source-natural map.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_signature_census.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_signature_census.json`
