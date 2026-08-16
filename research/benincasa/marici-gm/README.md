# marici-gm

Dependency-free Rust machinery for finite-field Griffiths--Dwork reduction of
the final four-master Benincasa block.

Commands:

- `sample <u> <v> <u|v> [output.json]`
- `grid <u0> <nu> <v0> <nv> <u|v> <output.json>`
- `reconstruct <max-total-degree> <output.json>`

The reconstruction command uses deterministic independent pseudorandom field
points, requires a full-rank interpolation system, validates on a disjoint
point stream, and evaluates both curvature sign conventions.

The committed certificate records the first complete bivariate reconstruction:
all 32 entries close at total degree at most 7, all 1,024 independent
entry checks pass, and row-basis flatness is zero.
