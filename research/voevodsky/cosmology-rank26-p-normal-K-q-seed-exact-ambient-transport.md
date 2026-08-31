# Exact rational ambient transport of canonical seeds

## Result

The complete exact degree-14 source words, including all `T`, `S_K`, and q coefficients, were mapped by typed source descriptors into ambient degrees 12 and 16. Integer rows were independently reconstructed by four-prime CRT at each target degree.

Both mapped words reconstruct their complete canonical targets over the rationals:

| ambient degree | pole 0 source rows | pole 1 source rows | full reconstruction |
|---:|---:|---:|---|
| 12 | 27 | 45 | yes |
| 16 | 27 | 45 | yes |

Together with the degree-14 exact solve, the same rational source words hold at degrees 12, 14, and 16.

## Disposition

N5c3a is completed. The rational canonical seed identity is ambient-compatible at all three tested degrees.

N5c3 remains active through N5c3b: shift every source descriptor and coefficient by each monomial of degree at most \(A-7\), then reconstruct every corresponding K target over the rationals. This tests the full interior family rather than only the canonical monomial.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_seed_exact_ambient_transport.py`
- Results:
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_seed_exact_ambient_a12.json`
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_seed_exact_ambient_a16.json`
