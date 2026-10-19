# Scalar C versus the retained native core: a quantitative typed comparison

[Contract](contracts/scalar-c-native-comparison.v1.json) · [exact checker](check_scalar_c_native_comparison.py) · [receipt](results/scalar-c-native-comparison.v1.json)

## Result and nonredundant scope

The source already proves that its eight hidden coordinates are reachable. This audit adds a **two-point error bound**, allowing arbitrary refitting of the constant visible block, hidden energy and couplings. It is not another recount of the eleven-state closure.

For the specified native three-visible-coordinate effective operator, every fixed Hermitian finite-core surrogate with **at most two hidden states** has

```
max(||K_eff(-1)-F(-1)||_Hport, ||K_eff(-2)-F(-2)||_Hport) >= 1/8192.
```

The literal E–C–2–3 model has one hidden state when E,2,3 are retained and is a special case. The bound holds after any fixed metric-isometric identification of all three visible coordinates. It does not assert that native belt/carrier characters are E/2gamma/3gamma states.

Both z points are off-spectrum diagnostics in the source's stored **K units**, not incoming negative-energy particles or an interval in the physical propagating band. The bound concerns effective operators, not directly scattering amplitudes, resolvents or probabilities. No relative physical energy scale is selected.

## Typed models

For the native source, keep its fixed metric and first three coordinates P, with all eight remaining coordinates Q:

```
K_eff(z)=K_PP+Sigma(z),
Sigma(z)=K_PQ (zI-K_QQ)^(-1) K_QP.
```

The source metric is diagonal, so this is an orthogonal split in that metric. Whitened K is Hermitian. The checker freshly verifies the source/metric and constructs the hidden inverses at -1 and -2 exactly over Q(sqrt(151)); it does not infer them from stored pass flags.

In the literal source, visible order is E,2,3 and hidden state is C:

```
D_literal = [[0,0,0],[0,0,c],[0,c,0]],
v = (a,b,0),
F_literal(z)=D_literal+v v*/z.
```

Here real a,b,c and hidden energy zero are the literal choices. We enlarge the comparison class to

```
F(z)=D+V*(zI-A)^(-1)V,
D=D*, A=A*, dim(A)=r<=2,
```

with arbitrary constant D, A, V, regular at the tested points. Fixed visible unitary changes are absorbed into D,V after whitening. This grants more freedom than the literal toy and does **not** require its direct block to match K_PP. A nonremovable pole at a tested point cannot achieve a finite error there; an uncoupled removable pole is omitted from the realization.

## Exact source witness

Let `J_s=(sI+K_QQ)^(-1)`, s=1,2. Hidden positivity is freshly checked, so these inverses exist. Resolvent algebra gives

```
Delta = K_eff(-2)-K_eff(-1)
      = K_PQ (J_1-J_2) K_QP
      = K_PQ J_1 J_2 K_QP.
```

Its visible metric is `Hport=diag(1196/15,20,20)`. The checker independently forms both expressions, verifies their equality and metric self-adjointness, and checks

```
inertia[Hport (Delta-(1/4096)I3)] = (3 positive,0 negative,0 zero).
```

Thus the whitened Delta is strictly above `(1/4096)I`. This is an exact rational-quadratic-field congruence certificate, not a floating singular-value estimate. The hidden coupling itself has rank three; retaining two output response scalars from one symmetric input would miss that full-input fact.

## Why arbitrary direct-block fitting cannot evade the bound

Set `E_j=K_eff(z_j)-F(z_j)`. The candidate's constant D cancels from `F(-2)-F(-1)`. Its difference factors through the same r-dimensional hidden space and therefore has rank at most r<=2. This remains true for any fixed visible isometry.

Choose a unit vector x in the kernel of that candidate difference. Then

```
||(E_2-E_1)x|| = ||Delta x|| >= 1/4096,
||E_2||+||E_1|| >= 1/4096.
```

At least one endpoint error is at least 1/8192. The argument needs neither a fitted candidate nor a numerical optimization. It also applies to uniform approximation on any domain containing those two points, but does not establish an error lower bound on the positive-energy band alone.

The constant D freedom matters: a one-point self-energy rank test by itself would not prevent a refitted visible block from absorbing that discrepancy. Conversely, at a single chosen point an arbitrary D can match the entire native effective operator with V=0. This checker includes that negative control against claiming a one-point obstruction with D free.

## What remains possible

This rules out exact full-visible identity, and accuracy finer than the stated floor, only for the declared constant finite-state class. It does not rule out:

- a reduction for one preparation, symmetry sector or selected readout;
- a model with three or more hidden states (the source's exact realization uses eight);
- energy-dependent direct terms, visible maps or retained environment terms;
- a coarser approximation or an approximation restricted to a different energy interval;
- richer source-authorized comparison/separation constructions.

It is not a physical no-go. The literal chain still lacks a supplied photon asymptotic-state/measurement dictionary; attaching leads adds assumptions not licensed by this effective-operator calculation. The bare ratio G_3E=(c/z)G_2E remains non-observable without those additional data.

The historical native adapter-helper mismatch is preserved. This result uses the pinned finite K as a conditional mathematical model and does not reissue owner receipts or claim freshness of all ancestors. C1–C12 and their budgets remain unchanged; no high-energy cycle is executed.

## Verification boundary and next executable step

The finite field inverses, metric identities, coupling rank and shifted inertia are replayed. The universal kernel/norm argument is documented linear algebra, not a machine-formalized proof. Next, a source-justified preparation/readout-dependent approximation can be specified and tested, rather than attempting a literal scalar-C identification of the full visible response or repeating the closure construction.

```sh
python -S research/scattering/low-energy/check_scalar_c_native_comparison.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_scalar_c_native_comparison.py
```
