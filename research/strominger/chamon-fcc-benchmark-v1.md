# Chamon FCC benchmark and first published operator import

## Construction

The checker generates periodic supports using the unchanged native `makeLatticeItem` octahedra. Each physical odd-sum center has six FCC vertices. The three opposite pairs carry X, Y and Z respectively. No octahedral diagonal is selected by the interaction, and no center spin is added.

The periodic covers tested are `2x2x2`, `4x4x4`, `6x6x6` and `4x6x8` in physical FCC coordinates. Each factor retains its unwrapped position, wrapped qubit address and deck crossing. The four center classes are the paper's A/B/C/D classes `100,010,001,111`; shift `111` identifies their class set with our even-sum vertex classes.

## Reused implementation

The unmodified upstream `create_chamon_stabs` function and cubic coordinate conversion functions are archived with their content identifiers in [the upstream reference directory](references/chamon-decoder-upstream/README.md).

The checker evaluates only those selected function definitions. The builder's `np.zeros` operation is supplied by a small indexed zero-array adapter, avoiding installation of the full decoder and NumPy. The actual builder body is unchanged. For all three noncollapsed covers, every row of the published binary support matrix is compared after an explicit coordinate reordering: **236 stabilizer rows** in total.

The cubic index helpers are also checked directly. The anisotropic cover uses the builder's documented loop ordering rather than applying a helper restricted to cubes.

## Signed stabilizer proof

Represent a Pauli word by `(x,z,p)`, meaning `i^p X^x Z^z`. Multiplication retains both repeated-site cancellation and the phase from crossing X and Z factors.

For every cover the checker verifies:

1. All generators square to identity.
2. Every pair commutes.
3. Each of the four class products is positive identity.
4. Binary elimination retains the phase of every dependency relation; none generates minus identity.
5. The logical dimension agrees with `4 gcd(Lx/2,Ly/2,Lz/2)`.

| Physical cover | Spins/checks | Binary rank | Logical qubits | Ground-space dimension |
|---|---:|---:|---:|---:|
| `2x2x2` | 4 | 0 | 4 | 16 |
| `4x4x4` | 32 | 24 | 8 | 256 |
| `6x6x6` | 108 | 96 | 12 | 4096 |
| `4x6x8` | 96 | 92 | 4 | 16 |

At period two, each opposite pair acts twice on the same physical spin and cancels. Every stabilizer becomes identity. The upstream builder is used only on noncollapsed covers; this small-cover test multiplies the actual six factors rather than deduplicating their addresses.

Controls reject a flipped generator sign, corruption of one Pauli axis, an incorrect check-coordinate alignment, and deduplication of repeated factors.

## Import of Shirley–Liu–Dua Eq. (C1)

The first published Laurent-polynomial stabilizer map is now matched directly to the native-cell operators, not merely recognized by shape.

For physical FCC coordinates `(x,y,z)`, use primitive coordinates

```
u = ((y+z-x)/2, (x+z-y)/2, (x+y-z)/2).
```

Their basis vectors in physical coordinates are `(0,1,1)`, `(1,0,1)`, `(1,1,0)`. The physical metric in these coordinates is

```
[2 1 1]
[1 2 1]
[1 1 2].
```

For an odd octahedral center c, choose the check anchor `c+(1,1,1)`, an even FCC vertex. Apply the Pauli-frame cycle

```
X_native -> Z_paper
Y_native -> X_paper
Z_native -> Y_paper.
```

The resulting operator is exactly the column in Appendix C, Eq. (C1), of `references/2206.12791v1.pdf`:

```
sigma_X = (1+x^-1)(y^-1+z^-1)
sigma_Z = (1+y^-1)(x^-1+z^-1).
```

Here x,y,z denote formal primitive translations, not the original Cartesian coordinates. The checker compares the full signed operator for all **240 octahedra** across the four covers. It also verifies the Laurent-polynomial commutation identity `sigma^dagger Omega sigma = 0` over F2 and the Pauli multiplication relation for the frame cycle.

The primitive period generators are retained explicitly. A rectangular torus in physical FCC coordinates generally becomes a skew-periodic quotient in the paper's primitive coordinates. It is not replaced by a rectangular cubic torus with unrelated periods.

## Outcome and continuation

The FCC stabilizer benchmark is complete, and the coordinate/operator dictionary for importing the published polynomial construction is explicit.

The next import is the larger gauge-to-Chamon map from Appendix B: the symplectic matrix with six gauge-edge qubits plus two ancillary qubits per unit cell. Its ancillas, unit-cell enlargement and periodic quotient belong in the interface contract. The current result imports Eq. (C1), not that full circuit or a map from native five-coefficient readers to qubits.

## Reproduce

```
python research/strominger/checkers/check_chamon_fcc_benchmark.py
```

Outputs:

- `research/strominger/results/chamon-fcc-covers/verification.json`
- `research/strominger/results/chamon-fcc-benchmark/verification.json`

The benchmark receipt stores signed generators, phase-checked kernel relations, class products, upstream comparisons, the imported polynomial column and direct source fingerprints. Native grammar, solver and viewer are unchanged.
