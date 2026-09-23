# Adjacent-minor fork repairs image rank, not history matching

The exact failure of three proposed seven-point cells has a simple algebraic repair **candidate**. In a rank-two source matrix, the conditions

    Delta(i,i+1)=Delta(i+1,i+2)=0

have two different codimension-two positive branches:

1. **parallel triple:** if the shared column `C_(i+1)` is nonzero, its two neighbors are each parallel to it;
2. **zero column:** `C_(i+1)=0`, with the other six columns generically positive.

The rank-table compiler chose the first branch for histories 1, 3 and 5, yielding positive one-dimensional fibres and seven-dimensional images. It did not distinguish the zero-column branch merely from the two named vanishing minors. A zero column imposes two equations on `G(2,7)`, so it ALSO has source dimension eight. Its six retained external-data rows form an invertible 6x6 matrix at positive moment-curve `Z`. Therefore `C -> CZ` is a linear Grassmannian isomorphism on each zero-column carrier: its image is eight-dimensional, and each image point has a unique source lift on that carrier.

Candidate replacements are:

| History | Adjacent vanishing cyclic minors | Replace parallel triple by zero column | `det Z_retained` |
|---:|---|---:|---:|
| 1 | 23, 34 | 3 | 518400 |
| 3 | 71, 12 | 1 | 34560 |
| 5 | 45, 56 | 5 | 518400 |

Each carrier has a checked positive top-cell point with exactly the six ordered minors involving the zero column vanishing; all other fifteen are strictly positive. A fixed interior image point from the history-zero separated-pair chart has a UNIQUE inverse in each repaired carrier, but these inverse matrices have mixed-sign ordered minors (respectively 2, 7, and 2 negative). Thus that particular point lies in none of their positive images. This is a precise local separation check, not a global disjointness or coverage theorem.

**Do not promote the repair to a physical compiler.** The six-point top-cell canonical form pulled through a deleted-label `Z` matrix is not yet proved equal to any of the corresponding seven-point generalized-R history terms. A source codimension and a full image-rank certificate do not determine the correct history form. The next gate is a same-external-data normalized form/pole comparison of the zero-column carrier against one adjacent-omission history. If it fails, the candidate is a geometric dimension repair only.

Run `uv run --with sympy python research/nima/checkers/check_seven_point_zero_column_repair.py`. Packet: `research/nima/results/seven-point-zero-column-repair.json`. This extends the negative result in `seven-point-positroid-compiler-has-three-collapsed-image-cells.md` without undoing it.
