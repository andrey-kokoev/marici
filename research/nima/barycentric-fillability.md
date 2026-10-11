# Barycentric closure versus admitted boundary fillers

## Question

The operator proposed that comparison fillability may be definable by the shape of its barycenter. The bounded test distinguishes center coordinates, the embedded lower-dimensional configuration, and the full incidence structure including admitted fillers. SCC obligation: forward additive realization and descent of fillability to a geometric readout.

## Claim boundary

Use triangle ABC and tetrahedron ABCD from the existing regular coordinates. Retain their vertex barycenter M. For each oriented exterior face f, form a candidate cone simplex (M,f). Every proper face of every cone simplex is admitted in every presentation. Independently admit or omit each top-dimensional cone simplex. This gives eight presentations for the triangle and sixteen for the tetrahedron, without changing any vertices, center equations, edges, or other lower-dimensional cells within each example.

The comparison boundary z is the oriented boundary of the original simplex. It satisfies boundary(z)=0. Fillability here means existence of an integral chain h of the admitted top-dimensional cells with boundary(h)=z. It is not asserted to be equivalent to arbitrary native WG filling.

### Positive construction

Admitting every cone cell gives the explicit oriented cone chain M*z, with

\[
\partial(M*z)=z-M*(\partial z)=z.
\]

Thus the center supplies a concrete way to construct a filler once the needed cone cells are admitted. For the triangle these are three interior triangles; for the tetrahedron they are four interior tetrahedra.

### Counterexample to center-only and lower-skeleton-only criteria

All barycenter equations and edge-midpoint equations hold in every presentation, but only the full set of cone cells fills z. If a cone cell is missing, its exterior face appears in no admitted top-cell boundary. The functional extracting that face's coefficient annihilates every possible admitted boundary, but evaluates to +1 or -1 on z. This proves nonfillability over the integers, rationals and reals; it is not merely failure of a guessed filler.

| Source | Fixed barycenter | Tested top-cell subsets | Fillable subsets |
|---|---|---:|---:|
| ABC | (1/3,1/3,-1/3) | 8 | 1 |
| ABCD | (0,0,0) | 16 | 1 |

A control alters one exterior-face coefficient. Its boundary is then nonzero, so it fails the prior cycle condition despite the unchanged center. A closed boundary and an admitted filler are separate conditions.

## Disposition

- Problem: identify what geometric information determines comparison fillability.
- Conjecture tested: center or retained lower-skeleton geometry suffices.
- Rival: top-cell admissibility carries information erased by that geometry.
- Risky consequence: presentations with the same geometry must have the same fillability.
- Falsifier: deleting a cone top cell preserves the tested geometric data but exposes an exterior-face obstruction; all 22 incomplete presentations are nonfillable.
- Surviving scope: the barycenter organizes a constructive cone filling, but does not authorize its cells. Full oriented incidence plus admitted chain generators gives an exact fillability test in these examples. If “shape” includes that full data, this is consistent with the operator's proposal; it does not derive those admissibility rules from center geometry.

The next missing source datum is a native WG rule deciding when these cone cells are admitted, together with the native-to-chain filling comparison. This test neither manufactures that rule nor infers thermodynamic energy from its obstruction.

Verification: `python research/aspect/scc/scc.py check nima-barycentric-fillability` passed via execution `structured_command_execution:e_32876_1791223593616553800_23`. Checker: `checkers/check_barycentric_fillability.py`; exact certificates: `results/barycentric-fillability.json`; manifest: `scc-models/barycentric-fillability.json`. SCC's adapter reports exit-code evidence only. No commit or publication is claimed.
