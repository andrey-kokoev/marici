# Iteration 6: base change over the actual small host triangle

## Contract being tested

The iteration-5 projector atlas was freshly read and completely reverified. Its mode image Z corresponds to the full potential ABC face. The actual host is the smaller triangle T=(F_ABC,A,B).

This iteration tests an additional, restrictive attachment rule:

```text
j(x) = L_AB applied to the geometric position x in the host triangle.
Gamma(v) = L_AB d(v), for potential boundary direction v.
```

A geometric location is not automatically the value of the coefficient ports located there. The fixed-position rule is a candidate to test, not a consequence of the original 1836 network or a requirement supplied by the operator.

The actual new pullback is

```text
R = T x_Z B,
B = the refined potential direction sphere from iteration 5,
R = {(x,v): j(x)=Gamma(v)}.
```

Both maps are explicit PL maps into the source-bound selected-mode disk. The checker constructs their base change as a subcomplex of the retained fold atlas, with both projections and the commuting square checked on every cell.

## 1. Closed-form lifts, not just a selected mesh

Write a host point in barycentric coordinates relative to (F_ABC,A,B) as

```text
x = (f,a,b),  f+a+b=1,  f,a,b >= 0.
```

The complete potential-direction fiber is

```text
upper(x) = (a+f/3, b+f/3, f/3, 0),
lower(x) = (a, b, 0, f).
```

Their selected modes agree. These are all solutions by the complete endpoint classification of iteration 5. They coincide exactly when f=0, i.e. on the host edge AB.

The upper lift is the subtriangle (F_ABC,A,B) inside potential face ABC. The lower lift is the entire potential face (D,A,B). They are two disks identified along AB, not a sphere and not an annulus.

This also gives the universal property: any compatible maps into T and B give a unique map into their pair space R. The formulas identify that pair space with the constructed two-triangle union. Its triangulation makes the projections simplicial; the mediator is PL after compatible subdivision.

## 2. Exact realized-vertex fiber

At the realized host barycenter q=(1/3,1/3,1/3), the two directions are

```text
upper(q) = (4/9,4/9,1/9,0),
lower(q) = (1/3,1/3,0,1/3).
```

The second is the potential ABD face barycenter. There are two points, not the full direction sphere of iteration 3.

If the resolved radial coordinate is also retained, it is determined by t=h_T(x). Equivalently, this same R is the pullback over I x Z of

```text
T -> I x Z,             x -> (h_T(x), j(x)),
I x B -> I x Z,         (t,v) -> (t, Gamma(v)).
```

At q both directions have t=0 and blow down to the same original potential barycenter. Keeping the radial coordinate does not restore the directions excluded by the mode equation.

## 3. Retention audit: this stricter rule fails the main requirement

The constructed complex has 11 vertices, 22 edges and 12 triangles. It is an oriented disk with an eight-edge boundary.

Only eight original potential fold-chart interiors occur:

- two upper ABC flags, each refined into three triangles;
- six lower ABD flags, unchanged.

The other sixteen of the required twenty-four fold-chart interiors are explicitly listed in the receipt. Some lower-dimensional boundaries may still be shared with retained cells; that does not mean their missing two-dimensional interiors were retained.

The entire original potential complex remains in the source packet, but retaining it as provenance does not make it part of this new pullback's active fiber. We therefore do **not** accept this fixed-position rule as fulfillment of the full inward-fold-retention requirement.

This failure belongs to the added matching contract. It is not a no-go result for the operator's direction-bearing vertex proposal or for the earlier resolved depth pullback.

## 4. The actual seam is not the host belt

The global potential mode seam has six edges, but its base change to this particular host triangle is only AB and its midpoint: three vertices and two edges, with interval homology.

Thus identifying that potential seam with the host's six-panel annulus would be incorrect. The distinction is now checked by actual interface maps, not just a warning about similar counts.

A loop in the interior of the host belt has two globally defined lifts, upper and lower, and each closes on itself. Both sections extend across the host disk and meet only at AB. No odd sheet monodromy is forced.

## 5. Next repair to construct

The failed rule fixed a coefficient value by the host's geometric position. A nonredundant repair is to retain the mode as a separate typed interface variable:

```text
host interface: T x Z,
(x,z) -> (h_T(x),z),
resolved potential: I x B,
(t,v) -> (t,Gamma(v)).
```

Their pullback should retain (x,v), with z=Gamma(v), rather than impose z=j(x). This proposed repair distinguishes the location of a port from its value, and a mode from the fold witness above it. It was not implemented in this iteration. The later `proton-electron-single-link-potential-v1.md` now constructs this free-mode pullback as T x B, verifies all 1,296 maximal cells and retains all 24 fold-chart interiors. That continuation keeps the spinor/link identification as a separate missing map.

No particle identity, electron operator, neutron glue or replacement H-1/H-2 arrow total is inferred from the rejected candidate.

## Verification and artifacts

All 18 checks passed, including the **failure of full fold retention** as an expected, measured result. Checks cover the source-bound square, all twelve cell interiors, a 91-point host grid with 169 compatible pairs, exact center lifts, omitted folds, seam topology, actual host-loop lifts, rehashed mutations and complete packet replay.

The grid has 78 double fibers and 13 single fibers; the single fibers lie precisely on AB.

```text
python research/voevodsky/checkers/check_host_coefficient_pullback.py
```

- `research/voevodsky/checkers/check_host_coefficient_pullback.py`
- `research/voevodsky/results/host_coefficient_pullback_store.json`
- `research/voevodsky/results/host_coefficient_pullback.json`

Root: `a1a5f666ada385841fd957adf891674e080a1d5ea1fcace5077159798135a78a`.
