# marici-gm

Dependency-free Rust machinery for finite-field Griffiths--Dwork reduction of
the final four-master Benincasa block.

Commands:

- `sample <u> <v> <u|v> [output.json]`
- `grid <u0> <nu> <v0> <nv> <u|v> <output.json>`
- `reconstruct <max-total-degree> <output.json>`
- `gysin-test <point-count> <output.json>`
- `algebraic-test <point-count> <output.json>`
- `algebraic-reconstruct <max-total-degree> <output.json>`
- `algebraic-dlog-test <point-count> <output.json>`
- `algebraic-split-test <max-total-degree> <output.json>`
- `other-block-reconstruct <max-total-degree> <output.json>`
- `other-block-test <point-count> <output.json>`
- `cargo run --release --bin et_intersection_census -- <output.json>`

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

The algebraic commands restrict the reconstructed connection to the explicit
Gysin kernel, reconstruct its diagonal rank-one quotient, and test a
predeclared dlog divisor basis including the source quartic `Q`.

The split command searches a frozen rational gauge for the algebraic-plane
extension. The other-block commands derive and validate the remaining
`1+2+2` parity blocks of the rank-seven Gysin kernel.

The total-energy census restricts every frozen signed-energy, elliptic, and
algebraic-kernel divisor to `u=ell4=E_T=0`. It verifies exactly that every
additional genuine intersection is one of the site-soft roots `v=0,2`;
there is no additional nonsoft energy-carrier intersection.
