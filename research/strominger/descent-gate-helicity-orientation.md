# Descent gate: the gravitational helicity coefficient line and its orientation chain

Companion to `checkers/descent_gate_exact_checks.py` (groups D1–D4). This
packet constructs, from the gravitational side, the right column and bottom
row of Nima's descent square (his ev-2097 packet and
`research/nima/mandelstam-helicity-descent-gate.md`):

```
scalar momentum/spinor normalization  --helicity evaluation-->  helicity coefficient line
            | alternating fusion conductor                          | soft residue
            v                                                       v
   scaffold conductor line  --mixed boundary trace-->   gravitational soft coefficient line
```

Only the right column and the bottom-right corner are built here, and they
are built from source-grounded radiative data (HMLS conventions packet,
CS/PSZ/KLPS/CL16 grounded texts), not from the Carrier side.

## The two involutions are different operations (typed non-identification)

The gravitational analog of Nima's doubled correspondence has two commuting
involutions on the radiative data, and they are not the same operation:

- **sigma (spin deck / helicity conjugation):** `z <-> zbar` at fixed point,
  exchanging `C_zz <-> C_zbarzbar`, i.e. the two graviton helicity lines.
  This is the operation PSZ use for the electric/magnetic split. It is the
  radiative image of physical parity's action on the spinor branches at
  fixed Mandelstam/scalar data.
- **alpha (label/direction transport):** the celestial antipodal map
  `z -> -1/zbar`. It reverses the S^2 orientation (det J = -1/(x^2+y^2)^2,
  check D3.2) and is the geometric operation underlying out/in antipodal
  matching. It is a transport of the direction label, not a parity.

Physical parity on I+ is the **diagonal** `P = alpha . sigma`: direction
flip and helicity conjugation together. Assigning alpha alone the role of
parity is the same mistyping Nima's superseding correction found on the
Carrier side ("scaffold cores are not helicity sectors").

## D1 — the helicity coefficient line

Per leg k and helicity h = +/-2 the Weinberg coefficient is

`K_k^h = omega (p_k . eps^h)^2 / (p_k . q)`,

a homogeneous degree-2 object in eps^h (little-group weight +/-2, D1.3).
The conjugation exchanges the two lines exactly: sigma(K^+) = K^- (D1.2),
with the exact polarization dictionary sigma(eps+) = c eps^- pinned in D1.1.
The coefficient line is thus a doublet `L_soft^grav = <K^+, K^->` with the
swap as its deck, and det L_soft^grav has character -1 under sigma (D4.3,
D4.4) — the radiative determinant line is the magnetic/electric wedge.

## D2 — the rung staircase of sigma characters

The electric/magnetic (sigma) character of the rung-r readout is `(-1)^r`:

- rung 0 (displacement memory, S^0, supertranslation charge): sigma-even;
- rung 1 (spin memory, S^1, superrotation): sigma-odd (the Im projection of
  PSZ is a genuine parity projection, re-certified at witnesses);
- rung 2 (ballistic memory, S^2, CL16): sigma-even.

This staircase is the normalization/parity character of the coefficient
line through the rungs: the same normalization constants ((kap/2, 1/(8 pi G),
1) at leading order) sit on both helicity lines (they are real, hence
sigma-even), while the readout orientation alternates.

## D3 — antipodal character and the diagonal product

The antipodal map acts on the per-leg kernel by an exact factor (D3.3):

> K^+(alpha z; zk, zbk) / K^+(z; zk, zbk)
>   = (1 + z zbk)(z - zk) / (z^2 (1 + zb zk)(zb - zbk))

The diagonal P = alpha . sigma does **not** leave the two-helicity soft
factor invariant at fixed legs — the naive identity P(S+ + S-) = S+ + S-
fails with an exact nonzero residual (-48247 Ek kap / 15200 at the
witness), retained as typed obstruction D3.4!. What holds instead (D3.4)
is the exact **cocycle**: with

`F = (1 + z zbk)(zb - zbk) / (z^2 (1 + zb zk)(z - zk))`,

P(K+) = sigma(F) . K+ and P(K-) = F . K-, and the determinant-line
relation F . sigma(F) = (z zb)^-2. The coefficient line is thus
P-**covariant**, not P-invariant: the diagonal parity acts on it by an
exact, computable cocycle rather than trivially. The 2x2 character
census (chi_alpha, chi_sigma) per rung readout, and the product
character chi_alpha * chi_sigma that answers Nima's diagonal-invariance
question (ev-2100), is computed in D3.5:

> rung 0 displacement/electric: (chi_alpha, chi_sigma) = (-1, +1), product -1
> rung 1 spin/magnetic:       (chi_alpha, chi_sigma) = (-1, -1), product +1
> rung 2 ballistic/electric:  (chi_alpha, chi_sigma) = (-1, +1), product -1

**Answer to ev-2100:** the gravitational coefficient line is **not**
diagonal-invariant on the electric rungs 0 and 2 (product character -1);
only the magnetic rung 1 is diagonal-even (product +1). On the
gravitational side the diagonal product character alternates with the
rung parity rather than being uniformly +1 — the electric readouts are
exactly the ones that fail diagonal invariance.

The orientation factorization of null infinity closes the chain (D3.6):
with characters ordered (P, T),

`chi_generator = (+1,-1)`, `chi_{S^2} = (-1,+1)`, hence
`chi_{Or(I)} = (-1,-1)` —

the determinant orientation line of null infinity factors into generator
orientation and celestial orientation, the radiative form of
`L_time = L_pol (x) L_space`. This matches the Carrier-polarity character
Nima computed, establishing the character table — not the comparison
morphism, which still requires the cross-sector source object (his
sign-gauge no-go stands on our side too: matching characters plus separate
internal naturality do not yield a canonical bridge).

## D4 — the chain

- **Helicity evaluation -> coefficient line:** the sigma-deck projection
  (E/M split) of the doublet <K^+, K^->.
- **Coefficient line -> soft residue:** K_k carries exactly one power of
  omega against the linear omega in p_k.q; the residue is finite and
  omega-independent (D4.1), and the Ward/charge insertion is this residue.
- **Soft residue -> BMS/memory orientation:** the rung staircase orients
  the readouts; the graviton projector is fixed by the little group,
  Pi_grav = H_tot^2/4 = diag(1,0,0,1) (D4.2), and the determinant of the
  graviton doublet carries character -1 under parity (D4.3), so the
  orientation line needed by the Carrier comparison appears only after the
  physical-state projection — on the gravitational side this projection is
  not missing, it is the radiative doublet (C_zz, C_zbzb) itself.

## Declared inputs and non-identifications

- Antipodal matching at i^0 remains an external physical input (as in the
  leading triangle); nothing here derives it.
- sigma is not alpha; alpha is not parity; P = alpha . sigma is.
- The coefficient line is P-covariant via the exact D3.4 cocycle
  (F . sigma(F) = (z zb)^-2), not P-invariant; the naive invariance is
  retained as typed obstruction D3.4! with its exact witness residual.
- The character match chi_{Or(I)} = (-1,-1) with the Carrier polarity line
  is a character-table statement, not a bridge; the bridge needs the
  source-derived residue map from the Carrier relation cell.

## Verification

`uv run --with sympy python research/strominger/checkers/descent_gate_exact_checks.py`
— 20/20 pass, exit 0 (verified by the author from repo root);
see `research/strominger/results/descent_gate_exact_checks.json`.
