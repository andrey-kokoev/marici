# Ambient-degree transport of K residual support

## Result

The graded residual census was rerun independently at ambient degrees 12 and 16 over \(\mathbb F_{32003}\), deriving family offsets from constructor counts rather than degree-14 constants.

| ambient degree | monomials through \(A-4\) | residual rows modulo `T+S_K` | residual rank | after IBP rows | after IBP rank |
|---:|---:|---:|---:|---:|---:|
| 12 | 45 | 90 | 59 | 45 | 30 |
| 14 | 66 | 132 | 72 | 66 | 38 |
| 16 | 91 | 182 | 88 | 91 | 46 |

At both new degrees, the residual support has exactly the degree-14 form:

- one row for every monomial of degree at most \(A-4\) at each K pole 0 and 1;
- one marked-level pattern only, `(1,1,2,1,1)`;
- adjoining special IBP removes the complete pole-0 copy and leaves the pole-1 copy.

## Disposition

N3b4a is completed. The support decomposition transports across three ambient degrees; it is not an isolated degree-14 coincidence.

This remains finite single-prime evidence. The next child N3b4b should verify at degrees 12 and 16 that special marked-\(q\) relations again absorb the complete residual family and test the predicted three-degree cutoff boundary: interior shift closure through degree \(A-7\), followed by boundary degrees \(A-6,A-5,A-4\).

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_residual_ambient_profile.py`
- Results:
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_residual_ambient_a12.json`
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_residual_ambient_a16.json`
