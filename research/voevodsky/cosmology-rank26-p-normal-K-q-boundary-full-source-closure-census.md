# Full-source boundary dependency census

## Result

A `T+S_K+Q` pivot DAG was built for every top-three-degree K target at ambient degrees 12, 14, and 16.

| degree | targets | pole-0 closure range | pole-1 closure range | largest closure | maximum depth |
|---:|---:|---:|---:|---:|---:|
| 12 | 48 | 37–63 | 49–73 | 73 | 4 |
| 14 | 60 | 47–77 | 53–91 | 91 | 4 |
| 16 | 72 | 57–92 | 67–110 | 110 | 4 |

Every active closure is square: the number of retained source rows equals the number of retained columns. Q support ranges from 9 to 17 rows. All targets reduce exactly over \(\mathbb F_{32003}\).

The earlier planning count of 54 degree-12 targets was corrected to 48: the top three degrees 6, 7, and 8 contain 7, 8, and 9 monomials per pole.

## Disposition

N5b2a is completed. Exact boundary solving is bounded by 110-by-110 square systems, smaller than the completed interior maximum.

N5b2b becomes active: reconstruct each retained source row and target over the integers using four-prime CRT, solve all 180 square systems over the rationals, and verify complete target reconstruction. Closure squareness does not itself authorize a rational claim; exact nonsingularity and reconstruction remain required.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_full_source_closure_census.py`
- Results: corresponding `..._a12.json`, `..._a14.json`, and `..._a16.json` files.
