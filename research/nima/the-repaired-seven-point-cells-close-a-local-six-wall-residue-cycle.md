# The repaired seven-point candidates close a local six-wall residue cycle

The two missing local adjacency checks (1/2 and 3/4) now pass. Taken with the four prior edges, all six proposed repaired seven-point source cells form a **locally checked** adjacency cycle

    0--1--2--3--4--5--0.

Each edge has an independently built positive source face and a rational moment-curve external `Z`. At ONE explicit face point its target image tangent rank is seven; both inward derivatives are transverse and point to opposite sides. Independently, the source cyclic top-form residues on the common seven-coordinate face have exactly equal symbolic rational coefficients (ratio one):

| Edge | Inward target Jacobian ratio | Symbolic source residue ratio |
|---|---:|---:|
| 0/1 | -14/5 | 1 |
| 1/2 | -2/5 | 1 |
| 2/3 | -105 | 1 |
| 3/4 | -21 | 1 |
| 4/5 | -2/15 | 1 |
| 5/0 | -14/5 | 1 |

The 1/2 wall has `C3=0` and `Delta71=0`. Its seven-column source form requires two distinct transverse variables to resolve minors 34 and 71 before taking the zero-column limit. The 3/4 wall has `C1=0` and `Delta56=0`; resolving minor 71 introduces a factor of the vanishing first-column weight, which is explicitly retained in both cyclic denominator and ten-coordinate gauge Jacobian. Both comparisons use the actual six-column top cyclic form on the respective zero-column replacement, not an assumed `dlog` guess.

This completes the finite **local boundary test** for the proposed six-cell cycle. It does not certify the whole wall, prove that these are the ONLY image incidences, supply global closed-image coverage, establish an oriented target-chain equation, or match the pushed-forward source forms to the physical seven-point generalized-R histories at identical external data. The earlier triple-parallel assignments remain collapsed; the repaired zero-column branches are still candidates.

The fixed-target fibre polygon is the right place for the global next gate: classify feasible active sets of its 21 affine minor inequalities, prove every positive fibre contains at least one repaired closed stratum, prove generic uniqueness, and account for all shared-wall coincidences. A single fixed linear objective cannot provide this selection, by the separate exact three-fibre obstruction. Even a successful fibre theorem would not prove the analytic `n^-2` completion law.

Run:

    uv run --with sympy python research/nima/checkers/check_seven_point_one_two_wall.py
    uv run --with sympy python research/nima/checkers/check_seven_point_three_four_wall.py
    python research/nima/checkers/check_seven_point_local_six_cycle.py

The aggregate certificate is `research/nima/results/seven-point-local-six-cycle.json`; it names the four earlier orientation/residue packets as well.
