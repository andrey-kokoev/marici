# Three local opposite-side walls for seven-point repair candidates

For positive moment-curve external data, the zero-column alternatives now have three exact local common-wall tests against separated-pair cells:

| Pair | Shared source conditions | Image tangent rank | Inward target Jacobian ratio | Source residue comparison |
|---|---|---:|---:|---|
| old cell 0 / zero-column 3 | `C3=0`, `Delta56=0` | 7 | `-14/5` | exact ratio `1` |
| old cell 0 / zero-column 5 | `C5=0`, `Delta23=0` | 7 | `-14/5` | exact ratio `1` |
| old cell 2 / zero-column 1 | `C1=0`, `Delta34=0` | 7 | `-105` | exact ratio `1` |

At each rational source point, the two indicated inward rays retain all required positive ordered minors. The target image of the common face has rank seven; both inward target derivatives are transverse and their oriented determinants have opposite signs. For ALL THREE walls, the standard source cyclic-form residues on the common face agree as rational functions, not merely at the sample. This is a local geometric and form-coherence test for the replacement **candidates**.

The third wall uses its own boundary-coordinate treatment: resolve `Delta71` with `C1=-h(1,v+e)`, resolve `Delta34` by splitting columns 3 and 4, then take the two cyclic residues followed by the zero-column `h` residue. The `71` minor contains both `h` and `e`; their factors are tracked explicitly in the ten-coordinate top-form Jacobian. The resulting symbolic seven-coordinate residue ratio against the six-column top form is exactly `1`.

None of the three tests identifies a repaired source cell with a physical generalized-R term, proves global image overlap/coverage, or supplies an arbitrary-n compiler. The earlier three triple-parallel branches remain invalid as eight-dimensional image charts.

Reproduction:

    uv run --with sympy python research/nima/checkers/check_seven_point_repair_shared_wall.py
    uv run --with sympy python research/nima/checkers/check_seven_point_repair_wall_residue.py
    uv run --with sympy python research/nima/checkers/check_seven_point_second_repair_wall.py
    uv run --with sympy python research/nima/checkers/check_seven_point_third_repair_wall.py
    uv run --with sympy python research/nima/checkers/check_seven_point_third_wall_residue.py

Reports: `research/nima/results/seven-point-repair-shared-wall.json`, `seven-point-repair-wall-residue.json`, `seven-point-second-repair-wall.json`, `seven-point-third-repair-wall.json`, and `seven-point-third-wall-residue.json`.
