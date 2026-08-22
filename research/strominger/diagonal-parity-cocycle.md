# The diagonal-parity cocycle of the gravitational helicity coefficient line

A standalone reference object for cross-sector use. Everything stated here
is certified by `checkers/cocycle_bridge_gates_checks.py` (group C1) at
symbolic level and at exact rational witnesses; the reader does not need
the descent-gate suite (`descent-gate-helicity-orientation.md`) to use
this packet, though that packet derives the objects below.

## Cast

- `z, zbar` — celestial stereographic coordinate of the soft graviton
  direction on `S^2`.
- `z_k, zbar_k` — celestial coordinate of leg `k` (fixed).
- `sigma` — helicity conjugation `z <-> zbar` (the PSZ electric/magnetic
  deck). Exchanges the two graviton helicity lines.
- `alpha` — the celestial antipodal map `z -> -1/zbar` (direction
  transport; reverses the `S^2` orientation, Jacobian determinant
  `-1/(x^2+y^2)^2` in real stereographic coordinates).
- `P = alpha . sigma` — physical parity on `I+`. The two involutions
  commute; `P` is their diagonal.
- `K^+_k, K^-_k` — the per-leg Weinberg soft coefficients
  `omega (p_k . eps^±)^2 / (p_k . q)`, homogeneous of degree 2 in
  `eps^±` (little-group weight `±2`).

## The cocycle

The diagonal `P` acts on the helicity doublet not trivially but by an
exact rational factor: with

```
F(z, zbar; z_k, zbar_k) = (1 + z zbar_k)(zbar - zbar_k)
                          / (z^2 (1 + zbar z_k)(z - z_k))
```

the certified identities (C1.2) are

```
P(K^+) = sigma(F) . K^+ ,   P(K^-) = F . K^- ,
```

together with the determinant-line relation (C1.1)

```
F . sigma(F) = (z zbar)^-2 .
```

`F` is the antipodal transport factor of `K^+` measured in the `K^-`
frame: `F = alpha(K^+)/K^-` (this is how it was computed, cf. D3.3/D3.4
of the descent-gate suite).

## It is a cocycle: the twisted action is a Z_2 action

Applying the twisted action twice returns each kernel exactly (C1.3):

```
P(sigma(F) . K^+) = K^+ ,   P(F . K^-) = K^- .
```

This is the 1-cocycle (no-loop) condition: the diagonal parity is a
well-defined involution on the coefficient line **with** the factor `F`.
Without `F` the action does not close; with it, it does. The coefficient
line is therefore a **P-covariant** object — it carries a canonical
twisted representation of the diagonal `Z_2` — and not a P-invariant
one.

## The obstruction to naive invariance (typed, retained)

The naive statement `P(S^+ + S^-) = S^+ + S^-` at fixed legs is false.
Its exact residual at witness `(z, zbar, z_k, zbar_k) = (2, 3/5, 1/3, 7/5)`
is

```
-48247 E_k kap / 15200     (D3.4!, nonzero)
```

and at the fresh witness `(3, 2/7, 5/3, 11/13)` (independently
recomputed with the same derivation chain, which reproduces the D3.4!
value above exactly):

```
-8441318041 E_k kap / 2679807648     (nonzero)
```

Physical parity invariance of the soft factor is recovered only after
the antipodal leg-matching input (momentum conservation at `i^0`) is
imposed — a declared external input, not derived here.

## Exact witness values

At `(z, zbar, z_k, zbar_k) = (3, 2/7, 5/3, 11/13)` (C1.4; all
denominators of `F` and `sigma(F)` nonzero there):

```
F|W2         = -1173/10478
sigma(F)|W2  = -256711/21114
F.sigma(F)|W2 = 49/36 = (z zbar)^-2   (z zbar = 6/7)
```

## Non-identification declarations

- `sigma` is not `alpha`: helicity conjugation is not direction
  transport.
- `alpha` is not parity: it is an orientation-reversing label transport.
- `P = alpha . sigma` is the only physical parity; identifying either
  factor alone with parity is a mistyping (the same mistyping found and
  corrected on the Carrier/fusion side).
- The cocycle `F` is an exact rational function of the celestial data;
  it is not a phase convention and cannot be gauged away without
  changing the frame on the helicity doublet.

## The square-root existence gate (C1.5)

The diagonal obstruction character is a perfect square of a
`sigma`-invariant rational function:

```
(z zbar)^-2 = ((z zbar)^-1)^2 ,   sigma((z zbar)^-1) = (z zbar)^-1 ,
```

and `F . sigma(F) = ((z zbar)^-1)^2` exactly. This is an **existence
gate, not a curiosity**: even character parity is what permits the
cocycle square root. An odd-exponent character `(z zbar)^k`, `k` odd,
has no square root in `Q(z zbar)` (valuation parity at `u = 0`,
`u = z zbar`), so with an odd-parity obstruction character no diagonal
`sigma`-invariant cocycle could exist at all. The gravitational sector
handed us an even character; whether the same parity gate selects
admissible characters on the Carrier side is a candidate cross-sector
selection rule (flagged to marici.Nima).

## Unified P-covariance of the radiative readouts (C3.4)

On the exact P-symmetric spin-2 datum of the anchor gate (C3.2), the
identity `z^4 A = zbar^4 B` collapses the separate diagonal weights
`z^10 zbar^2` (of `A`) and `z^2 zbar^10` (of `B`) to single characters.
With `u = z zbar`:

```
P(M) = -u^6 . M ,   P(E) = +u^6 . E ,
```

exactly, for the raw magnetic readout `M = d_zbar D_z^3 C_zz - d_z D_zbar^3 C_zbarzbar`
and the electric combination `E = d_zbar D_z^3 C_zz + d_z D_zbar^3 C_zbarzbar`.
Hence the typed obstruction `C3.2!` has the closed form

```
P(M) - M = -(1 + u^6) . M ,
```

which explains the exact divisibility of the `C3.2!` residual numerator
by the value of `M` at the witness (ratio `-164305/117649 = -(1+(6/7)^6)`,
checker `C3.4b`) — structure, not coincidence. Note the readout
characters are powers of the cocycle determinant line:
`±u^6 = ±(F . sigma(F))^-3`.

## Sign-vector-free characterization of the anchor rung (C3.5)

The bridge packet (`spin-grade-bridge-spec.md`, gate C3.1) records that
the gravitational diagonal-character vector `(-1,+1,-1)` and the
declared Carrier conductor-rung vector `(+1,+1,+1)` agree at exactly one
rung — rung 1, the magnetic one. marici.Nima's discriminating test for
whether this agreement is structural: characterize the anchor rung
**without using either sign vector**, then ask whether any symmetry
preserving all admitted data can move it.

Outcome (exact, checker C3.5): the rung `sigma`-parities from C2.1–C2.3
are `(+1,-1,+1)` — the magnetic rung is the **unique sigma-odd rung**,
using no diagonal-product information. Since `chi_alpha = -1` uniformly,
the diagonal product vector is `-chi_sigma`, so the unique
diagonal-even rung *is* the unique sigma-odd rung. Enumerating all six
rung permutations, exactly the two preserving the `sigma`-parity pattern
(identity and the electric-rung swap `0 <-> 2`) preserve the admitted
data — and both fix rung 1. No data-preserving symmetry can move the
anchor among the rungs. **The C3.1 agreement is structural, not
accidental or convention-dependent**: the unique rung where a
character-preserving comparison map could land is independently singled
out by helicity-deck parity alone.

## Verification

`uv run --with sympy python research/strominger/checkers/cocycle_bridge_gates_checks.py`
— 17/17 checks pass, exit 0; see
`research/strominger/results/cocycle_bridge_gates.json`,
groups C1 (cocycle, including the square-root gate C1.5), C3.4/C3.4b
(unified covariance theorem and closed-form obstruction), C3.5
(sign-vector-free anchor characterization), and the descent-gate suite
D3.3/D3.4/D3.4! for the original derivation.
