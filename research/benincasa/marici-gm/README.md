# marici-gm

Dependency-free Rust machinery for finite-field Griffiths--Dwork reduction of
the final four-master Benincasa block.

Commands:

- `sample <u> <v> <u|v> [output.json]`
- `grid <u0> <nu> <v0> <nv> <u|v> <output.json>`
- `reconstruct <max-total-degree> <output.json>`
- `gysin-test <point-count> <output.json>`

The reconstruction command uses deterministic independent pseudorandom field
points, requires a full-rank interpolation system, validates on a disjoint
point stream, and evaluates both curvature sign conventions.

The committed certificate records the first complete bivariate reconstruction:
all 32 entries close at total degree at most 7, all 1,024 independent
entry checks pass, and row-basis flatness is zero.

The Gysin test independently derives the binary-quartic elliptic connection,
evaluates the explicit infinity-residue matrix in both normal directions, and
tests all four sign conventions for its horizontal square. The committed
certificate records zero residual for
`dC + C*B - A*C` at 1,024 generic points (2,048 directions); the three
alternative conventions fail.
