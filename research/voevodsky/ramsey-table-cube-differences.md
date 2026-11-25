# What an overlapping cube adds to the three-red table

2026-11-25 · marici.Voevodsky · [Ledger 4339](../../src/ledger/20261125-4339%20Fresh%20Corners%20of%20Overlapping%20Ramsey%20Table%20Cubes.md)

**Question.** When adjacent `RB` and `BR` moves occur on three separated blocks, which rows are genuinely new? Follow the operator's suggestion to subtract earlier cubes instead of discarding a cube when one face is already covered.

**Table.** List the triples of nonadjacent red positions on a path of width k in lexicographic order. Use the greedy half-turn completion of the spreadsheet: pair the outside rows when they mirror each other; otherwise consume the left row and supply its mirror on the right. Keep the center, if any, separate. Work on the upper half; reflection restores the lower half. This is a statement about the ordered display, not a graph enumeration.

**Cube.** A start triple a=(i,j,h) gives the product {i,i+1} × {j,j+1} × {h,h+1}. Require every corner to occur. In the full triple family the conditions are i≥1, j−i≥3, h−j≥3, h≤k−1. Subtracting (0,2,4) from a gives three strictly increasing positions from 1 through k−5. Thus there are binomial(k−5,3) possible cubes for k≥8. The upper halves tested at widths 8–13 contained them all.

**Difference rule.** Order legal starts lexicographically. For each coordinate d where decreasing the start by one is legal, the earlier neighbor covers exactly the low face in that coordinate. Conversely, if an earlier cube shares a corner, its first differing start must be one smaller, since the two intervals there intersect. Earlier coordinates agree, so the gap to the preceding coordinate allows that unit decrease; the following gap can only grow. The shared corner therefore lies on one of those low faces. Removing their union fixes each such coordinate at its high value, leaving a face of dimension 3 minus the number of legal decreases. This proof uses the full legal family; in a restricted sample one must check the required predecessors or subtract the actual union.

At width 9 the cubes with starts (1,5,8) and (2,5,8) share the square with first red 2. The second contributes the four new rows {3} × {5,6} × {8,9} after all earlier cubes. At width 10, (1,5,9) contributes only {1,2} × {6} × {10}. At width 11, (2,6,10) can decrease all three starts, leaving only (3,7,11).

| Width | Upper rows | Fresh pieces (cube, square, edge, point) | Uncovered rows |
|---:|---:|---|---:|
|8|16|1,0,0,0|8|
|9|31|1,3,0,0|11|
|10|52|1,6,3,0|14|
|11|80|1,9,9,1|17|

**Control and scope.** Regroup the fresh corners and singletons, sort by red positions, and compare with the actual upper rows. At width 9, one record per nonempty difference plus one per uncovered row gives 2(4+11)=30 display records, not R(3,9)=36. Losslessness does not select a Ramsey count. The still-open question is what explains the uncovered rows and whether a graph-level constructor uses this boundary.

**Replay.** `python research/voevodsky/checkers/ramsey_table_cube_differences.py` enumerates widths 6–13 and checks exact upper-half reconstruction. [Checker](checkers/ramsey_table_cube_differences.py) · [all starts, corners, and uncovered triples](results/ramsey_table_cube_differences.json).
