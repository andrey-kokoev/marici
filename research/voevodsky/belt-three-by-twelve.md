# A geometric (3,12) realization of the belt

## Result

Conjecture 1 has an explicit realization: the existing six-piece belt admits **three rotating sectors with twelve intrinsic coordinates each**, without duplicating triangles or adding a numerically chosen correction.

The three-stage intrinsic core has

```text
L = 3×12²       = 432
G = 3²×12       = 108
N = (3×12)²     = 1296
TOTAL           = 1836.
```

It has one collective mode, GL=LG=N, N²=N, and the strict positive-cycle fixed-weight deletion certificate.

**The interface and local selection have changed.** Keeping the old ambient-coordinate input and output requires 102 transfers in each direction, making that complete implementation 2040. The 1836 count belongs to the intrinsic core, not to a cost-free relabelling of the prior 5346 network.

## Where twelve comes from

The actual six belt faces form a cyclic adjacency graph. There are two ways to pair adjacent faces so that the three pairs are permuted by the actual 120-degree spatial rotation. Both are tested.

Each sector consists of:

```text
2 adjacent belt faces
× 3 centroid-edge triangles per face
× 2 intrinsic real coordinate axes per triangle
= 12 coordinates.
```

The three sectors contain all eighteen original small triangles exactly once. Their twelve local coordinate axes are real; the amplitudes on them are complex, just as amplitudes on the original three Cartesian axes were complex. This is not a switch from complex-coordinate counting to counting real and imaginary parts separately.

## Geometrically generated plane coordinates

For a source triangle (F,a,b), its cyclic mode is

```text
v = F + ω a + ω² b = r + i sqrt(3) s,
r = F − (a+b)/2,
s = (a−b)/2.
```

Both r and s lie in the triangle's real tangent plane and are independent. Let

```text
a0 = s·s,
b0 = r·s,
t = r − (b0/a0) s,
beta = t·t.
```

Then e1=s/sqrt(a0), e2=t/sqrt(beta) are orthonormal real axes. The intrinsic mode coordinates are

```text
w1 = (b0 + i sqrt(3) a0)/sqrt(a0),
w2 = sqrt(beta).
```

Both are nonzero. Every number is derived from the actual displayed geometry; no target support count or measured mass enters the frame construction.

The actual spatial rotation carries each derived frame to the corresponding frame in the next sector. Therefore transport in the co-rotating coordinate charts is I_12. This is a valid unitary monomial representation of C3, albeit a trivial action on local coordinates. The action on the three sector placements is nontrivial.

The general theorem allows such a representation; it does not require the local action to be faithful or irreducible. In particular, this is not an induced one-dimensional-character representation of degree twelve from a subgroup of the order-three group.

## Local selection is also different

The old belt selected eighteen individual triangle modes, then coupled three seed families. Here each sector's twelve-coordinate reference vector defines one rank-one local projector. There are three such projectors.

Thus this construction performs six-triangle coherence within a sector at the local stage. It is an alternate implementation of the same collective return, not merely a permutation of the old local operators.

## Exact return comparison and interface cost

Let W embed the two intrinsic coordinates of each triangle into its three ambient Cartesian coordinates. The derived frames give W*W=I_36. The source-generated ambient mode equals W times the intrinsic mode, with exactly the same squared norm, 1196/15.

The checker compares every coefficient of

```text
W N_intrinsic W* = N_original
```

against the existing 54-by-54 collective return. Equality holds on all original inputs, not only on the coherent vector.

W and W* each have 102 nonzero coefficients in the original proton Cartesian frame. Thus:

| Interface convention | Transfers |
|---|---:|
| Intrinsic three-stage core | 1836 |
| Core plus original ambient input/output conversions | 2040 |

The two directions are required to preserve both original interfaces. The eighteen omitted ambient normal coordinates are killed by the collective mode selection, but omitting them internally is still a representation change.

This also identifies the physical-model obligation: why should the neutron candidate use this intrinsic interface while the proton is counted in its original ambient interface? Equal internal totals do not answer that question.

## Retention verification

Every one of the 1836 intrinsic arrows occurs in a strictly positive three-step closed trace. The 1296 closed-cycle contributions sum to one. Any proper fixed-weight deletion removes at least one positive contribution and changes the complete return.

For exact arithmetic, coordinates are represented as z_i/sqrt(d_i), where d_i is positive rational. Matrix entries are stored as A_ij/sqrt(d_i d_j), with exact complex rational numerators. Composition divides the intermediate summand by d_k. No floating-point zero tests are used.

## Artifacts and status

```text
python research/voevodsky/checkers/check_belt_three_by_twelve.py
```

Thirteen exact checks pass, plus explicit serialization/reconstruction of all arrow numerators. Both geometric sector matchings work.

- `results/belt_three_by_twelve.json`
- `results/belt_three_by_twelve_store.json`

This establishes an explicit (3,12) intrinsic realization and its count. It does not establish a physical neutron identity or a rule uniquely selecting this architecture. The other four conjectures have not been tested by this checker.
