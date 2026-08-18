# marici-gm

The cross-sector marked-Cut overlap test is reproducible with:

```powershell
cargo run --release --bin cross_sector_overlap
```

It restricts the exact Cayley--Menger polynomial to
`q_G12=q_G23=0`, records all induced affine marks, and audits the frozen
six-term source for a joint marked-Cut pole.

The corresponding relative-pair properness gate is reproducible with:

```powershell
cargo run --release --bin relative_pair_gysin_gate
```

The purity and coefficient-arrow type audit is reproducible with:

```powershell
cargo run --release --bin overlap_coefficient_type_gate
```

The local normal-specialization and Euler-class gate is reproducible with:

```powershell
cargo run --release --bin overlap_normal_specialization_gate
```

The ordered two-Cut Cousin determinant gate is reproducible with:

```powershell
cargo run --release --bin two_cut_cousin_determinant_gate
```

The full occurrence-resolved three-Cut Cousin cocycle test is reproducible
with:

```powershell
cargo run --release --bin three_cut_cousin_cocycle
```

The pairing of that packet with the literal positive Bunch--Davies chain is
audited with:

```powershell
cargo run --release --bin three_cut_relative_chain_pairing
```

Cyclic naturality of the six boundary-value Leray germs is checked with:

```powershell
cargo run --release --bin cyclic_leray_naturality
```

The generic full-rank logarithmic versus Cut--nearby layer comparison is
checked with:

```powershell
cargo run --release --bin full_rank12_cut_nearby_layers
```

The first joint total-energy/conductor/elliptic/soft cospan corner is checked
with:

```powershell
cargo run --release --bin joint_soft_conductor_elliptic_cospan
```

The genuine two-parameter total-energy/site-soft resolution is checked with:

```powershell
cargo run --release --bin two_parameter_et_nearby_resolution
```

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
- `generic-et-test <point-count> <output.json>`
- `soft-corner-common-frame-test <output.json>`
- `soft-support-test <output.json>`
- `soft-support-both-sites-test <output.json>`
- `soft-support-nine-master-test <output.json>`
- `cargo run --release --bin marked_soft_support -- <output.json>`
- `cargo run --release --bin soft_rees_smith -- <output.json>`
- `cargo run --release --bin double_soft_rees -- <output.json>`
- `cargo run --release --bin cyclic_occurrence_rees -- <output.json>`

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

The generic total-energy test reconstructs the exact univariate Laurent
residue of the full final block and its elliptic Gysin quotient at independent
values of `v` on `u=E_T=0`. It verifies the residue-level horizontal Gysin
square, adapts to kernel/quotient coordinates, and solves the logarithmic
extension-splitting equation.

The `gysin-polynomial-split-test` command tests the complete simultaneous
two-direction splitting equation in the same Gysin-adapted frame for a
pole-free polynomial gauge through a declared total-degree bound.  The
committed degree-ten certificate finds no solution; this is a bounded ansatz
no-go, not a proof that the differential-module extension is nonsplit.

The `gysin-local-residue-obstruction-test` command takes transverse Laurent
residues on eight explicitly parameterized source divisors.  It tests the
residue extension equation and the indicial operators at positive pole orders.
The committed sixteen-point certificate finds no residue-class obstruction;
only `v-u`, `y-u^2`, and `y+u^2` resonate, and only at pole order one through the tested
order ten.

The `gysin-adapted-reconstruct` command serializes the validated exact
bivariate rational connection in the Gysin-adapted frame.  The companion
`gysin_function_field_residues.py` checker reduces it directly in
`GF(p)(u)[v]/(P6)` and `GF(p)(u)[v]/(Q)`, with no sampling or fitting of points
on either divisor.

`generic-et-nearby-synthesis.json` combines that certificate with the exact
other-block connections and the total-energy intersection census. It records
the complete generic nine-master Deligne nearby object, the second Rees datum,
and the precise typing boundary of the still-unconstructed Cut--nearby square.

The soft-corner command reconstructs the complete bivariate connection,
moves it to one source-defined Gysin-adapted frame before specialization, and
takes both normal residues at `u=v=0`. It extracts their common simple-pole
principal part, removes that diagonal Deligne coboundary, and compares the
finite algebraic--elliptic off-diagonal blocks. The committed certificate
records zero antisymmetric difference and hence
`epsilon_e6=epsilon_v_alg=0` on the generic finite-field de Rham locus.
Build with `--features replication-prime` to repeat the same calculation at
`p=2305843009213693921` with a disjoint deterministic reconstruction stream.

The soft-support command first saturates the degenerating algebraic generator
by replacing `v_alg` with `v_alg/X2^2`, then extracts the Laurent expansion of
the total-energy residue at `X2=0` (`u=0,v=2`). It distinguishes a genuinely
supported logarithmic extension from regular finite mixing. The two committed
prime-field certificates find a zero kernel-to-quotient principal part, while
retaining the regular finite coefficient `-1/4`.

The both-sites command transports the direct `X2=0` computation through the
source involution `x<->y`, `a<->b`, `e8<->e9`, including its fiber-orientation
sign. This tests the union `X1*X2=0` without treating the unavailable `X1=0`
point of the `X1=1` affine chart as an ordinary finite specialization.

The nine-master command combines the both-site result with the exact
`1+2+2+4` character decomposition. It records the site-soft Kummer poles
internal to the two algebraic rank-two blocks and checks that all
off-character entries into the unique elliptic character remain zero.

The marked-soft-support binary adds the three conductor/top quotient classes
of the canonical rank-twelve localization extension. It takes the actual
soft principal parts of both wall columns and checks their infinity-Gysin
images directly; the primitive top column is regular at either individual
site-soft branch.

The soft-Rees Smith binary keeps the site-soft normal (t) in the physical
enhanced/conductor comparison. It verifies the exact factorization
`D_soft*Phi=(D_soft*J)*K` and computes Smith data `(1,2,2*t)`: two
directions remain on the leading soft fiber and one moves to the next Rees
grade, with no new torsion prime.

The double-soft binary retains (x=X_1) and (y=X_2) independently. Since
(mathbb Z[x,y]) is not a one-normal PID, it reports the exact diagonal
presentation and Fitting ideals rather than inventing a one-variable Smith
form.

The cyclic occurrence binary assembles the six literal source summands into
their two (C_3)-orbits, verifies the saturated occurrence-forgetting
kernel and multiplicity two, and transports the two-axis Rees presentations
between sectors. It deliberately does not fabricate Čech transition maps
between distinct residue surfaces.
